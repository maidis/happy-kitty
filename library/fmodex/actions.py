#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

bits = "64" if get.ARCH() == "x86_64" else "32"

WorkDir = "%s/fmodapi%slinux%s" % (get.ARCH(), get.srcVERSION().replace('.', ''), bits)

NoStrip = "/"

def install():
    # ask for permission to redistributing in binary form
    # http://projects.archlinux.org/svntogit/community.git/tree/fmodex/trunk/PERMISSION
    # syming libs
    # http://projects.archlinux.org/svntogit/community.git/tree/fmodex/trunk/PKGBUILD
    # http://gpo.zugaina.org/media-libs/fmodex
    # https://build.opensuse.org/package/files?package=fmodex&project=games
    pisitools.dolib_so("api/lib/*")
    pisitools.dolib_so("fmoddesignerapi/api/lib/*")

    pisitools.insinto("/usr/include/fmodex", "api/inc/*")
    pisitools.insinto("/usr/include/fmodex", "fmoddesignerapi/api/inc/*")

    pisitools.insinto("/usr/share/fmodex", "examples/*")

    pisitools.dodoc("documentation/*")
