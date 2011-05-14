#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "FrozenCow-gish-14a41db"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    pisitools.insinto("/opt/gish/animation", "animation/*")
    pisitools.insinto("/opt/gish/level", "level/*")
    pisitools.insinto("/opt/gish/music", "music/*")
    # pisitools.insinto("/opt/gish/replay", "replay/*")
    pisitools.insinto("/opt/gish/sound", "sound/*")
    pisitools.insinto("/opt/gish/texture", "texture/*")
    
    pisitools.dobin("gish", "/opt/gish")
    
    pisitools.dodoc("COPYING.txt", "License.txt", "README.markdown")
