# Overview

# Setup

## Requirements

Install pysteamcmd with pip:

```sh
$ pip install pysteamcmd
```

or directly from the source code:

```sh
$ git clone https://github.com/f0rkz/pysteamcmd.git
$ cd pysteamcmd
$ python setup.py install
```

# Usage

After installation, the package can be imported and used to install and manage gameserver files:

```
>>> import pysteamcmd
>>> import os
>>> steamcmd_path = os.path.join('/','home','f0rkz','steamcmd')
>>> gameserver_path = os.path.join('/','home','f0rkz','mygameserver')
>>> steamcmd = pysteamcmd.Steamcmd(steamcmd_path)
>>> steamcmd.install()
True
>>> steamcmd.install_gamefiles(gameid=232330, game_install_dir=gameserver_path, user='anonymous', password=None, validate=True)
Redirecting stderr to '/home/f0rkz/steamcmd/logs/stderr.txt'
Looks like steam didn't shutdown cleanly, scheduling immediate update check
[  0%] Checking for available updates...
[  0%] Downloading update (0 of 10175 KB)...
[  0%] Downloading update (3376 of 10175 KB)...
[ 33%] Downloading update (5501 of 10175 KB)...
[ 54%] Downloading update (7624 of 10175 KB)...
[ 74%] Downloading update (9748 of 10175 KB)...
[ 95%] Downloading update (10175 of 10175 KB)...
[100%] Download complete.
[----] Installing update...
[----] Extracting package...
[----] Extracting package...
[----] Extracting package...
[----] Installing update...
[----] Installing update...
[----] Installing update...
[----] Cleaning up...
[----] Update complete, launching %appname%...
Redirecting stderr to '/home/f0rkz/steamcmd/logs/stderr.txt'
[  0%] Checking for available updates...
[----] Downloading update (0 of 7057 KB)...
[  0%] Downloading update (2137 of 7057 KB)...
[ 30%] Downloading update (3570 of 7057 KB)...
[ 50%] Downloading update (5002 of 7057 KB)...
[ 70%] Downloading update (6296 of 7057 KB)...
[ 89%] Downloading update (7057 of 7057 KB)...
[100%] Download complete.
[----] Installing update...
[----] Extracting package...
[----] Extracting package...
[----] Extracting package...
[----] Installing update...
[----] Installing update...
[----] Installing update...
[----] Cleaning up...
[----] Update complete, launching Steamcmd...
Redirecting stderr to '/home/f0rkz/steamcmd/logs/stderr.txt'
[  0%] Checking for available updates...
[----] Verifying installation...
Steam Console Client (c) Valve Corporation
-- type 'quit' to exit --
Loading Steam API...Created shared memory when not owner SteamController_Shared_mem
OK.

Connecting anonymously to Steam Public...Logged in OK
Waiting for license info...OK
    Update state (0x3) reconfiguring, progress: 0.00 (0 / 0)
    Update state (0x61) downloading, progress: 0.00 (4022 / 2284840496)
    Update state (0x61) downloading, progress: 1.47 (33674125 / 2284840496)
    Update state (0x61) downloading, progress: 3.40 (77714317 / 2284840496)
    Update state (0x61) downloading, progress: 5.10 (116511629 / 2284840496)
    Update state (0x61) downloading, progress: 6.36 (145424871 / 2284840496)
    Update state (0x61) downloading, progress: 7.33 (167444967 / 2284840496)
    Update state (0x61) downloading, progress: 10.08 (230359527 / 2284840496)
    Update state (0x61) downloading, progress: 12.78 (291997133 / 2284840496)
    Update state (0x61) downloading, progress: 15.33 (350367250 / 2284840496)
    Update state (0x61) downloading, progress: 18.04 (412233234 / 2284840496)
    Update state (0x61) downloading, progress: 19.97 (456273426 / 2284840496)
    Update state (0x61) downloading, progress: 21.65 (494684996 / 2284840496)
    Update state (0x61) downloading, progress: 23.44 (535579460 / 2284840496)
    Update state (0x61) downloading, progress: 24.86 (568085316 / 2284840496)
    Update state (0x61) downloading, progress: 24.96 (570182468 / 2284840496)
    Update state (0x61) downloading, progress: 24.96 (570182468 / 2284840496)
    Update state (0x61) downloading, progress: 26.10 (596396868 / 2284840496)
    Update state (0x61) downloading, progress: 26.52 (605834052 / 2284840496)
    Update state (0x61) downloading, progress: 27.30 (623659748 / 2284840496)
    Update state (0x61) downloading, progress: 28.48 (650769616 / 2284840496)
    Update state (0x61) downloading, progress: 29.66 (677730149 / 2284840496)
    Update state (0x61) downloading, progress: 31.13 (711284581 / 2284840496)
    Update state (0x61) downloading, progress: 32.42 (740644709 / 2284840496)
    Update state (0x61) downloading, progress: 32.51 (742741861 / 2284840496)
    Update state (0x61) downloading, progress: 32.51 (742741861 / 2284840496)
    Update state (0x61) downloading, progress: 33.59 (767584760 / 2284840496)
    Update state (0x61) downloading, progress: 34.35 (784937352 / 2284840496)
    Update state (0x61) downloading, progress: 35.46 (810103176 / 2284840496)
    Update state (0x61) downloading, progress: 36.79 (840511880 / 2284840496)
    Update state (0x61) downloading, progress: 38.67 (883501970 / 2284840496)
    Update state (0x61) downloading, progress: 40.23 (919153554 / 2284840496)
    Update state (0x61) downloading, progress: 41.61 (950813657 / 2284840496)
    Update state (0x61) downloading, progress: 42.85 (979125209 / 2284840496)
    Update state (0x61) downloading, progress: 44.28 (1011631065 / 2284840496)
    Update state (0x61) downloading, progress: 45.29 (1034699737 / 2284840496)
    Update state (0x61) downloading, progress: 46.52 (1063011289 / 2284840496)
    Update state (0x61) downloading, progress: 47.78 (1091603641 / 2284840496)
    Update state (0x61) downloading, progress: 49.24 (1125158073 / 2284840496)
    Update state (0x61) downloading, progress: 50.85 (1161861778 / 2284840496)
    Update state (0x61) downloading, progress: 52.70 (1204098614 / 2284840496)
    Update state (0x61) downloading, progress: 54.07 (1235382127 / 2284840496)
    Update state (0x61) downloading, progress: 55.17 (1260547951 / 2284840496)
    Update state (0x61) downloading, progress: 56.38 (1288228031 / 2284840496)
    Update state (0x61) downloading, progress: 58.49 (1336291743 / 2284840496)
    Update state (0x61) downloading, progress: 60.77 (1388412992 / 2284840496)
    Update state (0x61) downloading, progress: 62.50 (1427913512 / 2284840496)
    Update state (0x61) downloading, progress: 63.80 (1457642021 / 2284840496)
    Update state (0x61) downloading, progress: 65.10 (1487396657 / 2284840496)
    Update state (0x61) downloading, progress: 66.84 (1527171368 / 2284840496)
    Update state (0x61) downloading, progress: 68.68 (1569170292 / 2284840496)
    Update state (0x61) downloading, progress: 70.88 (1619533318 / 2284840496)
    Update state (0x61) downloading, progress: 72.69 (1660793181 / 2284840496)
    Update state (0x61) downloading, progress: 74.79 (1708838013 / 2284840496)
    Update state (0x61) downloading, progress: 75.39 (1722469501 / 2284840496)
    Update state (0x61) downloading, progress: 75.39 (1722469501 / 2284840496)
    Update state (0x61) downloading, progress: 76.46 (1746991720 / 2284840496)
    Update state (0x61) downloading, progress: 76.60 (1750137448 / 2284840496)
    Update state (0x61) downloading, progress: 76.67 (1751783050 / 2284840496)
    Update state (0x61) downloading, progress: 77.85 (1778682504 / 2284840496)
    Update state (0x61) downloading, progress: 78.86 (1801751482 / 2284840496)
    Update state (0x61) downloading, progress: 79.59 (1818528698 / 2284840496)
    Update state (0x61) downloading, progress: 80.85 (1847363192 / 2284840496)
    Update state (0x61) downloading, progress: 81.54 (1863091926 / 2284840496)
    Update state (0x61) downloading, progress: 82.45 (1883773660 / 2284840496)
    Update state (0x61) downloading, progress: 83.93 (1917612606 / 2284840496)
    Update state (0x61) downloading, progress: 85.58 (1955381097 / 2284840496)
    Update state (0x61) downloading, progress: 87.31 (1994933911 / 2284840496)
    Update state (0x61) downloading, progress: 89.62 (2047699106 / 2284840496)
    Update state (0x61) downloading, progress: 91.32 (2086518658 / 2284840496)
    Update state (0x61) downloading, progress: 91.50 (2090712962 / 2284840496)
    Update state (0x61) downloading, progress: 91.53 (2091224790 / 2284840496)
    Update state (0x61) downloading, progress: 92.60 (2115846060 / 2284840496)
    Update state (0x61) downloading, progress: 93.52 (2136818384 / 2284840496)
    Update state (0x61) downloading, progress: 94.42 (2157366218 / 2284840496)
    Update state (0x61) downloading, progress: 94.91 (2168451131 / 2284840496)
    Update state (0x61) downloading, progress: 94.91 (2168451131 / 2284840496)
    Update state (0x61) downloading, progress: 95.01 (2170904180 / 2284840496)
    Update state (0x61) downloading, progress: 95.15 (2174053630 / 2284840496)
    Update state (0x61) downloading, progress: 95.15 (2174053630 / 2284840496)
    Update state (0x61) downloading, progress: 95.46 (2181138751 / 2284840496)
    Update state (0x61) downloading, progress: 96.20 (2197916101 / 2284840496)
    Update state (0x61) downloading, progress: 97.29 (2222829813 / 2284840496)
    Update state (0x61) downloading, progress: 97.44 (2226375547 / 2284840496)
    Update state (0x81) committing, progress: 96.75 (2210543352 / 2284840496)
Success! App '232330' fully installed.
0
>>> quit()
f0rkz@test:~/mygameserver$ ls -lah
total 132K
drwxrwxr-x 7 f0rkz f0rkz   10 Mar 26 02:23 .
drwxr-xr-x 6 f0rkz f0rkz   12 Mar 26 02:16 ..
drwxrwxr-x 2 f0rkz f0rkz   28 Mar 26 02:23 bin
drwxrwxr-x 9 f0rkz f0rkz   26 Mar 26 02:23 cstrike
drwxrwxr-x 5 f0rkz f0rkz   15 Mar 26 02:23 hl2
drwxrwxr-x 6 f0rkz f0rkz    8 Mar 26 02:23 platform
-rwxrwxr-x 1 f0rkz f0rkz 8.0K Mar 26 02:23 srcds_linux
-rwxrwxr-x 1 f0rkz f0rkz 9.6K Mar 26 02:23 srcds_run
drwxrwxr-x 4 f0rkz f0rkz    6 Mar 26 02:23 steamapps
-rwxrwxr-x 1 f0rkz f0rkz  47K Mar 26 02:22 thirdpartylegalnotices.txt
```

You can upload items to the steam workshop:

```python
import pysteamcmd
import os

steamcmd_path = os.path.join('/','home','f0rkz','steamcmd')
steamcmd = pysteamcmd.Steamcmd(steamcmd_path)
steamcmd.install()
steamcmd.upload_workshopfiles(user='foo', password='bar', workshop_vdf_path='/home/f0rkz/workshop/project/myvdf.vdf')
```

This project is useful for designing gameserver control panels or the like. It is still under development and will be
updated as time goes by and new features are requested/supported.
