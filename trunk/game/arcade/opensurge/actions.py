#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "opensurge-src-build597"

def setup():
    shelltools.system("./configure")
    #cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dobin("opensurge")
    pisitools.insinto("/usr/share/opensurge/characters", "characters/*")
    pisitools.remove("/usr/share/opensurge/opensurge")
    pisitools.remove("/usr/share/opensurge/readme.html")
    pisitools.remove("/usr/share/opensurge/license.txt")

    pisitools.dodoc("readme.html", "bleeding_edge.txt", "license.txt")
