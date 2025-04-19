import requests

def fetch_leetcode_stats(username):
    """
    Fetch the number of submissions made by the student on LeetCode.
    """
    url = f"https://leetcode.com/{username}/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Extracting the number of submissions from the HTML page
        submissions_section = response.text.split('submissions={')[1].split('}')[0]
        submissions_data = eval(f"{{{submissions_section}}}")  # Convert to dictionary
        total_submissions = submissions_data.get('total', 0)
        
        return total_submissions
    except Exception as e:
        print(f"Error fetching LeetCode data: {e}")
        return 0  # Return 0 if there is an issue
