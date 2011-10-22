#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dobin("opentyrian")

    pisitools.insinto("/usr/share/applications", "linux/opentyrian.desktop")
    pisitools.insinto("/usr/share/pixmaps", "linux/icons/tyrian-128.png", "opentyrian.png")

    pisitools.doman("linux/man/opentyrian.6")

    pisitools.dodoc("COPYING", "CREDITS", "NEWS", "README")

    pisitools.insinto("/usr/share/opentyrian/data", "../tyrian21/*")

    pisitools.remove("/usr/share/opentyrian/data/*.exe")
