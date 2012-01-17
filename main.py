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
else:
	dir_develop='/home/'+uname+'/develop'

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

# THIS IS THE SCRIPT FOR REMOVING GNOME PACKAGES

print '============================='
print 'BEGIN REMOVING GNOME PACKAGES'

def purge_packages(file):
    for line in open(file):
        os.system('apt-get purge -y ' + line)

# The only_lmde_gnome.txt file in this repository contains the list of packages in
# LMDE GNOME but not LMDE Xfce.
# NOTE: libfam0 is kept because removing it causes a time-consuming upgrade of LibreOffice.
purge_packages(dir_develop + "/ui-gnome/only_lmde_gnome.txt")

print 'FINISHED REMOVING GNOME PACKAGES'
print '================================'
