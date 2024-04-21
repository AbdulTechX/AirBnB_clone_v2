#!/usr/bin/python3

""" fabric script that creates and distributes an archive
    to web servers
"""
from fabric.api import local
from datetime import datetime
import os
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
env.hosts = ['100.25.211.171', '100.24.72.44']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file

def do_deploy(archive_path):
    """Deploys an archive to the web servers"""
    if os.path.isfile(archive_path) is False:
        return False

    # Extract archive to /data/web_static/releases/<archive_filename>
    archive_file = archive_path.split('/')[-1]
    archive_name = archive_file.split('.')[0]

    # Upload the archive
    if put(archive_path, "/tmp/{}".format(archive_file)).failed is True:
        return False
    # Uncompress the archive to the folder
    if run("rm -rf /data/web_static/releases/{}/".
           format(archive_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(archive_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(archive_file, archive_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(archive_file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(archive_name, archive_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(archive_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(archive_name)).failed is True:
        return False
    return True

def deploy():
    """
    Deploys the web static content to web servers.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
