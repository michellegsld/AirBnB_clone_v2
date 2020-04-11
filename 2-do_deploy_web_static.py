#!/usr/bin/python3
"""
2-do_deploy_web_static.py
Task 2:
Fabric script based off the previous task (file 1-pack_web_static.py)
In order to distribute an archive to my web servers
(Contains do_pack() func from file 1-pack_web_static.py)
"""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['35.196.120.179', '35.229.21.132']


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


def do_deploy(archive_path):
    """
    A function that returns either True or False
    True:  if all operations have been done correctly
    False: if the file at archive_path doesn’t exist or if true statement fails
    """

    if os.path.exists(archive_path) is False:
        return False

    file_name_exe = archive_path.split('/')[1]
    file_name = file_name_exe[:-4]
    new_folder = "/data/web_static/releases/" + file_name

    try:
        put(archive_path, '/tmp/ +')
        run("mkdir -p" + new_folder)
        run("tar -xzf /tmp/" + file_name_exe + " -C " + new_folder)
        run("rm /tmp/" + file_name_exe)
        run("mv " + new_folder + "/web_static/* " + new_folder)
        run("rm -rf " + new_folder + "/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + new_folder + " /data/web_static/current")
        return True
    except:
        return False
