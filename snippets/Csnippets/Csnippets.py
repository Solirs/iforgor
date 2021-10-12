from colorama import Fore, Style
from .. import syntax

def struct():
    print(syntax.highlight('''struct StructName
    {
    int variable1;
    int variable2;
    int OtherVariable;
    double  DecimalNumber;
    };
    '''))

def ifelse():
    print(syntax.highlight('''if (test expression) 
{
   // code
}'''))

#TODO! Add lists and functions