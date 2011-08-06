#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def build():
    pisitools.dosed("Makefile", "/usr/local", "/usr/")
    pisitools.dosed("Makefile", "-llualib", "")
    pisitools.dosed("Makefile", "-llua5.1", "-llua")

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("documents/*")
