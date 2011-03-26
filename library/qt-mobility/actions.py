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
    # this must be autotools, look gentoo package
    shelltools.system("./configure -prefix /usr \
                                   -plugindir /usr/lib/qt4/plugins \
                                   -silent")

def build():
    # need test and then remove -j1
    autotools.make("-j1")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    # documentation not installed
    pisitools.dodoc("changes-1.1.1", "LGPL_EXCEPTION.txt", "LICENSE.FDL", "LICENSE.LGPL")
