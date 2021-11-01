
from colorama import Fore, Style, init

import colorama
import re

#No shebang as this is supposed to be used as a module.


darkyellowcolor = f"{Fore.YELLOW}{Style.NORMAL}"

darkbluecolor =f"{Fore.BLUE}{Style.DIM}"

whitecolor = f"{Fore.WHITE}"

green = ['+', '-', '*', '/', '%', '**', '=', '+=', '-=', '==', '*=', '/=', '%=', '//=', '!=', '&=', '|=', '^=', '>>=', '<<=',';']

darkyellow = ["if", "else", "elif", "except", "break", "pass", "continue", 'return'] #What we want to color in dark yellow

darkblue = ['void', 'int', 'char', 'double', 'float', 'double', 'struct', 'def', 'import'] #Same for dark blue

white = ['(', ')', '{', '}',','] #Same for white

def highlight(code):
    finished = code

    for i in darkyellow:
        if i in code:
            finished = re.sub(fr"\b{i}\b", f"{darkyellowcolor}{i}{Style.RESET_ALL}", finished) #Iterate trough every string in darkyellow and replace its occurences (if any) by its colored version
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

    for i in green:
        if i in code:
            finished = finished.replace(i, f'{Fore.GREEN}{i}{Style.RESET_ALL}') #Used this method instead of regex as operators tend to cause problems when using it.
        else:
            pass


    try:


        finished = re.sub('("[^"]+")', Fore.BLUE + r'\1' + Style.RESET_ALL, finished) #Replace any text between double quotes by its blue self (keeping the double quotes)
        finished = re.sub(r"('[^']')", Fore.BLUE + r'\1' + Style.RESET_ALL, finished) #Same for single quotes
    except:
        pass

            

    return finished

