import random
ycho = ('yes', 'ye', 'y', 's')
def savefile(l):
    save = open('svdpswd.txt', 'a+')
    xa = '• '
    save.write(xa);save.write(''.join(l));save.write('\n');save.close()
    return
def main():
    print('-----' * 25); print("Random Password Generator"); print()
    print('1. Generate Random Password');print('2. View Saved Passwords');print('3. Exit');print()
    ch0 = int(input('Enter your choice? (1/2/3) '))
    if ch0 == 1:
        lg = int(input("Enter the required length of the generated password:  "))
        ch1 = input("Include Numbers? (y/n)").lower()
        l = []
        alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        def options(l):
            ch2 = input('Edit or Remove a character in this password? (y/n) ').lower()
            if ch2 in ycho:
                ch3 = input('Do you want to remove a character? (y/n) ').lower();print()
                print('Current Password: ', ''.join(l));print()
                if ch3 in ycho:
                    ch4 = int(input('Enter character number you want to remove? (Ex. 1,3,7) '))
                    del l[ch4 - 1];print()
                    print('Generated Password: ', "".join(l));print()
                    sv = input('Do you want to save your password: (y/n) ')
                    if sv in ycho:
                        savefile(l)
                    print()
                    ch11 = input('Do you want to create a new password (y/n): ').lower()
                    if ch11 in ycho:
                        main()
                    else:
                        print()
                        ch5 = input('Do you wanna go back to the previous options? (y/n) ').lower()
                        print()
                        if ch5 in ycho:
                            options(l)
                        else:
                            print('-----' * 25);main()
                else:
                    ch4 = int(input('Enter character number you want to edit: (Ex. 1,4,5) '))
                    ch6 = input('Enter the character you want to replace the original character with: ')
                    ind = ch4 - 1
                    del l[ind]
                    l.insert(ind, ch6);print()
                    print('Generated Password: ', "".join(l));print()
                    sv = input('Do you want to save your password: (y/n) ')
                    if sv in ycho:
                        savefile(l)
                    print()
                    ch12 = input('Do you want to create a new password: (y/n) ').lower()
                    if ch12 in ycho:
                        main()
                    else:
                        print()
                        ch7 = input('Do you wanna go back to the previous options? (y/n) ').lower()
                        print()
                        if ch7 in ycho:
                            options(l)
                        else:
                            print('-----' * 25);main()
            else:
                print('-----' * 25);main()
        def generate(l):
            print()
            print('Generated Password: ', "".join(l));print()
            c = input('Edit or remove a charcter in the generated password? (y/n) ')
            if c in ycho:
                options(l)
            sv = input('Do you want to save your password: (y/n) ')
            if sv in ycho:
                savefile(l)
            print()
            ch13 = input('Do you want to create a new password: (y/n) ').lower()
            if ch13 in ycho:
                main()
            else:
                print();options(l)
        def start(l):
            l.clear()
            i = 0
            if ch1 in ycho:
                while i != lg:
                    tmp1 = random.choice(alp)
                    tmp2 = str(random.randint(0, 9))
                    l.append(tmp1)
                    l.append(tmp2)
                    if lg == len(l) + 1:
                        tmp3 = str(random.randint(0, 9))
                        l.append(tmp3)
                        generate(l)
                    i = i + 2
                if i == lg:
                    print()
                    print('Generated Password: ', "".join(l));print()
                    d = input('Edit or remove a character in the generated password? (y/n) ')
                    if d in ycho:
                        options(l)
                    sv = input('Do you want to save your password: (y/n) ')
                    if sv in ycho:
                        savefile(l)
                    print()
                    ch14 = input('Do you want to create a new password: (y/n) ').lower()
                    if ch14 in ycho:
                        main()
                    else:
                        print();options(l)
                    ch9 = input('Do you want to create a new password: (y/n) ').lower()
                    if ch9 in ycho:
                        main()
                    else:
                        print();options(l)
            else:
                while i != lg:
                    tmp3 = random.choice(alp)
                    l.append(tmp3)
                    i = i + 1
                print()
                print("Generated Password: ", "".join(l));print()
                sv = input('Do you want to save your password: (y/n) ')
                if sv in ycho:
                    savefile(l)
                print()
                ch10 = input('Do you want to create a new password: (y/n) ').lower()
                if ch10 in ycho:
                    main()
                else:
                    ch8 = input('Do you wanna go back to the previous options? (y/n) ').lower()
                    print()
                    if ch8 in ycho:
                        options(l)
                    else:
                        print('-----' * 25);main()
        start(l)
    elif ch0 == 2:
        with open('svdpswd.txt') as fl:
            data = fl.read()
        print(data)
        t = input('Do you want to clear all saved passwords? (y/n)')
        print()
        if t in ycho:
            f = open('svdpswd.txt', 'a+')
            f.truncate(0);f.close()
            print('All saved passwords cleared.');print()
        s = input('Do you wanna return to the main menu? (y/n)')
        if s in ycho:
            main()
        else:
            exit()
    elif ch0 == 3:
        print('-----' * 25);exit()
    else:
        print('Invalid Choice. Please try again.');main()
main()