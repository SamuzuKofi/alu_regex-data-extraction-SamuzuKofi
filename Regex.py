import re 


PATTERNS = {
  "emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
  "urls": r'https?://[^\s]+',
  "phone_numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
  "credit_cards": r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}',
  "times": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b'
}

def read_text_file(filename):
  with open(filename, 'r') as file:
    return file.read()

def extract_everything(text):
  for label, pattern in PATTERNS.items():
      matches = re.findall(pattern, text)
      print(f"\n{label.replace('_', ' ').upper()} FOUND")
      if matches:
          for match in matches:
              print(f"- {match}")
      else:
          print("No matches found.")

