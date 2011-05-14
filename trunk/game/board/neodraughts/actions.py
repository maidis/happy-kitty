#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "NeoDraughts-0.3"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()

    pisitools.dosed("src/Makefile", "-I`sdl-config --cflags`", "-I/usr/include/SDL")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/doc")
    pisitools.dodoc("AUTHORS", "bugs.txt", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
