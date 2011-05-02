#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DBUILD_SHARED_LIBS=1 \
                          -DBUILD_DEMOS=0 \
                          -DBUILD_EXTRAS=1 \
                          -DINSTALL_LIBS=1 \
                          -DINSTALL_EXTRA_LIBS=1", installPrefix="/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/bullet", "Demos/*")

    pisitools.insinto("/usr/share/doc/bullet", "Bullet_User_Manual.pdf")

    pisitools.dodoc("BulletLicense.txt", "ChangeLog", "LICENSE", "NEWS", "README")
