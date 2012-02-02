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

print '============================='
print 'BEGIN REMOVING GNOME PACKAGES'

def purge_packages(file):
    for line in open(file):
        print 'PURGING ' + line
        os.system('apt-get purge -y ' + line)

# The only_lmde_gnome.txt file in this repository contains the list of packages in
# LMDE GNOME but not LMDE Xfce.
# NOTE: libfam0 is kept because removing it causes a time-consuming upgrade of LibreOffice.
# NOTE: mint-meta-debian is kept because removing it takes out /usr/local/bin
purge_packages(dir_develop + "/remove-gnome/only_lmde_gnome.txt")

# Use the command "deborphan (package name)" to see dependants (includes recommended/suggested)
# Use the command "deborphan -n (package name)" to see dependants (ignores recommended/suggested)

# Remove Compiz packages
os.system('apt-get purge -y libdecoration0')

# Remove Totem packages (media player)
os.system('apt-get purge -y totem totem-common totem-mozilla totem-plugins mint-meta-codecs')
os.system('apt-get purge -y gstreamer0.10-pitfdll libtotem-plparser17')

# No Metacity packages remain

# Remove selected Nautlius packages
os.system('apt-get purge -y nautilus-gksu nautilus-open-terminal nautilus-sendto')

# Remove Pidgin packages (chat)
os.system('apt-get purge -y pidgin pidgin-data pidgin-facebookchat libpurple0 libpurple-bin')

# Remove Banshee (media player)
os.system('apt-get purge -y banshee')

# Remove Brasero
os.system('apt-get purge -y brasero brasero-common libbrasero-media0')

# Remove EOG (graphics viewer)
os.system('apt-get purge -y eog')

# Remove EVince (pdf viewer)
os.system('apt-get purge -y evince evince-common libevince2')

# Remove Evolution and dependants (mail suite)
os.system('apt-get purge -y python-evolution evolution-data-server-common libedataserverui1.2-8')
os.system('apt-get purge -y libcamel1.2-14 libebook1.2-9 libebook1.2-9 libedata-book1.2-2')
os.system('apt-get purge -y libcamel1.2-19 libebook1.2-10 deskbar-applet deskbar-applet mintmenu')
os.system('apt-get purge -y libebackend1.2-0 libedata-cal1.2-7 libecal1.2-8')
os.system('apt-get purge -y libedataserver1.2-13 libedataserver1.2-14 libegroupwise1.2-13')


# Remove GCalc (calculator)
os.system('apt-get purge -y gcalctool')

# Remove GEdit (editor)
os.system('apt-get purge -y gedit gedit-common')

# Remove Gmenu (menu editor)
os.system('apt-get purge -y gnome-menus')

# Remove GNOME About
os.system('apt-get purge -y gnome-about')

# Remove GNOME Character Map
os.system('apt-get purge -y gucharmap')

# Remove GNOME Dictionary
os.system('apt-get purge -y gnome-dictionary')

# Remove GNOME Disk Utility
os.system('apt-get purge -y gnome-disk-utility')

# Remove GNOME NetTool
os.system('apt-get purge -y gnome-nettool')

# Remove GNOME Network Manager
os.system('apt-get purge -y network-manager-gnome')

# Remove GNOME Search
os.system('apt-get purge -y gnome-search-tool')

# Remove GNOME Sound Recorder
os.system('apt-get purge -y gnome-media')

# Remove GNOME System Log
os.system('apt-get purge -y gnome-system-log')

# Remove GNOME System Monitor
os.system('apt-get purge -y gnome-system-monitor')

# Remove GNOME User Share
os.system('apt-get purge -y gnome-user-share')

#Remove gthumb (thumbnails)
os.system('apt-get purge -y gthumb gthumb-data')
     
# Remove gtk2-engines
os.system('apt-get purge -y gtk2-engines gtk2-engines-aurora gtk2-engines-candido')

# Remove Seahorse
os.system('apt-get purge -y seahorse')

# Remove Tomboy (note taking)
os.system('apt-get purge -y tomboy')

# Remove Yelp
os.system('apt-get purge -y gnome-doc-utils yelp')

# Applications to keep:
# Baobab
# GNOME-MPlayer
# Gecko Media Player


     




      



# Remove GNOME Desktop Environment (universe) and dependants
os.system('apt-get purge -y mint-x-icons mint-x-theme mint-artwork-debian')

# Remove GNOME Desktop Environment and dependants
# To see the list of installed packages, open Synaptic and go to Sections -> 
# GNOME Desktop Environment and sort by the first column.
# os.system('apt-get purge -y ')
os.system('apt-get purge -y at-spi python-pyatspi')
os.system('apt-get purge -y capplets-data')
os.system('apt-get purge -y gnome-audio')
os.system('apt-get purge -y gnome-desktop-data')
os.system('apt-get purge -y gnome-media-common libgnome-media0')
os.system('apt-get purge -y gnome-session-bin gnome-session-canberra gnome-session-common')
os.system('apt-get purge -y gnome-settings-daemon')
os.system('apt-get purge -y gnome-system-tools')
os.system('apt-get purge -y policykit-1-gnome libpolkit-gtk-1-0')
os.system('apt-get purge -y mintnanny') # MintNanny
      

      
      
      


      
      


      


# os.system('apt-get purge -y ')
# os.system('apt-get purge -y ')      

if os.path.exists('/usr/share/icons/gnome/icon-theme.cache'):
    print ('Removing /usr/share/icons/gnome/icon-theme.cache')
    os.remove('/usr/share/icons/gnome/icon-theme.cache')

print 'FINISHED REMOVING GNOME PACKAGES'
print '================================'
