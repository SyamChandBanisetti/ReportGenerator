import requests

def fetch_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        submitStats: submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """
    variables = {"username": username}
    response = requests.post(url, json={"query": query, "variables": variables})
    
    if response.status_code == 200:
        data = response.json()
        submissions = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
        total_solved = sum(item["count"] for item in submissions if item["difficulty"] != "All")
        return total_solved
    else:
        return 0
