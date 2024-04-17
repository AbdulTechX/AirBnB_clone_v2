from fabric.api import local
from date import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # Create timestamp for the archive name
    timestamp = datetime now().strftime(’%Y%m%d%H%M%S’)
    # Generate a .tgzfron the webstatic folder
    archive_name = f’web_static_{timestamp}.tgz
    archive_path = os.path.join ('versions',archive_name)

    if not os.path.exist ('versions'):
        os.mkdirs('versions')

    try:
        local('tar -cvzf {} webstatic'.format(archieve-path))
        return archive-path
    except Exception as e:
        print("failed to generate archive:",e)
           return none
