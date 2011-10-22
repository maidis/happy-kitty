#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons

WorkDir="pink-pony"

def build():
    pisitools.dosed("install/pink-pony", "/usr/share/pink-pony", "/opt/pink-pony")
    pisitools.dosed("install/pink-pony", "./Pony $1", "pasuspender ./Pony $1")
    pisitools.dosed("install/pink-pony", "./Pony ~/", "pasuspender ./Pony ~/")

    scons.make()

def install():
    pisitools.dobin("./install/pink-pony")
    pisitools.dobin("Pony", "/opt/pink-pony")

    pisitools.insinto("/opt/pink-pony/GLSL", "GLSL/*")
    pisitools.insinto("/opt/pink-pony/fonts", "fonts/*")
    pisitools.insinto("/opt/pink-pony/levels", "levels/*")
    pisitools.insinto("/opt/pink-pony/models", "models/*")
    pisitools.insinto("/opt/pink-pony/music", "music/*")
    pisitools.insinto("/opt/pink-pony/textures", "textures/*")
    pisitools.insinto("/opt/pink-pony", "pony.options")
    pisitools.insinto("/opt/pink-pony", "levels.xml")

    pisitools.dodoc("README")
