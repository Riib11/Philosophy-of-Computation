import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

a = tf.random_normal([2,3],0.0,1.0,dtype=tf.float32)  #sampling from a std normal
print(type(a))
#<class 'tensorflow.python.framework.ops.Tensor'>

tf.InteractiveSession()  # run an interactive session in Tf.
a_np = a.eval()
print(type(a_np))
#<class 'numpy.ndarray'>
