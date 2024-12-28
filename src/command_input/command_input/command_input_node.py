import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandInputNode(Node):
    def __init__(self):
        super().__init__('command_input_node')
        self.publisher = self.create_publisher(String, 'user_command', 10)
        self.get_logger().info('Command Input Node Initialized.')

    def run(self):
        while rclpy.ok():
            item_name = input("Enter item name (boxA, boxB, boxC): ").strip()
            if item_name:
                msg = String()
                msg.data = item_name
                self.publisher.publish(msg)
                self.get_logger().info(f'Published command: {item_name}')

def main(args=None):
    rclpy.init(args=args)
    node = CommandInputNode()
    try:
        node.run()
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Command Input Node.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
