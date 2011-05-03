#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dobin("bloqus")

    pisitools.insinto("/usr/share/pixmaps", "images/bloqus_icon_64.png", "bloqus.png")

    pisitools.dodoc("Licence_CeCILL_V2-en.txt")
