c1r1 = ' '
c1r2 = ' '
c1r3 = ' '
c2r1 = ' '
c2r2 = ' '
c2r3 = ' '
c3r1 = ' '
c3r2 = ' '
c3r3 = ' '


def displayboard(c1r1,c1r2,c1r3,c2r1,c2r2,c2r3,c3r1,c3r2,c3r3):
    print("|",c1r1,"|",c2r1,"|",c3r1,"|")
    print("-------------")
    print("|",c1r2,"|",c2r2,"|",c3r2,"|")
    print("-------------")
    print("|",c1r3,"|",c2r3,"|",c3r3,"|")

def userinput():
    while True:
        try:
            position = int(input("Please input which position you would like to play (1-9): "))
            if position<1 or position>9:
                print("Please input a valid number within the playing range.")
            if 1<=position<=9:
                return position
        except:
            print("Please input a number.")
            
def changeboard(position):
    if position == 1:
        globals()['c1r1'] = "x"
    if position == 4:
        globals()['c1r2'] = "x"
    if position == 2:
        globals()['c2r1'] = "x"
    if position == 3:
        globals()['c3r1'] = "x"
    if position == 5:
        globals()['c2r2'] = "x"
    if position == 6:
        globals()['c3r2'] = "x"
    if position == 7:
        globals()['c1r3'] = "x"
    if position == 8:
        globals()['c2r3'] = "x"
    if position == 9:
        globals()['c3r3'] = "x"
    
def checkwin():
    pass

def main():
    
    board = [' ']*9
    
    while True:
        
        displayboard(c1r1,c1r2,c1r3,c2r1,c2r2,c2r3,c3r1,c3r2,c3r3)
        position = userinput()
        changeboard(position)
    
main()