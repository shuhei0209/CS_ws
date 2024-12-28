import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

# 辞書でアイテムとその座標を定義
ITEMS = {
    "boxA": (1.0, 2.0),
    "boxB": (3.5, -1.2),
    "boxC": (-2.0, 1.5)
}

class CommandInputNode(Node):
    def __init__(self):
        super().__init__('command_input_node')
        self.publisher = self.create_publisher(PoseStamped, '/goal_pose', 10)
        self.get_logger().info('Command Input Node Initialized.')
        self.timer = self.create_timer(0.1, self.check_input)
        self.input_pending = True

    def check_input(self):
        if self.input_pending:
            print("\nAvailable items: " + ", ".join(ITEMS.keys()))
            item_name = input("Enter item name (or 'exit' to quit): ").strip()
            if item_name == 'exit':
                self.get_logger().info("Exiting Command Input Node.")
                rclpy.shutdown()
                return

            if item_name in ITEMS:
                x, y = ITEMS[item_name]
                pose = PoseStamped()
                pose.header.frame_id = "map"
                pose.pose.position.x = x
                pose.pose.position.y = y
                pose.pose.orientation.w = 1.0  # 向きの初期値（必要に応じて変更）

                # 座標をパブリッシュ
                self.publisher.publish(pose)
                self.get_logger().info(f'Sent goal pose for {item_name} at ({x}, {y}).')
            else:
                self.get_logger().warn("Invalid item name. Please try again.")
            self.input_pending = False
        else:
            self.input_pending = True  # 次のループで入力を受け付ける

def main(args=None):
    rclpy.init(args=args)
    node = CommandInputNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Command Input Node.")
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
