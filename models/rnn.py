"""
# Author: OGW.Saunders
# Date: 15 Oct 2020
# Content: Recurrent Neural Network (RNN) Model
# 
"""
#!/usr/bin/python2.7
import tensorflow as tf
import numpy as np

class RNN:

    def __init__(self, parameter_list):
        """
        docstring
        """
        self.in_seq = tf.placeholder('float', [None])
        self.target = tf.placeholder('float', [None])
        pass

    def build(self):
        """
        docstring
        """
        pass

    def propagate(self, num_epochs, parameter_list):
        """
        docstring
        """
        for epoch in range(num_epochs):
            continue
        pass

    def predict(self, paramter_list):
        """
        docstring
        """
        pass
    
