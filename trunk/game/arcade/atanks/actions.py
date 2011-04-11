#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("BINDIR=/usr/bin \
                    INSTALLDIR=/usr/share/atanks")

def install():
    pisitools.dobin("atanks")

    pisitools.insinto("/usr/share/atanks/button", "button/*")
    pisitools.insinto("/usr/share/atanks/misc", "misc/*")
    pisitools.insinto("/usr/share/atanks/missile", "missile/*")
    pisitools.insinto("/usr/share/atanks/sound", "sound/*")
    pisitools.insinto("/usr/share/atanks/stock", "stock/*")
    pisitools.insinto("/usr/share/atanks/tank", "tank/*")
    pisitools.insinto("/usr/share/atanks/tankgun", "tankgun/*")
    pisitools.insinto("/usr/share/atanks/text", "text/*")
    pisitools.insinto("/usr/share/atanks/title", "title/*")
    pisitools.insinto("/usr/share/atanks", "unicode.dat")
    pisitools.insinto("/usr/share/atanks", "credits.txt")

    #pisitools.dodesktop("atanks.desktop")
    #pisitools.doicon("atanks.png")
    pisitools.insinto("/usr/share/applications", "atanks.desktop")
    pisitools.insinto("/usr/share/pixmaps", "atanks.png")

    pisitools.dodoc("Changelog", "COPYING", "credits.txt", "README", "TODO")
