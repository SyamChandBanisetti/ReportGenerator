# utils/leetcode_fetcher.py

import requests

def fetch_leetcode_data(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "totalSolved": data.get("totalSolved", 0),
            "easySolved": data.get("easySolved", 0),
            "mediumSolved": data.get("mediumSolved", 0),
            "hardSolved": data.get("hardSolved", 0),
            "ranking": data.get("ranking", "N/A")
        }
    else:
        raise Exception("Failed to fetch data from LeetCode API")
