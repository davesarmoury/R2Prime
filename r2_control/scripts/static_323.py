#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

names = ["ankle_joint", "shoulder_joint", "center_ankle_joint", "center_leg_joint"]
two = [0.0, 0.0, 0.0, 0.255]
three = [0.3054326, -0.6108652, 0.3054326, 0.0]
values = three

class StaticR2JointPublisher(Node):
    def __init__(self):
        super().__init__('static_r2_joint_publisher')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.05, self.timer_callback)  # 20 Hz

    def timer_callback(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = names

        msg.position = values

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = StaticR2JointPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
