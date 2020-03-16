from __future__ import absolute_import, division, print_function, unicode_literals

import subprocess
import tensorflow as tf
import os

is_gpu_available = tf.test.is_gpu_available()
message = "GPU available: {}".format(is_gpu_available)
print(message)

try:
    os.mkdir('run-result')
except OSError:
    pass

with open('run-result/output.txt', 'w') as f:
    f.write(message)

    if is_gpu_available:

        gpu_count = str(subprocess.check_output(["nvidia-smi", "--query-gpu=count", "--format=csv,noheader" ]), "utf-8")
        gpu_name = str(subprocess.check_output(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader" ]), "utf-8")
        gpu_memory = str(subprocess.check_output(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader" ]), "utf-8")


        message = "Test Summary"
        print (message)
        f.write(message)

        message = "GPU count: {}".format(gpu_count)
        print (message)
        f.write(message)

        message = "GPU name: {}".format(gpu_name)
        print (message)
        f.write(message)

        message = "GPU memory: {}".format(gpu_memory)
        print (message)
        f.write(message)    
    
print("DONE")
