#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get


def build():
    scons.make("-j1")

def install():
    scons.install("install-all --prefix %s/usr --python-prefix %s/usr/lib/python2.7/site-packages/" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README")
