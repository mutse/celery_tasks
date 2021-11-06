#!/bin/env python3
# -*- coding: utf-8 -*-

from task_app import task1
from task_app import task2

if __name__ == '__main__':
    task1.add.delay(2, 3)
    task2.multiply.delay(2, 3)
    print("end...")

