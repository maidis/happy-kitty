#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--enable-sound \
                         --enable-SMPF \
                         --enable-admin \
                         --bindir=/usr/bin \
                         --prefix=/usr/share/xblast \
                         --with-otherdatadir=/usr/share/xblast")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/xblast/image", "../images-2005-01-06/*")

    # FIXME: don't remove change name
    # <type 'exceptions.UnicodeDecodeError'>: 'utf8' codec can't decode byte 0xee in position 34: invalid continuation byte
    shelltools.unlink(get.workDIR() + '/' + 'levels-2005-01-06' + "/reconstruct*on2.xal")

    pisitools.insinto("/usr/share/xblast/level", "../levels-2005-01-06/*")

    pisitools.insinto("/usr/share/xblast/image/sprite", "../models-2005-01-06/*")

    # FIXME: sound effects and musics
    pisitools.insinto("/usr/share/xblast/sounds", "../musics-2005-01-06/*")

    pisitools.insinto("/usr/share/xblast/sounds", "../sounds/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
