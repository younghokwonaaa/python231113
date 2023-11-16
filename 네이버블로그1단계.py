#네이버 블로그 1단계
import requests
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    # URL for Naver blog search
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information from the parsed HTML
        #blog_entries = soup.select('.sh_blog_title')

        blog_posts = soup.find_all('li', {'class':'bx'})

        # Iterate through each blog entry and extract information
        for entry in blog_posts:
            blog_url = entry['href']
            blog_name = entry.select_one('.txt84').get_text(strip=True)
            post_title = entry['title']
            posting_date = entry.select_one('.txt_time').get_text(strip=True)

            # Print or store the extracted information
            print("Blog URL:", blog_url)
            print("Blog Name:", blog_name)
            print("Post Title:", post_title)
            print("Posting Date:", posting_date)
            print("\n")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Set the search keyword
search_keyword = "iPhone 15"

# Call the function to start crawling
naver_blog_crawler(search_keyword)
