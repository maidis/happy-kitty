#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Stringrolled"

def install():
    pisitools.insinto("/usr/share/stringrolled", "*")

    pisitools.dodoc("README.txt")

    pisitools.remove("/usr/share/stringrolled/README.txt")

    shelltools.chmod(get.installDIR() + "/usr/share/stringrolled/*", 0644)
    shelltools.chmod(get.installDIR() + "/usr/share/stringrolled/data/*", 0644)
    shelltools.chmod(get.installDIR() + "/usr/share/stringrolled/gamelib/*", 0644)
