#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="xix"

def build():
    pisitools.dosed("Makefile", "^CC=.*", "CC=%s %s" % (get.CXX(), get.CXXFLAGS()))

    autotools.make()

def install():
    pisitools.dobin("xix")

    pisitools.dodoc("README", "VERSIONS")
