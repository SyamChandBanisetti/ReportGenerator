# leetcode_fetcher.py
import requests

def fetch_leetcode_stats(username):
    """
    Fetches the number of Leetcode submissions made by the given user.
    Returns the number of submissions.
    """
    url = f"https://leetcode.com/{username}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Scraping the number of problems solved from the user's profile page
        solved = response.text.split('class="total-solved-problems"')[1]
        solved = solved.split('<span>')[1].split('</span>')[0]
        return int(solved)
    else:
        return 0
