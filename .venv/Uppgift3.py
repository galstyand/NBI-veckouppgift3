print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
amountSum = 0

while True:
    amount = input("Skriv in ett belopp: ")
    if amount == "quit":
        break
    elif amount.isdigit() and int(amount) >= 0:
        amountSum += int(amount)
    else:
        print("Fel, prova ange ett tal")

print("Det blir " + str(amountSum) + " kr totalt. Välkommen åter!")