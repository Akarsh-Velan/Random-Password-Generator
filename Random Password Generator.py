import random
print('---------------------------------------------------------------------------------------------------------------------------------')
print("Random Password Generator")
print()
lg = int(input("Enter the required length of the generated password:  "))
ch1 = input("Do you want to include numbers? (Y/N)")
l=[]
alp='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lgth = len(l)
i=0

def options(l):
    ch2 = input('Do you want to edit/remove this password? (Y/N)')
    if ch2 in ('Y','yes','Yes','YES','y'):
        ch3 = input('Do you want to remove a character? (Y/N)')
        if ch3 in ('Y','yes','Yes','YES','y'):
            ch4 = int(input('Enter character number you want to remove? (Ex. 1,3,7)'))
            del l[ch4-1]
            print()
            print('Generated Password: ',"".join(l))
            print()
            ch5 = input('Do you wanna go back to the previous options?')
            print()
            if ch5 in ('Y', 'yes', 'Yes', 'YES', 'y'):
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
            ch7 = input('Do you wanna go back to the previous options?')
            print()
            if ch7 in ('Y', 'yes', 'Yes', 'YES', 'y'):
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
    options(l)

if ch1 in ('Y','yes','Yes','YES','y'):
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
    ch8 = input('Do you wanna go back to the previous options?')
    print()
    if ch8 in ('Y', 'yes', 'Yes', 'YES', 'y'):
        options(l)
    else:
        print('---------------------------------------------------------------------------------------------------------------------------------')
        print()
        exit()