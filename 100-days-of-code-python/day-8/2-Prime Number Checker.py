# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if is_prime:
        print("Número primo.")
    else:
        print("Número não é primo.")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Checar este número: "))
prime_checker(number=n)
