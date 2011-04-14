#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sdk/angelscript/projects/gnuc"

def build():
    autotools.make()
    autotools.make("SHARED=1 VERSION=2.20.2")

def install():
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s SHARED=1 VERSION=2.20.2" % get.installDIR())

    pisitools.dohtml("../../../docs/*")
