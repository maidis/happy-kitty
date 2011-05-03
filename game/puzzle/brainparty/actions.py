#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "brainparty"

def build():
    pisitools.dosed("Makefile", "-Wno-deprecated", "-Wno-deprecated %s" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "-lSDL_image", "-lSDL_image %s" % get.LDFLAGS())
    pisitools.dosed("Makefile", "^CXX=.*", "CXX=%s" % get.CXX())

    autotools.make()

def install():
    pisitools.dobin("brainparty", "/opt/brainparty")

    pisitools.insinto("/opt/brainparty/Content", "Content/*")

    pisitools.dodoc("COPYING", "CREDITS", "README")
