import rclpy
from math import sin, cos
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from utilities.srv import StringCommand

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.callback_group = ReentrantCallbackGroup()
        self.srv = self.create_service(StringCommand, '/navigate_to_goal', self.handle_navigation_request, callback_group=self.callback_group)
        self.get_logger().info('Navigation Node Initialized and Service Ready.')

        # ActionClient for NavigateToPose
        self.navigation_client = ActionClient(self, NavigateToPose, 'navigate_to_pose', callback_group=self.callback_group)

    def handle_navigation_request(self, request, response):
        self.get_logger().info(f'Received navigation request: {request.command}')

        try:
            x, y, yaw = map(float, request.command.split(','))
            self.get_logger().info(f'Navigating to goal: ({x}, {y}, {yaw})')

            # Navigation using NavigateToPose Acition
            if self.navigate_to_goal(x, y, yaw):
                response.answer = 'success'
                self.get_logger().info('Successfully reached the goal pose.')
            else:
                response.answer = 'failed'
                self.get_logger().warn('Failed to reach the goal pose.')

        except ValueError:
            response.answer = 'failed'
            self.get_logger().error('Invalid coordinates format in request.')

        return response

    def navigate_to_goal(self, x, y, yaw):
        # Navigate to a goal pose using Nav2
        while not self.navigation_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('Waiting for the start-up of action server')

        # Create PoseStamped message
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.z = sin(yaw / 2)
        goal_msg.pose.pose.orientation.w = cos(yaw / 2)

        self.future = self.navigation_client.send_goal_async(goal_msg)
        self.get_logger().info('Goal message sent')

        self.get_logger().info(f'Future done? {self.future.done()}')
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info('Future completed')

        goal_handle = self.future.result()
        if goal_handle is None:
            self.get_logger().error('Goal handle is None.')
            return False
            
        if not goal_handle.accepted:
            self.get_logger().error('Goal was rejected by the action server.')
            return False

        self.get_logger().info('Goal was accepted')
        self.result_future = goal_handle.get_result_async()
        self.get_logger().info('Waiting for result...')
        rclpy.spin_until_future_complete(self, self.result_future)
        result = self.result_future.result()

        self.get_logger().info(f"Nav2 result status: {result.status}")

        if result.status == 4:  # Success status in Nav2
            self.get_logger().info('Goal reached successfully.')
            return True
        else:
            self.get_logger().error('Failed to reach the goal.')
            return False

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Navigation Node.')
    finally:
        node.get_logger().info('Shutting down Navigation Node finally.')
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
