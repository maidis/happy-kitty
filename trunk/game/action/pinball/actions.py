#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Copyright 2009-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial=["libtool"]

def setup():
    autotools.configure("--enable-shared \
                         --enable-static \
                         --prefix=/usr \
                         --disable-sdltest \
                         --with-x")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README")
