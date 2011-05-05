#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "capitan-1.0.3"

def build():
    #işi var daha bu paketin
    autotools.make("-j1 depsclean")
    autotools.make("-j1 deps")
    autotools.make("-j1")

def install():
    pisitools.dobin("capitan")
    pisitools.insinto("/usr/share/capitan/data", "data/*")
    pisitools.insinto("/usr/share/capitan/lang", "lang/*")
    pisitools.insinto("/usr/share/pixmaps", "extra/capitan.png")
    pisitools.insinto("/usr/share/applications", "extra/capitan.desktop")
    #pisitools.dodoc("docs/licen*", "readme*", "instructions.pdf")
