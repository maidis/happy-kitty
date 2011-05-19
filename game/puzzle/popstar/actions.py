#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    pisitools.dosed("Makefile", "/usr/local/", "/usr/")

    autotools.make()

def install():
    pisitools.dobin("popstar")

    pisitools.insinto("/usr/share/popstar", "data/*")

    pisitools.dodoc("docs/*")
