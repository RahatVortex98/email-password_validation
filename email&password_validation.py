import re

# Email validation pattern
email_pattern = re.compile(r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)")
# Password validation pattern (at least 8 characters with allowed symbols)
password_pattern = re.compile(r"^[a-zA-Z0-9$%#@]{8,}$")

# Take input from the user
email = input("Enter your email: ")
password = input("Enter your password (at least 8 characters): ")

# Validate email
email_match = email_pattern.search(email)
password_match = password_pattern.search(password)

# Check email validity
if email_match:
    print('Valid email:', email_match.group())
else:
    print('Invalid email')

# Check password validity
if password_match:
    print('Valid password:', password_match.group())
else:
    print('Invalid password')
