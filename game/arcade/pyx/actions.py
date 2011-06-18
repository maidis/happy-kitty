#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def install():
    pisitools.insinto("/opt/pyx", "*")

    #shelltools.copy("./*", "%s/opt/pyx/" % get.installDIR()) önce dizin yarat
    shelltools.chmod("%s/opt/pyx/scores" % get.installDIR(), 0666)

    #pisitools.dodoc("changes")
    #pisitools.dosym("/opt/pyx/pyx.py","/usr/bin/pyx")
    #pisitools.remove("/opt/pyx/changes")
