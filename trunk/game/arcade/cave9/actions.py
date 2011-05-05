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
    shelltools.export("CFLAGS", "")
    shelltools.export("LDFLAGS", "")

    pisitools.dosed("src/GNUmakefile", "-Werror", "")
    pisitools.dosed("src/GNUmakefile", "--cflags`", "--cflags` %s" % get.CFLAGS())
    pisitools.dosed("src/GNUmakefile", "-lSDL_image", "-lSDL_image %s" % get.LDFLAGS())
    pisitools.dosed("src/GNUmakefile", "^CXX=.*", "CXX=%s" % get.CXX())

    autotools.make()

def install():
    pisitools.dobin("cave9")

    pisitools.insinto("/usr/share/cave9", "../data/*")

    pisitools.dodoc("*.txt")
