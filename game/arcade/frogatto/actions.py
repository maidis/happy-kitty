#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make("game server")
    autotools.make("update-mo")

def install():
    pisitools.dobin("game", "/opt/frogatto")
    pisitools.dobin("server", "/opt/frogatto")

    pisitools.insinto("/opt/frogatto/data", "data/*")
    pisitools.insinto("/opt/frogatto/images", "images/*")
    pisitools.insinto("/opt/frogatto/music", "music/*")
    pisitools.insinto("/opt/frogatto/sounds", "sounds/*")
    pisitools.insinto("/opt/frogatto/locale", "locale/*")
    pisitools.insinto("/opt/frogatto", "FreeMono.ttf")
    pisitools.insinto("/opt/frogatto", "DejaVuSans.ttf")

    pisitools.dodoc("CHANGELOG","LICENSE")
