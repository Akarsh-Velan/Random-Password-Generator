import random
print('---------------------------------------------------------------------------------------------------------------------------------')
print("Random Password Generator")
print()
lg = int(input("Enter the required length of the generated password:  "))
ch1 = input("Do you want to include numbers? (y/n)")
l=[]
alp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lgth = len(l)

choices_y = ('YES','YE','Y','yes','ye','y','Yes')
def options(l):
    ch2 = input('Do you want to edit or remove a character in this password? (y/n)')
    if ch2 in choices_y:
        ch3 = input('Do you want to remove a character? (y/n)')
        print()
        print('Current Password: ',''.join(l))
        print()
        if ch3 in choices_y:
            ch4 = int(input('Enter character number you want to remove? (Ex. 1,3,7)'))
            del l[ch4-1]
            print()
            print('Generated Password: ',"".join(l))
            print()
            ch11 = input('Do you want to create a different password (y/n): ')
            if ch11 in choices_y:
                start(l)
            else:
                print()

                ch5 = input('Do you wanna go back to the previous options? (y/n)')
                print()
                if ch5 in choices_y:
                    options(l)
                else:
                    print('---------------------------------------------------------------------------------------------------------------------------------')
                    exit()
        else:
            ch4 = int(input('Enter character number you want to edit: (Ex. 1,4,5)'))
            ch6 = input('Enter the character you want to replace the original character with: ')
            ind = ch4 - 1
            del l[ind]
            l.insert(ind,ch6)
            print()
            print('Generated Password: ',"".join(l))
            print()
            ch12 = input('Do you want to create a different password: (y/n) ')
            if ch12 in choices_y:
                start(l)
            else:
                print()
                ch7 = input('Do you wanna go back to the previous options? (y/n)')
                print()
                if ch7 in choices_y:
                    options(l)
                else:
                    print('---------------------------------------------------------------------------------------------------------------------------------')
                    exit()
    else:
        print('---------------------------------------------------------------------------------------------------------------------------------')
        exit()

def generate(l):
    print()
    print('Generated Password: ',"".join(l))
    print()
    ch13 = input('Do you want to create a different password: (y/n)')
    if ch13 in choices_y:
        start(l)
    else:
        print()
        options(l)

def start(l):
    l.clear()
    i = 0
    if ch1 in choices_y:
        while i != lg:
            tmp1 = random.choice(alp)
            tmp2 = str(random.randint(0,9))
            l.append(tmp1)
            l.append(tmp2)
            if lg == len(l)+1:
                tmp3=str(random.randint(0,9))
                l.append(tmp3)
                generate(l)
            i=i+2
        if i == lg:
            print()
            print('Generated Password: ',"".join(l))
            ch9 = input('Do you want to create a different password: (y/n)')
            if ch9 in choices_y:
                start(l)
            else:
                print()
                options(l)

    else:
        while i != lg:
            tmp3 = random.choice(alp)
            l.append(tmp3)
            i=i+1
        print()
        print("Generated Password: ","".join(l))
        print()
        ch10 = input('Do you want to create a different password: (y/n)')
        if ch10 in choices_y:
            start(l)
        else:
            ch8 = input('Do you wanna go back to the previous options? (y/n)')
            print()
            if ch8 in choices_y:
                options(l)
            else:
                print('---------------------------------------------------------------------------------------------------------------------------------')
                exit()

start(l)