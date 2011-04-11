#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    shelltools.system("gunzip ./man/tuxpuck.6.gz")
    autotools.make("-j1")

def install():
    pisitools.dobin("tuxpuck")

    pisitools.doman("man/tuxpuck.6")

    pisitools.dodoc("bugs.txt", "COPYING", "readme.txt", "thanks.txt", "todo.txt")
