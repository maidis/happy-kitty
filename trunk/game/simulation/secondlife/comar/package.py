#!/usr/bin/python

import os
import platform

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if platform.machine() == "x86_64":
        for packages in ["freealut-32bit gtk2-32bit libidn-32bit mesa-32bit libsdl-32bit alsa-lib-32bit pulseaudio-libs-32bit"]:
            os.system("hav call pisi System.Manager installPackage %s" % packages)

    pass

def preRemove():
    # FIXME This is not needed when upgrading package; but pisi does not
    #       provide a way to learn operation type.
    pass
