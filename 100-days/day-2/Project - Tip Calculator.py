# 1. Dar saudações ao usuário.
print("Welcome to the tip calculator.")

# 2. Peça ao usuário o total da conta.
total_bill = float(input("What was the total bill? $"))

# 3. Pergunte ao usuário a porcentagem de gorjeta
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# 4. Calculo do total da conta com a gorjeta inclusa.
total_bill_with_tip = total_bill * (tip / 100)

# 5. Pergunte em quantas pessoas deve-se dividir a conta.
people = int(input("How many people to split the bill? "))
# 6. Calculo do total por pessoa.
total_people = total_bill_with_tip / people
# 7. Informe ao usuário quanto cada pessoa deve pagar.
print(f"Each person should pay: ${total_people:.2f}")
