print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
amountSum = 0

while True:
    amount = input("Skriv in ett belopp: ")
    if amount == "quit":
        personCount = input("Hur många är ni? ")

        while not personCount.isdigit() or int(personCount) <= 0:
            personCount = input("Ogiltigt tal. Ange ett tall 1 eller större ")

        tip = input("Hur mycket procent dricks vill ni ge? Lämna tomt blir dricksen 10%. ")
        while not tip.isdigit() or int(tip) <= 0:
            if tip != "":
                tip = input("Ogiltigt tal. Ange ett tall 1 eller större. ")
            else:
                tip = 10
                break

        tipAmount = int(tip) * amountSum / 100
        amountSum += tipAmount

        print("Det blir " + str(amountSum) + " kr totalt, alltså " + str(amountSum/int(personCount)) +
                  "kr per person. Välkommen åter!")
        break
    elif amount.isdigit() and int(amount) >= 0:
        amountSum += int(amount)
    else:
        print("Fel, prova ange ett tal")