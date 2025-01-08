import rclpy
import smach
import time
from math import pi, sin, cos
from std_msgs.msg import String
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient


# State: Idle
class IdleState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['proceed'], input_keys=['goal_pose'], output_keys=['goal_pose'])
        self.node = node
        self.logger = self.node.get_logger()
        self.subscriber = self.node.create_subscription(String, 'goal_pose', self.goal_pose_callback, 10)
        self.goal_pose = None

    def goal_pose_callback(self, msg):
        self.goal_pose = msg.data

    def execute(self, userdata):
        self.logger.info("Idle: Waiting for goal pose...")
        while not self.goal_pose:
            rclpy.spin_once(self.node, timeout_sec=1.0)
        userdata.goal_pose = self.goal_pose
        self.goal_pose = None
        self.logger.info(f"Received goal_pose: {userdata.goal_pose}")
        return 'proceed'


# State: Navigate
class NavigationState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded', 'failed'], input_keys=['goal_pose'])
        self.node = node
        self.logger = self.node.get_logger()

    def execute(self, userdata):
        self.logger.info('Starting navigation...')
        goal_pose = userdata.goal_pose.split(',')
        x, y, yaw = map(float, goal_pose)

        if self.node.navigate_to_goal(x, y, yaw):
            self.logger.info('Successfully arrived at the goal_pose.')
            return 'succeeded'
        else:
            self.logger.warn('Failed to navigate to the goal_pose.')
            return 'failed'


# State: DetectObject
class DetectObjectState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("DetectObject: Searching for the object...")
        time.sleep(5)
        return 'succeeded'


# State: Pickup
class PickupState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("Pickup: Picking up the object...")
        time.sleep(5)
        return 'succeeded'


# State: Deliver
class DeliverState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node
        self.logger = self.node.get_logger()

    def execute(self, userdata):
        self.logger.info('Deliver: Navigating to delivery location...')
        x, y, yaw = (1.2, 2.5, pi / 2)

        if self.node.navigate_to_goal(x, y, yaw):
            self.logger.info('Successfully delivered the object.')
            return 'succeeded'
        else:
            self.logger.warn('Failed to deliver the object.')
            return 'failed'


# State: Place
class PlaceState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("Place: Placing the object...")
        time.sleep(5)
        return 'succeeded'


# TaskState node
class TaskState(Node):
    def __init__(self):
        super().__init__('task_state_node')
        self.nav_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def navigate_to_goal(self, x, y, yaw):
        while not self.nav_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('Waiting for the start-up of action server')

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.z = sin(yaw / 2)
        goal_msg.pose.pose.orientation.w = cos(yaw / 2)

        self.future = self.nav_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, self.future)

        goal_handle = self.future.result()
        if not goal_handle or not goal_handle.accepted:
            self.get_logger().error('Goal was rejected by the action server.')
            return False

        self.get_logger().info('Goal was accepted. Waiting for result...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        result = result_future.result()

        if result.status == 4:  # Success status in Nav2
            self.get_logger().info('Goal reached successfully.')
            return True
        else:
            self.get_logger().error('Failed to reach the goal.')
            return False

    def execute(self):
        sm = smach.StateMachine(outcomes=['task_complete'])

        with sm:
            smach.StateMachine.add('IDLE', IdleState(self), transitions={'proceed': 'NAVIGATE'})
            smach.StateMachine.add('NAVIGATE', NavigationState(self), transitions={'succeeded': 'DETECT_OBJECT', 'failed': 'NAVIGATE'})
            smach.StateMachine.add('DETECT_OBJECT', DetectObjectState(self), transitions={'succeeded': 'PICKUP'})
            smach.StateMachine.add('PICKUP', PickupState(self), transitions={'succeeded': 'DELIVER'})
            smach.StateMachine.add('DELIVER', DeliverState(self), transitions={'succeeded': 'PLACE'})
            smach.StateMachine.add('PLACE', PlaceState(self), transitions={'succeeded': 'IDLE'})

        sm.execute()


def main():
    rclpy.init()
    node = TaskState()
    node.execute()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
