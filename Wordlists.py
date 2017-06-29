#!/usr/bin/python3
# simple function to add words to the include or exclude lists
#

import sys
import enchant

# Homedir = input("What is the working directory? ")
Homedir = '/Users/lmenzies/Documents/1Docs2017/SU17/LoC/LoC4Robots/wordlists/'
print("What is the name of the inclusion list? ")
wordlist = Homedir+input("     %s" % Homedir)
print("What is the name of the exclusion list? ")
exceptlist = Homedir+input("     %s" % Homedir)
standict = enchant.Dict("en_US")
d = enchant.DictWithPWL("en_US", pwl=wordlist, pel=exceptlist)
choice = " "
while True:
    print("\n" * 50)
    print("Please enter one of the choices below: ")
    print("    s  : check the spelling of a word against the \'en_US\' dictionary")
    print("   su  : show suggestions for a word")
    print("    i  : add a word to the inclusion list (i.e. words to be considered \'correctly\' spelled")
    print("    e  : add a word to the exclusion list (i.e. words to be considered \'incorrectly\' spelled")
    print("   ci  : check whether a word is on the inclusion list")
    print("   ce  : check whether a word is on the exclusion list")
    print("   vi  : view the inclusion list")
    print("   ve  : view the exclusion list")
    print("    q  : quit")
    choice = input("What would you like to do? ").lower()
    if choice == 's':
        word = input("What is the word to check? ")
        ans = standict.check(word)
        if ans == True:
            print("True")
        elif ans == False:
            print("False")
        else:
            print("error")
        pause = input("Enter to continue.")
    elif choice == 'su':
        word = input("What is the word? ")
        ans = standict.suggest(word)
        print(ans)
        pause = input("Enter to continue.")
    elif choice == 'i':
        word = input("What is the word (do not include spaces or extranneous marks)? ")
        d.add_to_pwl(word)
        pause = input("Added (%s) to inclusion list. \nEnter to continue." % word)
    elif choice == 'e':
        word = input("What is the word (do not include spaces or extranneous marks)? ")
        d.remove(word)
        pause = input("Added (%s) to exclusion list. \nEnter to continue." % word)
    elif choice == 'ci':
        word = input("What word would you like to check? ")
        yesno = d.is_added(word)
        if yesno == True:
            print("Yes, (%s) is on the inclusion list." %word)
        if yesno == False:
            print("No, (%s) is not on the inclusion list." %word)
        print("\n")
        pause = input("Enter to continue." )
    elif choice == 'ce':
        word = input("What word would you like to check? ")
        yesno = d.is_removed(word)
        if yesno == True:
            print("Yes, (%s) is on the exclusion list." %word)
        if yesno == False:
            print("No, (%s) is not on the exclusion list." %word)
        print("\n")
        pause = input("Enter to continue." )
    elif choice == 'vi':
        with open(wordlist, 'r') as infile:
            print(infile.read())
        pause = input("Enter to continue." )
    elif choice == 've':
        with open(exceptlist, 'r') as infile:
            print(infile.read())
        pause = input("Enter to continue." )
    elif choice == 'q':
        print("Quitting ...")
        print("\n")
        break
    else:
        print("\n")
sys.exit
