#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "numptyphysics-svn-r157"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure()

def build():
    autotools.make("CXX=%s" % get.CXX())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "data/icon64/numptyphysics.png")
    pisitools.insinto("/usr/share/numptyphysics", "numptyphysics-levels/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
