
from colorama import Fore, Style, init

import colorama
import re

colorama.init()


darkyellowcolor = f"{Fore.YELLOW}{Style.NORMAL}"

darkbluecolor =f"{Fore.BLUE}{Style.DIM}"

whitecolor = f"{Fore.WHITE}{Style.BRIGHT}"

darkyellow = ['+', '-', '*', '/', '%', '**', '=', '+=', '-=', '==', '*=', '/=', '%=', '//=', '!=', '&=', '|=', '^=', '>>=', '<<=', "if", "else", ';', 'return']

darkblue = ['void', 'int', 'char', 'double', 'float', 'double', 'struct', 'def']

white = ['(', ')', '{', '}']

def highlight(code):
    finished = code

    for i in darkyellow:
        if i in code:
            finished = re.sub(fr"{i}", f"{darkyellowcolor}{i}{Style.RESET_ALL}", finished)
    for i in darkblue:
        if i in code:
            finished = re.sub(fr"\b{i}\b", f"{darkbluecolor}{i}{Style.RESET_ALL}", finished)
        else:
            pass

    for i in white:
        if i in code:
            finished = re.sub(fr"\{i}", f"{whitecolor}{i}{Style.RESET_ALL}", finished)
        else:
            pass

    

    
    p = re.search(r'\"(.+?)\"', finished)
    try:
        finished = re.sub('"[^"]+"', Fore.BLUE + "\"" + p.group(1) + "\"", finished)
        finished = re.sub('\'[^"]+\'', Fore.BLUE + "\'" + p.group(1) + "\'", finished)
    except:
        pass

            

    return finished

