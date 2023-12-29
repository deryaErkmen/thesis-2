import re

def detect_xss_vectors(text):
    # Regular expression for detecting potential XSS vectors
    xss_pattern = re.compile(r'(<|&lt;)[^>]*(script|alert)\s*\(.*\)[^>]*(>|&gt;)', re.IGNORECASE)

    # Find matches in the input text
    matches = re.findall(xss_pattern, text)

    return matches

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def main():
    # Replace 'your_file_path_here' with the path to your input file
    file_path = r'C:\Users\derya\Documents\thesis-2\js_code.js'

    # Read input text from the file
    input_text = read_text_from_file(file_path)

    if input_text is not None:
        # Detect XSS vectors
        xss_matches = detect_xss_vectors(input_text)

        # Print the results
        if xss_matches:
            print("Potential XSS Vectors Detected:")
            for match in xss_matches:
                print(match)
        else:
            print("No potential XSS vectors detected.")

if __name__ == "__main__":
    main()
