import re

with open("input.txt", "r") as file:
    content = file.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, content)

with open("emails_found.txt", "w") as output_file:
    for email in emails:
        output_file.write(email + "\n")

print("Found", len(emails), "email(s). Saved to emails_found.txt")
print(emails)