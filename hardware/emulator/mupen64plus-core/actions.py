#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("-C projects/unix all")

def install():
    pisitools.dolib("projects/unix/*.so*")

    pisitools.insinto("/usr/share/mupen64plus", "data/*")
    pisitools.insinto("/usr/include/mupen64plus", "src/api/m64p_*.h")

    pisitools.dodoc("LICENSES", "README", "RELEASE")
