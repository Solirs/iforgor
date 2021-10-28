# Iforgor

Iforgor is a customisable and easy to use command line tool to manage code samples.
It's a good way to quickly get your hand on syntax you dont remember right from your terminal.
Iforgor also contains a simple universal syntax highlighting engine.

# Installation

## Requirements : 

Python.
Git.
The colorama python module. 

## Step by step procedure :

1. Open a terminal and cd into the directory you want to install the program into.

2. Run "git clone https://github.com/Solirs/iforgor/"

3. Cd into the "iforgor" directory

4. Run "./setup.sh"

5. Close your terminal and open another one.

6. Run "iforgor.py -h"

If it works, the install was successful.


# Iforgor 101

To display a piece of code, run the following.

**iforgor.py LANGUAGE SNIPPET**

The language argument represents a folder in the "snippets" directory.
You can add any language you want by creating a folder in it.

The snippet argument represents a *.txt file in the specified language directory that containd the code sample you want to display.
You can add any code sample by creating a *.txt in a desired language folder.

So if you want to add a function sample for the, lets say Rust language for example.
You will have to create a directory named "rust" in the snippets folder.
And create a function.txt file in the rust folder with the code you want inside.

You can then print it out by running **iforgor.py rust function**






# Screenshots:

![alt text](https://github.com/Solirs/iforgor/blob/master/ressources/demo2.png?raw=true)



# Compatibility

This should work on pretty much any linux distro, but i can make mistakes, so dont hesitate opening an issue if you face problems.

Iforgor has been tested on the following :

Debian 11 "Bullseye" : *Working*




# Want to contribute ?

Sure. All help is accepted.
