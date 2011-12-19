#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# def setup():
#     autotools.configure()

def build():
    shelltools.export("RESOURCE_PATH", "/usr/share/beret/")
    autotools.make()

def install():
    pisitools.dobin("beret")

    pisitools.insinto("/usr/share/beret/images", "images/*")
    pisitools.insinto("/usr/share/beret/music", "music/*")
    pisitools.insinto("/usr/share/beret/rooms", "rooms/*")
    pisitools.insinto("/usr/share/beret/sfx", "sfx/*")
    pisitools.insinto("/usr/share/beret/", "tahoma.ttf")

    # pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "NEWS", "README")
