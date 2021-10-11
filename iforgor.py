import argparse
import os
import sys
from snippets.Csnippets.Csnippets import *


parser = argparse.ArgumentParser(description='')


parser.add_argument('-C',
                       "--Clang",
                       action='store_true',
                       help='Order the program to display C code.')

parser.add_argument(
                       "Snippet",
                       nargs='?',
                       type=str,
                       help='The code snippet you want to display.')

args = parser.parse_args()                                              


if args.Clang:

    try:
        d = {
            "a":None
        }
        d["a"] = (args.Snippet)
        result = eval(d["a"] + "()")
    except Exception as e:
        pass

