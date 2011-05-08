#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "battle/Battle"

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod("%s/opt/smashbattle/gfx/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/opt/smashbattle/music/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/opt/smashbattle/sfx/*" % get.installDIR(), 0644)
    shelltools.chmod("%s/opt/smashbattle/stage/*" % get.installDIR(), 0644)

    pisitools.insinto("/usr/share/pixmaps", "gfx/SB.png", "smashbattle.png")
    pisitools.insinto("/usr/share/applications", "linux/smashbattle.desktop")

    shelltools.chmod("%s/usr/share/pixmaps/smashbattle.png" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/share/applications/smashbattle.desktop" % get.installDIR(), 0644)
    # I'm crying now, know?
