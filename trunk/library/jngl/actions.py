#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
    scons.make("python=1")

def install():
    shelltools.system("./install.sh %s/usr" % get.installDIR())

    pisitools.dolib_so("python/libjngl.so", "/usr/lib/python2.7/site-packages")

    pisitools.dosym("/usr/lib/python2.7/site-packages/libjngl.so", "/usr/lib/python2.7/site-packages/jngl.so")

    pisitools.insinto("/usr/share/pixmaps", "jngl.png")

    pisitools.dodoc("COPYING*", "README")
