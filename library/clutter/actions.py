#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    autotools.autoreconf("-vfi")

    autotools.configure("--enable-introspection \
                         --with-json=system \
                         --enable-shared")

def build():
    autotools.make()

def install():
    #autotools.rawInstall('DESTDIR=%s INSTALL="install -p -c"' % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "README*", "NEWS")
