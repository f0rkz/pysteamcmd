import os
import platform
import urllib
import zipfile
import tarfile
import subprocess


class SteamcmdException(Exception):
    """
    Base exception for the pysteamcmd package
    """
    def __init__(self, message=None, *args, **kwargs):
        self.message = message
        super(SteamcmdException, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return repr(self.message)

    def __str__(self):
        return repr(self.message)


class Steamcmd(object):
    def __init__(self, install_path):
        """
        install_path: os.path object pointing to the install location of steamcmd
        example: os.path.join('home','user','steamcmd')
        :param install_path:
        """
        self.install_path = install_path
        if not os.path.isdir(self.install_path):
            raise SteamcmdException('Install path is not a directory or does not exist: '
                                      '{}'.format(self.install_path))

        self.platform = platform.system()
        if self.platform is 'Windows':
            self.steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
            self.steamcmd_zip = 'steamcmd.zip'
            self.steamcmd_exe = 'steamcmd.exe'

        elif self.platform is 'Linux':
            self.steamcmd_url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
            self.steamcmd_zip = 'steamcmd.tar.gz'
            self.steamcmd_exe = 'steamcmd'

        else:
            raise SteamcmdException('The operating system is not supported.'
                                      'Expected Linux or Windows, received: {}'.format(self.platform))

    def _download_steamcmd(self):
        try:
            return urllib.urlretrieve(self.steamcmd_url, self.steamcmd_zip)
        except Exception as e:
            raise SteamcmdException('An unknown exception occurred! {}'.format(e))

    def _extract_steamcmd(self):
        if self.platform == 'Windows':
            with zipfile.ZipFile(self.steamcmd_zip, 'r') as f:
                return f.extractall(self.install_path)

        elif self.platform == 'Linux':
            with tarfile.open(self.steamcmd_zip, 'r:gz') as f:
                return f.extractall(self.install_path)

        else:
            # This should never happen, but let's just throw it just in case.
            raise SteamcmdException('The operating system is not supported.'
                                      'Expected Linux or Windows, received: {}'.format(self.platform))

    def install(self):
        """
        Installs Steamcmd to path. Returns True if everything went aok.
        """
        # Download steamcmd and extract it
        try:
            self._download_steamcmd()
        except SteamcmdException as e:
            return e

        try:
            self._extract_steamcmd()
        except SteamcmdException as e:
            return e

        return True

    def install_gamefiles(self, gameid, game_install_dir, user='anonymous', password=None, validate=False):
        steamcmd_params = []
        steamcmd_params.append('+force_install_dir {}'.format(game_install_dir))
        steamcmd_params.append('+app_update {}'.format(gameid))

        if user == 'anonymous':
            steamcmd_params.append('+@NoPromptForPassword 1')
            steamcmd_params.append('+login anonymous')
        else:
            steamcmd_params.append('+login {} {}'.format(user, password))

        steamcmd_params.append('+quit')

        return subprocess.call([self.steamcmd_exe, steamcmd_params], shell=True)
