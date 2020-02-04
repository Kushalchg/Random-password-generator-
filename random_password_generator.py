import random,string


lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
symbol=string.punctuation
digits=string.digits


password_count=int(input("enter the length of  password:  "))
lowercase_count=int(input("how many lowercase letter in your password?  "))
uppercase_count=int(input("how many uppercase letter in your password?  "))
symbol_count= int(input("how many symbol letter in your password?  "))
digits_count= int(input("how many digits letter in your password?  "))



random_lowercase=random.choices(lowercase,k=lowercase_count)
random_uppercase=random.choices(uppercase,k=uppercase_count)
random_symbol=random.choices(symbol,k=symbol_count)
random_digits=random.choices(digits,k=digits_count)


if (password_count < lowercase_count+uppercase_count+symbol_count+digits_count):
    print("you entered extra  word than your password length")
elif(password_count > lowercase_count+uppercase_count+symbol_count+digits_count):
    print("you enterd less no of word than your password length")
else:
    final_password=random_digits+random_lowercase+random_symbol+random_uppercase
    print(" ".join(map(str,final_password)))

