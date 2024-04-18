#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create timestamp for the archive name
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

        # Generate a .tgz from the webstatic folder
        archive_name = "web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path
        return os.path.join("versions", archive_name)
    except Exception as e:
        return None
