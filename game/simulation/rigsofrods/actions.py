#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ror-2311"

def setup():
    cmaketools.configure("-DROR_BUILD_CONFIGURATOR=TRUE \
                          -DROR_BUILD_CONVERTER=TRUE \
                          -DROR_BUILD_SIM=TRUE \
                          -DROR_BUILD_TOOLS=TRUE \
                          -DROR_USE_MYGUI=TRUE \
                          -DROR_USE_OPENAL=TRUE \
                          -DROR_USE_SOCKETW=TRUE \
                          -DROR_USE_PAGED=TRUE \
                          -DROR_USE_CAELUM=TRUE \
                          -DROR_USE_ANGELSCRIPT=TRUE \
                          -DROR_USE_CURL=TRUE \
                          -DSOCKETW_INCLUDE_DIRS=/usr/include \
                          -DSOCKETW_LIBRARIES=/usr/lib/libSocketW.so \
                          -DMYGUI_INCLUDE_DIRS=/usr/include/MYGUI \
                          -DMYGUI_LIBRARIES=/usr/lib/libMyGUIEngine.so \
                          -DCMAKE_PREFIX_PATH=/opt/rigsofrods")

def build():
    cmaketools.make()

def install():
    #not works for now
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/opt/rigsofrods/resources", "bin/resources/*")

    pisitools.dobin("bin/RoR", "/opt/rigsofrods")
    pisitools.dobin("bin/rorconfig", "/opt/rigsofrods")
    pisitools.dobin("bin/tdr2svg", "/opt/rigsofrods")

    pisitools.dolib_a("bin/libangelscript_addons.a", "/opt/rigsofrods")

    #pisitools.insinto("/opt/rigsofrods", "bin/plugins.cfg")

    pisitools.dodoc("COPYING", "LICENSE.txt", "readme.txt")
