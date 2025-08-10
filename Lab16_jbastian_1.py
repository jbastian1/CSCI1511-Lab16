from operator import itemgetter

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")


# Process information about each submission. 2 submission_ids = r.json()

# Lab 16: empty repo modules only needed; python3 -m pip install requests, link to repository (hard to forget data file)        ?not having an exception?
# 1 in-textbook code CH17 hn_submissions.py take it load in - will cause exception - not everything has descendants likely - have not hit error - rewrite build dictionary for each block
# 2 plotting: python_repos_visual.py in the textbook & in resources rename python, from GitHub API, looks for python related projects and how many stars they have, rest is replace Python (in text, might have to change stas number 10000) with a different programming language

# short answers:
# 1 starin GitHub, give a star repository, look up what does and why good thing
# 2 hacker news API - section textbook - website returns articles, API website specialized sends back GitHub instead of render website, benefits - freeform search internet ex. wikipedia