#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DMYGUI_BUILD_SAMPLES:BOOL=OFF \
                          -DMYGUI_INSTALL_SAMPLES:BOOL=OFF \
                          -DMYGUI_INSTALL_SAMPLES_SOURCE=ON \
                          -DMYGUI_BUILD_TOOLS:BOOL=OFF \
                          -DMYGUI_INSTALL_TOOLS:BOOL=ON \
                          -DMYGUI_INSTALL_MEDIA:BOOL=ON \
                          -DMYGUI_BUILD_PLUGINS:BOOL=ON \
                          -DMYGUI_INSTALL_DOCS:BOOL=ON", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    # libMyGUI.OgrePlatform.a ?
    # non-bin files in bin: plugins.cfg, resources.xml? opt?
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog.txt", "COPYING.LESSER", "Readme.txt")
