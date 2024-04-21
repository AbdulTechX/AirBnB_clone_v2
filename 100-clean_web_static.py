#!/usr/bin/python3
"""write a fabric script that deletes out of date archive using
   the function
"""
from fabric.api import *
import os
from datetime import datetime

env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
env.hosts = ['100.25.211.171', '100.24.72.44']

def do_clean(number=0):
     """Deletes out-of-date archives.

    Args:
        number (int): Number of the archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/release"):
        archive = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
