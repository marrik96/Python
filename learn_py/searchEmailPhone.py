#! python3
import re, pyperclip

# Email RegEx
emailRegex = re.compile(r'[a-zA-z0-9_.+]+@[a-zA-z0-9_.+]+', re.VERBOSE)

# Phone RegEx
phoneRegex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract email from text
extractedEmail = emailRegex.findall(text)
extractedPhone = phoneRegex.findall(text)

print(extractedEmail)
print(extractedPhone)

# TODO: Copy the extracted email/phone to the clipboard