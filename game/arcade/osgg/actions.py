#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

WorkDir = "osgg"

def setup():
    autotools.make("clean")

    shelltools.cd("launcher")

    qt4.configure()

def build():
    autotools.make()

    shelltools.cd("launcher")

    qt4.make()

def install():
    pisitools.dobin("osgg")

    pisitools.dobin("launcher/launcher")
    pisitools.rename("/usr/bin/launcher", "osgg-launcher")

    pisitools.insinto("/usr/share/osgg/demos", "demos/*")
    pisitools.insinto("/usr/share/osgg/levels", "levels/*")
    pisitools.insinto("/usr/share/osgg", "*.txt")
    pisitools.insinto("/usr/share/osgg", "*.ogg")
    pisitools.insinto("/usr/share/osgg", "Bandal.ttf")
    pisitools.insinto("/usr/share/osgg", "icon.png")

    pisitools.dosym("/usr/share/osgg/icon.png", "/usr/share/pixmaps/osgg.png")

    pisitools.dodoc("README")
