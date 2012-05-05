#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR REPLACING THE MDM DISPLAY MANAGER

def message (string):
    os.system ('echo ' + string)

def add_pkg (packages):
    os.system ('echo INSTALLING ' + packages)
    os.system ('apt-get install -qq ' + packages)

def purge_packages_file (filename):
    list_with_newlines = open(filename, 'r').read()
    list_with_spaces = list_with_newlines.replace ('\n', ' ')
    os.system ('apt-get purge -qq ' + list_with_spaces)
        
def purge_packages (packages):
    os.system ('echo PURGING ' + packages)
    os.system ('apt-get purge -qq ' + packages)

os.system ('python ' + dir_develop + '/apt/main.py')
os.system ('update-rc.d -f mdm remove')
purge_packages ('mdm')

message ('Adding Geany, IceWM, ROX, and PCManFM to provide a usable desktop in the absence of GNOME')
message ('Configuration comes later')
add_pkg ('geany icewm rox-filer pcmanfm')
message ('Adding LightDM')
add_pkg ('lightdm')
message ('Enabling LightDM')
os.system ('dpkg-reconfigure lightdm')


