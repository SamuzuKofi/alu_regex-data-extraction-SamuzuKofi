import re

PATTERNS = {
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\.[A-Za-z]{2,})?\b',
    "urls" : r'https?://(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?:/[^\s]*)?',
    "phone_numbers": r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "credit_cards": r'\b(?:\d[ -]*?){13,19}\b',
    "times": r'\b((?:[01]\d|2[0-3]):[0-5]\d|(?:0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM|am|pm))\b',
    "html_tags": r'<\/?[A-Za-z][A-Za-z0-9]*(?:\s+[A-Za-z-]+=(?:"[^"]*"|\'[^\']*\'))*\s*\/?>',
    "hashtags": r'#[\w]+',
    "currency_amounts": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+(?:\.\d{2})?'
}

def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def find_patterns(text):
    for label,pattern in PATTERNS.items():
        matches = re.findall(pattern, text)
        print(f"\n{label.upper()} Matches:")
        if matches:
            for match in matches:
                print(f" - {match}")
        else:
            print("No matches found")

if __name__ == "__main__":
    text = read_text_file("Sample_data.txt")
    find_patterns(text)