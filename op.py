import requests
from bs4 import BeautifulSoup
import re

def analyze_meta_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    meta_title = soup.find('meta', attrs={'name': 'title'})
    meta_desc = soup.find('meta', attrs={'name': 'description'})

    if meta_title:
        title = meta_title['content']
        if len(title) > 60:
            print(f"Meta Title: {title} (> 60 characters)")
        else:
            print(f"Meta Title: {title} (OK)")
    else:
        print("Meta Title not found")

    if meta_desc:
        description = meta_desc['content']
        if len(description) > 150:
            print(f"Meta Description: {description} (> 150 characters)")
        else:
            print(f"Meta Description: {description} (OK)")
    else:
        print("Meta Description not found")

def analyze_headings(html):
    soup = BeautifulSoup(html, 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    for heading in headings:
        print(f"Heading: {heading.text} (Tag: {heading.name})")

def analyze_url(url):
    if len(url) > 2048:
        print(f"URL: {url} (> 2048 characters)")
    else:
        print(f"URL: {url} (OK)")

def analyze_content_structure(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')

    if not paragraphs:
        print("No paragraphs found")
    else:
        print("Paragraphs found:")
        for paragraph in paragraphs:
            print(f" - {paragraph.text}")

def main(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        html = response.text
        analyze_meta_tags(html)
        analyze_headings(html)
        analyze_url(url)
        analyze_content_structure(html)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    print("Made by Satulabs - SEO On Page Audit Free Bot")
    url = input("Enter the URL to analyze: ")
    main(url)
