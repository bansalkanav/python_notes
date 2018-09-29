# pip install Werkzeug
from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)

wrong_check = check_password_hash(hashed_pass,'wrong')
print(wrong_check)

right_check = check_password_hash(hashed_pass,'mypassword')
print(right_check)
