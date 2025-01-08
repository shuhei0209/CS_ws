import rclpy
from rclpy.node import Node
from utilities.srv import StringCommand

class TestServer(Node):
    def __init__(self):
        super().__init__('test_server')
        self.srv = self.create_service(StringCommand, '/navigate_to_goal', self.callback)
        self.get_logger().info('Test Server Ready')

    def callback(self, request, response):
        self.get_logger().info(f"Received request: {request.command}")
        response.answer = 'success'
        return response


def main(args=None):
    rclpy.init(args=args)
    node = TestServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
