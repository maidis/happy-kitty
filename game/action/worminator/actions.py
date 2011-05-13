#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "worminator-3.0R2.1"

def build():
    shelltools.export("DATADIR", "/usr/shre/worminator/")
    shelltools.system("gcc -O2 -fsigned-char -DDATADIR=\\\"/usr/share/worminator/\\\" -o worminator Worminator.c `allegro-config --libs`")

def install():
    pisitools.dobin("worminator")

    pisitools.dodoc("license*", "ReadMe.txt")
