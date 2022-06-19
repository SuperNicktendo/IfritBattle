materia1 = "Fire"
materia2 = "Blizzard"
materia3 = "Thunder"

print("One of your summons has gone rogue! You better tame them with the right materia!");
materia = input("It's Ifrit! Will you use Fire, Blizzard or Thunder materia? ")
if materia == materia2:
    print("Excellent! Ifrit's flame is snuffed out by Blizzard!")
elif materia == materia1:
    print("Uh-oh! Fire has made Ifrit stronger!")
    materia = input("Try another materia: ")
    if materia == materia2:
        print("Excellent! Ifrit's flame is snuffed out by Blizzard!")
    elif materia == materia1:
        print("Ifrit's strength goes supernova! Your party falls...")
    elif materia == materia3:
        print("Thunder has little effect on Ifrit, but it stuns him long enough for your party to flee!")
elif materia == materia3:
    print("You zap Ifrit with Thunder, but he shrugs it off.")
    materia=input("Try another materia: ")
    if materia == materia2:
        print("Excellent! Ifrit's flame is snuffed out by Blizzard!")
    elif materia == materia1:
        print("Ifrit's strength goes supernova! Your party falls...")
    elif materia == materia3:
        print("Your second Thunder attack stuns Ifrit, giving your party a chance to flee!")