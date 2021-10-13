import argparse, os
import sys
import snippets
from snippets.syntax import *

parser = argparse.ArgumentParser(description='')

dirname = os.path.dirname(__file__)


parser.add_argument('-C',
                       "--Clang",
                       action='store_true',
                       help='Order the program to display C code.')

parser.add_argument('-Py',
                       "--Python",
                       action='store_true',
                       help='Order the program to display Python code.')

parser.add_argument(
                       "Snippet",
                       nargs='?',
                       type=str,
                       help='The code snippet you want to display.')

args = parser.parse_args()                                              


if args.Clang:


    if os.path.exists(os.path.join(dirname, "snippets/Csnippets/" + args.Snippet + ".txt")): #Checks for text files corresponding to the snippet argument
        try:
            l = (dirname + "/snippets/Csnippets/" + args.Snippet + ".txt")
            f = open(l, 'r')
            print(highlight(f.read())) #Highlight and print
        except Exception as e:
            print(e)


if args.Python:


    if os.path.exists(os.path.join(dirname, "snippets/PythonSnippets/" + args.Snippet + ".txt")): #Checks for text files corresponding to the snippet argument
        try:
            l = (dirname + "/snippets/PythonSnippets/" + args.Snippet + ".txt")
            f = open(l, 'r')
            print(highlight(f.read())) #Highlight and print
        except Exception as e:
            print(e)
