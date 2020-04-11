#!/usr/bin/python3
"""
1-pack_web_static.py
Task 1:
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo
"""
import os
from fabric.api import *
from datetime import datetime

def do_pack():
    """
    A function that returns None or the archive path
    """

    now = datetime.now()
    time_now = now.strftime("%Y%m%dD%H%M%S")
    archive_name = "versions/web_static_" + time_now + ".tgz"
    local('mkdir -p versions')
    archive_command = local("tar -zcvf " + archive_name + " web_static")

    if archive_command.succeeded:
        return archive_name

    return None
