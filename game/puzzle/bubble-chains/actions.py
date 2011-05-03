#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "chains-0.1.1-src"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    shelltools.chmod(get.installDIR() + "/usr/share/chains/data", 0644)

    pisitools.insinto("/usr/share/pixmaps", "images/icon256.png", "bubble-chains.png")

    pisitools.dodoc("README")
