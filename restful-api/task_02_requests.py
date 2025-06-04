import requests
import csv


# Function to fetch posts and print their titles

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # Parse JSON response
        for post in posts:
            print(post['title'])  # Print the title of each post


# Function to fetch posts and save selected data to a CSV file

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()  # Parse JSON response

        # Create a list of dictionaries with only 'id', 'title', and 'body'
        selected_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Write the selected data to a CSV file
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()  # Write the header row
            writer.writerows(selected_posts)  # Write all posts as rows
