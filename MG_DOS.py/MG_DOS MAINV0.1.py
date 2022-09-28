#MG_DOSV0.0.2ALPHA
import time
import random as RANDOM

def flipacoin():
    flipresult = RANDOM.choice(['Heads','Tails'])
    print('Type "flip" to flip a coin!')
    flip = input('')
    if flip == 'flip':
        print("It's:", flipresult,'!')
        print('Try again or go to the menu? 1. Again! 2. Menu')
        gotomenuchoose = input('')
        if gotomenuchoose == '1':
                  flipacoin()
        if gotomenuchoose == '2':
                  mainmenu()
              


def file_flipacoin():
    print('Starting "flipacoin.exe"...')
    time.sleep(1)
    print('3%')
    time.sleep(0.3)
    print('6%')
    time.sleep(0.5)
    print('34%')
    time.sleep(0.1)
    print('45%')
    time.sleep(0.6)
    print('67%')
    time.sleep(0.25)
    print('85%')
    time.sleep(0.78)
    print('98%')
    time.sleep(0.3)
    print('100%')
    time.sleep(1)
    print('Loading Complete!')
    time.sleep(0.5)
    print('Starting...')
    time.sleep(1)
    print('===============================FLIPACOIN.EXE===============================')
    flipacoin()


    
def bootupmenu():
    bootupmenu = input('MG_DOS>>>')
    if bootupmenu == 'help':
        help()
    if bootupmenu == 'logon':
        logon()
    
    elif bootupmenu == '':
        print('Command not recognised.')
        bootupmenu()
    else:
        print('Command not recognised.')
        bootupmenu()
        

def bootup():
    time.sleep(2)
    print('Local Bootup Initiated.')
    time.sleep(3)
    print('All systems online.')
    time.sleep(1)
    print('MG Robotics 2021, all rights reserved.')
    print('Type "help" for a list of commands.')
    bootupmenu()



def file_readme():
    print('Dear User,')
    print('Hello and welcome to your new computer! This Operating System will guide you')
    print('from typing commands to using comlicated applications. We hope you will enjoy')
    print('your new PC and Operating System, and we wish you the best of luck!')
    print('Sincerely,')
    print('Mike Redstone(CEO and Founder of MG Robotics)')
    print('=============================================================================')
    mainmenu()


def listdir():
    print('Finding Directory Contents...')
    time.sleep(1)
    print('3%')
    time.sleep(0.3)
    print('6%')
    time.sleep(0.5)
    print('34%')
    time.sleep(0.1)
    print('45%')
    time.sleep(0.6)
    print('67%')
    time.sleep(0.25)
    print('85%')
    time.sleep(0.78)
    print('98%')
    time.sleep(0.3)
    print('100%')
    time.sleep(1)
    print('Loading Complete!')
    time.sleep(0.5)
    print('Listing Directory...')
    time.sleep(1)
    print('===============================DIRECTORY===============================')
    print('C:')
    print('1. readme.txt')
    print('2. flipacoin.exe')
    filechoose = input('Please choose the file with the number, or type "menu" to go to the main menu.')
    if filechoose == '1':
        file_readme()
    if filechoose -- '2':
        file_flipacoin()
    
    
def mainmenu():
    print('===============================MAIN_MENU===============================')
    menuchoose = input('admin>>>')
    if menuchoose == 'help':
        mainhelp()
    if menuchoose == 'list dir':
        listdir()
    else:
        print('Command not recognised.')
        mainmenu()

def logoncomplete():
    print('Welcome, "admin"!')
    mainmenu()
def help():
    print('===============================HELP===============================')
    print('help: Displays this menu.')
    print('logon: Initiates log on protocol.')
    bootupmenu()
def mainhelp():
    print('===============================HELP===============================')
    print('help: Displays this menu.')
    print('list dir: lists all files in current folder.')
    mainmenu()

def logon():
    print('Initiating logon protocol...')
    time.sleep(1)
    print('Loading Successful!')
    time.sleep(0.5)
    userlogon = input('User: ')
    if userlogon == 'admin':
        passlogon = input('Password: ')
        if passlogon == 'minecraft':
            logoncomplete()
        else:
            print('Wrong password')
            logon()
    else:
        print('User not recognised')
        logon()


#MAIN


bootup()
