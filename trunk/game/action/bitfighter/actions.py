#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    # it needs some love, conf files, deps...
    pisitools.dobin("exe/bitfighter", "/opt/bitfighter")

    pisitools.insinto("/opt/bitfighter/levels", "installer/levels/*")
    pisitools.insinto("/opt/bitfighter/robots", "installer/robots/*")
    pisitools.insinto("/opt/bitfighter/sfx", "installer/sfx/*")
    
    pisitools.dodoc("installer/*.txt", "LICENSE.txt", "ReadMe.html")
