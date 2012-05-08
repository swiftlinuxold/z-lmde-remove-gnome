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

# THIS IS THE SCRIPT FOR REMOVING GNOME PACKAGES

# Use the command "deborphan (package name)" to see dependants (includes recommended/suggested)
# Use the command "deborphan -n (package name)" to see dependants (ignores recommended/suggested)

def message (string):
    os.system ('echo ' + string)

message ('=============================')
message ('BEGIN REMOVING GNOME PACKAGES')
message ('NOTE: The screen output is suppressed due to excessive volume.')

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

# ==========
# The only_lmde_gnome.txt file in this repository contains the list of packages in
# LMDE GNOME but not LMDE Xfce.

# NOTE: The removal of certain packages in LMDE with MATE/Cinnamon can cause problems with the X server in VirtualBox.
# Thus, the following packages are retained:
# virtualbox-guest-dkms
# virtualbox-guest-utils
# virtualbox-guest-x11
message ('Removing packages that come with LMDE GNOME but not LMDE Xfce')
purge_packages_file (dir_develop + "/remove-gnome/remove-deb/only_lmde_gnome.txt")
# ==========
# Replace MDM with LightDM
purge_packages ('mdm')
add_pkg ('lightdm')

# ==========
message ('Adding Geany as a replacement for Pluma')
add_pkg ('geany')
message ('Adding PCManFM as a replacement for Nautilus')
add_pkg ('pcmanfm')
message ('Adding IceWM and ROX as replacements for GNOME/MATE')
message ('Note that configuring IceWM and ROX comes later.')
add_pkg ('icewm rox-filer')
# ==========
message ('Creating the /usr/local/bin directory deleted in the GNOME removal process')
os.system ('mkdir /usr/local/bin')


message ('FINISHED REMOVING GNOME PACKAGES')
message ('================================')
