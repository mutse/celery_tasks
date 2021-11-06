#!/bin/env python3
# -*- coding: utf-8 -*-

from celery import Celery

app = Celery("demo")
app.config_from_object("task_app.config")

