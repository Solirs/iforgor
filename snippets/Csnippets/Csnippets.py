from colorama import Fore, Style

def struct():
    print(f'''{Fore.BLUE}struct{Style.RESET_ALL} StructName
    {{
    {Fore.GREEN}int {Style.RESET_ALL} variable1;
    {Fore.GREEN}int {Style.RESET_ALL}variable2;
    {Fore.GREEN}int {Style.RESET_ALL}OtherVariable;
    {Fore.GREEN}double {Style.RESET_ALL} DecimalNumber;
    }};
    ''')

#TODO! Add lists and functions