import re


if __name__ == '__main__':
    # Check whether email is in correct format or not using regular expressions
    email = input('Enter email::')
    email_check = re.search('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$', email)

    if email_check:
        print('\nEmail is in correct format')
    else:
        print('\nEmail is not in correct format')

