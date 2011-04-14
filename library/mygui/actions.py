#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "my-gui-4141"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DMYGUI_BUILD_SAMPLES:BOOL=OFF \
                          -DMYGUI_INSTALL_SAMPLES:BOOL=OFF \
                          -DMYGUI_BUILD_TOOLS:BOOL=OFF \
                          -DMYGUI_BUILD_PLUGINS:BOOL=OFF", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    # libMyGUI.OgrePlatform.a ?
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog.txt", "COPYING.LESSER", "Readme.txt")
