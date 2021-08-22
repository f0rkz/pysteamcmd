import sys
import os
import platform
import zipfile
import tarfile
import subprocess

import vdf

# urllib.urlretrieve no longer exists in python 3.
pythonVersion = sys.version_info[0]
if pythonVersion == 3:
    from urllib.request import urlretrieve
elif pythonVersion == 2:
    from urllib import urlretrieve


class SteamcmdException(Exception):
    """
    Base exception for the pysteamcmd package
    """
    pass


class Steamcmd(object):
    def __init__(self, install_path):
        """
        :param install_path: installation path for steamcmd
        """
        self.install_path = install_path
        if not os.path.isdir(self.install_path):
            raise SteamcmdException('Install path is not a directory or does not exist: {}'.format(self.install_path))

        self.platform = platform.system()
        if self.platform == 'Windows':
            self.steamcmd_url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'
            self.steamcmd_zip = 'steamcmd.zip'
            self.steamcmd_exe = os.path.join(self.install_path, 'steamcmd.exe')

        elif self.platform == 'Linux':
            self.steamcmd_url = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz"
            self.steamcmd_zip = 'steamcmd.tar.gz'
            self.steamcmd_exe = os.path.join(self.install_path, 'steamcmd.sh')

        else:
            raise SteamcmdException(
                'The operating system is not supported. Expected Linux or Windows, received: {}'.format(self.platform)
            )

    def _download_steamcmd(self):
        try:
            return urlretrieve(self.steamcmd_url, self.steamcmd_zip)
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
            raise SteamcmdException(
                'The operating system is not supported. Expected Linux or Windows, received: {}'.format(self.platform)
            )

    def _parse_vdf(self, vdf_path=None, vdf_data=None):
        if vdf_path and os.path.isfile(vdf_path):
            return vdf.parse(open(vdf_path))
        if vdf_data:
            return vdf.parse(vdf_data)
        return None

    def install(self, force=False):
        """
        Installs steamcmd if it is not already installed to self.install_path.
        :param force: forces steamcmd install regardless of its presence
        :return:
        """
        if not os.path.isfile(self.steamcmd_exe) or force is True:
            # Steamcmd isn't installed. Go ahead and install it.
            try:
                self._download_steamcmd()
            except SteamcmdException as e:
                return e

            try:
                self._extract_steamcmd()
            except SteamcmdException as e:
                return e
        else:
            raise SteamcmdException('Steamcmd is already installed. Reinstall is not necessary.'
                                    'Use force=True to override.')
        return

    def install_gamefiles(self, gameid, game_install_dir, user='anonymous', password=None, validate=False):
        """
        Installs gamefiles for dedicated server. This can also be used to update the gameserver.
        :param gameid: steam game id for the files downloaded
        :param game_install_dir: installation directory for gameserver files
        :param user: steam username (defaults anonymous)
        :param password: steam password (defaults None)
        :param validate: should steamcmd validate the gameserver files (takes a while)
        :return: subprocess call to steamcmd
        """
        if validate:
            validate = 'validate'
        else:
            validate = None

        steamcmd_params = (
            self.steamcmd_exe,
            '+login {} {}'.format(user, password),
            '+force_install_dir {}'.format(game_install_dir),
            '+app_update {}'.format(gameid),
            '{}'.format(validate),
            '+quit',
        )
        try:
            return subprocess.check_call(steamcmd_params)
        except subprocess.CalledProcessError:
            raise SteamcmdException("Steamcmd was unable to run. Did you install your 32-bit libraries?")

    def install_workshopfiles(self, gameid, workshop_id, game_install_dir, user='anonymous', password=None,
                              validate=False):
        """
        Installs gamefiles for dedicated server. This can also be used to update the gameserver.
        :param gameid: steam game id for the files downloaded
        :param workshop_id: id of workshop item to download
        :param game_install_dir: installation directory for gameserver files
        :param user: steam username (defaults anonymous)
        :param password: steam password (defaults None)
        :param validate: should steamcmd validate the gameserver files (takes a while)
        :return: subprocess call to steamcmd
        """
        if validate:
            validate = 'validate'
        else:
            validate = None

        steamcmd_params = (
            self.steamcmd_exe,
            '+login {} {}'.format(user, password),
            '+force_install_dir {}'.format(game_install_dir),
            '+workshop_download_item {} {}'.format(gameid, workshop_id),
            '{}'.format(validate),
            '+quit',
        )
        try:
            return subprocess.check_call(steamcmd_params)
        except subprocess.CalledProcessError:
            raise SteamcmdException("Steamcmd was unable to run. Did you install your 32-bit libraries?")

    def upload_workshopfiles(self, user, password, workshop_vdf_path=None, workshop_vdf=None):
        """
        Uploads workshop items in accordance to the workshop vdf file.
        :param workshop_vdf_path: path to workshop vdf file.
        :param workshop_vdf: Optional, vdf object See https://pypi.org/project/vdf/
        :param user: steam username (required valid user)
        :param password: steam password (required valid user password)
        """
        if workshop_vdf_path:
            vdf_data = self._parse_vdf(vdf_path=workshop_vdf_path)
        elif workshop_vdf:
            vdf_data = self._parse_vdf_text(vdf_data=workshop_vdf)

        with open("{install_path}/workshop.vdf".format(install_path=self.install_path), "w") as vdf_file:
            vdf.dumps(vdf_data, vdf_file)

        # Upload the workshop files
        steamcmd_params = (
            self.steamcmd_exe,
            '+login {} {}'.format(user, password),
            '+workshop_build_item',
            '{install_path}/workshop.vdf'.format(install_path=self.install_path),
            '+quit',
        )
        try:
            return subprocess.check_call(steamcmd_params)
        except subprocess.CalledProcessError:
            raise SteamcmdException("Steamcmd was unable to run. Did you install your 32-bit libraries?")
