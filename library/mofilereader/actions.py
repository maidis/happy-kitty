#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.cd("build")
    cmaketools.configure("-DCOMPILE_DLL=ON")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.insinto("/usr/include", "include/*")
    pisitools.dolib_so("lib/libmoFileReader.so")
    pisitools.dohtml("reference/*")
    pisitools.dodoc("misc/BoxIcons_License.pdf", "misc/license.txt")
