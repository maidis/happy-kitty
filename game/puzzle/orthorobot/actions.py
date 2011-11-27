#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/orthorobot", "Ortho Robot.love")

    shelltools.chmod("%s/usr/share/orthorobot/Ortho Robot.love" % get.installDIR(), 0644)
