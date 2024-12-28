import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10)
        self.bridge = CvBridge()
        self.get_logger().info("Vision node started.")

    def image_callback(self, msg):
        # Konversi pesan ROS ke OpenCV
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        
        # Deteksi warna atau proses lainnya
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = (110, 50, 50)
        upper_blue = (130, 255, 255)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Tampilkan hasil
        cv2.imshow("Original", frame)
        cv2.imshow("Processed", result)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
