import re

def validate_resident_registration(resident_number):
    pattern = re.compile(r'^\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])-[1234]\d{6}$')
    if re.search(pattern, resident_number):
        print(f"Resident registration number {resident_number} is valid.")
        return True
    else:
        print(f"Resident registration number {resident_number} is invalid.")
        return False

# Sample resident registration numbers to test
sample_numbers = [
    '920101-1234567',
    '750212-2234567',
    '880331-1456789',
    '051212-5212121',  # Invalid last digit
    '040506-1111111',
    '710607-2123456',
    '961008-1234567',
    '830909-2234567',
    '101010-1456789',
    '202011-6456789'   # Invalid first digit
]

# Testing each sample resident registration number
for number in sample_numbers:
    validate_resident_registration(number)
