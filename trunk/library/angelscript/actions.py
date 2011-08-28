#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "angelscript/projects/gnuc"

def build():
    autotools.make()
    autotools.make("SHARED=1 VERSION=%s" % get.srcVERSION())

def install():
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s SHARED=1 VERSION=%s" % (get.installDIR(), get.srcVERSION()))

    shelltools.chmod("%s/usr/include/*" % get.installDIR(), 0644)

    pisitools.dohtml("../../../docs/*")
