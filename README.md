# AoW-RT-Bot
> A personal bot for Art of War: Red Tides AI

This is part of my 'study-the-examples' series, of how certain things can be done in python through 3rd-party libraries. Scripts are designed as accord to me, and not for client use. You can however download and edit them to work on your computer.

Note that this Bot is designed personally for AoW:RT AI matches! Using it against a real human does not guarantee you a win.

## Documentation
### Libraries
- PyAutoGUI
- Win32Gui
### Usage
Since this bot is designed using PyAutoGUI for personal use, the script is not flawless and have many bugs. Technically, if memory hacking were to be used instead it would be much more effective.

Unfortunately the way it is coded is so restrictive thus:
* Supports ONLY
  * Resolution: 1280x720 @ windowed mode
  * Atlac units of the following order:
    * Silver Guardian
    * Heavy Blade Slave
    * Scholar
    * Wrath Chanter
    * Shadow Fish
    * Staff Slave
    * Vajra
    * Lightning Arhat
    * Azure Dragon
    * Great Whale

#### Workflow
1. Script can be run before or after the game has started
2. It will then detect the game window after launched
3. Script will wait for next command, waiting for match to start
4. Once match has started (After game's preload), the script will start running
5. Script will end after the match has finished

### To-do
- Improve Bot versatility to work with more races/units (More actions)
- Automatically starts a new AI match when end
- Reduce code redundancies for better memory usage
