# Tutedude_Assignments
Assignments are written and demonstrated here.
1. File created.
2. cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost


3. xyzNBBLRBYGFJB4 MINGW64 ~/OneDrive - abc/Documents/My Folder/Tutedude_Assignments (main)                                                     
$ grep "localhost" /etc/hosts
# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost

4.# Zipping and Unzipping

## Compress Directory (Windows PowerShell)
```powershell
Compress-Archive -Path test_dir -DestinationPath test_dir.zip
Expand-Archive -Path test_dir.zip -DestinationPath unzipped_dir
o/p= test_dir.zip created
Files extracted inside unzipped_dir

5.# Downloading Files

## Command
```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/github/gitignore/main/README.md" -OutFile "sample.txt"

6.
# Changing Permissions

## Create File
```bash
touch secure.txt
``
change permission - chmod 444 secure.txt
ls -l secure.txt

-r--r--r-- 1 pkm00 1049089 0 May 11 22:45 secure.txt

7.

pkm00@NBBLRBYGFJB4 MINGW64 ~/OneDrive - Textron/Documents/My Folder/Tutedude_Assignments (main)
$ export MY_VAR="Hello, Linux!"

pkm00@NBBLRBYGFJB4 MINGW64 ~/OneDrive - Textron/Documents/My Folder/Tutedude_Assignments (main)                                                     
$ echo $MY_VAR
``
Hello, Linux!







