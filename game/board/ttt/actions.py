#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("ttt.c", "images/", "/usr/share/ttt/images/")
    pisitools.dosed("ttt.c", "sounds/", "/usr/share/ttt/sounds/")
    autotools.make()

def install():
    pisitools.dobin("ttt")

    pisitools.insinto("/usr/share/ttt/images", "images/*")
    pisitools.insinto("/usr/share/ttt/sounds", "sounds/*")

    shelltools.chmod("%s/usr/share/ttt/images/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/ttt/sounds/*" % get.installDIR(), 0644)

    pisitools.dodoc("*.txt")
