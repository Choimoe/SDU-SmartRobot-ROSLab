#!~/.pyenv/shims/python
import sys 
import rospy
from turtlesim.srv import Spawn

def turtle_spawn():# ROS 节点初始化
    rospy.init_node('turtle_spawn')

# 发现/spawn 服务后，创建一个服务客户端，连接名为/spawn的service
    rospy.wait_for_service('/spawn') 
    try:
        add_turtle = rospy.ServiceProxy('/spawn', Spawn)
#请求服务调用,输入请求数据
        response = add_turtle(2.0, 2.0, 0.0,"turtle2")
        return response.name
    except rospy.ServiceException as e:
        print("Service call failed: %s",e)
if  __name__== "__main__":#服务调用并显示调用结果
    print ("Spwan turtle successfully [name:%s]" %(turtle_spawn()))