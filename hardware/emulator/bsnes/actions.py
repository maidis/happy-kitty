#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.cd("bsnes")
    autotools.make("compiler=gcc platform=x profile=compatibility")

    shelltools.cd("../snespurify")
    shelltools.system("./cc-gtk.sh")

def install():
    # pisitools.dobin("bsnes/out/bsnes")
    # pisitools.insinto("/usr/share/pixmaps", "bsnes/data/bsnes.png")
    #pisitools.insinto("/usr/share/applications", "bsnes/data/bsnes.desktop")
    shelltools.cd("bsnes")
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())

    pisitools.dobin("../snespurify/snespurify-gtk")
