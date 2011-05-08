#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/pixmaps", "data/icon/icon_highres.png", "usf.png")
    pisitools.insinto("/usr/share/applications", "ultimate-smash-friends.desktop")

    pisitools.dodoc("*.txt")
