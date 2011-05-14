#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "cgmadness"

def build():
    autotools.make()

def install():
    pisitools.dobin("cgmadness")
    pisitools.dobin("convert-cgm")

    pisitools.insinto("/usr/share/cgmadness/data", "data/*")
    pisitools.insinto("/usr/share/cgmadness/levels", "levels/*")

    pisitools.dodoc("credits.txt", "license.txt")
