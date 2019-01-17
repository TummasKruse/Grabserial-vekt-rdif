import thread

program_running = True

def readVekt():
    print("")
    exec(open("grabVekt.py").read(), globals())
    print("")

def readRFID():
    print("")
    exec(open("grabRFID.py").read(), globals())
    print("")


while(program_running):
 
    menuchoice = input('choose 1, 2, 3 : ')

    if(menuchoice==1):
        exec(open("grabvekt.py").read(), globals())
        break
    elif(menuchoice==2):
        exec(open("grabrfid.py").read(), globals())
        break
    elif(menuchoice==3):
        program_running = False