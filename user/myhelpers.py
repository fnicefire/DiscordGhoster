import os
from pyfiglet import Figlet
from colorama import Fore, Style

# Configs
ScriptName = "DiscordGhoster"
Version    = "1.1"
Author     = "rotafn"
urls = {
    "Github": "https://github.com/fnicefire",
    "My Website": "https://rotafn.xyz",
    "X": "https://link.rotafn.xyz/x",
    "Cheap Games": "https://link.rotafn.xyz/instant"
}

def get_clickable_text(text, url):
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear()
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText(ScriptName))
    
    main_url = list(urls.values())[0] if urls else "#"
    clickable_author = get_clickable_text(Author, main_url)
    
    print(f"{Fore.WHITE}Version: {Fore.YELLOW}{Version}")
    print(f"{Fore.WHITE}Author:  {Fore.MAGENTA}{clickable_author} {Style.DIM}(Click to open Github)")
    
    links_str = " | ".join([get_clickable_text(name, link) for name, link in urls.items()])
    print(f"{Fore.CYAN}Links:   {links_str}")
    print(f"{Fore.CYAN}{'='*60}\n")
