import discord
import asyncio
import sys
import webbrowser
from colorama import Fore, Style, init
import questionary
from questionary import Choice

# helpers
from myhelpers import print_header, urls, get_clickable_text, clear, Author

# Colorama Colors Fixes
init(autoreset=True)

# Main Classes
class Ghoster(discord.Client):
    async def on_ready(self):
        print_header()
        print(f"{Fore.GREEN}[+] Authenticated as: {self.user}\n")
        
        # Read All Servers
        guilds = list(self.guilds)

        # if !guilds, i close the script
        if not guilds:
            print(f"{Fore.RED}[!] No servers found.")
            await self.close()
            return

        choice = await questionary.select("Main Menu:",
                                          choices=["Leave ALL servers",
                                                   "SELECT servers to leave (Multi-Select)",
                                                   "Socials & Links",
                                                   "Exit"]
                                          ).ask_async()

        if choice == "Leave ALL servers":
            confirm = await questionary.confirm("Are you sure you want to leave EVERY server?").ask_async()
            if confirm:
                await self.process_leave(guilds)
            await self.close()

        elif choice == "SELECT servers to leave (Multi-Select)":
            server_options = [
                Choice(title=f"{g.name} (ID: {g.id})", value=g) 
                for g in guilds
            ]
            
            selected_guilds = await questionary.checkbox(
                "Select servers to leave (Space to select, Enter to continue):",
                choices=server_options
            ).ask_async()

            if selected_guilds:
                print(f"\n{Fore.YELLOW}[*] Selected {len(selected_guilds)} servers.")
                confirm = await questionary.confirm("Proceed with leaving these servers?").ask_async()
                if confirm:
                    await self.process_leave(selected_guilds)
            else:
                print(f"{Fore.YELLOW}[!] No servers selected.")
            
            await asyncio.sleep(2)
            await self.on_ready()

        elif choice == "Socials & Links":
            social_choice = await questionary.select(
                "Open link:",
                choices=list(urls.keys()) + ["Back"]
            ).ask_async()
            if social_choice != "Back":
                webbrowser.open(urls[social_choice])
            await self.on_ready()

        else:
            await self.close()

    async def process_leave(self, target_list):
        print(f"\n{Fore.RED}[!] Starting process... (Delay: 2.0s)")
        for guild in target_list:
            try:
                await guild.leave()
                print(f"{Fore.GREEN}[LEFT] {guild.name}")
                await asyncio.sleep(2.0)
            # RATE LIMIT
            except discord.HTTPException as e:
                if e.status == 429:
                    print(f"{Fore.RED}[RATE LIMIT] Discord is angry. Pausing for 15s...")
                    await asyncio.sleep(15)
                else:
                    print(f"{Fore.RED}[ERROR] Could not leave {guild.name}: {e}")
        print(f"\n{Fore.CYAN}[+] Task finished.")

def main():
    print_header()
    
    ddp_link = get_clickable_text("Discord Developer Portal", "https://discord.com/developers/applications")
    print(f"{Fore.CYAN}          DISCORD BOT CONFIGURATION")
    print(f"{Fore.WHITE}Ensure you have created an application at {Fore.YELLOW}{ddp_link}")
    print(f"{Fore.WHITE}and enabled the required {Fore.GREEN}Privileged Gateway Intents.\n")

    token = input(f"{Fore.CYAN}[?] Enter Bot Token: {Fore.WHITE}").strip()

    intents = discord.Intents.default()
    intents.guilds = True

    def attempt_bot_login():
        client_instance = Ghoster(intents=intents)
        try:
            print(f"{Fore.YELLOW}[*] Attempting Bot Login...")
            client_instance.run(token)
            return True
        except discord.LoginFailure:
            print(f"\n{Fore.RED}[!] Error: Invalid Bot Token.")
            return False
        except Exception as e:
            print(f"\n{Fore.RED}[ERROR] {e}")
            return False

    if not attempt_bot_login():
        print(f"{Fore.RED}[!] Login failed. Please verify your token in the Developer Portal.")
        sys.exit()

# RUN
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Interrupted.")
        sys.exit()
