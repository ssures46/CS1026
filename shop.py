# File Name: shop.py
# Author Name: Sivaramchandar Suresh
# Date: Saturday, March 11, 2022
# The purpose of this program is to demonstrate my knowledge of calling functions, using return values, getting user
# input in a loop, conditionals, lists, 2d lists and tuples, and string formatting and cleaning output to get the user
# to purchase or order a custom build or prebuilt computer online.
# Here the constants SSD, HDD, CPU, MOTHERBOARD, RAM, GRAPHICS_CARD, PSU, CASE, PREBUILTS are being initialized to a
# list.
SSD= [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD= [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU= [['1', 'Intel Core i7-11700k', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD= [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM= [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD= [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU= [['1', 'Corsair RM750', 164.99]]
CASE= [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
PREBUILTS= [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99],
            ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]

# This function will present two options for the CPU and mandate the user to select one of them. Afterwards, this
# function will return the CPU that the user has selected.
def selectCPU():
    print("First, let's pick a CPU.")
    print("1 : Intel Core i7-11700k, $499.99")
    print("2 : AMD Ryzen 7 5800X, $312.99")
    numberForCPU= input("Choose the number that corresponds with the part you want: ")
    while True:
        if numberForCPU== '1':
            break
        elif numberForCPU== '2':
            break
        else:
            numberForCPU= input("Choose the number that corresponds with the part you want: ")
    # addPrice(CPU, int(numberForCPU))
    return numberForCPU

# If the user selects option 2(AMD Ryzen 7 5800X, $312.99) for the CPU, this function will present option 1 which is
# MSI B550-A PRO, $197.46 $312.99 as the compatible motherboard for that CPU and mandate the user to select that
# motherboard. If the user selects option 1(Intel Core i7-11700k, $499.99) for the CPU, this function will present
# option 2 (MSI B550-A PRO, $197.46) as the compatible motherboard for that CPU and mandate the user to select that
# motherboard. Afterwards, this function will return the compatible motherboard that the user has selected.
def selectCompatibleMotherBoard(cpuNumber):
    print("\n", end= "")
    print("Next, let's pick a compatible motherboard.")
    if cpuNumber== '1':
        # totalPrice+= MOTHERBOARD[0][2]
        print("2 : MSI Z490-A Pro, $262.30")
        numberForCompatibleMotherBoard= input("Choose the number that corresponds with the part you want: ")
        while numberForCompatibleMotherBoard!= '2':
            numberForCompatibleMotherBoard= input("Choose the number that corresponds with the part you want: ")
    elif cpuNumber== '2':
        # totalPrice+= MOTHERBOARD[1][2]
        print("1 : MSI B550-A PRO, $197.46")
        numberForCompatibleMotherBoard= input("Choose the number that corresponds with the part you want: ")
        while numberForCompatibleMotherBoard!= '1':
            numberForCompatibleMotherBoard= input("Choose the number that corresponds with the part you want:")
    return numberForCompatibleMotherBoard
# This function will present two options for the RAM and mandate the user to select one of them. Afterwards, this
# function will return the RAM that the user has selected.
def selectRAM():
    print("\n", end= "")
    print("Next, let's pick your RAM.")
    print("1 : 16 GB, $82.99")
    print("2 : 32 GB. $174.99")
    numberForRam= input("Choose the number that corresponds with the part you want: ")
    while True:
        if numberForRam== '1':
            break
        elif numberForRam== '2':
            break
        else:
            numberForRam= input("Choose the number that corresponds with the part you want: ")
    # addPrice(RAM, int(numberForRam))
    return numberForRam
# This function will present a only one option for the PSU and mandate the user to select that PSU. Afterwards, this
# function will return the PSU that the user has selected.
def selectPSU():
    print("\n", end= "")
    # totalPrice= 0
    print("Next, let's pick your PSU.")
    print("1 : Corsair RM750, $164.99")
    numberForPSU= input("Choose the number that corresponds with the part you want: ")
    while True:
        if numberForPSU== '1':
            # totalPrice+= PSU[0][2]
            break
        else:
            numberForPSU= input("Choose the number that corresponds with the part you want: ")
    # addPrice(PSU, int(numberForPSU))
    return numberForPSU
# This function will present two options for the case and mandate the user to select one of them. Afterwards, this
# function will return the case that the user selected.
def selectCase():
    # totalPrice= 0
    print("\n", end= "")
    print("Next, let's pick your case.")
    print("1 : Full Tower (black), $149.99")
    print("2 : Full Tower (red), $149.99")
    numberForCase= input("Choose the number that corresponds with the part you want: ")
    while True:
        if numberForCase== '1':
            # totalPrice+= CASE[0][2]
            break
        elif numberForCase== '2':
            # totalPrice+= CASE[1][2]
            break
        else:
            numberForCase= input("Choose the number that corresponds with the part you want:")
    # addPrice(CASE, int(numberForCase))
    return numberForCase
# This function will present two options for the SSD and mandate the user to select one of them. Afterwards,
# this function will return the SSD that the user has selected.
def selectSSD():
    # totalPrice= 0
    print("\n", end= "")
    print("Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
    print("1 : 250 GB, $69.99")
    print("2 : 500 GB, $93.99")
    print("3 : 4 TB, $219.99")
    numberForSSD= input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
    while True:
        if numberForSSD== '1':
            # totalPrice+= SSD[0][2]
            break
        elif numberForSSD== '2':
            # totalPrice+= SSD[1][2]
            break
        elif numberForSSD== '3':
            # totalPrice+= SSD[2][2]
            break
        elif numberForSSD== 'x' or numberForSSD== 'X':
            break
        else:
            numberForSSD= input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
    # addPrice(SSD, int(numberForSSD))
    return numberForSSD
# This function will present two options for the HDD. If the user selected x or X to decline the SSD, the user will
# be mandated to select one of the options for the HDD. If the user did not select x or X for the SDD, the user will
# have the option of decline to purchase an HDD.
def selectHDD(numberForSDD):
    # totalPrice= 0
    print("\n", end= "")
    print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
    print("1 : 500 GB, $106.33")
    print("2 : 1 TB, $134.33")
    if numberForSDD== 'x' or numberForSDD == 'X':
        numberForHDD= input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")
        while True:
            if numberForHDD== '1':
                break
            elif numberForHDD== '2':
                break
            else:
                numberForHDD= input("Choose the number that corresponds with the part you want(since you did mot get an SSD, you must get an HDD): ")
    else:
        numberForHDD= input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
        while True:
            if numberForHDD== '1':
                break
            elif numberForHDD== '2':
                break
            elif numberForHDD== 'x' or numberForHDD== 'X':
                break
            else:
                numberForHDD= input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
    return numberForHDD
# This functions presents only one option for the graphics card and the user will either have the option to select
# that graphics card or decline it. Afterwards, this function will return the graphics card that the user has selected.
def selectGraphicsCard():
    print("\n", end= "")
    print("Finally, let's pick your graphics card (or X to not get a graphics card).")
    print("1 : MSI GeForce Rix 3060 12GB, $539.99")
    numberForGraphicsCard= input("Choose the number that corresponds with the part you want: ")
    while numberForGraphicsCard!= '1' and numberForGraphicsCard!= 'x' and numberForGraphicsCard!= 'X':
        numberForGraphicsCard= input("Choose the number that corresponds with the part you want: ")
    return numberForGraphicsCard
# This function will calculate and returns the total price of all the custom PC parts.
def calculateTotalPriceForBuildingACustomPC():
    totalPrice= 0
    numberForCPU= selectCPU()
    numberForCompatibleMotherBoard= selectCompatibleMotherBoard(numberForCPU)
    numberForRAM= selectRAM()
    numberForPSU= selectPSU()
    numberForCase= selectCase()
    numberForSSD= selectSSD()
    numberForHDD= selectHDD(numberForSSD)
    numberForGraphicsCard= selectGraphicsCard()
    if numberForCPU== '1':
        totalPrice+= CPU[0][2]
    elif numberForCPU== '2':
        totalPrice+= CPU[1][2]

    if numberForCompatibleMotherBoard== '1':
        totalPrice+= MOTHERBOARD[0][2]
    elif numberForCompatibleMotherBoard== '2':
        totalPrice+= MOTHERBOARD[1][2]
    if numberForRAM== '1':
        totalPrice+= RAM[0][2]
    elif numberForRAM== '2':
        totalPrice+= RAM[1][2]
    if numberForPSU== '1':
        totalPrice+= PSU[0][2]

    if numberForCase== '1':
        totalPrice+= CASE[0][2]
    elif numberForCase== '2':
        totalPrice+= CASE[1][2]

    if numberForSSD== '1':
        totalPrice+= SSD[0][2]
    elif numberForSSD== '2':
        totalPrice+= SSD[1][2]
    elif numberForSSD== '3':
        totalPrice+= SSD[2][2]

    if numberForHDD== '1':
        totalPrice+= HDD[0][2]
    elif numberForHDD=='2':
        totalPrice+= HDD[1][2]

    if numberForGraphicsCard== '1':
        totalPrice+= GRAPHICS_CARD[0][2]
    else:
        totalPrice= totalPrice
    return totalPrice

# This function presents three options for the prebuilt computer and mandates the user select one of them. If the user
# selects option 1, this function will return $3699.99 as the total cost for the prebuilt PC. If the user selects option
# 2, this function will return $2839.99 as the total price for the prebuilt PC. If the user selects option 3, this
# function will return $1099.99 as the total cost for the prebuilt PC.
def calculateTotalPriceForPrebuiltPC():
    totalPrice= 0
    print("\n", end= "")
    print("Which prebuilt would you like to order? ")
    print("1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99")
    print("2 : SkyTech Prism II Gaming PC, $2839.99")
    print("3 : ASUS ROG Strix G10CE Gaming PC, $1099.99")
    numberForPrebuiltPC= input("Choose the number that corresponds with the part you want: ")
    while numberForPrebuiltPC!= '1' and numberForPrebuiltPC!= '2' and numberForPrebuiltPC!='3':
        numberForPrebuiltPC= input("Choose the number that corresponds with the part you want: ")
    if numberForPrebuiltPC== '1':
        totalPrice+= PREBUILTS[0][2]
    elif numberForPrebuiltPC== '2':
        totalPrice+= PREBUILTS[1][2]
    elif numberForPrebuiltPC== '3':
        totalPrice+= PREBUILTS[2][2]
    return totalPrice
# This function keeps asking user for their order until the user enters 3 for the answer variable. If the user enters 1,
# for the answer variable, this function will call the calculateTotalPriceForBuildingACustomPC() to let the user
# purchase custom PC parts. Afterwards, the calculateTotalPriceForBuildingACustomPC() will calculate and return the
# total price of all the custom PC parts that the user has purchased. If the user enters 2 for the answer variable,
# this function will call the calculateTotalPriceForPrebuiltPC() to let the user purchase a prebuilt computer.
# Afterwards, calculateTotalPriceForPrebuiltPC() will calculate and return the total price of a prebuilt PC. If the user
# enters 3 for the answer variable, this function will return the total cost of the PC that the user has purchased in
# a list.
def pickItems():
    # global totalPrice
    listOfTotalPrices= []
    print("Welcome to my PC shop!")
    while True:
        print("\n", end= "")
        answer= input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
        while answer!= '1' and answer!= '2' and answer!= '3':
            print("\n", end= "")
            answer= input("Would you like to build a custom PC(1), purchase a pre-built PC(2) or would you like to checkout(3)? ")
        if answer== '1':
            print("\n", end= "")
            print("Great! Let's start building your PC!\n")
            totalPriceOfAllPC= calculateTotalPriceForBuildingACustomPC()
            print("\n", end= "")
            print("You have selected all of the required parts! Your total for this PC is $%.2f"%totalPriceOfAllPC)
            listOfTotalPrices.append(round(totalPriceOfAllPC, 2))
        elif answer== '2':
            print("\n", end= "")
            print("Great! Let's pick a pre-built PC!")
            totalPriceOfAllPrebuilts= calculateTotalPriceForPrebuiltPC()
            print("\n", end= "")
            print("Your total price for this prebuilt is $%.2f"%totalPriceOfAllPrebuilts)
            listOfTotalPrices.append(round(totalPriceOfAllPrebuilts, 2))
        elif answer== '3':
            return listOfTotalPrices
            break
# This
print(pickItems())



















