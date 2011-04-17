#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "jvgs-%s-src" % get.srcVERSION()

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release", installPrefix="/opt")

def build():
    cmaketools.make()

def install():
    pisitools.insinto("/opt/jvgs/resources", "resources/*")
    #pisitools.insinto("/opt/jvgs", "poems")
    pisitools.insinto("/opt/jvgs", "main.lua")
    pisitools.insinto("/opt/jvgs", "AUTHORS")
    pisitools.insinto("/opt/jvgs", "README*")
    pisitools.insinto("/opt/jvgs", "src/jvgs")

    shelltools.touch("./data.xml")
    pisitools.insinto("/opt/jvgs", "data.xml")
    shelltools.chmod("%s/opt/jvgs/data.xml" % get.installDIR(), 0666)

    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dodoc("AUTHORS", "poems", "README")
