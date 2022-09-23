import re
def fun(s):
    pattern="^[a-zA-Z0-9\-\_]+@[A-Za-z0-9]+[\.][a-zA-Z]{1,3}$"
    return re.search(pattern,s)!=None
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(('lara@hackerrank.com','brian-23@hackerrank.com','britts_54@hackerrank.com'))
filtered_emails.sort()
print(filtered_emails)