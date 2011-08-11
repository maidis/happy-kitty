#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")
    shelltools.system("./confg")

def build():
    shelltools.cd("src")
    shelltools.system("./build")

def install():
    pisitools.dobin("bin/caph")

    pisitools.insinto("/usr/share/caph", "share/caph/*")

    pisitools.dosym("/usr/share/caph/icon.png", "/usr/share/pixmaps/caph.png")

    pisitools.dodoc("doc/caph/*")
