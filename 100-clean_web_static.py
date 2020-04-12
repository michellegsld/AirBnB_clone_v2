#!/usr/bin/python3
"""
100-clean_web_static.py
Task 4:
Fabric script based off the previous task (file 3-deploy_web_static.py)
That deletes out-of-date archives using the func do_clean
(Contains funcs from file 3-deploy_web_static.py)
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
    time_now = now.strftime("%Y%m%d%H%M%S")
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
        put(archive_path, "/tmp/{}".format(file_name_exe))
        run("mkdir -p {}".format(new_folder))
        run("tar -xzf /tmp/{} -C {}/".format(file_name_exe, new_folder))
        run("rm /tmp/{}".format(file_name_exe))
        run("mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("rm -rf {}/web_static".format(new_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(new_folder))
        return True
    except:
        return False


def deploy():
    """
    A function that returns either:
    False if no archive has been created
    The value of do_deploy
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    deploy_done = do_deploy(archive_path)

    return deploy_done


def do_clean(number=0):
    """
    number is the number of archives to keep (includes the most recent)
    If number is 0 or 1: keep only the most recent version of your archive
    If number is 2: keep most recent and second most
    If number is ... etc ...
    """
    files = local("ls -tr versions", capture=True)

    number = int(number)

    if number == 0:
        number = 1

    files = files.split("\n")
    length = len(files)
    for num in range(0, length - number):
        local("rm -rf versions/{}".format(files[num]))

    files = run("ls -tr /data/web_static/releases")
    files = files.split("\n")
    length = len(files)
    for num in range(0, length - number):
        run("rm -rf /data/web_static/releases/{}".format(files[num]))
