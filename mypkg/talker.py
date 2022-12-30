import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('talker_publisher_spiral')
        self.pub = self.create_publisher(Twist, 'turtle', 1)
        self.n = 0.0
        self.create_timer(0.5, self.cb)

    def cb(self):
        msg = Twist()
        msg.linear.x = float(sys.argv[1])
        msg.angular.z = float(sys.argv[2]) + self.n
        self.get_logger().info('Sending - Linear Velocity : %f, Angular Velocity : %f' % (msg.linear.x, msg.angular.z))
        self.pub.publish(msg)
        self.n += float(sys.argv[3])

def main(args=None):
    rclpy.init(args=args)
    minimal_Publisher = MinimalPublisher()
    rclpy.spin(minimal_Publisher)
    minimal_Publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
