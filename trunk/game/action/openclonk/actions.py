#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "openclonk-release-%s-src" % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # pisitools.dobin("clonk", "/opt/openclonk")
    # pisitools.insinto("/opt/openclonk", "planet/*")
    # pisitools.remove("/opt/openclonk/AUTHORS")
    # pisitools.remove("/opt/openclonk/COPYING")
    pisitools.insinto("/usr/share/applications", "clonk.desktop")
    pisitools.insinto("/usr/share/pixmaps", "planet/Graphics.ocg/Player.png", "clonk.png")

    pisitools.dodoc("Credits.txt", "README.linux.txt", "licenses/*", "planet/AUTHORS", "planet/COPYING")
