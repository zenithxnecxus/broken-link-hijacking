import requests
import re
from urllib.parse import urljoin, urlparse
import time
import random
from collections import deque
from colorama import init, Fore, Style
from colorama import init, Fore, Back, Style

init(autoreset=True)

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

print(f"""{RED}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠴⠖⠒⠛⠛⠒⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⠃⠀⠀⠀⣀⡀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣴⣶⣿⣿⣷⠟⠉⠉⢳⡄⠀⠀⠀⠀⠀⠀⣯⠉⠙⠒⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣆⣀⣀⣴⠇⠀⠀⠀⠀⡤⠀⣼⣇⠀⠀⠀⠀⠈⠙⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⣿⠾⠷⣿⣿⣦⡀⠀⠀⠀⠀⣴⠃⢠⠇⢹⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠀⣠⡟⠁⠙⠿⣦⠀⢀⣾⠏⢠⠏⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⡏⠉⠉⠙⠛⠛⠛⠛⠛⠿⠶⠶⠶⢶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠟⣟⠀⠀⣀⣴⣟⣴⣟⣡⣴⣯⣤⣀⣼⠀⠀⠀⢰⡄⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⢸⠀⠸⣿⣿⣟⣋⣉⣉⣯⣀⣸⠃⠀⠈⠃⠀⠀⠀⢘⣇⠀⠀⠀⠀⠀⣠⡦⠀⠙⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⢸⡆⢰⣟⣚⣛⣛⣿⣛⣛⣛⣿⣆⣀⣀⣀⣤⡀⠀⠀⢿⡄⡄⠀⢀⣾⣿⠇⠀⠀⠹⡄⠀⠀⠀⠀⠀
⢤⢤⣤⣀⣀⣱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⢀⣀⣀⣠⣾⣧⣸⡇⠀⠀⠀⠀⣠⡾⣛⣋⣭⡥⠴⠂⠘⣿⡄⠀⠘⣿⣧⡴⠟⠋⣁⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠉⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡟⠉⠙⠻⣍⠉⠃⠙⠷⠤⢤⠤⠤⠼⠿⣿⣯⠤⠤⠐⠀⠀⢻⣿⣦⣤⣾⠿⣷⣶⣯⣥⣴⣶⣶⣦⣼⡆⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡶⠶⠒⣿⣄⣀⣀⡀⠀⢸⡆⠀⠀⢠⠏⢳⡖⠒⠒⠀⠀⢸⣿⣇⠈⠙⡆⠀⠙⠣⠀⠀⠀⠀⠀⠙⣧⠀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣥⣿⣯⣿⣿⣿⠿⢿⣶⣶⣾⠤⢬⣽⣷⣶⣦⣴⣿⣿⠏⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣈⣉⣽⣿⣶⠖⠀⠉⠉⠙⠳⠤⣤⣴⣃⣀⣀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠲⠤⢄⣀⣀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⠟⠛⠛⠛⠛⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠓⠛⠓⠢⠤⣄
⠸⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠬⠭⠭⠿⠶⢶⣶⣾⣯⡤⡥⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢼
{RESET}
{Back.LIGHTBLACK_EX}{Fore.CYAN}     BROKEN LINK HIJACKING SCANNER     {Style.RESET_ALL}
{Back.BLUE}{Fore.WHITE}developer: zenithx | telegram: @zenithx_9{Style.RESET_ALL}
""")

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 KHTML, like Gecko Version/17.1 Safari/605.1.15',
]

def get_random_ua():
    return random.choice(USER_AGENTS)

SOCIAL_PATTERNS = {
    'Instagram': {
        'pattern': r'instagram\.com/([a-zA-Z0-9_.]+)',
        'check_url': 'https://www.instagram.com/{}/'
    },
    'Twitter': {
        'pattern': r'twitter\.com/([a-zA-Z0-9_]+)',
        'check_url': 'https://twitter.com/{}'
    },
    'Facebook': {
        'pattern': r'facebook\.com/([a-zA-Z0-9.]+)',
        'check_url': 'https://facebook.com/{}'
    },
    'GitHub': {
        'pattern': r'github\.com/([a-zA-Z0-9_-]+)',
        'check_url': 'https://github.com/{}'
    },
    'LinkedIn': {
        'pattern': r'linkedin\.com/in/([a-zA-Z0-9_-]+)',
        'check_url': 'https://linkedin.com/in/{}'
    },
    'Telegram': {
        'pattern': r't\.me/([a-zA-Z0-9_]+)',
        'check_url': 'https://t.me/{}'
    },
    'YouTube': {
        'pattern': r'youtube\.com/@([a-zA-Z0-9_.-]+)',
        'check_url': 'https://www.youtube.com/@{}'
    },
    'TikTok': {
        'pattern': r'tiktok\.com/@([a-zA-Z0-9_.]+)',
        'check_url': 'https://www.tiktok.com/@{}'
    },
}

def extract_links_from_html(html, current_url, base_domain):
    links = []
    href_pattern = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)

    for match in href_pattern.finditer(html):
        url = match.group(1)
        if not url or url.startswith('#') or url.startswith('javascript:'):
            continue

        full_url = urljoin(current_url, url)
        parsed = urlparse(full_url)
        if not parsed.netloc:
            continue

        skip_ext = ['.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico', '.webp', '.mp4', '.pdf', '.zip']
        if any(full_url.lower().endswith(ext) for ext in skip_ext):
            continue

        if base_domain in parsed.netloc:
            links.append(('internal', full_url, current_url))
        else:
            links.append(('external', full_url, current_url))

    return links

def crawl_all_pages(start_url, max_pages=100):
    print(f"[*] Starting full website crawl")
    print(f"[*] Target: {start_url}")
    print(f"[*] Max pages: {max_pages}\n")

    parsed_start = urlparse(start_url)
    base_domain = parsed_start.netloc

    visited = set()
    queue = [start_url]
    external_links = {}
    pages_crawled = 0

    while queue and pages_crawled < max_pages:
        current_url = queue.pop(0)

        if current_url in visited:
            continue

        visited.add(current_url)
        pages_crawled += 1

        print(f"{CYAN}[{pages_crawled}/{max_pages}] Crawling: {current_url[:80]}{RESET}")

        try:
            headers = {'User-Agent': get_random_ua()}
            response = requests.get(current_url, headers=headers, timeout=10)
            if response.status_code != 200:
                continue

            links = extract_links_from_html(response.text, current_url, base_domain)

            for link_type, link_url, source_page in links:
                if link_type == 'internal':
                    if link_url not in visited and link_url not in queue:
                        queue.append(link_url)
                else:
                    if link_url not in external_links:
                        external_links[link_url] = []
                    if source_page not in external_links[link_url]:
                        external_links[link_url].append(source_page)

            time.sleep(0.3)

        except Exception as e:
            print(f"{RED}    Error: {e}{RESET}")
            continue

    print(f"\n[+] Crawl completed")
    print(f"[+] Pages crawled: {pages_crawled}")
    print(f"[+] Unique external links found: {len(external_links)}\n")

    return external_links

def extract_social_from_url(url):
    for platform, data in SOCIAL_PATTERNS.items():
        match = re.search(data['pattern'], url, re.IGNORECASE)
        if match:
            username = match.group(1)
            username = username.split('?')[0].split('/')[0].split('#')[0]
            return platform, username
    return None, None

def check_account_status(platform, username):
    check_url = SOCIAL_PATTERNS[platform]['check_url'].format(username)

    headers = {
        'User-Agent': get_random_ua(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    try:
        response = requests.get(check_url, headers=headers, timeout=10, allow_redirects=True)

        if response.status_code == 200:
            text_lower = response.text.lower()
            keywords = ['not found', 'sorry', 'page not found', 'doesn\'t exist']
            if any(kw in text_lower for kw in keywords):
                return 'INACTIVE', f"{RED}[INACTIVE] Can be hijacked{RESET}"
            return 'ACTIVE', f"{GREEN}[ACTIVE]{RESET}"
        elif response.status_code == 404:
            return 'INACTIVE', f"{RED}[INACTIVE] Can be hijacked{RESET}"
        else:
            return 'UNKNOWN', f"{YELLOW}[UNKNOWN] HTTP {response.status_code}{RESET}"

    except Exception:
        return 'UNKNOWN', f"{YELLOW}[UNKNOWN] Request failed{RESET}"

def main():
    target = input(f"{CYAN}[?] Enter website URL: {RESET}").strip()
    if not target.startswith('http'):
        target = 'https://' + target

    max_pages_input = input(f"{CYAN}[?] Max pages to crawl (default 50, 0 = unlimited): {RESET}").strip()
    max_pages = 999999 if max_pages_input == '0' else int(max_pages_input) if max_pages_input.isdigit() else 50

    print()

    external_links = crawl_all_pages(target, max_pages)

    if not external_links:
        print(f"{RED}[-] No external links found!{RESET}")
        return

    social_accounts = {}
    for link_url, source_pages in external_links.items():
        platform, username = extract_social_from_url(link_url)
        if platform and username:
            key = f"{platform}:{username}"
            if key not in social_accounts:
                social_accounts[key] = {
                    'platform': platform,
                    'username': username,
                    'url': link_url,
                    'found_on': source_pages
                }

    if not social_accounts:
        print(f"{YELLOW}[-] No social media accounts found!{RESET}")
        return

    print(f"{BLUE}LIST OF FOUND ACCOUNTS:{RESET}")
    for i, (key, acc) in enumerate(social_accounts.items(), 1):
        print(f"  {i}. {acc['platform']}: @{acc['username']}")
        print(f"     URL: {acc['url']}")
        print(f"     Found on:")
        for src in acc['found_on']:
            print(f"       -> {src}")
        print()

    print(f"{BLUE}CHECKING ACCOUNT STATUS{RESET}\n")

    results = []
    for i, (key, acc) in enumerate(social_accounts.items(), 1):
        print(f"{BLUE}[{i}/{len(social_accounts)}] Checking {acc['platform']}: @{acc['username']}...{RESET}")
        status, msg = check_account_status(acc['platform'], acc['username'])

        results.append({
            'platform': acc['platform'],
            'username': acc['username'],
            'url': acc['url'],
            'found_on': acc['found_on'],
            'status': status,
            'message': msg
        })

        print(f"    Status: {msg}\n")
        time.sleep(0.5)

    hijackable = [r for r in results if r['status'] == 'INACTIVE']
    active = [r for r in results if r['status'] == 'ACTIVE']

    if hijackable:
        print(f"{RED}POTENTIALLY HIJACKABLE ({len(hijackable)}):{RESET}\n")
        for item in hijackable:
            print(f"  Platform : {item['platform']}")
            print(f"  Username : @{item['username']}")
            print(f"  URL      : {item['url']}")
            print(f"  Status   : {RED}INACTIVE - Can be hijacked{RESET}")
            print(f"  Found on pages:")
            for src in item['found_on']:
                print(f"    -> {src}")
            print(f"  {'-'*50}\n")

    if active:
        print(f"{GREEN}ACTIVE ACCOUNTS ({len(active)}):{RESET}")
        for item in active:
            print(f"  - {item['platform']}: @{item['username']}")
        print()

    save = input(f"{CYAN}[?] Save report to file? (y/n): {RESET}").lower()
    if save == 'y':
        filename = f"hijack_report_{int(time.time())}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("BROKEN LINK HIJACKING REPORT\n")
            f.write("="*60 + "\n")
            f.write(f"Target URL : {target}\n")
            f.write(f"Scan Date  : {time.ctime()}\n")
            f.write(f"Total Social Accounts Found : {len(social_accounts)}\n")
            f.write("="*60 + "\n\n")

            if hijackable:
                f.write("POTENTIALLY HIJACKABLE ACCOUNTS:\n")
                f.write("-"*40 + "\n")
                for item in hijackable:
                    f.write(f"\nPlatform : {item['platform']}\n")
                    f.write(f"Username : @{item['username']}\n")
                    f.write(f"URL      : {item['url']}\n")
                    f.write("Found on pages:\n")
                    for src in item['found_on']:
                        f.write(f"  - {src}\n")
                    f.write("\n")

            f.write(f"\nACTIVE ACCOUNTS ({len(active)}):\n")
            f.write("-"*40 + "\n")
            for item in active:
                f.write(f"  - {item['platform']}: @{item['username']}\n")

        print(f"{GREEN}[+] Report saved to: {filename}{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[!] Scan interrupted by user{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}")







