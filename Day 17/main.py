class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Panda")
user2 = User("002", "Nirav")

user1.follow(user2)
print(f"{user1.id} = {user1.name} with {user1.followers} followers and {user1.following} following")
print(f"{user2.id} = {user2.name} with {user2.followers} followers and {user2.following} following")
