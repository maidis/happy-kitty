#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

arch = "amd64" if get.ARCH() == "x86_64" else "i586"
WorkDir = "%s/jogl-1.1.1-linux-%s" % (get.ARCH(), arch)
NoStrip = "/"

def install():
    pisitools.insinto("/usr/share/java/jogl", "lib/*.jar")
    pisitools.dolib("lib/*.so")

    pisitools.dodoc("*.txt")
    pisitools.dohtml("*.html")
