# Introduction #

[CMake](http://www.cmake.org/) is a cross-platform, open-source build system. CMake is part of a family of tools designed to build, test and package software. CMake is used to control the software compilation process using simple platform and compiler independent configuration files. CMake generates native makefiles and workspaces that can be used in the compiler environment of your choice.


# Example Usages #

## meandmyshadow ##

**CMakeLists.txt**

```
PROJECT(meandmyshadow)
CMAKE_MINIMUM_REQUIRED(VERSION 2.6)


Find_Package(SDL REQUIRED)
Find_Package(SDL_ttf REQUIRED)
Find_Package(SDL_image REQUIRED)
Find_Package(SDL_mixer REQUIRED)

INCLUDE_DIRECTORIES(${SDL_INCLUDE_DIR})
INCLUDE_DIRECTORIES(${SDLIMAGE_INCLUDE_DIR})
INCLUDE_DIRECTORIES(${SDLMIXER_INCLUDE_DIR})
INCLUDE_DIRECTORIES(${SDLTTF_INCLUDE_DIR})

if ( NOT SDL_FOUND )
    message(FATAL_ERROR "SDL not found !")
endif ( NOT SDL_FOUND )

if ( NOT SDLTTF_FOUND )
    message(FATAL_ERROR "SDL_ttf not found !")
endif ( NOT SDLTTF_FOUND )

if ( NOT SDLMIXER_FOUND )
    message(FATAL_ERROR "SDL_mixer not found !")
endif ( NOT SDLMIXER_FOUND )

configure_file (
  "${PROJECT_SOURCE_DIR}/src/config.h.in"
  "${PROJECT_BINARY_DIR}/config.h"
  )

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR})
set(SRC_DIR ${PROJECT_SOURCE_DIR}/src)

include_directories(
	${PROJECT_BINARY_DIR}
	${SDL_INCLUDE_DIR}
	${SDLTTF_INCLUDE_DIR}
	${SDLMIXER_INCLUDE_DIR}
	${SDLIMAGE_INCLUDE_DIR}
)

SET(CMAKE_CXX_FLAGS "-Wall -g")

# Déclaration de l'exécutable
file(GLOB Sources ${SRC_DIR}/*.cpp)
add_executable(meandmyshadow ${Sources})

target_link_libraries(
    meandmyshadow
    ${SDL_LIBRARY}
	${SDLTTF_LIBRARY}
	${SDLIMAGE_LIBRARY}
	${SDLMIXER_LIBRARY}
)

install(DIRECTORY ${PROJECT_BINARY_DIR}/data DESTINATION share/meandmyshadow/)
install(TARGETS meandmyshadow RUNTIME DESTINATION bin)
if("${CMAKE_SYSTEM_NAME}" MATCHES "Linux") 
	install(FILES meandmyshadow.desktop DESTINATION share/applications/)
	install(FILES meandmyshadow.xpm DESTINATION share/pixmaps/)
endif("${CMAKE_SYSTEM_NAME}" MATCHES "Linux")

```


**config.h.in**
```
#ifndef CONFIG_H
#define CONFIG_H

#if defined(WIN32)
//#define DATA_PATH
#else
#define DATA_PATH "@CMAKE_INSTALL_PREFIX@/share/meandmyshadow/"
#endif

#endif
```


**Globals.h**
```
#ifndef GLOBALS_H
#define GLOBALS_H

...

#ifdef WIN32
//#define DATA_PATH
#else
#include "config.h"
#endif

...

#endif
```


**Functions.cpp**
```
...

#include "Globals.h"

...

string m_sUserPath,m_sDataPath,m_sAppPath,m_sEXEName;

...

    //get the data path
    {
        FILE *f;
        string s;
        for(;;){
            //try existing one
            if(!m_sDataPath.empty()){
                s=m_sDataPath+"data/font/ComicBook.ttf";
                if((f=fopen(s.c_str(),"rb"))!=NULL){
                    fclose(f);
                    break;
                }
            }
            //try "./"
            m_sDataPath="./";
            s=m_sDataPath+"data/font/ComicBook.ttf";
            if((f=fopen(s.c_str(),"rb"))!=NULL){
                fclose(f);
                break;
...

            //try DATA_PATH
#ifdef DATA_PATH
            m_sDataPath=DATA_PATH;
            s=m_sDataPath+"data/font/ComicBook.ttf";
            if((f=fopen(s.c_str(),"rb"))!=NULL){
                fclose(f);
                break;
            }
#endif
            //error: can't find file
            return false;
        }
        font = TTF_OpenFont(s.c_str(), 28);
        font_small = TTF_OpenFont(s.c_str(), 20);
    }

    s_dark_block = load_image(GetDataPath()+"data/gfx/dark.png");
    s_black = load_image(GetDataPath()+"data/gfx/black.png");
    music = Mix_LoadMUS((GetDataPath()+"data/sfx/Music.mid").c_str());
    bool b=o_mylevels.load_levels("%DATA%/data/level/levellist.txt","levelprogress.txt");
    b=s_dark_block!=NULL && s_black!=NULL
        && font!=NULL && font_small != NULL && b;

    if(music==NULL)
        printf("Warning: Unable to load background music! \n");

    if(b){
        printf("Data files will be fetched from: '%s'\n",m_sDataPath.c_str());
        printf("User preferences will be fetched from: '%s'\n",m_sUserPath.c_str());
    }
    return b;
}

...

```