#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/nottetris2", "Not Tetris 2.love")

    shelltools.chmod("%s/usr/share/nottetris2/Not Tetris 2.love" % get.installDIR(), 0644)

    pisitools.dodoc("Not Readme.txt")
