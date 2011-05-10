#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("DATA_PREFIX=/usr/share/madbomber/ \
                    BIN_PREFIX=/usr/bin/")

def install():
    pisitools.dobin("madbomber")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS.txt", "CHANGES.txt", "COPYING.txt", "README.txt", "TODO.txt")
