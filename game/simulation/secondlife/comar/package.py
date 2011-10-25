#!/usr/bin/python

import os

packages = "freealut-32bit gtk2-32bit libidn-32bit mesa-32bit libsdl-32bit alsa-lib-32bit pulseaudio-libs-32bit"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("hav call pisi System.Manager installPackage %s" % packages)

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL %s/libGL.so.1.2" % libdir)
    pass
