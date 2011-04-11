#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "alienblaster"

def build():
    autotools.make()

def install():
    pisitools.dobin("alienBlaster")
    pisitools.insinto("/usr/share/alienblaster/cfg", "cfg/*")
    pisitools.insinto("/usr/share/alienblaster/images", "images/*")
    pisitools.insinto("/usr/share/alienblaster/sound", "sound/*")
    pisitools.dodoc("AUTHORS", "CHANGELOG", "LICENSE", "README")
