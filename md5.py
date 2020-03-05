import hashlib
print("This program will convert string to md5 hash")
value = input("Enter string : ")
result = hashlib.md5(value.encode())
print("hash by md5 : ", end="")
print(result.hexdigest())
