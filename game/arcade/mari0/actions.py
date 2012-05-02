#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/mari0", "mari0_%s.love" % get.srcVERSION())
    pisitools.rename("/usr/share/mari0/mari0_%s.love" % get.srcVERSION(), "mari0.love")

    shelltools.chmod("%s/usr/share/mari0/mari0.love" % get.installDIR(), 0644)

    pisitools.dodoc("readme.txt")
