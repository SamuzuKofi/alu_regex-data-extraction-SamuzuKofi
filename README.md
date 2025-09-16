# alu_regex-data-extraction-SamuzuKofi

## Project Overview

This project demonstrates how to use Python's regular expressions (`re` module) to extract structured data from unstructured text. The script, [`Regex.py`](Regex.py), scans a sample data file ([`Sample_data.txt`](Sample_data.txt)) and identifies patterns such as:

- URLs
- Phone numbers (various formats)
- Email addresses
- Credit card numbers
- Time (24-hour and 12-hour formats)
- HTML tags
- Hashtags
- Currency amounts

The results are printed to the console, grouped by pattern type.

## File Structure

- [`Regex.py`](Regex.py): Main script containing regex patterns and extraction logic.
- [`Sample_data.txt`](Sample_data.txt): Example text file with data to extract.
- [`README.md`](README.md): Project documentation.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.

### Steps

1. **Clone the repository or download the files** to your local machine.

2. **Navigate to the project directory** in your terminal:
   ```sh
   cd /path/to/alu_regex-data-extraction-SamuzuKofi
3. Run the script:
   ```sh
   python Regex.py

### Customization

To extract data from a different file, replace the contents of Sample_data.txt or modify the filename in Regex.py.
You can add or modify regex patterns in the PATTERNS dictionary in Regex.py to suit your needs.