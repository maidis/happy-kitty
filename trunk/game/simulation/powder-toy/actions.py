#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "FacialTurd-The-Powder-Toy-0fb9990"

def build():
    autotools.make("powder")

def install():
    pisitools.dobin("build/powder")

    pisitools.dodoc("console_README", "LICENSE", "README", "roadmap")
