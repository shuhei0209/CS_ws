import rclpy
import smach
from std_msgs.msg import String
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from utilities.srv import StringCommand

# アイテムの座標を辞書で定義
ITEMS = {
    "boxA": (1.0, 2.0),
    "boxB": (3.5, -1.2),
    "boxC": (-2.0, 1.5)
}

# State: Idle
class IdleState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['proceed'], output_keys=['target_location'])
        self.node = node
        self.logger = self.node.get_logger()
        self.subscriber = self.node.create_subscription(String, 'user_command', self.command_callback, 10)
        self.command = None

    def command_callback(self, msg):
        self.command = msg.data

    def execute(self, userdata):
        self.logger.info("Idle: Waiting for command...")
        while not self.command:
            rclpy.spin_once(self.node, timeout_sec=1.0)
        item_name = self.command
        self.command = None

        if item_name in ITEMS:
            x, y = ITEMS[item_name]
            pose = PoseStamped()
            pose.header.frame_id = "map"
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.orientation.w = 1.0
            userdata.target_location = pose
            self.logger.info(f"Command received: Moving to {item_name} at ({x}, {y})")
            return 'proceed'
        else:
            self.logger.warn("Invalid item name. Please try again.")
            return self.execute(userdata)

# State: Navigate
class NavigationState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['arrived', 'failed'], input_keys=['target_location'])
        self.node = node
        self.logger = self.node.get_logger()

    def execute(self, userdata):
        # サービスクライアントの初期化をここで実行
        self.cli = self.node.create_client(StringCommand, '/navigate_to_target')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.logger.info('Waiting for the navigation service...')

        self.req = StringCommand.Request()
        self.logger.info('Starting navigation...')

        # `target_location` をリクエストに設定
        target = userdata.target_location
        self.req.command = f"{target.pose.position.x},{target.pose.position.y}"

        # サービスリクエストの送信
        result = self.send_request()

        if result:
            self.logger.info('Successfully arrived at the target location.')
            return 'arrived'
        else:
            self.logger.warn('Failed to navigate to the target location.')
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
        smach.State.__init__(self, outcomes=['object_found'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("DetectObject: Searching for the object...")
        return 'object_found'

# State: PickObject
class PickObjectState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['picked'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("PickObject: Picking up the object...")
        return 'picked'

# State: PlaceObject
class PlaceObjectState(smach.State):
    def __init__(self, node):
        smach.State.__init__(self, outcomes=['placed'])
        self.node = node

    def execute(self, userdata):
        self.node.get_logger().info("PlaceObject: Placing the object...")
        return 'placed'

# TaskStateノードの定義
class TaskState(Node):
    def __init__(self):
        super().__init__('task_state_node')

    def execute(self):
        sm = smach.StateMachine(outcomes=['task_complete'])

        with sm:
            smach.StateMachine.add('IDLE', IdleState(self), transitions={'proceed': 'NAVIGATE'})
            smach.StateMachine.add('NAVIGATE', NavigationState(self), transitions={'arrived': 'DETECT_OBJECT', 'failed': 'NAVIGATE'})
            smach.StateMachine.add('DETECT_OBJECT', DetectObjectState(self), transitions={'object_found': 'PICK_OBJECT'})
            smach.StateMachine.add('PICK_OBJECT', PickObjectState(self), transitions={'picked': 'PLACE_OBJECT'})
            smach.StateMachine.add('PLACE_OBJECT', PlaceObjectState(self), transitions={'placed': 'task_complete'})

        outvome = sm.execute()

# メイン関数
def main():
    rclpy.init()
    node = TaskState()
    node.execute()
    rclpy.shutdown()

if __name__ == '__main__':
    main()