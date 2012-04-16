#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

WorkDir = "Mandarancio-OpenGOO-e3b79f7"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dobin("OpenGOO")

    pisitools.insinto("/usr/share/opengoo", "*level*")
    pisitools.insinto("/usr/share/opengoo", "menu.index")
    pisitools.insinto("/usr/share/opengoo/Artwork", "Artwork/*")

    pisitools.dodoc("LICENSE", "README")
