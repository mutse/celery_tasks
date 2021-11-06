#!/bin/env python3
# -*- coding: utf-8 -×-

from __future__ import absolute_import

import time
from task_app import app

@app.task
def add(x, y):
    time.sleep(2)
    return x + y

