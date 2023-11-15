import re

def is_valid_email(email):
    # Define the regular expression pattern for a simple email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the search() function to check if the pattern matches the email
    match = re.search(pattern, email)
    
    # Return True if a match is found, indicating a valid email address
    return bool(match)

# Test 10 sample email addresses
sample_emails = [
    "user@example.com",
    "john.doe@company.co.uk",
    "invalid_email.com",
    "missing@dotcom",
    "user@.com",
    "user@company",
    "user@company.",
    "user@company..com",
    "@company.com",
    "user@company@com"
]

for email in sample_emails:
    print(f"{email}: {is_valid_email(email)}")



#import re


def validate_resident_registration_number(rrn):
    pattern = re.compile(r'^\d{6}-[1-2]\d{6}$')

    if pattern.match(rrn):
        return True
    else:
        return False

# 10 sample codes for testing
sample_rrns = [
    "950101-1234567",
    "021231-1123456",
    "880505-2123456",
    "731201-1123456",
    "041010-2123456",
    "110622-1123456",
    "960731-2123456",
    "800815-1123456",
    "690430-2123456",
    "050505-1123456"
]

# Test the sample codes
for rrn in sample_rrns:
    if validate_resident_registration_number(rrn):
        print(f"{rrn} is a valid Korean resident registration number.")
    else:
        print(f"{rrn} is NOT a valid Korean resident registration number.")
