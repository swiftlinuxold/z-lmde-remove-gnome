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

# Remove GNOME Desktop Environment (universe) and dependants
os.system('apt-get purge -y mint-x-icons mint-x-theme mint-artwork-debian')

# Remove GNOME Desktop Environment and dependants
# To see the list of installed packages, open Synaptic and go to Sections -> 
# GNOME Desktop Environment and sort by the first column.
os.system('apt-get purge -y brasero banshee nautilus')
os.system('apt-get purge -y brasero-common brasero libbrasero-media0')
os.system('apt-get purge -y eog')
os.system('apt-get purge -y evince evince-common')
os.system('apt-get purge -y gnome-applets gnome-panel')  
os.system('apt-get purge -y gnome-applets-data') 
os.system('apt-get purge -y gnome-bluetooth gnome-user-share network-manager-gnome nautilus-sendto') 
# Keeping gnome-icon-theme due to dependants
os.system('apt-get purge -y gnome-nettool') 
os.system('apt-get purge -y gnome-power-manager') 
os.system('apt-get purge -y gnome-settings-daemon') 
os.system('apt-get purge -y libevolution') 
# Keeping libreoffice-gnome, libreoffice-gtk, and policykit-1-gnome due to dependants
# Keeping simple-scan
os.system('apt-get purge -y vino') 
# Keeping zenity for its use in some scripts
# Keeping at-spi for its utility for the disabled and its light footprint
# Keeping baobab (graphical display of disk space usage)
os.system('apt-get purge -y capplets-data') 
# Keeping cups-pk-helper due to need for CUPS
os.system('apt-get purge -y deskbar-applet mintmenu mint-meta-common') 
os.system('apt-get purge -y dmz-cursor-theme') 
os.system('apt-get purge -y evolution-data-server python-evolution pidgin') 
os.system('apt-get purge -y evolution-data-server-common libedataserverui1.2-8 libedataserverui1.2-11') 
# Keeping file-roller for working with *.zip, *.tar, and other archives
os.system('apt-get purge -y gedit gedit-common') 


      
      
      
      



print 'FINISHED REMOVING GNOME PACKAGES'
print '================================'
