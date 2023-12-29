from bs4 import BeautifulSoup

def analyze_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            analyze_html(html_content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

def analyze_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    form_elements = soup.find_all('form')
    
    if not form_elements:
        print("No forms found on the page.")
        return

    for form in form_elements:
        print(f"\nForm ID: {form.get('id', 'N/A')}, Method: {form.get('method', 'N/A')}")
        
        input_elements = form.find_all(['input', 'textarea', 'select'])

        text_boxes = 0
        password_boxes = 0
        check_boxes = 0
        radio_buttons = 0

        for input_element in input_elements:
            input_type = input_element.get('type', '').lower()

            if input_type == 'text':
                text_boxes += 1
            elif input_type == 'password':
                password_boxes += 1
            elif input_type == 'checkbox':
                check_boxes += 1
            elif input_type == 'radio':
                radio_buttons += 1

        print(f"Text Boxes: {text_boxes}")
        print(f"Password Boxes: {password_boxes}")
        print(f"Check Boxes: {check_boxes}")
        print(f"Radio Buttons: {radio_buttons}")

if __name__ == "__main__":
    # Replace 'your_file_path_here' with the path to your HTML file
    file_path = 'html_content.html'

    analyze_html_file(file_path)
