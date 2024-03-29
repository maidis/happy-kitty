#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "TheButterflyEffect-m%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/opt/thebutterflyeffect/", "tbe")
    pisitools.insinto("/opt/thebutterflyeffect/images", "images/*")
    pisitools.insinto("/opt/thebutterflyeffect/levels", "levels/*")
    pisitools.dodoc("AUTHORS", "COPYING", "README")
