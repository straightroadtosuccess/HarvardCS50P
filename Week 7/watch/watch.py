import re


def main():
    s = input("HTML: ")
    print(parse(s))


def parse(s):
    # Pick up a valid youtube link
    match = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    # If it matches
    if match:
        # the group ID of 1
        video_id = match.group(1)
        # Convert it to youtu.be format
        return f"https://youtu.be/{video_id}"
    # Otherwise no valid result message
    return None


if __name__ == "__main__":
    main()
