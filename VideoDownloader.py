#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

path = open('path.txt')
dir = []
url = open("url.txt")
app = "youtube-dl"

for line in path:
    dir.append(line.rstrip())

os.chdir(dir[0])

for line in url:
    os.system(app + ' ' + line.rstrip())










