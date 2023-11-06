import json
import random

from main_page.models import User, Post

with open(r'bot/bot_config.json') as config_file:
    config = json.load(config_file)

base_url = "http://127.0.0.1:8000"


def create_user(username, email, password):
    user = User.objects.create(username=username, email=email)
    user.set_password(password)
    user.save()


def create_post(user, content):
    post = Post.objects.create(user=user, content=content)
    post.save()


def create_users(num_users):
    for i in range(1, num_users + 1):
        username = f"test_user{i}"
        email = f"user{i}@example.com"
        password = "password"
        create_user(username, email, password)

        print(f'User{i} created')


# Function to create posts
def create_posts(num_users, max_posts):
    for i in range(1, num_users + 1):
        user = User.objects.get(username=f"test_user{i}")
        max_posts = max_posts
        content = "Random content"

        posts_per_user = random.randint(1, max_posts)
        for _ in range(posts_per_user):
            create_post(user, content)

        print(f'User{i} created {posts_per_user} posts')


def add_like(post, user):
    post.likes.add(user)
    post.save()


# Function to randomly like posts
def like_posts(max_likes):
    for post in Post.objects.filter(content="Random content"):
        likes_for_post = random.randint(1, max_likes)

        for user in User.objects.filter(username__startswith="test_user").order_by('?')[:likes_for_post]:
            add_like(post, user)

        print(f"Post{post.id} was liked {likes_for_post} times by users")


def clear_content():
    for user in User.objects.filter(username__startswith="test_user"):
        user.delete()

    for post in Post.objects.filter(content="Random content"):
        post.delete()


def run():
    # Sign up users
    create_users(num_users=config["number_of_users"])

    # Post creation
    create_posts(num_users=config["number_of_users"],
                 max_posts=config["max_posts_per_user"])

    # Post liking
    like_posts(max_likes=config["max_likes_per_user"])

    # clear_content()
