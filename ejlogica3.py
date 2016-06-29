#!/usr/bin/env python
# coding: utf-8

import os
clear = lambda: os.system('clear')
clear()

for i in range(1, 7):
    for j in range(i, 7):
        print("{}:{}".format(i, j))
