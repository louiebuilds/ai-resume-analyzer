import re


def load_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group(0) if match else None


def extract_phone(text):
    pattern = r"(\+?\d{1,2}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}"
    match = re.search(pattern, text)
    return match.group(0) if match else None
