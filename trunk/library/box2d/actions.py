#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Box2D_v%s/Box2D" % get.srcVERSION()

def setup():
    pisitools.dosed("CMakeLists.txt", "share/doc/Box2D", "share/doc/box2d") 
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DBOX2D_BUILD_SHARED=ON \
                          -DBOX2D_BUILD_STATIC=OFF \
                          -DBOX2D_INSTALL_DOC=ON \
                          -DBOX2D_BUILD_EXAMPLES=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("License.txt", "Readme.txt")
