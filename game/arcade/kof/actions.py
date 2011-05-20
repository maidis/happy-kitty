#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", "%s" % get.workDIR())

def build():
    shelltools.system("./build.sh")

def install():
    pisitools.insinto("/usr/share/kof", "kofv5.dcb")
    pisitools.insinto("/usr/share/pixmaps", "kof.png")

    pisitools.dodoc("manual.txt")
