#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def build():
    shelltools.makedirs("%s/build/obj/elements" % get.workDIR())

    autotools.make("powder")

def install():
    pisitools.dobin("build/powder")

    pisitools.dodoc("LICENSE", "README")
