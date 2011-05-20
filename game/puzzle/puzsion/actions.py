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
    shelltools.unlink("puzsion.dcb")
    shelltools.chmod("./puzsion.gpe", 755)
    shelltools.system("./puzsion.gpe")

def install():
    pisitools.insinto("/usr/share/puzsion", "puzsion.dcb")
    pisitools.insinto("/usr/share/pixmaps", "puzsion.png")

    pisitools.dodoc("readme.txt")
