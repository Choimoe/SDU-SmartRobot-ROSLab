#!/Users/choimoe/miniconda3/envs/ros_env/bin/python
import rospy
from turtlesim.msg import Pose
def poseCallback(msg):
    rospy.loginfo("Turtle pose: x:%0.6f, y:%0.6f", msg.x, msg.y)
def pose_subscriber():
# ROS 节点初始化
    rospy.init_node('pose_subscriber', anonymous=True)
# 创建一个Subscriber，订阅名为/turtle1/pose的topic，注册回调函数 poseCallback
    rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
# 循环等待回调函数 
    rospy.spin()
if __name__== '__main__':
    pose_subscriber()
