#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "gfx/oki40.png", "oki.png")
    pisitools.insinto("/usr/share/applications", "extra/oki.desktop")

    pisitools.domove("/usr/share/oki/oki", "/usr/bin")
    pisitools.domove("/usr/share/oki/oki_me", "/usr/bin")

    pisitools.dodoc("CHANGELOG", "COPYING", "README", "TODO")
