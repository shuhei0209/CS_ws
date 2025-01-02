import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from math import pi

ITEMS = {
    "boxA": (4.1, 0.0, 0.0),
    "boxB": (3.1, 2.2, -pi/2),
    "boxC": (2.6, -0.5, pi)
}

class CommandInputNode(Node):
    def __init__(self):
        super().__init__('command_input_node')
        self.publisher = self.create_publisher(String, 'goal_pose', 10)
        self.get_logger().info('Command Input Node Initialized.')

        self.run()

    def run(self):
        while rclpy.ok():
            item_name = input("Enter item name (boxA, boxB, boxC): ").strip()
            if item_name in ITEMS:
                x, y, yaw = ITEMS[item_name]
                message = f"{x}, {y}, {yaw}"
                self.publisher.publish(String(data=message))
                self.get_logger().info(f'Published target location for {item_name}: {message}')
            else:
                self.get_logger().warn('Invalid item name. Please try again.')

def main(args=None):
    rclpy.init(args=args)
    node = CommandInputNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Command Input Node.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
