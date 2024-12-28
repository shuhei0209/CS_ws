import rclpy
from rclpy.node import Node
from utilities.srv import StringCommand

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self.srv = self.create_service(StringCommand, '/navigate_to_target', self.handle_navigation_request)
        self.get_logger().info('Navigation Node Initialized and Service Ready.')

    def handle_navigation_request(self, request, response):
        self.get_logger().info(f'Received navigation request: {request.command}')

        try:
            # リクエストの座標をパース
            x, y = map(float, request.command.split(','))
            self.get_logger().info(f'Navigating to target: ({x}, {y})')

            # 簡単なフェイクナビゲーション動作 (実際にはNav2や別のアルゴリズムを使用)
            if self.simulate_navigation(x, y):
                response.answer = 'success'
                self.get_logger().info('Successfully reached the target location.')
            else:
                response.answer = 'failed'
                self.get_logger().warn('Failed to reach the target location.')

        except ValueError:
            response.answer = 'failed'
            self.get_logger().error('Invalid coordinates format in request.')

        return response

    def simulate_navigation(self, x, y):
        # 簡単なシミュレーションでナビゲーションの成功/失敗を決定
        # 実際にはここにロボット制御コードを記述する
        import time
        time.sleep(5)  # ナビゲーション処理のシミュレーション

        # 成功例をシンプルに返す (条件を設定する場合はここにロジックを追加)
        return True

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
