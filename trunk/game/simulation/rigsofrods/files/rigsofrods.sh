#!/bin/sh

if [[ ! -f ~/.rigsofrods/packs/cars/accord.zip ]]; then
    cp -R /opt/rigsofrods/packs ~/.rigsofrods/
fi

/opt/rigsofrods/RoR
