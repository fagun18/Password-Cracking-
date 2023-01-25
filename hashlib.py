import hashlib
import itertools

# The hashed password
hashed_password = "5f4dcc3b5aa765d61d8327deb882cf99"

# The characters to use in the brute-force attack
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# Try all possible combinations of characters
for password_length in range(1, 9):
    for password in itertools.product(chars, repeat=password_length):
        password = "".join(password)
        # Hash the current password
        hashed_password_guess = hashlib.md5(password.encode()).hexdigest()
        # Compare the hashed password to the hashed password guess
        if hashed_password == hashed_password_guess:
            print("Password found:", password)
            exit()
