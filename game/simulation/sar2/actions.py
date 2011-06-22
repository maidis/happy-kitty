#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
    scons.make("SEARCHANDRESCUE2_DATA=/usr/share/sar2")

def install():
    pisitools.dobin("bin/sar2")

    pisitools.insinto("/usr/share/sar2", "data/*")
    pisitools.insinto("/usr/share/applications", "extra/sar2.desktop")
    pisitools.insinto("/usr/share/pixmaps", "extra/sar2.xpm")

    pisitools.dosym("/usr/share/pixmaps/sar2.xpm", "/usr/share/pixmaps/SearchAndRescue.xpm")

    pisitools.dodoc("AUTHORS", "CHANGELOG", "HACKING", "LICENSE", "README")
