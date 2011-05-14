#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
def build():
    autotools.make()

def install():
    pisitools.dobin("l-echo", "/opt/l-echo")
    pisitools.insinto("/opt/l-echo", "*.xml")
    pisitools.insinto("/opt/l-echo", "n-echo_template/apps/n-echo/*.xml.real")
    pisitools.dodoc("L_ECHO_README")
