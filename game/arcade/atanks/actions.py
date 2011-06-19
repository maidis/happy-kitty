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
    autotools.rawInstall("PREFIX=%s/usr/ INSTALL=\"install -c\"" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "atanks.desktop")
    pisitools.insinto("/usr/share/pixmaps", "atanks.png")

    pisitools.dodoc("Changelog", "COPYING", "credits.txt", "README", "TODO")
