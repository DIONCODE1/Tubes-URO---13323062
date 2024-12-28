import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class BoxRobotNode(Node):
    def __init__(self):
        super().__init__('box_robot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_robot)
        self.get_logger().info("Box robot node started.")

    def move_robot(self):
        msg = Twist()
        msg.linear.x = 0.2  # Gerak maju
        msg.angular.z = 0.1  # Putar
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = BoxRobotNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
