#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def setup():
    shelltools.copy("./makefiles/makefile.linux1", "./makefile")

def build():
    autotools.make()

def install():
    pisitools.dolib_a("libalpng.a")

    pisitools.insinto("/usr/include/", "src/alpng.h")
    shelltools.chmod("%s/usr/include/alpng.h" % get.installDIR(), 0644)

    pisitools.dodoc("changes.txt")
    pisitools.dohtml("doc.html")
