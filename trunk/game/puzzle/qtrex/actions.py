#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

WorkDir = "QTrex"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dobin("QTrex")

    pisitools.insinto("/usr/share/pixmaps", "main.PNG", "qtrex.png")

    shelltools.chmod(get.installDIR() + "/usr/share/pixmaps/qtrex.png", 0644)
