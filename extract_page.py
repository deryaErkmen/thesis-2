import os
import requests
from bs4 import BeautifulSoup
import re

def fetch_html_and_js(url):
    # Fetch HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract JavaScript code using regex
    script_tags = soup.find_all('script')
    js_code = '\n'.join(script.text for script in script_tags)

    return html_content, js_code

def write_to_file(file_name, content):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    return file_path

def main():
    # Replace 'your_url_here' with the URL you want to analyze
    url = 'https://medium.com/@jamischarles/xss-aka-html-injection-attack-explained-538f46475f6c'

    html_content, js_code = fetch_html_and_js(url)

    # Write HTML content to a file
    html_file_path = write_to_file(r'html_content.html', html_content)
    print(f"HTML content written to '{html_file_path}'")

    # Write JavaScript code to a file
    js_file_path = write_to_file(r'js_code.js', js_code)
    print(f"JavaScript code written to '{js_file_path}'")

if __name__ == "__main__":
    main()
