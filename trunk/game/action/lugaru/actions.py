#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lugaru-rev269-src"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release -DLUGARU_INSTALL_PREFIX=/opt/lugaru ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CONTENT-LICENSE.txt", "COPYING.txt", "README")
