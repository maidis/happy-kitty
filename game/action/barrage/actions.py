#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    autotools.automake("-afc")
    autotools.configure()

    pisitools.dosed("configure.in", "datadir/games/barrage", "datadir/barrage")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "barrage48.png", "barrage.png")

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")
