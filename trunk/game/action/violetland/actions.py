#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "violetland-v%s" % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/violetland/icon-light.png", "/usr/share/pixmaps/violetland.png")

    pisitools.dodoc("CHANGELOG", "README*")
