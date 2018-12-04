#!/usr/bin/env python

import rospy
import tf
import numpy as np

class PozyxSim(): 
    def __init__(self):
        self.listener = tf.TransformListener()
        
    def doRanging(self, local_tag, tag_to_range):
        try:
            (self.trans, self.rot) = self.listener.lookupTransform(local_tag, tag_to_range, rospy.Time(0))
            sim_range = (self.trans[0] * self.trans[0] + self.trans[1] * self.trans[1]) ** 0.5 * 1000 + np.random.normal(0, 120, 1)
            return sim_range
        except Exception as e:
            return 0