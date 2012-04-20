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

def message (string):
    os.system ('echo ' + string)

message ('=============================')
message ('BEGIN REMOVING GNOME PACKAGES')
message ('NOTE: The screen output is suppressed due to excessive volume.')

def purge_packages_file (filename):
    list_with_newlines = open(filename, 'r').read()
    list_with_spaces = list_with_newlines.replace ('\n', ' ')
    os.system ('apt-get purge -qq ' + list_with_spaces)
        
def purge_packages (packages):
    os.system ('echo PURGING ' + packages)
    os.system ('apt-get purge -qq ' + packages)

# Remove Compiz packages
purge_packages ('gdm3')

# The only_lmde_gnome.txt file in this repository contains the list of packages in
# LMDE GNOME but not LMDE Xfce.
# NOTE: libfam0 is kept because removing it causes a time-consuming upgrade of LibreOffice.
# NOTE: mint-meta-debian and mint-info-debian are kept because removing them takes out /usr/local/bin
message ('Removing packages that come with LMDE GNOME but not LMDE Xfce')
purge_packages_file (dir_develop + "/remove-gnome/only_lmde_gnome.txt")

# Use the command "deborphan (package name)" to see dependants (includes recommended/suggested)
# Use the command "deborphan -n (package name)" to see dependants (ignores recommended/suggested)

# Remove Compiz packages
purge_packages ('libdecoration0')

# Remove Totem packages (media player)
purge_packages ('totem totem-common totem-mozilla totem-plugins mint-meta-codecs')
purge_packages ('gstreamer0.10-pitfdll libtotem-plparser17')

# No Metacity packages remain

# Remove selected Nautlius packages
purge_packages ('nautilus-gksu nautilus-open-terminal nautilus-sendto')

# Remove Pidgin packages (chat)
purge_packages ('pidgin pidgin-data pidgin-facebookchat libpurple0 libpurple-bin')

# Remove Banshee (media player)
purge_packages ('banshee')

# Remove Brasero
purge_packages ('brasero brasero-common libbrasero-media0')

# Remove EOG (graphics viewer)
purge_packages ('eog')

# Remove EVince (pdf viewer)
purge_packages ('evince evince-common libevince2')

# Remove Evolution and dependants (mail suite)
purge_packages ('python-evolution evolution-data-server-common libedataserverui1.2-8')
purge_packages ('libcamel1.2-14 libebook1.2-9 libebook1.2-9 libedata-book1.2-2')
purge_packages ('libcamel1.2-19 libebook1.2-10 deskbar-applet deskbar-applet mintmenu')
purge_packages ('libebackend1.2-0 libedata-cal1.2-7 libecal1.2-8')
purge_packages ('libedataserver1.2-13 libedataserver1.2-14 libegroupwise1.2-13')

# Remove other Evolution packages
purge_packages ('libbeagle1 python-beagle')
purge_packages ('libcamel-1.2-29 libebook-1.2-12 libedata-book-1.2-11')
purge_packages ('libebackend-1.2-1 libedata-cal-1.2-13 libecal-1.2-10')
purge_packages ('libedataserver-1.2-15')
purge_packages ('libgdata1.2-1 libgdata-google1.2-1')

      

      



# Remove GCalc (calculator)
purge_packages ('gcalctool')

# Remove GEdit (editor)
purge_packages ('gedit gedit-common')

# Remove Gmenu (menu editor)
purge_packages ('gnome-menus')

# Remove GNOME About
purge_packages ('gnome-about')

# Remove GNOME Character Map
purge_packages ('gucharmap')

# Remove GNOME Dictionary
purge_packages ('gnome-dictionary')

# Remove GNOME Disk Utility
purge_packages ('gnome-disk-utility')

# Remove GNOME NetTool
purge_packages ('gnome-nettool')

# Remove GNOME Search
purge_packages ('gnome-search-tool')

# Remove GNOME Sound Recorder
purge_packages ('gnome-media')

# Remove GNOME System Log
purge_packages ('gnome-system-log')

# Remove GNOME System Monitor
purge_packages ('gnome-system-monitor')

# Remove GNOME User Share
purge_packages ('gnome-user-share')

# Remove gthumb (thumbnails)
purge_packages ('gthumb gthumb-data')
     
# Remove gtk2-engines
purge_packages ('gtk2-engines gtk2-engines-aurora gtk2-engines-candido')

# Remove Seahorse
purge_packages ('seahorse')

# Remove Tomboy (note taking)
purge_packages ('tomboy')

# Remove Yelp
purge_packages ('gnome-doc-utils yelp')

# Remove Zenity
purge_packages ('zenity')

# Remove GNOME Desktop Environment (universe) and dependants
purge_packages ('mint-x-icons mint-x-theme')

# Remove GNOME Desktop Environment and dependants
# To see the list of installed packages, open Synaptic and go to Sections -> 
# GNOME Desktop Environment and sort by the first column.
purge_packages ('at-spi python-pyatspi')
purge_packages ('capplets-data')
purge_packages ('gnome-audio')
purge_packages ('gnome-desktop-data')
purge_packages ('gnome-media-common libgnome-media0')
purge_packages ('gnome-session-bin gnome-session-canberra gnome-session-common')
purge_packages ('gnome-settings-daemon')
purge_packages ('gnome-system-tools')
purge_packages ('policykit-1-gnome libpolkit-gtk-1-0')
purge_packages ('mintnanny') # MintNanny      

# GNOME Network Manager
purge_packages ('network-manager network-manager-pptp network-manager-pptp-gnome') 
purge_packages ('libnm-glib-vpn1 libnm-glib2 libnm-glib4 libnm-util1 libnm-util2')

# Applications to keep:
# Baobab
# GNOME-MPlayer
# Gecko Media Player     
      
if os.path.exists('/usr/share/icons/gnome/icon-theme.cache'):
    print ('Removing /usr/share/icons/gnome/icon-theme.cache')
    os.remove('/usr/share/icons/gnome/icon-theme.cache')

os.system ('echo FINISHED REMOVING GNOME PACKAGES')
os.system ('echo ================================')
