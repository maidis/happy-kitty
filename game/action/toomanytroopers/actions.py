#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "TooManyTroopers"

def build():
    shelltools.system("g++ *.cpp -c")
    shelltools.system("g++ *.o -o toomanytroopers -lSDL -lSDL_mixer -lGL")

def install():
    pisitools.dobin("toomanytroopers")
    pisitools.insinto("/usr/share/toomanytroopers", "data/*")
    pisitools.dodoc("about.txt", "gpl-3.0.txt")

    shelltools.chmod("%s/usr/share/toomanytroopers/sounds/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/toomanytroopers/textures/*" % get.installDIR(), 0644)
