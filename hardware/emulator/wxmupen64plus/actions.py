#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("waf --mupenapi=/usr/include/mupen64plus --wxconfig=/usr/bin/wx-config-2.9 --prefix=%s/usr configure" % get.installDIR())

def build():
    shelltools.system("waf")

def install():
    shelltools.system("waf install")

    pisitools.dodoc("*.txt")
