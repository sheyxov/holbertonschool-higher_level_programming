#!/usr/bin/python3
"""Module that interacts with JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print status code + titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save id, title, body into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Extract required fields
        cleaned_posts = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(cleaned_posts)
