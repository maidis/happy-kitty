#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    # not works yet
    # qt4.install()
    pisitools.dobin("Ballway", "/opt/ballway")

    pisitools.insinto("/opt/ballway/audio", "audio/*")
    pisitools.insinto("/opt/ballway/graphics", "graphics/*")
    pisitools.insinto("/opt/ballway/screens", "screens/*")
    pisitools.insinto("/opt/ballway/specs", "specs/*")
    pisitools.insinto("/opt/ballway/ts", "ts/*")
    pisitools.insinto("/opt/ballway/icons", "icons/*") # :)

    shelltools.chmod(get.installDIR() + "/opt/ballway/graphics/ball.png", 0644)

    pisitools.dosym("/opt/ballway/icons/ballway_128.png", "/usr/share/pixmaps/ballway.png")

    pisitools.dodoc("copying.txt", "README")
