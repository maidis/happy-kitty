# Introduction #

This document shows how to use a source repository at Pardus.


# Details #
  * For add Happy Kitty repository to system:
```
$ sudo pisi ar happy-kitty http://happy-kitty.googlecode.com/svn/trunk/pisi-index.xml.xz
Repo happy-kitty added to system.
Updating repository: happy-kitty
pisi-index.xml.xz.sha1sum      (40.0  B)100%    157.54 KB/s [00:00:00] [complete]
pisi-index.xml.xz              (1.0 KB)100%      4.70 MB/s [00:00:00] [complete]
No signature found for http://happy-kitty.googlecode.com/svn/trunk/pisi-index.xml.xz
* Package database updated. 
```

  * For install a package from Happy Kitty repository:
```
$ sudo pisi em airstrike
Outputting binary packages in the package cache.
The following list of packages will be built and
installed in the respective order to satisfy dependencies:
airstrike
pspec.xml                      (2.0 KB)100%      8.54 MB/s [00:00:00] [complete]
actions.py                     (548.0  B)100%      2.20 MB/s [00:00:00] [complete]
Safety switch: system.devel is already installed
translations.xml               (379.0  B)100%      1.28 MB/s [00:00:00] [complete]
airstrikerc.diff               (269.0  B)100%      1.02 MB/s [00:00:00] [complete]
fix-buffer-overflow.diff       (426.0  B)100%      1.67 MB/s [00:00:00] [complete]
fix_paths.diff                 (1.0 KB)100%      4.24 MB/s [00:00:00] [complete]
fix-red-baron-has-unlimited-bombs.diff (683.0  B)100%      2.65 MB/s [00:00:00] [complete]
fix-segfault-on-close.diff     (477.0  B)100%      5.76 MB/s [00:00:00] [complete]
fix-spawn-level.diff           (485.0  B)100%      2.06 MB/s [00:00:00] [complete]
fix-unusable-on-amd64.diff     (900.0  B)100%     10.59 MB/s [00:00:00] [complete]
manpage.diff                   (275.0  B)100%      1.06 MB/s [00:00:00] [complete]
system-flags.diff              (617.0  B)100%      2.38 MB/s [00:00:00] [complete]
airstrike.desktop              (313.0  B)100%    952.49 KB/s [00:00:00] [complete]
airstrike.png                  (43.0 KB)100%      3.89 MB/s [00:00:00] [complete]
Building source package: airstrike
Safety switch: system.devel is already installed
PartOf tag not defined, looking for component
component.xml                  (44.0  B)100%    172.63 KB/s [00:00:00] [complete]
Source is part of game.arcade component
airstrike-pre6a-src.tar.gz [cached]
Unpacking archive(s)...
* Applying patch: airstrikerc.diff
* Applying patch: fix-buffer-overflow.diff
* Applying patch: fix_paths.diff
* Applying patch: fix-red-baron-has-unlimited-bombs.diff
* Applying patch: fix-segfault-on-close.diff
* Applying patch: fix-spawn-level.diff
* Applying patch: fix-unusable-on-amd64.diff
* Applying patch: manpage.diff
* Applying patch: system-flags.diff
 unpacked (/var/pisi/airstrike-0.99-1/work)
Setting up source...
Building source...
Sandbox enabled build...
Installing...
Sandbox enabled build...
Including directory '/var/pisi/airstrike-0.99-1/install/usr/share/airstrike/sound'
Building package: airstrike
Creating /var/cache/pisi/packages/airstrike-0.99-1-p11-i686.pisi...
Keeping build directory
Installation order: airstrike
Installing airstrike, version 0.99, release 1
Running pre removal operations for airstrike
Running post removal operations for airstrike
Extracting the files of airstrike
Configuring airstrike package
Configured airstrike
Installed airstrike
```

  * For search a package in Happy Kitty:
```
$ pisi sr -s airstrike
airstrike - A 2d dogfight game
```

  * For update Happy Kitty database:
```
$ pisi ur happy-kitty
Updating repository: happy-kitty
pisi-index.xml.xz.sha1sum      (40.0  B)100%    124.40 KB/s [00:00:00] [complete]                           
happy-kitty repository information is up-to-date.
```

  * For list available sources at Happy Kitty:
```
$ pisi ls happy-kitty
airstrike - A 2d dogfight game
apricots - A simple 2D flying and bombing game
box2d - 2D rigid body simulation library
happyfrog - A funny game based on Qt and Box2D
qt-mobility - Qt APIs for mobile devices
```

  * For remove a package from system:
```
$ sudo pisi rm airstrike
The following list of packages will be removed
in the respective order to satisfy dependencies:
airstrike
Removing package airstrike
Running pre removal operations for airstrike
Running post removal operations for airstrike
Removed airstrike
```

  * For remove Happy Kitty repository from system:
```
$ sudo pisi rr happy-kitty
Password: 
Repo happy-kitty removed from system.
```