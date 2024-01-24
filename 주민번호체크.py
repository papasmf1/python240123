import re

def check_korean_id(id_number):
    pattern = r'^\d{6}-?[1-4]\d{6}$'
    if re.match(pattern, id_number):
        return "Valid"
    else:
        return "Invalid"

# 샘플 주민등록번호 10개
sample_ids = [
    '950101-1234567',
    '011010-2345678',
    '8912121234567',
    '750505-3456789',
    '9901011234567',
    '810101-1234567',
    '620505-2345678',
    '0303031234567',
    '041212-3456789',
    '123-45-6789012'  # Invalid: 형식에 맞지 않음
]

# 각 주민등록번호에 대한 결과 출력
for id_number in sample_ids:
    result = check_korean_id(id_number)
    print(f'{id_number}: {"Valid" if result == "Valid" else "Invalid"}')
