import random
import time

def void():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def Noob():
    Noob_RN = random.randrange(1, 100)
    Noob_running = True
    while Noob_running == True:
        try:
            inp = int(input("Guess the correct random number from 1 - 100 \n>> "))
            if Noob_RN == inp:
                print("You Win!")
                time.sleep(2)
                void()
                break
            elif inp < Noob_RN:
                print("Too low")
            elif inp > Noob_RN:
                print("Too high")
            elif inp > 100:
                print("Cant be higher than 100")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input")
        except TypeError:
            pass
        except KeyboardInterrupt:
            break


def Starter():
    Starter_RN = random.randrange(1, 500)
    Starter_running = True
    while Starter_running == True:
        try:
            inp = int(input("Guess the correct random number from 1 - 500 \n>> "))
            if Starter_RN == inp:
                print("You Win!")
                time.sleep(2)
                void()
                break
            elif inp < Starter_RN:
                print("Too low")
            elif inp > Starter_RN:
                print("Too high")
            elif inp > 500:
                print("Cant be higher than 500")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input")
        except TypeError:
            pass
        except KeyboardInterrupt:
            break


def Medium():
    Medium_RN = random.randrange(1, 1000)
    Medium_running = True
    while Medium_running == True:
        try:
            inp = int(input("Guess the correct random number from 1 - 1,000 \n>> "))
            if Medium_RN == inp:
                print("You Win!")
                time.sleep(2)
                void()
                break
            elif inp < Medium_RN:
                print("Too low")
            elif inp > Medium_RN:
                print("Too high")
            elif inp > 1000:
                print("Cant be higher than 1,000")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input")
        except TypeError:
            pass
        except KeyboardInterrupt:
            break

def Hard():
    Hard_RN = random.randrange(1, 5000)
    Hard_running = True
    while Hard_running == True:
        try:
            inp = int(input("Guess the correct random number from 1 - 5,000 \n>> "))
            if Hard_RN == inp:
                print("You Win!")
                time.sleep(2)
                void()
                break
            elif inp < Hard_RN:
                print("Too low")
            elif inp > Hard_RN:
                print("Too high")
            elif inp > 5000:
                print("Cant be higher than 5000")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input")
        except TypeError:
            pass
        except KeyboardInterrupt:
            break

def Nightmare():
    NM_RN = random.randrange(1, 10000)
    NM_running = True
    while NM_running == True:
        try:
            inp = int(input("Guess the correct random number from 1 - 10,000 \n>> "))
            if NM_RN == inp:
                print("You Win!")
                time.sleep(2)
                void()
                break
            elif inp < NM_RN:
                print("Too low")
            elif inp > NM_RN:
                print("Too high")
            elif inp > 10000:
                print("Cant be higher than 10,000")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input")
        except TypeError:
            pass
        except KeyboardInterrupt:
            break

def literal_aids():
    LA_RN = random.randrange(1, 1000000) 
    LA_running = True
    while LA_running == True:
        try:
            inp = int(input("Guess the correct random number from 1 - 1,000,000 \n>> "))
            if LA_RN == inp:
                print("You Win!")
                time.sleep(2)
                void()
                break
            elif inp < LA_RN:
                print("Too low")
            elif inp > LA_RN:
                print("Too high")
            elif inp > 1000000:
                print("Cant be higher than 1,000,000")
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a valid input")
        except TypeError:
            pass
        except KeyboardInterrupt:
            break



running = True
while running == True:
    print("1. Noob \n2. Starter \n3. Medium \n4. Hard \n5. Literal aids")
    menuinp = input(">> ")
    if menuinp == "1":
        void()
        Noob()
    elif menuinp == "2":
        void()
        Starter()
    elif menuinp == "3":
        void()
        Medium()
    elif menuinp == "4":
        void()
        Hard()
    elif menuinp == "5":
        void()
        literal_aids()
    else:
        print("Invalid input")
