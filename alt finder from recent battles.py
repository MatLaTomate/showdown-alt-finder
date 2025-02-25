import requests
import re
from bs4 import BeautifulSoup

# Set user-agent to avoid getting blocked
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

# Function to fetch user data
def get_user_data(user):
    try:
        website = requests.get(f"https://pokemonshowdown.com/users/{user}", headers=HEADERS)
        usersoup = BeautifulSoup(website.content, "html.parser")

        # Check if the page contains a "Joined:" string to determine if the user is registered
        if usersoup.body.findAll(string='Joined:'):
            # If "Joined:" is found, it means the user is registered, so we skip adding them
            return None  # Registered user, return None
        else:
            # If the profile doesn't contain "Joined:", or the profile failed to load, add to stealable list
            return user  # Unregistered or failed to load profile
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for {user}, skipping... Error: {e}")
        return user  # Return username in case of error (means it's unregistered or failed to load)

# Fetch ladder data for a specific tier
def get_ladder_data(tier):
    # Fetch the ladder page
    website = requests.get(f'https://pokemonshowdown.com/ladder/{tier}', headers=HEADERS)
    soup = BeautifulSoup(website.content, "html.parser")

    # Empty list to store usernames and stealable usernames
    usernames = []
    stealable = []

    # Extract all usernames from the ladder page
    for a in soup.find_all('a', href=True)[7:]:  # Skipping the first 7 elements to avoid irrelevant links
        usernames.append(a['href'].replace("/users/", ""))

    print(f"Found {len(usernames)} usernames on the ladder.")

    # Check each username for registration
    for user in usernames:
        stealable_user = get_user_data(user)
        if stealable_user:
            stealable.append(stealable_user)

    print(f"Stealable usernames (unregistered or failed to load): {stealable}")

# Main entry point
if __name__ == "__main__":
    tier = input("Enter the tier (e.g., 'gen9ou'): ")
    get_ladder_data(tier)

input("Press Enter to exit...")
