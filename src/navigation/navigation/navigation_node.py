import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient
from utilities.srv import StringCommand

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.srv = self.create_service(StringCommand, '/navigate_to_target', self.handle_navigation_request)
        self.get_logger().info('Navigation Node Initialized and Service Ready.')

        # ActionClient for NavigateToPose
        self.navigation_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def handle_navigation_request(self, request, response):
        self.get_logger().info(f'Received navigation request: {request.command}')

        try:
            # リクエストの座標をパース
            x, y = map(float, request.command.split(','))
            self.get_logger().info(f'Navigating to target: ({x}, {y})')

            # NavigateToPoseアクションを使用したナビゲーション
            if self.navigate_to_target(x, y):
                response.answer = 'success'
                self.get_logger().info('Successfully reached the target location.')
            else:
                response.answer = 'failed'
                self.get_logger().warn('Failed to reach the target location.')

        except ValueError:
            response.answer = 'failed'
            self.get_logger().error('Invalid coordinates format in request.')

        return response

    def navigate_to_target(self, x, y):
        """Navigate to a target location using Nav2"""
        if not self.navigation_client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('NavigateToPose action server not available!')
            return False

        # Create PoseStamped message
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = 1.0  # 向きは適宜調整

        self.get_logger().info(f'Sending goal: ({x}, {y})')
        self.future = self.navigation_client.send_goal_async(goal_msg)

        # Wait for the goal to complete
        rclpy.spin_until_future_complete(self, self.future)
        goal_handle = self.future.result()

        if not goal_handle.accepted:
            self.get_logger().error('Goal was rejected by the action server.')
            return False

        self.result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, self.result_future)
        result = self.result_future.result()

        if result.status == 4:  # Nav2の成功ステータス
            self.get_logger().info('Goal reached successfully.')
            return True
        else:
            self.get_logger().error('Failed to reach the goal.')
            return False

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Navigation Node.')
    finally:
        node.get_logger().info('Shutting down Navigation Node finally.')
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
