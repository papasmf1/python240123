import re

def check_email(email):
    #raw string notation:날것 그대로 표기 
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 이메일 주소 10개
sample_emails = [
    'user@example.com',
    'john.doe123@gmail.com',
    'info@company.net',
    'invalid.email@',
    'no_at_sign.com',
    'missing_dot@domaincom',
    'special!chars@example.org',
    'user@localhost',
    'email with space@example.com',
    '@missing_username.com'
]

# 각 이메일 주소에 대한 결과 출력
for email in sample_emails:
    result = check_email(email)
    print(f'{email}: {"Valid" if result else "Invalid"}')
