import bcrypt
import base64
import hashlib

password = "admin123"

hashed = bcrypt.hashpw(
	password, bcrypt.gensalt()
)

print(hashed)

#myhash = "$2a$10$EhKZbt52HYMWt0y8K4XqHuVsYXIKYyRjfog9Ohja6ywj4OVM17c2y"
#myhash = "$2a$10$APpOlap0TaMKX2i/6rU.1uFxN4RbCrwqbubxnQTYIkQ0fjakOcR4C"
myhash = "$2y$05$CLTHKADluV4REYqQCQckeuj.SMvjEXC0MaR2BHvimq12o/f7zqHqi"

if bcrypt.checkpw(password, myhash):
	print("It Matches!")
else:
	print("It Does not Match :(")


