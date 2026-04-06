<p align="center">
  <img src=".github/DiscordGhosterBanner.png" alt="DiscordGhoster Banner">
</p>

<h1 align="center">DiscordGhoster</h1>

<p align="center">
  <a href="https://github.com/fnicefire/DiscordGhoster/stargazers">
    <img src="https://img.shields.io/github/stars/fnicefire/DiscordGhoster?style=for-the-badge&color=5865F2&cacheSeconds=5" alt="Stars">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  </a>
  <a href="https://discordpy.readthedocs.io/">
    <img src="https://img.shields.io/badge/discord.py-supported-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="discord.py">
  </a>
  <a href="DiscordGhoster/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </a>
</p>

---

**DiscordGhoster** is The Ultimate Discord Account Tool.

It supports:

- leaving **all servers** at once
- selecting **specific servers** with a multi-select prompt
- attempting login with both **bot tokens** and, if requested, **user tokens**

## Warning

This project includes support for **user token login** via self-bot mode.

Using user tokens on Discord is against the [Discord Terms of Service](https://discord.com/terms) and may put an account at risk of restrictions or bans. Use this software responsibly and only if you fully understand the risks.

## Features

- Interactive terminal UI powered by `questionary`
- Clean styled output with `colorama` and `pyfiglet`
- Bulk leave workflow with built-in delay between guild exits
- Multi-select server picker for more controlled cleanup
- Fallback flow for user-token login if bot-token login fails
- Quick access to external links from inside the menu

## Requirements

- `Python 3.10+`
- `discord.py`
- `discord.py-self`
- `questionary`
- `pyfiglet`
- `colorama`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/fnicefire/DiscordGhoster.git
cd DiscordGhoster
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with:

```bash
python main.py
```

At startup the tool:

1. shows a legal warning
2. asks you to accept responsibility
3. prompts for a Discord token
4. tries bot login first
5. optionally asks whether the token is a user token if standard login fails

After login, the main menu lets you:

- leave every server
- choose which servers to leave
- open socials and links
- exit safely

## Project Structure

```text
DiscordGhoster/
│   .gitignore
│   LICENSE
│   main.py
│   myhelpers.py
│   requirements.txt
│
└── .github/
        DiscordGhosterBanner.png
```

## Notes

- The script adds a small delay between leave requests to reduce the chance of hitting Discord rate limits.
- If a rate limit is detected, it pauses before continuing.
- Server management requires the token to have access to the guilds visible to that account.

## License

Distributed under the MIT License. See [LICENSE](DiscordGhoster/LICENSE) for details.

## Credits

Created by [rotafn](https://github.com/fnicefire).
