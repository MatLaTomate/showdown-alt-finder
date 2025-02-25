# showdown-alt-stealer
A python pokemon showdown alt stealer checking the top 500 players of any ladder

You need to have python installed, i am using pythong 3.12 but some older versions might work such as 3.9

Pokémon Showdown Alt Finder
Description
This script allows you to scrape usernames from the Pokémon Showdown ladder for a specified tier and check whether those users are registered or not. It finds potentially unregistered accounts (alts) that could be "stealable" or used for various purposes. This is useful for people who want to identify unregistered users in specific tiers and potentially collect "alt" accounts.

Features
Scrapes the ladder of a given tier on Pokémon Showdown (e.g., gen9ou).
Checks if users are registered by attempting to fetch their profile data.
Outputs a list of unregistered users (alts).
Allows you to choose the tier to search.
Requirements
To run this script, you will need the following Python libraries:

requests
beautifulsoup4
re (regular expression, part of Python's standard library)

Installation

Clone this repository:
git clone https://github.com/yourusername/pokemon-showdown-alt-finder.git

Install the required dependencies:
pip install requests beautifulsoup4

How to Use

Run the script:
python alt_finder.py

The script will ask you to input the Pokémon Showdown tier you want to scrape (e.g., gen9ou).

It will fetch usernames from the ladder for the given tier and check if their profile is registered or unregistered. If a user's profile fails to load or doesn't contain the "Joined" text, they are considered an unregistered user (alt).

The script will output the list of "stealable" usernames (unregistered accounts).

Example Output

Enter the tier (e.g., 'gen9ou'): gen9ou
Found 20 usernames on the ladder.
Failed to fetch data for moyagoku, skipping...
Failed to fetch data for olfafa, skipping...
Stealable usernames (unregistered or failed to load): ['moyagoku', 'olfafa']

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
This script is for educational and research purposes only. Make sure to use it responsibly and within the rules of the Pokémon Showdown platform. Do not engage in any malicious activity with this script.

Source : https://replit.com/@allweezy/showdown-alt-finder 
