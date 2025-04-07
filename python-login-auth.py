# This package will be used in this basic form for delaying the time
import time

# Configurable credentials
USERNAME = 'EZZY'
PASSWORD = 'botcoder'

# Made it a function so that we can call it anytime we need and fill the form.
# The .strip() function will remove any space placed while inputting the credentials to avoid errors
def authenticate():
    username_input = input('🔐 Enter your username: ').strip()
    password_input = input('🔑 Enter your password: ').strip()

    # Used the if statement to confirm the credentials the user puts
    if username_input == USERNAME:
        if password_input == PASSWORD:
            print('\n✅ Access granted.')
            loading_sequence()
        else:
            print('\n❌ Password incorrect.')
    elif password_input == PASSWORD:
        print('\n❌ Username incorrect.')
    else:
        print('\n⚠️ Check both fields. Something’s off.')

# This function handles the response after successful login
def loading_sequence():
    print('⏳ Please wait...')
    time.sleep(2)
    print('🔄 Verifying credentials...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('\n🛡️ Security clearance granted.')
    print('🧠 Welcome! Accessing the system dashboard...')

if __name__ == '__main__':
    authenticate()
