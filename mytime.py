#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

def get_current_day():
    return datetime.now().day

def get_current_month():
    return datetime.now().month

def get_current_year():
    return datetime.now().year