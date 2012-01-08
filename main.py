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
# Use the command "deborphan (package name)" to see dependants (includes recommended/suggested)
# Use the command "deborphan -n (package name)" to see dependants (ignores recommended/suggested)
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
os.system('apt-get purge -y gnome-about') 
os.system('apt-get purge -y gnome-audio') 
os.system('apt-get purge -y gnome-colors-common gnome-wise-icon-theme shiki-wise-theme') 
os.system('apt-get purge -y gnome-desktop-data') 
os.system('apt-get purge -y gnome-dictionary gnome-utils') 
os.system('apt-get purge -y gnome-doc-utils yelp gnome-user-guide') 
os.system('apt-get purge -y gnome-media gnome-media-common libgnome-media0') 
# Keeping gnome-keyring
os.system('apt-get purge -y gnome-menus alacarte') 
# Keeping gnome-mime-data due to several dependants
os.system('apt-get purge -y gnome-netstatus-applet') 
os.system('apt-get purge -y gnome-panel-data') 
os.system('apt-get purge -y gnome-screensaver') 
os.system('apt-get purge -y gnome-screenshot')
os.system('apt-get purge -y gnome-search-tool')      
os.system('apt-get purge -y gnome-session-bin') 
os.system('apt-get purge -y gnome-session-canberra')    
os.system('apt-get purge -y gnome-session-common') 
os.system('apt-get purge -y gnome-system-log') 
os.system('apt-get purge -y gnome-system-monitor') 
os.system('apt-get purge -y gnome-system-tools') 
os.system('apt-get purge -y gnome-terminal') 
os.system('apt-get purge -y gnome-terminal-data') 
os.system('apt-get purge -y gnome-themes') 
# Keeping gparted
# Keeping gsettings-desktop-schemas due to many dependants
os.system('apt-get purge -y gthumb-data') 
os.system('apt-get purge -y gtk2-engines') 
os.system('apt-get purge -y gtk2-engines-aurora') 
os.system('apt-get purge -y gtk2-engines-candido') 
os.system('apt-get purge -y gucharmap')
os.system('apt-get purge -y gvfs-backends')
os.system('apt-get purge -y gvfs-bin')
# Keeping libbonobo2-common due to many dependants
os.system('apt-get purge -y libgnome-menu2 libslab0a libgnome-window-settings1 python-gmenu compiz-gnome')
os.system('apt-get purge -y mousetweaks')
os.system('apt-get purge -y nautilus-actions')
os.system('apt-get purge -y nautilus-data')
os.system('apt-get purge -y nautilus-open-terminal')
os.system('apt-get purge -y seahorse')
os.system('apt-get purge -y shiki-colors-metacity-theme')
# Keeping system-config-printer-udev due to several dependants
os.system('apt-get purge -y tomboy')

# Remove Metacity packages
# In Synaptic, go to Status -> Installed, enter "metacity" in quick filter
os.system('apt-get purge -y compiz-gtk')
os.system('apt-get purge -y libmetacity-private0 metacity metacity-common')

# Remove Compiz packages
# In Synaptic, go to Status -> Installed, enter "compiz" in quick filter
os.system('apt-get purge -y compiz-plugins compiz-core libcompizconfig0 python-compizconfig compizconfig-backend-gconf compizconfig-settings-manager')
os.system('apt-get purge -y libdecoration0')

# Remove Totem packages
# In Synaptic, go to Status -> Installed, enter "totem" in quick filter
os.system('apt-get purge -y totem totem-mozilla totem-plugins')
os.system('apt-get purge -y totem-common')
os.system('apt-get purge -y libtotem-plparser17 gstreamer0.10-pitfdll')

# Remove GNOME packages not specifically in the GNOME section
# In Synaptic, go to Status -> Installed, enter "GNOME" in quick filter, and sort by section.
# Section: admin
os.system('apt-get purge -y gdebi')
os.system('apt-get purge -y gnome-disk-utility')
os.system('apt-get purge -y mintdesktop')
os.system('apt-get purge -y system-tools-backends liboobs-1-4')
# Keeping libpam-gnome-keyring
# Section: cli-mono
os.system('apt-get purge -y libart2.0-cil libgnome2.24-cil libgnomepanel2.24-cil giver')
os.system('apt-get purge -y libgconf2.0-cil')
# Keeping libglib2.0-cil due to many dependants
# Keeping libgnome-keyring1.0-cil
os.system('apt-get purge -y libgnome-vfs2.0-cil')
# Section: libs
os.system('apt-get purge -y gconf-defaults-service gconf-editor')
# Keeping gconf2, gconf2-common due to many dependants
# Keeping gnome-utils-common due to baobab dependant
os.system('apt-get purge -y gstreamer0.10-gnomevfs')
# Keeping libatspi1.0-0
# Keeping libbonoboui2-0 and libbonoboui2-common due to numerous dependants
os.system('apt-get purge -y libcryptui0a')
# Keeping libfm-gtk0 and libfm0 due to pcmanfm dependant
# Keeping libgail-common, libgail-gnome-module, and libgail18
# Keeping libgconf2-4 due to numerous dependants
os.system('apt-get purge -y libgdict-1.0-6')
# Keeping libgdu0 due to several dependants
# Keeping libglib2.0-0, libglib2.0-data, and libglibmm-2.4-1c2a due to many dependants
os.system('apt-get purge -y libgnome-bluetooth7 libgnome-desktop-2-17 python-gnomedesktop')
# Keeping libgnome-keyring0
os.system('apt-get purge -y libgnome-mag2 gnome-mag')
os.system('apt-get purge -y libgnome-speech7')
# Keeping libgnome2-0 and libgnome2-common due to many dependants
# Keeping libgnomecanvas2-0 due to many dependants
os.system('apt-get purge -y libgnomekbd-common libgnomekbd4')
# Keeping libgnomeui-0 and libgnomeui-common due to many dependants
os.system('apt-get purge -y libgnomekbd-common libgsf-1-common libgsf-1-114')
# Keeping libgtop2-7 and libgtop2-common due to baobab among dependants
# Keeping libmenu-cache1 due to several dependants
# Keeping libnautilus-extension1 due to many dependants
# Keeping libpanel-applet2-0 due to many dependants
# Keeping libpisock9 due to sylpheed as dependant
os.system('apt-get purge -y libseed0')
# Keeping libsoup-gnome2.4-1 and libsoup2.4-1 due to too many dependants
# Keeping libstart-notification0 due to to many dependants
# Keeping libxml2 due to many dependants
# Section: oldlibs
# Keeping libgnomevfs2-0, libgnomevfs2-common, and libgnomevfs2-extra due to dependants
# Section: interpreters
os.system('apt-get purge -y gnome-js-common')
# Section: math
os.system('apt-get purge -y gcalctool')
# Section: net
os.system('apt-get purge -y gnome-ppp network-manager-pptp-gnome')
# Section: video
os.system('apt-get purge -y gnome-mplayer gecko-mediaplayer')

      









      






# Remove remaining Nautilus packages
# os.system('apt-get purge -y nautilus-gksu')

# os.system('apt-get purge -y ')




print 'FINISHED REMOVING GNOME PACKAGES'
print '================================'
