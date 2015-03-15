Dealing to fix paths is very common in the game packaging industry :) Here are some examples that everyone (both developers and packagers) can easily get an idea about path issues on GNU/Linux. Feel free to add new examples.

> "Two roads diverged in the wood and I, I took the one less traveled by, and that has made all the difference."[\*](http://en.wikipedia.org/wiki/The_Road_Not_Taken_(poem))


## barrage-1.0.3-paths.diff ##

```
diff -Naur barrage-1.0.3.orig/configure.in barrage-1.0.3/configure.in
--- barrage-1.0.3.orig/configure.in	2010-12-24 13:01:38.000000000 +0200
+++ barrage-1.0.3/configure.in	2011-03-27 14:25:05.450000015 +0200
@@ -33,7 +33,7 @@
 AC_SUBST(audio_flag)
 AC_SUBST(audio_lib)
 
-src_dir="$datadir/games/barrage"
+src_dir="$datadir/barrage" 
```


## chains-paths.diff ##

```
diff -Naur chains-0.1.1-src.orig/Game.pro chains-0.1.1-src/Game.pro
--- chains-0.1.1-src.orig/Game.pro	2010-01-09 18:11:18.000000000 +0200
+++ chains-0.1.1-src/Game.pro	2011-01-15 19:36:33.956000045 +0200
@@ -5,9 +5,9 @@
     opengl
 unix: {
     TARGET = ./bin/chains
-    target.path = /usr/local/bin/
+    target.path = /usr/bin/
     INSTALLS += target
-    datas.path = /usr/local/games/chains
+    datas.path = /usr/share/chains
     datas.files = data
     INSTALLS += datas
     LIBS += -lXrandr
diff -Naur chains-0.1.1-src.orig/main.cpp chains-0.1.1-src/main.cpp
--- chains-0.1.1-src.orig/main.cpp	2010-01-09 20:23:48.000000000 +0200
+++ chains-0.1.1-src/main.cpp	2011-01-15 19:38:04.394000045 +0200
@@ -31,7 +31,7 @@
     // on X11, we'll check if data directory exists locally first
   #ifdef Q_WS_X11
     if (!QDir(resourcePath).exists())
-      resourcePath = "/usr/local/games/chains/data/";
+      resourcePath = "/usr/share/chains/data/";
   #endif
 
     if (!QDir(resourcePath).exists()) {
```


## fix\_paths.diff ##

```
--- airstrike-0.99+1.0pre6a.orig/src/config.h
+++ airstrike-0.99+1.0pre6a/src/config.h
@@ -6,7 +6,7 @@
 /* absolute path to main config file (for now it's airstrikerc in the
    current dir)*/
 #ifndef ROOT_CONFIG_FILE
-#define ROOT_CONFIG_FILE "airstrikerc"
+#define ROOT_CONFIG_FILE "/etc/airstrikerc"
 #endif
 /* path to file in users $HOME */
 #ifndef USER_CONFIG_FILE
--- airstrike-0.99+1.0pre6a.orig/src/airstrike.c
+++ airstrike-0.99+1.0pre6a/src/airstrike.c
@@ -74,7 +74,7 @@
   console_set_pos(9,254);
   console_load_bg(path_to_data("console-bg.png"));
   sprite_types_setup();
-  sprite_background_load("data/bg.png","data/bgmask.png");
+  sprite_background_load("/usr/share/airstrike/bg.png","/usr/share/airstrike/bgmask.png");
 
   level_setup();
   winds_setup();
--- airstrike-0.99+1.0pre6a.orig/Makefile
+++ airstrike-0.99+1.0pre6a/Makefile
@@ -29,3 +29,15 @@
 # packages new files listed in new-files.txt
 new:
 	tar -zcvf new.tgz -T new-files.txt
+
+install:
+	install -d $(DESTDIR)/usr/bin
+	install airstrike $(DESTDIR)/usr/bin/airstrike
+	install -d $(DESTDIR)/usr/share/airstrike
+	install -d $(DESTDIR)/usr/share/airstrike/sound
+	install -m 644 data/*.png $(DESTDIR)/usr/share/airstrike
+	install -m 644 data/*.txt $(DESTDIR)/usr/share/airstrike
+#	install -m 644 data/sound/*.wav $(DESTDIR)/usr/share/airstrike/sound
+	install -d $(DESTDIR)/etc
+	install -m 644 airstrikerc $(DESTDIR)/etc/airstrikerc
+
```


## jamp-1.0.2-paths.diff ##

```
diff -Naur jamp-1.0.2.orig/globals.h jamp-1.0.2/globals.h
--- jamp-1.0.2.orig/globals.h	2009-01-16 01:23:54.000000000 +0200
+++ jamp-1.0.2/globals.h	2011-04-25 17:55:58.814000009 +0300
@@ -41,6 +41,6 @@
 
 #include "Singleton.h"
 
-const std::string path("/usr/share/games/jamp/");
+const std::string path("/usr/share/jamp/");
 
 #endif
diff -Naur jamp-1.0.2.orig/Makefile jamp-1.0.2/Makefile
--- jamp-1.0.2.orig/Makefile	2009-01-16 01:30:39.000000000 +0200
+++ jamp-1.0.2/Makefile	2011-04-25 17:56:48.347000012 +0300
@@ -1,6 +1,6 @@
-BINDIR = /usr/games
+BINDIR = /usr/bin
 SHAREDIR = /usr/share
-DATADIR = /usr/share/games
+DATADIR = /usr/share
 
 PROJECT= ./box2d
 CXXFLAGS= -g -O2 -I$(PROJECT)/Include
```


## highscore-path.diff ##

```
--- HighScore.py.orig	2011-02-23 20:42:26.000000000 +0200
+++ HighScore.py	2011-05-25 22:13:39.777000020 +0300
@@ -78,7 +78,11 @@
                 if not os.path.exists(lpackpath):
                     os.makedirs(lpackpath)
                 file = open(lpackpath+"highscore.hsc", "rb")
-            else: file = open("data/maps/{0}highscore.hsc".format(levelpack), "rb")
+            else:
+                lpackpath = os.environ['HOME']+"/.somyeol2d/highscore/{0}".format(levelpack)
+                if not os.path.exists(lpackpath):
+                    os.makedirs(lpackpath)
+                file = open(lpackpath+"highscore.hsc", "rb")
             data = cPickle.load(file)
             self.scores = data
         except EOFError:
@@ -119,7 +123,11 @@
             if not os.path.exists(lpackpath):
                 os.makedirs(lpackpath)
             file = open(lpackpath+"highscore.hsc", "wb")
-        else: file = open("data/maps/{0}highscore.hsc".format(levelpack), "wb")
+        else:
+            lpackpath = os.environ['HOME']+"/.somyeol2d/highscore/{0}".format(levelpack)
+            if not os.path.exists(lpackpath):
+                os.makedirs(lpackpath)
+            file = open(lpackpath+"highscore.hsc", "wb")
         data = self.scores
         cPickle.dump(data, file)
```


## paths.patch ##

```
--- src/main.h.orig	2007-08-06 21:42:47.000000000 +0300
+++ src/main.h	2010-12-01 14:19:40.164000017 +0200
@@ -27,9 +27,9 @@
 #include <iostream>
 #include <fstream>
 
-#define DATA_PREFIX "data/"
+#define DATA_PREFIX "/usr/share/balloons/"
 
-#define LEVELS DATA_PREFIX "levels/%d.DAT"
+#define LEVELS DATA_PREFIX "/usr/share/balloons/%d.DAT"
 
 
 // Tiles
```


## redeclipse.sh-paths.diff ##

```
--- redeclipse.sh.orig	2011-02-27 22:30:20.000000000 +0200
+++ redeclipse.sh	2011-04-30 19:06:02.793000080 +0300
@@ -2,10 +2,10 @@
 # RE_DATA should refer to the directory in which Red Eclipse data files are placed.
 #RE_DATA=~/redeclipse
 #RE_DATA=/usr/local/redeclipse
-RE_DATA=.
+RE_DATA=/usr/share/redeclipse
 
 # RE_BIN should refer to the directory in which Red Eclipse executable files are placed.
-RE_BIN=${RE_DATA}/bin
+RE_BIN=/usr/bin
 
 # RE_OPTIONS contains any command line options you would like to start Red Eclipse with.
 RE_OPTIONS="-r"
@@ -55,10 +55,10 @@
     MACHINE_SUFFIX=""
 fi
 
-if [ -x ${RE_BIN}/reclient${SYSTEM_SUFFIX}${MACHINE_SUFFIX} ]
+if [ -x ${RE_BIN}/reclient ]
 then
     cd ${RE_DATA}
-    exec ${RE_BIN}/reclient${SYSTEM_SUFFIX}${MACHINE_SUFFIX} ${RE_OPTIONS} "$@"
+    exec ${RE_BIN}/reclient ${RE_OPTIONS} "$@"
 else
     echo "Your platform does not have a pre-compiled Red Eclipse client."
     echo -n "Would you like to build one now? [Yn] "
@@ -75,4 +75,3 @@
         exit 1
     fi
 fi
-
```