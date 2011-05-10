#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("PACKAGE_DATA_DIR=/usr/share/gnurobbo \
                    BINDIR=/usr/bin \
                    DOCDIR=/usr/share/doc/gnurobbo")

def install():
    pisitools.dobin("gnurobbo")
    pisitools.insinto("/usr/share/gnurobbo", "data/*")
    pisitools.dodoc("AUTHORS", "Bugs", "ChangeLog", "COPYING", "LICENSE*", "NEWS", "README", "TODO")
