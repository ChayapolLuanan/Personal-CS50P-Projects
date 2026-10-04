import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    if match := re.search(pattern, s, re.IGNORECASE):
        return f"https://youtu.be/{match.group(1)}"
    return None

if __name__ == "__main__":
    main()
