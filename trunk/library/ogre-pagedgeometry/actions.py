#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ogre-paged-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("CMakeLists.txt", "} DESTINATION doc", "} DESTINATION share/doc/ogre-pagedgeometry")

    cmaketools.configure("-DPAGEDGEOMETRY_BUILD_SAMPLES=0")

def build():
    cmaketools.make("--silent")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("GettingStarted.txt", "Todo.txt", "docs/*.odt")
