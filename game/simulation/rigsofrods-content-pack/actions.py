#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
Dirs = ["aircraft",  "cars", "extra-terrains", "misc-land", "terrains", "trucks",
        "buses", "crawlers", "loads", "offroad-vehicles", "testing", "vehicles"]


def install():
    for Dir in Dirs:
        pisitools.insinto("/opt/rigsofrods/packs/%s" % Dir, "streams/%s/*" % Dir)

        shelltools.chmod("%s/opt/rigsofrods/packs/%s/*.zip" % (get.installDIR(), Dir), 0644)

    pisitools.dodoc("readme-content-pack-0.37.txt")
