#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SecondLife-i686-%s" % get.srcVERSION()

def install():
    for secondlife in ["app_settings", "bin", "character", "etc", "fonts", "lib", "res-sdl", "skins"]:
        pisitools.insinto("/usr/share/SecondLife", secondlife)

    pisitools.insinto("/usr/share/pixmaps", "secondlife_icon.png", "secondlife.png")

    pisitools.insinto("/usr/share/SecondLife", "secondlife", "secondlife")

    pisitools.insinto("/usr/share/SecondLife", "featuretable_linux.txt", "featuretable_linux.txt")

    pisitools.insinto("/usr/share/SecondLife", "gpu_table.txt", "gpu_table.txt")

    pisitools.insinto("/usr/share/SecondLife", "licenses.txt", "licenses.txt")

    pisitools.insinto("/usr/share/SecondLife", "README-linux-joystick.txt", "README-linux-joystick.txt")

    pisitools.insinto("/usr/share/SecondLife", "README-linux-voice.txt", "README-linux-voice.txt")

    pisitools.insinto("/usr/share/SecondLife", "README-linux.txt", "README-linux.txt")

    pisitools.insinto("/usr/share/SecondLife", "summary.json", "summary.json")

    pisitools.dodoc("README-linux.txt", "README-linux-voice.txt", "licenses.txt", "README-linux-joystick.txt")