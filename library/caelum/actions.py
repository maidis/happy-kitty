#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "} DESTINATION doc", "} DESTINATION share/doc/caelum")

    cmaketools.configure()

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
