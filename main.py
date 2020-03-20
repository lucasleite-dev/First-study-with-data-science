# A list of dictionaries with the data for each user.
users = [{"id": 0, "name": "Hero"}, {"id": 1, "name": "Dunn"}, {"id": 2, "name": "Sue"}, {"id": 3, "name": "Chi"}, {"id": 4, "name": "Thor"},{"id": 5, "name": "Clive"}, {"id": 6, "name": "Hicks"}, {"id": 7, "name": "Devin"}, {"id": 8, "name": "Kate"}, {"id": 9, "name": "Klein"}] 

# Friendship connections using each user's id
friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)] 

# Scroll through each user by adding the "friends" key that will receive a list of friends
for user in users: user["friends"] = []

for user , friend in friendship:
    users[user]["friends"].append(users[friend])# Add friend as user friend
    users[friend]["friends"].append(users[user]) # Add user as friend
    
def number_friends(user): # Returns the size of the user's friends list
    return len(user["friends"])

total_connections = sum(number_friends(user) for user in users) # Sums the size of the friends lists of all users
number_users = len(users) # Total users
avg_connections = total_connections / number_users # Average connections

number_friends_for_id = [(user["id"], number_friends(user)) for user in users] # Insert user id and number of friends eg: (id = 1, friend_type = 3)

number_friends_for_id.sort(key=lambda num: num[1], reverse=True) # Sort from largest to smallest

print(f"Total connections: {total_connections}") # Prints the total connections
print(f"Avg connections: {avg_connections}") # Prints the average of connections
print(f"Number friends for id: {number_friends_for_id}") # Print the list of friends by id
