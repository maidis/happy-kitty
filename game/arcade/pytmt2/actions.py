#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Too Many Troopers 2"

def install():
    pisitools.insinto("/usr/share/pytmt2", "*")

    pisitools.dodoc("AAA_readme!.txt", "gpl-3.0.txt", "data/credits.txt")
