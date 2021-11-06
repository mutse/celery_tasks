#!/bin/env python3
# -*- coding: utf-8 -*-

broker_url = "redis://localhost:6379/1"
result_backend = "redis://localhost:6379/2"

timezone = "Asia/Shanghai"
imports = [
    "task_app.task1",
    "task_app.task2"
]
