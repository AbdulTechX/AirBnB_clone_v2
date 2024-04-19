#!/usr/bin/python3
"""fabric script that distribute an archive to web servers using
   using do_deploy function.
"""
from fabric.api import env, put, run
from os import path

env.user = 'ubuntu'  # Set the SSH user dynamically
env.key_filename = '~/.ssh/id_rsa'
env.hosts = ['100.25.211.171', '100.24.72.44']


def do_deploy(archive_path):
    """Deploys an archive to the web servers"""
    if not (path.exists(archive_path)):
        return False

    try:
        # Upload archive to /tmp/ directory on servers
        put(archive_path, '/tmp/')
        # Extract archive to /data/web_static/releases/<archive_filename>
        archive_filename = os.path.basename(archive_path).split('.')[0]

        # Uncompress the archive to the folder 
        release_folder = '/data/web_static/releases/' + archive_filename
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(archive_filename, release_folder))

        # Delete the archive from tmp directory from the web server
        run('rm /tmp/{}.tgz'.format(archive_filename))

        # delete symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')


        #Create a new the symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(release_folder))

        return True
    except:
        return False

