import rosbag
import cv2
from pathlib import Path
import shutil
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
bag_path = "/home/pmarg/HSR_RosBags/"

import os
# get all .bag files in the bag_path
bag_files = list(Path(bag_path).rglob("*.bag"))
bridge = CvBridge()
topic_name = "/hsrb/head_rgbd_sensor/rgb/image_rect_color"
# open the bag file
for bag_path in bag_files:
    print("Processing file ", bag_path)
    # get folder name
    folder_name = os.path.basename(bag_path)
    with rosbag.Bag(bag_path, 'r') as bag:
        
        count = 0
        num_msgs = bag.get_message_count(topic_filters=[topic_name])
        
        for topic, msg, t in bag.read_messages(topics=[topic_name]):
                # convert the image message to a cv2 image
                count += 1
                if count%(num_msgs//10) != 0:
                    continue
                cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
                # save the image
                cv2.imwrite(f"{folder_name}_img_{count}.png", cv_image)