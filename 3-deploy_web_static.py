#!/usr/bin/python3

""" fabric script that creates and distributes an archive
    to web servers
"""
import fabric.api
from Airbone_clone_v2.1-pack_web_static.py  import do_pack

env.hosts = ['100.25.211.171', '100.24.72.44']


