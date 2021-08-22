"""
Python Steamcmd Library
pysteamcmd is a suite of tools to use the steamcmd command line tool for dedicated gameservers.

It is important that you install the appropriate package to run 32-bit libraries on 64-bit systems.

IE: Ubuntu

    sudo apt-get install lib32stdc++6

Usage:

    >>> import pysteamcmd
    >>> import os
    >>> steamcmd_path = os.path.join('/','home','f0rkz','steamcmd')
    >>> steamcmd = pysteamcmd.Steamcmd(steamcmd_path)
    >>> steamcmd.install()
    True
    >>> gameserver_path = os.path.join('/','home','f0rkz','mygameserver')
    >>> steamcmd.install_gamefiles(
    ...    gameid=232330,
    ...    game_install_dir=gameserver_path,
    ...    user='anonymous',
    ...    password=None,
    ...    validate=True,
    ... )

"""
