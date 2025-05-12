#!/Users/choimoe/miniconda3/envs/ros_env/bin/python
import rospy
from learning_topic.msg import Person
import time 
def velocity_publisher():
    rospy.init_node('person_publisher', anonymous=True)
    person_info_pub = rospy.Publisher('/person_info', Person, queue_size=10)
    rate =rospy.Rate(10)
    while not rospy.is_shutdown():
        person_msg = Person()
        person_msg.name = "Tom"; person_msg.age=18;
        person_msg.sex=Person.male;
        person_info_pub.publish(person_msg)
        rospy.loginfo("Publsh person message[%s, %d, %d]",person_msg.name, person_msg.age, person_msg.sex)
        rate.sleep()
        time.sleep(1)
if __name__ =='__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass
