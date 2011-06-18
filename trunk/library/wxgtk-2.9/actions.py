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
    cflags = "%s -fno-strict-aliasing" % get.CFLAGS()
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cflags)

    # unicode support?
    autotools.configure("--enable-gtk2 \
                         --enable-shared \
                         --disable-optimise \
                         --disable-debug \
                         --enable-no_deps \
                         --disable-rpath \
                         --enable-intl \
                         --enable-geometry \
                         --enable-timer \
                         --enable-unicode \
                         --enable-sound \
                         --enable-mediactrl \
                         --enable-xrc \
                         --enable-graphics_ctx \
                         --enable-display \
                         --enable-joystick \
                         --disable-gtktest \
                         --disable-sdltest \
                         --disable-precomp-headers \
                         --with-gtk=2 \
                         --with-libpng=sys \
                         --with-libjpeg=sys \
                         --with-libtiff=sys \
                         --with-libxpm=sys \
                         --with-sdl \
                         --without-gnomeprint \
                         --without-gnomevfs \
                         --without-odbc \
                         --with-opengl \
                         --with-regex=sys \
                         --with-zlib=sys \
                         --with-expat=sys")

def build():
    autotools.make()
    #autotools.make("-C contrib")
    autotools.make("-C locale allmo")

def install():
    autotools.install()

    # i don't sure about this
    #autotools.install("-C contrib")

    # provide compatibility with wxGTK package
    # don't remove locale files, try rename
    pisitools.removeDir("/usr/share/locale")
    pisitools.removeDir("/usr/share/bakefile")
    pisitools.remove("/usr/bin/wx-config")
    pisitools.remove("/usr/bin/wxrc")
    # it seems there is no need to disable unicode but i try first with ansi
    pisitools.dosym("/usr/lib/wx/config/gtk2-unicode-2.9", "/usr/bin/wx-config-2.9")
    #pisitools.dosym("/usr/lib/wx/config/gtk2-ansi-2.9", "/usr/bin/wx-config-2.9")
    pisitools.rename("/usr/share/aclocal/wxwin.m4", "wxwin-2.9.m4")

    pisitools.dodoc("docs/*.txt", "docs/*.htm")
