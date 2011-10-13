#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "pardus_flags", "%s" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dolib_a("lib/linux/libalfont.a")

    pisitools.insinto("/usr/include", "include/alfont*.h")

    pisitools.dodoc("CHANGES.txt", "README.txt", "docs/*")
