#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "celeron55-minetest-d566ffa"

def setup():
    pisitools.dosed("src/irrlichttypes.h", "typedef uint64_t u64;", "//typedef uint64_t u64;")

    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README.txt", "doc/*")
