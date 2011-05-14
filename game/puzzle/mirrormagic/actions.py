#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile", "# RO_GAME_DIR = /usr/games", "RO_GAME_DIR = /usr/share/mirrormagic")
    pisitools.dosed("Makefile", "# RW_GAME_DIR = /var/games", "RW_GAME_DIR = /var/games")
    pisitools.dosed("Makefile", "TARGET=x11", "TARGET=sdl")

def build():
    autotools.make()

def install():
    pisitools.dobin("mirrormagic")

    pisitools.insinto("/usr/share/mirrormagic/graphics", "graphics/*")
    pisitools.insinto("/usr/share/mirrormagic/levels", "levels/*")
    pisitools.insinto("/usr/share/mirrormagic/music", "music/*")
    pisitools.insinto("/usr/share/mirrormagic/sounds", "sounds/*")

    pisitools.dodoc("CHANGES", "COPYING", "CREDITS", "mirrormagic-2.0.2.lsm", "README", "TODO")
