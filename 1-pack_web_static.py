from fabric.api import local
from date import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the name of the archive
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
    )
