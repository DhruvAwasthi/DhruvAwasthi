import feedparser

# Define the RSS feed URL
FEED_URL = 'https://www.dhruvawasthi.com/blog-feed.xml'

def fetch_recent_posts(feed_url, num=5):
    feed = feedparser.parse(feed_url)
    entries = feed.entries[:num]
    return [{"title": entry.title, "link": entry.link} for entry in entries]

def update_readme(posts):
    with open('README.md', 'r') as file:
        content = file.read()

        # Placeholder in your README
        placeholder = '<!-- BLOGS_START -->'
        end_placeholder = '<!-- BLOGS_END -->'

        start_index = content.find(placeholder) + len(placeholder)
        end_index = content.find(end_placeholder)

        new_content = ""
        for post in posts:
            new_content += f"- [{post['title']}]({post['link']})\n"

        updated_content = content[:start_index] + "\n" + new_content + content[end_index:]

        with open('README.md', 'w') as file:
            file.write(updated_content)

if __name__ == '__main__':
    recent_posts = fetch_recent_posts(FEED_URL, 5)
    update_readme(recent_posts)
