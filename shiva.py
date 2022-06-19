materia1 = "Fire"
materia2 = "Blizzard"
materia3 = "Thunder"

print("One of your summons has gone rogue! You better tame them with the right materia!");
materia = input("It's Shiva! Will you use Fire, Blizzard or Thunder materia? ")
if materia == materia1:
    print("Excellent! Shiva's power melts in the face of your Fire magic!")
elif materia == materia2:
    print("Uh-oh! Blizzard has made Shiva stronger!")
    materia = input("Try another materia: ")
    if materia == materia1:
        print("Excellent! Shiva's power melts in the face of your Fire magic!")
    elif materia == materia2:
        print("You have empowered Shiva and she unleashes Diamond Dust! Your party falls...")
    elif materia == materia3:
        print("Thunder has little effect on Shiva, but it stuns her long enough for your party to flee!")
elif materia == materia3:
    print("You zap Shiva with Thunder, but she shrugs it off.")
    materia=input("Try another materia: ")
    if materia == materia1:
        print("Excellent! Shiva's power melts in the face of your Fire magic!")
    elif materia == materia2:
        print("You have empowered Shiva and she unleashes Diamond Dust! Your party falls...")
    elif materia == materia3:
        print("Your second Thunder attack stuns Ifrit, giving your party a chance to flee!")
