import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

# アイテムの座標を辞書で定義
ITEMS = {
    "boxA": (1.0, 2.0),
    "boxB": (3.5, -1.2),
    "boxC": (-2.0, 1.5)
}

class CommandInputNode(Node):
    def __init__(self):
        super().__init__('command_input_node')
        self.publisher = self.create_publisher(PoseStamped, 'target_location', 10)
        self.get_logger().info('Command Input Node Initialized.')

        self.run()

    def run(self):
        while rclpy.ok():
            item_name = input("Enter item name (boxA, boxB, boxC): ").strip()
            if item_name in ITEMS:
                x, y = ITEMS[item_name]
                pose = PoseStamped()
                pose.header.frame_id = "map"
                pose.pose.position.x = x
                pose.pose.position.y = y
                pose.pose.orientation.w = 1.0
                self.publisher.publish(pose)
                self.get_logger().info(f'Published target location for {item_name}: ({x}, {y})')
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
