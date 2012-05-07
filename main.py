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

# Using MDM instead of LightDM for now.
# LightDM worked with the 201109 version of LMDE but does not work with the 201204 version.
# In the interest of expediency, sticking with the default MDM is better.
# Fortunately, much of the MDM bloat consists of help pages for languages other than English.
# This bloat is removed in the "final" repository.
# ==========
message ('Adding Geany as a replacement for Pluma')
add_pkg ('geany')
message ('Adding PCManFM as a replacement for Nautilus')
add_pkg ('pcmanfm')
message ('Adding IceWM and ROX as replacements for GNOME/MATE')
message ('Note that configuring IceWM and ROX comes later.')
add_pkg ('icewm rox-filer')

# ==========
# The only_lmde_gnome.txt file in this repository contains the list of packages in
# LMDE GNOME but not LMDE Xfce.
message ('Removing packages that come with LMDE GNOME but not LMDE Xfce')
purge_packages_file (dir_develop + "/remove-gnome/remove-deb/only_lmde_gnome.txt")

# ==========
message ('Creating the /usr/local/bin directory deleted in the GNOME removal process')
os.system ('mkdir /usr/local/bin')

message ('FINISHED REMOVING GNOME PACKAGES')
message ('================================')
