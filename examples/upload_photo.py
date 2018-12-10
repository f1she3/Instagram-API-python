#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

if(len(sys.argv) < 2):
    print("Usage : ", sys.argv[0], " /path/to/photo.jpg")
    sys.exit(0)
else:
    photo_path = sys.argv[1]
caption = "Sample photo"
tag_list = ["example_tag"]
for tag in tag_list:
    caption = caption + " #" + tag

InstagramAPI = InstagramAPI("login", "password")
InstagramAPI.login()  # login
InstagramAPI.uploadPhoto(photo_path, caption=caption)
