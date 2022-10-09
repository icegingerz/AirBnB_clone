#!/usr/bin/python3
"""A fabric script that generate a .tgz archive from the contents of
the web_static folder ofr your AirBnB clone repo"""
from fabric.api import *


def do_pack():
    """Generate the .tgz archive"""
    from datetime import datetime
    import os.path

    d = datetime.now()

    file_path = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
            d.year, d.month, d.day, d.hour, d.minute, d.second)

    if not os.path.exists('versions'):
        os.mkdir('versions')

    print('Packing web_static to ' + file_path)
    r = local('tar  -cvzf {} {}'.format(file_path, 'web_static'))

    if r.stderr:
        return None

    file_stats = os.stat(file_path)

    print('web_static packed: {} -> {}Bytes'.format(
        file_path, file_stats.st_size))

    return os.path.realpath(file_path) if not r.stderr else None
