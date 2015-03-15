# Introduction #

Both the KDE and GNOME desktop environments have adopted a similar format for "desktop entries", or configuration files describing how a particular program is to be launched, how it appears in menus, etc.

# Desktop Entry Keys #

| **Key** | **Description** |
|:--------|:----------------|
| Type  | This specification defines 3 types of desktop entries: Application, Link and Directory. To allow the addition of new types in the future, implementations should ignore desktop entries with an unknown type. |
| Version | Version of the Desktop Entry Specification that the desktop entry conforms with. Entries that confirm with this version of the specification should use 1.0. Note that the version field is not required to be present. |
| Name | Specific name of the application, for example "Mozilla". |
| GenericName | Generic name of the application, for example "Web Browser". |
| Comment | Tooltip for the entry, for example "View sites on the Internet". The value should not be redundant with the values of Name and GenericName. |
| Icon | Icon to display in file manager, menus, etc. If the name is an absolute path, the given file will be used. If the name is not an absolute path, the algorithm described in the Icon Theme Specification will be used to locate the icon. |
| Exec | Program to execute, possibly with arguments. |
| Terminal | Whether the program runs in a terminal window. |
| StartupNotify | If true, it is KNOWN that the application will send a "remove" message when started with the DESKTOP\_STARTUP\_ID environment variable set. If false, it is KNOWN that the application does not work with startup notification at all (does not shown any window, breaks even when using StartupWMClass, etc.). If absent, a reasonable handling is up to implementations (assuming false, using StartupWMClass, etc.). |
| Categories | A list of strings used to classify menu items. For example, applications in the AudioVideo category might end up in the "Sound & Video" submenu. |

# Registered Categories #
This section contains a number of well known categories and suggestions on how to use them. The list of Main Categories consist of those categories that every conforming desktop environment MUST support. By including one of these categories in an application's desktop entry file the application will be ensured that it will show up in a section of the application menu dedicated to this category. The list of Additional Categories provides categories that can be used to provide more fine grained information about the application. Additional Categories should always be used in combination with one of the Main Categories.

The table below lists all Main Categories. Note that category names are case-sensitive.

| **Main Category** | **Description** |
|:------------------|:----------------|
| AudioVideo | Application for presenting, creating, or processing multimedia (audio/video) |
| Audio | An audio application |
| Video | A video application |
| Development | An application for development |
| Education | Educational software |
| Game | A game |
| Graphics | Application for viewing, creating, or processing graphics |
| Network | Network application such as a web browser |
| Office | An office type application |
| Settings | Settings applications |
| System | System application, "System Tools" such as say a log viewer or network monitor |
| Utility | Small utility application, "Accessories" |

The table below describes Additional Categories.

| **Additional Category** | **Description** |
|:------------------------|:----------------|
| ActionGame | An action game |
| AdventureGame | Adventure style game |
| ArcadeGame | Arcade style game |
| BoardGame | A board game |
| BlocksGame | Falling blocks game |
| CardGame | A card game |
| Emulator | Emulator of another platform, such as a DOS emulator |
| KidsGame | A game for kids |
| LogicGame | Logic games like puzzles, etc |
| RolePlaying | A role playing game |
| Simulation | A simulation game |
| SportsGame | A sports game |
| StrategyGame | A strategy game |

# Example Desktop Entry File #
```
[Desktop Entry]
Type=Application
Version=1.0
Name=Airstrike
GenericName=Dogfight Game
GenericName[tr]=İtdalaşı Oyunu
Comment=A 2d dogfight game
Comment[tr]=İki boyutlu bir itdalaşı oyunu
Icon=airstrike
Exec=airstrike
Terminal=false
StartupNotify=false
Categories=Application;Game;ArcadeGame;
```

# References #
  * [Desktop Entry Specification](http://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html)
  * [Desktop Menu Specification](http://standards.freedesktop.org/menu-spec/menu-spec-latest.html)