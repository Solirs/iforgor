#!/bin/sh



#The install process creates a symlink of iforgor.py and the snippet directory in /usr/local/bin


chmod +x $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/iforgor #Gives iforgor.py aka the main script permissions to execute.

ln -s $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/iforgor /usr/local/bin #Creates symlink of iforgor.py in /usr/local/bin making it executable from anywhere.

ln -s $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/snippets /usr/local/bin #Creates symlink of snippets in /usr/local/bin so our iforgor synmlink can work.

case "$1" in

    "ungit" ) #Remove everything related to the github repository
        rm $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/README.md
        rm -rf $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/ressources
        rm $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/LICENSE
        rm -rf $(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/.git
        ;;

esac
