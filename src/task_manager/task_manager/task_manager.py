import rclpy
import smach
from std_msgs.msg import String
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from utilities.srv import StringCommand

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
        self.cli = self.node.create_client(StringCommand, '/navigate_to_goal')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.logger.info('Waiting for the navigation service...')

        self.logger.info('Starting navigation...')
        self.req = StringCommand.Request()
        self.req.command = userdata.goal_pose

        result = self.send_request()

        if result:
            self.logger.info('Successfully arrived at the goal_pose.')
            return 'succeeded'
        else:
            self.logger.warn('Failed to navigate to the goal_pose.')
            return 'failed'

    def send_request(self):
        self.future = self.cli.call_async(self.req)

        while rclpy.ok():
            rclpy.spin_once(self.node)
            if self.future.done():
                response = self.future.result()
                break

        if response and response.answer == 'success':
            return True
        else:
            return False


# State: DetectObject
class DetectObjectState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("DetectObject: Searching for the object...")
        return 'succeeded'

# State: PickObject
class PickObjectState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("PickObject: Picking up the object...")
        return 'succeeded'

# State: PlaceObject
class PlaceObjectState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['succeeded'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("PlaceObject: Placing the object...")
        return 'succeeded'

# TaskState node
class TaskState(Node):
    def __init__(self):
        super().__init__('task_state_node')

    def execute(self):
        sm = smach.StateMachine(outcomes=['task_complete'])

        with sm:
            smach.StateMachine.add('IDLE', IdleState(self), transitions={'proceed': 'NAVIGATE'})
            smach.StateMachine.add('NAVIGATE', NavigationState(self), transitions={'succeeded': 'DETECT_OBJECT', 'failed': 'NAVIGATE'})
            smach.StateMachine.add('DETECT_OBJECT', DetectObjectState(self), transitions={'succeeded': 'PICK_OBJECT'})
            smach.StateMachine.add('PICK_OBJECT', PickObjectState(self), transitions={'succeeded': 'PLACE_OBJECT'})
            smach.StateMachine.add('PLACE_OBJECT', PlaceObjectState(self), transitions={'succeeded': 'task_complete'})

        outvome = sm.execute()

def main():
    rclpy.init()
    node = TaskState()
    node.execute()
    rclpy.shutdown()

if __name__ == '__main__':
    main()