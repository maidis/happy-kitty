#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/include", "include/dumb.h")
    pisitools.insinto("/usr/include", "include/aldumb.h")

    pisitools.dolib("src/.libs/*.so")

    pisitools.dobin("examples/dumb2wav")
    pisitools.dobin("examples/dumbout")
    pisitools.dobin("examples/dumbplay")

    pisitools.dodoc("*.txt", "docs/*.txt")
