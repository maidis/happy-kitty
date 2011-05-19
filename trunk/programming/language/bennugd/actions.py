#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("core")
    shelltools.chmod("./configure", 0755)
    autotools.configure()

    shelltools.cd("../modules")
    shelltools.chmod("./configure", 0755)
    autotools.configure()

def build():
    shelltools.cd("core")
    autotools.make()

    shelltools.cd("../modules")
    autotools.make()

def install():
    shelltools.cd("core")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

    shelltools.cd("../modules")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
