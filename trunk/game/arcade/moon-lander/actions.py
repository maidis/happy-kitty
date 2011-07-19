#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "moon-lander"

def setup():
    shelltools.unlink("%s/moon-lander/moon-lander.bin" % get.workDIR())

def build():
    autotools.make()

def install():
    pisitools.dobin("moon-lander")

    pisitools.insinto("/usr/share/moon-lander/fonts", "fonts/*")
    pisitools.insinto("/usr/share/moon-lander/images", "images/*")
    pisitools.insinto("/usr/share/moon-lander/sounds", "sounds/*")
    pisitools.insinto("/usr/share/pixmaps", "debian/moon-lander.xpm")

    shelltools.chmod("%s/usr/share/moon-lander/fonts/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/moon-lander/images/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/moon-lander/images/backgrounds/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/moon-lander/images/kablam/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/moon-lander/sounds/*" % get.installDIR(), 0644)

    pisitools.doman("debian/moon-lander.6")

    pisitools.dodoc("README.txt")
