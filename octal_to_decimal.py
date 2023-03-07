num = int(input("Enter Octal number: "))



def OctalToDecimal(num):
    decimal_value = 0
    base = 1
    while(num):
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base = base * 8
    print("The decimal value is: ", decimal_value)


octal_num = input("Enter an octal number: ")
decimal_value = int(octal_num, 8)
print("The decimal of {} is {}".format(octal_num,decimal_value))