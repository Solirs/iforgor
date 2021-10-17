#!/usr/bin/python3



import argparse, os
from snippets.syntax import *
from colorama import *

parser = argparse.ArgumentParser(description='')

dirname = os.path.dirname(__file__)


parser.add_argument(
                       "lang",
                       nargs="?",
                       type=str.lower,
                       help='Order the program to display C code.')

parser.add_argument(
                       "Snippet",
                       nargs='?',
                       type=str.lower,
                       help='The code snippet you want to display.')

args = parser.parse_args()                                              


if args.lang:



    if os.path.exists(os.path.join(dirname, "snippets/" + args.lang + "/" + args.Snippet + ".txt")): #Checks for text files corresponding to the snippet argument
        try:
            l = (dirname + "/snippets/" + args.lang + "/" + args.Snippet + ".txt")
            f = open(l, 'r') #Open snippet
            print(highlight(f.read())) #Highlight and print
        except Exception as e:
            print(e)
    else:
        print(Fore.RED + os.path.join(dirname, "snippets/" + args.lang +"/" + args.Snippet + ".txt") + " Invalid path")