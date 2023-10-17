import json

# Load datasets
with open('followers_1.json') as f:
    followers_json = json.load(f)

with open('following.json') as f:
    following_json = json.load(f)

# Extract required fields
followers_cleaned = []
for follower in followers_json:
    for string in follower['string_list_data']:
        followers_cleaned.append(string['value'])

following_cleaned = []
for following in following_json['relationships_following']:
    for string in following['string_list_data']:
        following_cleaned.append(string['value'])

# Create list of following subtracted by followers
for follower in followers_cleaned:
    if follower in following_cleaned:
        following_cleaned.remove(follower)

# Sort list alphabetically
following_cleaned.sort()

# Write output list to storage
with open('not_followed_back.txt', 'w') as f:
    for following in following_cleaned:
        f.write(f"{following}\n")
