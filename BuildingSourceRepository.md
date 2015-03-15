# Introduction #

This document shows how to build a source repository for Pardus.


# Details #

  * Create some directories for components and sub components.
```
$ ls *
game:
action  adventure  arcade  board  engine  fps  misc  puzzle  rpg  simulation  sports  strategy

hardware:

library:
```

  * Create component.xml files for all components and sub components.
```
game/component.xml:

<PISI>
    <Name>game</Name>
</PISI>

game/action/component.xml:

<PISI>
    <Name>game.action</Name>
</PISI>

```

  * Create a components.xml file which contains all components and components related informations in root directory of repository.
```
<PISI>
    <Components>
        <Component>
            <Name>library</Name>
            <LocalName xml:lang="en">FIXME</LocalName>
            <Summary xml:lang="en">FIXME</Summary>
            <Description xml:lang="en">FIXME</Description>
            <Group>system</Group>
            <Maintainer>
                <Name>FIXME</Name>
                <Email>FIXME</Email>
            </Maintainer>
        </Component>
        <Component>
            <Name>hardware</Name>
            <LocalName xml:lang="en">FIXME</LocalName>
            <Summary xml:lang="en">FIXME</Summary>
            <Description xml:lang="en">FIXME</Description>
            <Group>system</Group>
            <Maintainer>
                <Name>FIXME</Name>
                <Email>FIXME</Email>
            </Maintainer>
        </Component>
        ...
        <Component>
            <Name>game.engine</Name>
            <LocalName xml:lang="en">FIXME</LocalName>
            <Summary xml:lang="en">FIXME</Summary>
            <Description xml:lang="en">FIXME</Description>
            <Group>games</Group>
            <Maintainer>
                <Name>FIXME</Name>
                <Email>FIXME</Email>
            </Maintainer>
        </Component>
        <Component>
            <Name>game.kids</Name>
            <LocalName xml:lang="en">FIXME</LocalName>
            <Summary xml:lang="en">FIXME</Summary>
            <Description xml:lang="en">FIXME</Description>
            <Group>games</Group>
            <Maintainer>
                <Name>FIXME</Name>
                <Email>FIXME</Email>
            </Maintainer>
        </Component>
    </Components>
</PISI>
```

  * Create a distribution.xml in root directory of repository.
```
<PISI>
    <SourceName>Pardus</SourceName>
    <Version>2011</Version>
    <Description xml:lang="tr">Happy Kitty Deposu</Description>
    <Description xml:lang="en">Happy Kitty Repository</Description>
    <Type>Extra</Type>
    <BinaryName>Pardus</BinaryName>
    <Obsoletes>
        <!-- Dropped packages -->


        <!--
            ************************************************************
            not gone to binary stable yet, please don't remove this mark
            ************************************************************
        -->

    </Obsoletes>
</PISI>
```

  * Run pisi index command in root directory of repository.
```
$ pisi index --skip-signing
* Building index of PiSi files under .
Adding distribution.xml to index...
Adding components.xml to index...
Adding ./game/arcade/airstrike/pspec.xml to source index
PartOf tag not defined, looking for component
Source is part of game.arcade component
* Index file written

$ ls pisi-index*
pisi-index.xml  pisi-index.xml.sha1sum  pisi-index.xml.xz  pisi-index.xml.xz.sha1sum
```

That's all. Realy? Yes :)

# Additional Information #
  * pisi index (or pisi ix) manual:
```
$ pisi index --help
usage: Index PiSi files in a given directory

Usage: index <directory> ...

This command searches for all PiSi files in a directory, collects PiSi
tags from them and accumulates the information in an output XML file,
named by default 'pisi-index.xml'. In particular, it indexes both
source and binary packages.

If you give multiple directories, the command still works, but puts
everything in a single index file.

 index options:
  -a [--absolute-urls]        : Store absolute links for indexed files.
  -o [--output] arg           : Index output file
  --compression-types arg     : Comma-separated compression types for index file
  --skip-sources              : Do not index PiSi spec files.
  --skip-signing              : Do not sign index.
```

# References #
  * [Paket deposu hazırlamak (Turkish)](http://tr.pardus-wiki.org/Pardus:Paket_deposu_haz%C4%B1rlamak)
  * [Repository Concepts](http://developer.pardus.org.tr/guides/releasing/repository_concepts/index.html)
  * [Pardus 2011/devel repository](https://svn.pardus.org.tr/pardus/2011/devel/)
  * [Pardus-Linux.org P2011/i686 repository](http://paketler.pardus-linux.org/P2011/i686/)