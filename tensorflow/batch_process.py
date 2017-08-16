
# Copyright (c) 2015-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the CC-by-NC license found in the
# LICENSE file in the root directory of this source tree.

#! /usr/bin/env python2

import numpy as np
import scipy.io as sio
import time
import os
import sys
import pandas as pd
import subprocess
import shlex

gpu_set = ['0','1']
parameter_set = ['0.0','1.0']
number_gpu = len(gpu_set)

process_set = []
for idx, parameter in enumerate(parameter_set):
    print('Test Parameter: {}'.format(parameter))
     
    command = 'python patch_network_train_triplet.py --data_dir /home/xuzhang/project/Medifor/code/Invariant-Descriptor/data/photoTour/ --training notredame --test liberty --learning_rate 0.1 --num_epoch 20 --loss_type 0 --reg_type 0 --alpha {} --descriptor_dim 128 --beta 1.0 --margin_1 0.5 --gpu_ind {} '\
            .format(parameter,gpu_set[idx%number_gpu])
    
    print(command)
    p = subprocess.Popen(shlex.split(command))
    process_set.append(p)
    
    if (idx+1)%number_gpu == 0:
        print('Wait for process end')
        for sub_process in process_set:
            sub_process.wait()
    
        process_set = []

for sub_process in process_set:
    sub_process.wait()

