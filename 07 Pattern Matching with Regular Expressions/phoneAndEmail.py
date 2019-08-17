#! /usr/bin/env python3

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re, pyperclip


# Create a regex for phone numbers
phoneRegex = re.compile(r'''(

(\d{3} | \(\d{3}\))?              # area code (optional)
(\s|-|\.)?                        # separator
(\d{3})                           # first 3 digits
(\s|-|\.)                         # separator
(\d{4})                           # last 4 digits
(\s*(ext|x|ext.)\s*               # extension word part (optional)
(\d{2,5}))?                       # extension number part (optional)
)
''', re.VERBOSE)


# Create a regex for email addresses.
emailRegex = re.compile(r'''(

[a-zA-Z0-9_.+]+                   # username
@                                 # @ symbol
[a-zA-Z0-9_.+]+                   # domain name
(\.[a-zA-Z]{2,4})                 # dot-something
)

''', re.VERBOSE)

   
# Get the text off the clipboard
text = pyperclip.paste()



# Extract the email/phone from this text.
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])



# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# TODO: Copy the extracted email/phone to the clipboard.
# results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
# pyperclip.copy(results)


# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
