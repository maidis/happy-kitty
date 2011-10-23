#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SecondLife-i686-%s" % get.srcVERSION()

def install():
    for secondlife in ["app_settings", "bin", "character", "etc", "fonts", "lib", "res-sdl", "skins"]:
        pisitools.insinto("/opt/secondlife", secondlife)
    pisitools.insinto("/usr/share/pixmaps", "secondlife_icon.png", "secondlife.png")
    pisitools.insinto("/opt/secondlife", "secondlife")
    pisitools.insinto("/opt/secondlife", "gpu_table.txt")
    pisitools.dodoc("README-linux.txt", "README-linux-voice.txt", "licenses.txt", "README-linux-joystick.txt")
    