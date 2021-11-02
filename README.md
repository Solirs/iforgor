# Iforgor

Iforgor is a customisable and easy to use command line tool to manage code samples.
It's a good way to quickly get your hand on syntax you dont remember right from your terminal without wasting time looking on the internet.

## Installation

### Method :

Creates symlinks of iforgor.py and the snippets folder to /usr/local/bin. So that it can be run from anywhere on the terminal.

### Requirements : 

- Python.
- Git.
- The colorama python module. 

### Step by step procedure :

1. Open a terminal and cd into the directory you want to install the program into.

2. Run "git clone https://github.com/Solirs/iforgor/"

3. Cd into the newly created "iforgor" directory

4. Run "./setup.sh" as root (it has to be run as root since it needs to create files in /usr/local/bin), add the ungit argument to remove github related files and folders like the readme and license.

5. Run "iforgor -h"

If it works, the install was successful.
You can then delete setup.sh 

### Uninstall:

To uninstall, simply delete the 'iforgor' and 'snippets' symlinks in /usr/local/bin.

Then delete the iforgor folder.



## Iforgor 101

To display a piece of code, run the following.

**iforgor LANGUAGE SNIPPET**

The language argument represents a folder in the "snippets" directory.
You can add any language you want by creating a folder in it.

The snippet argument represents a *.txt file in the specified language directory that containd the code sample you want to display.
You can add any code sample by creating a *.txt in a desired language folder.

So if you want to add a function sample for the, lets say Rust language for example.
You will have to create a directory named "rust" in the snippets folder.
And create a function.txt file in the rust folder with the code you want inside.

You can then print it out by running **iforgor rust function**

## Pro tips:

- Languages and snippets are case insensitive. So you can run 'iforgor lAnGuAgE sNiPpeT'.

- You dont need to do the setup process, but its required if you want to be able to run iforgor easily from anywhere.

- There are default snippets yes, but iforgor is designed to be customized, dont hesitate to add your own custom snippets and languages.






## Screenshots:

![alt text](https://github.com/Solirs/iforgor/blob/master/ressources/demo3.png?raw=true)



## Compatibility


### Linux 
This should work on pretty much any linux distro, but i can make mistakes, so dont hesitate opening an issue if you face problems.

Iforgor was tested on:

Debian 11  : *Working*

Void Linux : *Working*

Arch Linux : *Working*

### BSDs and other unix based operating systems.

Tested on:

FreeBSD : *Working*

OpenBSD : *Working if colorama python library is installed*




# Want to contribute ?

Sure. All help is accepted.

The code is very commented if you want to take a look at it.

PLEASE dont forget to star the project if you find it interesting, it helps out a ton.
