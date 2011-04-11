#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
