
from colorama import Fore, Style, init

import colorama
import re

colorama.init()


darkyellowcolor = f"{Fore.YELLOW}{Style.NORMAL}"

darkbluecolor =f"{Fore.BLUE}{Style.DIM}"

whitecolor = f"{Fore.WHITE}{Style.BRIGHT}"

darkyellow = ['+', '-', '*', '/', '%', '**', '=', '+=', '-=', '==', '*=', '/=', '%=', '//=', '!=', '&=', '|=', '^=', '>>=', '<<=', "if", "else", ';', 'return']

darkblue = ['void', 'int', 'char', 'double', 'float', 'double', 'struct', 'def', 'import']

white = ['(', ')', '{', '}',',']

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

    

    
    p = re.findall(r'\"(.+?)\"', finished)
    g = re.findall(r'\'(.+?)\'', finished) 


    for i in p:
        try:


            finished = re.sub('("[^"]+")', Fore.BLUE + r'\1' + Style.RESET_ALL, finished)
            finished = re.sub(r"('[^']')", Fore.BLUE + r'\1' + Style.RESET_ALL, finished)
        except:
            pass

            

    return finished

