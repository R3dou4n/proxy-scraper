import os
import requests


def fetch_proxies():
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip().split('\n')
    else:
        print(f"Failed to fetch proxies. Status code: {response.status_code}")
        return None


def save_proxies_to_desktop(proxies):
    # Determine the user's home directory and append 'Desktop' to find the desktop directory
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') if os.name == 'nt' else os.path.join(
        os.path.join(os.path.expanduser('~')), 'Desktop')

    # Specify the filename
    filename = os.path.join(desktop, 'proxies.txt')

    # Write the proxies to the file
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

    print(f"Proxies saved to {filename}")


def main():
    while True:
        user_input = input("Type 'generate' to fetch proxies or 'exit' to quit: ")

        if user_input.lower() == 'generate':
            proxies = fetch_proxies()
            if proxies is not None:
                for proxy in proxies:
                    print(proxy)
                save_proxies_to_desktop(proxies)

        elif user_input.lower() == 'exit':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
