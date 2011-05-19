#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/pyglet", "examples/*")

    pisitools.dosym("/usr/share/pyglet/pyglet.png", "/usr/share/pixmaps/pyglet.png")

    pisitools.dodoc("CHANGELOG", "LICENSE", "NOTICE", "README", "doc/pdf/programming_guide.pdf")

    pisitools.dohtml("doc/html/*")
