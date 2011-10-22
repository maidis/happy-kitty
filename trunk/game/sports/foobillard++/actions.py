#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make()

def install():
    # autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    # .svn files must go
    pisitools.dobin("src/foobillardplus")

    pisitools.insinto("/usr/share/foobillardplus", "data/*")
    pisitools.insinto("/usr/share/pixmaps", "foobillardplus.png")
    pisitools.insinto("/usr/share/applications", "foobillardplus.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
