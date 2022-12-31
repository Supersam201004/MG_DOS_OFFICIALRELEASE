#MG_DOSV0.1.0ALPHA
import time
import random as RANDOM
from datetime import datetime
import os
import platform
import socket
import winsound
#SRMODE MEANS SERVER REMOTE MODE, NOT SERVICE/REPAIR MODE!!!
textfile1_path = 'textfile1.txt'

dateandtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

textfile1nameread = open('sqlitefiles\\textfile1name.txt', 'r')
textfile1read = open('sqlitefiles\\textfile1.txt', 'r')

textfile1 = open('sqlitefiles\\textfile1.txt', 'w')
textfile1name = open('sqlitefiles\\textfile1name.txt', 'w')

ageretrieve = open('sqlitefiles\\user_age.txt', 'r')
nameretrieve = open('sqlitefiles\\user_name.txt', 'r')
lastnameretrieve = open('sqlitefiles\\user_last_name.txt', 'r')

ageset = open('sqlitefiles\\user_age.txt', 'w')
nameset = open('sqlitefiles\\user_name.txt', 'w')
lastnameset = open('sqlitefiles\\user_last_name.txt', 'w')

gamename = 'MG_OS'
gamever = 'V1.3'

normfreq = 1000
normdur = 500
errorfreq = 400
errordur = 300
warnfreq1 = 700
warndur = 300
warnfreq2 = 800

def errorbeep():
    winsound.Beep(errorfreq,errordur)
    winsound.Beep(errorfreq,errordur)
def normbeep():
    winsound.Beep(normfreq,normdur)
def warnbeep():
    winsound.Beep(warnfreq1,warndur)
    winsound.Beep(warnfreq2,warndur)
def shutdown():
    print('Are You Sure You Would Like To Shutdown? Y/N')
    warnbeep()
    shutdownconfirm = input('')
    
    if shutdownconfirm == 'y':
        print('Shutting Down...')
        time.sleep(3)
        quit()

    if shutdownconfirm == 'n':
        print('OK.')
        bootupmenu()
    else:
        print('Command Not Recognised.')
        errorbeep()
        shutdown()
        





def logoff():
    warnbeep()
    print('Are You Sure You Would Like To Logoff? Y/N')
    logoffconfirm = input('')
    if logoffconfirm == 'y':
        print('Logging Off...')
        time.sleep(1)
        bootupmenu()
    if logoffconfirm == 'n':
        print('OK.')
        mainmenu
    else:
        print('Command Not Recognised.')
        errorbeep()
        logoff()


def srmode():
    print('Welcome to Server Remote Mode! Finding A Server...')
    time.sleep(2)
    print('Unfortunatly, This Is A W.I.P, So This Is Not Finished Yet. Sorry!')
    time.sleep(1)
    logon()


def servrepairmenu():
    print('===============================SERVICE/REPAIRMENU===============================')
    print("There's Not Much Going On Here, Sorry!")
    time.sleep(2)
    bootupmenu()


def servrepairmode():
    print('STARTING IN SERVICE/REPAIR MODE...')
    time.sleep(2)
    print('Computer Information:')
    print('Bits:', platform.machine())
    print('Platform:', platform.platform())
    print('System:', platform.system())
    print('Processor:', platform.processor())
    print('Name:', platform.node())
    print('OS Information:')
    print('Name:', gamename)
    print('Version:', gamever)
    normbeep()
    time.sleep(2)
    servrepairmenu()
    






def textfile1write():
    textfile1contentwrite = input('Write Your Text, Then Press Enter.')
    textfile1.write(textfile1contentwrite)
    print('Completed. Exiting To Main Menu...')
    normbeep()
    time.sleep(1)
    mainmenu()



def txtedit():
    print('Starting Text Editor.exe...')
    time.sleep(4)
    print('===============================TXTEDIT.EXE===============================')
    time.sleep(1)
    print('Retrieving Text Files...')
    time.sleep(1)
    print('Text Files Retrieved. Listing:')
    wrtxtfile1 = input('Would You Like To Read The File, Write It, Or Delete It? ')
    if wrtxtfile1 == 'read':
        print(textfile1read.read())
        normbeep()
        mainmenu()
    if wrtxtfile1 == 'write':
        normbeep()
        text1write = input('Write Your Text Then Press Enter. ')
        textfile1.write(text1write)
        textfile1.close()
        mainmenu()
    if wrtxtfile1 == 'delete':
        warnbeep()
        confirmtext1delete = input('Are You Sure? Y/N ')
        if confirmtext1delete == 'y':
            textfile1.write('')
            print('Deleted.')
            mainmenu()
        if conriemtext1delete == 'n':
            print('OK.')
            mainmenu()
        else:
            print('Command Not Recognised.')
            txtedit()
            errorbeep()
    else:
        print('Command Not Recognised.')
        txtedit()
        errorbeep()
        
    


def resetall():
    ageset.write('')
    ageset.close()
    nameset.write('')
    nameset.close()
    lastnameset.write('')
    lastnameset.close()
    print('Reset Completed. Rebooting...')
    normbeep()
    time.sleep(3)
    bootup()



def resetprofile():
    ageset.write('')
    ageset.close()
    nameset.write('')
    nameset.close()
    lastnameset.write('')
    lastnameset.close()
    print('Profile Reset.')
    normbeep()
    mainmenu()



    
def reset():
    warnbeep()
    resetcode = input('ENTER MASTER RESET CODE: ')
    if resetcode == '105679':
        resetmenu()
    else:
        print('Invalid Code.')
        errorbeep()
        mainmenu()


def resetmenu():
    normbeep()
    print('What Would You Like To Reset?')
    print('1. Reset Profile')
    print('2. Master Reset')
    print('3. Cancel')
    resetchoose = input('Enter Number: ')
    if resetchoose == '1':
        print('This Will Reset Your Profile And Your Preferences. Are You Sure?')
        warnbeep()
        resetchooseconfirm1 = input('Y/N: ')
        if resetchooseconfirm1 == 'y':
            resetprofile()
        if resetchooseconfirm1 == 'n':
            resetmenu()
        else:
            print('Command Not Recognised.')
            errorbeep()
            resetmenu()
    if resetchoose == '2':
        print('This Will Reset Everything, Including Your Profile, Preferences And Will Reset All System Information. Are You Sure?')
        warnbeep()
        resetchooseconfirm2 = input('Y/N: ')
        if resetchooseconfirm2 == 'y':
            resetall()
        if resetchooseconfirm2 == 'n':
            reset()
        else:
            print('Command Not Recognised.')
            errorbeep()
            reset()
    if resetchoose == '3':
        print('Cancelled. Returning To Main Menu...')
        errorbeep()
        time.sleep(1)
        mainmenu()
def change_details_or_menu():
    print('Would You Like To Setup Again(Change Details)(1), Or Quit To Main Menu?(2)')
    warnbeep()
    setup_finish_2 = input('')
    if setup_finish_2 == '1':
        iris_setupprofile()
    if setup_finish_2 == '2':
        mainmenu()
    else:
        print('Command Not Recognised.')
        errorbeep()
        change_details_or_menu()

def iris_setupprofile():
    setusername = input('Your First Name: ')
    nameset.write(setusername)
    nameset.close()
    setlastname = input('Your Last Name: ')
    lastnameset.write(setlastname)
    lastnameset.close()
    setage = input('Your Age: ')
    ageset.write(setage)
    ageset.close()
    print('OK! I Will Call You:', nameretrieve.read(), lastnameretrieve.read(), 'And Your Age Is:', ageretrieve.read(), '. You Can Change This Later. Continue To I.R.I.S?')
    warnbeep()
    setup_finish = input('Y/N ')
    if setup_finish == 'Y' or 'y':
        print('OK, Continuing To I.R.I.S...')
        iris()
    if setup_finish == 'N' or 'n':
        change_details_or_menu()
def iris():
        iris_command = input('I.R.I.S>>>')
        if iris_command == 'setup profile':
            normbeep()
            iris_setupprofile()
        if iris_command == 'who am i':
            normbeep()
            print('You Are:', nameretrieve.read(), lastnameretrieve.read(), 'And Your Age Is:', ageretrieve.read(), '!')
            iris()
        if iris_command == 'help':
            print('List Of Commands:')
            print('who am i: Shows Your Profile')
            print('setup profile: Setup Your Profile(Name, Age, Last Name)')
            print('help: Shows This Menu')
            print('time: Shows Date And Time.')
            print('quit: Quits To The Main Menu.')
            normbeep()
            iris()
        if iris_command == 'time':
            print('The Current Time Is:', dateandtime, '.')
            normbeep()
        if iris_command == 'quit':
            normbeep()
            mainmenu()
        else:
            print('Command Not Recognised.')
            errorbeep()
            iris()
        

def iris_start():
    print('Starting I.R.I.S...')
    time.sleep(2)
    print('Retrieving User Information...')
    time.sleep(2)
    print('Welcome To I.R.I.S!')
    print("===============================I.R.I.S===============================")
    print('Type help For A List Of Commands.')
    normbeep()
    iris()

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
        elif gotomenuchoose == ' ':
            print('Command not recognised.')
            flipacoin()
        else:
            print('Command not recognised.')
            flipacoin()
    elif flip == ' ':
        print('Command not recognised.')
        flipacoin()
    else:
        print('Command not recognised.')
        flipacoin()
              


def file_flipacoin():
    normbeep()
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
    print('MG Robotics 2022, all rights reserved.')
    print('Type "help" for a list of commands.')
    bootupmenuchoose = input('MG_DOS>>>')
    if bootupmenuchoose == 'help':
        help()
    if bootupmenuchoose == 'logon':
        warnbeep()
        logon()
    if bootupmenuchoose == 'shutdown':
        shutdown()
    else:
        print('Command not recognised.')
        errorbeep()
        bootupmenu()
        

def bootup():
    time.sleep(2)
    print('Local Bootup Initiated.')
    time.sleep(3)
    print('All systems online.')
    time.sleep(1)
    print('Bootup In: 1. Normal or 2. Service/Repair?')
    bootupmodechoose = input('>>> ')
    if bootupmodechoose == '1':
        time.sleep(1)
        bootupmenu()
    if bootupmodechoose == '2':
        servrepairmode()
    else:
        print('COMMAND NOT RECOGNIZED')
        errorbeep()
        bootup()
    



def file_readme():
    normbeep()
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
    normbeep()
    filechoose = input('Please choose the file with the number, or type "menu" to go to the main menu.')
    if filechoose == '1':
        file_readme()
    if filechoose == '2':
        file_flipacoin()
    
    
def mainmenu():
    print('===============================MAIN_MENU===============================')
    print('Type Help For A List Of Commands.')
    menuchoose = input('admin>>>')
    if menuchoose == 'help':
        mainhelp()
    if menuchoose == 'list dir':
        listdir()
    if menuchoose == 'iris':
        iris_start()
    if menuchoose == 'time':
        print('The Current Time Is:', dateandtime, '.')
        normbeep()
        mainmenu()
    if menuchoose == 'reset':
        reset()
    if menuchoose == 'txtedit':
        txtedit()
    if menuchoose == 'logoff':
        logoff()
    else:
        print('Command not recognised.')
        errorbeep()
        mainmenu()

def logoncomplete():
    print('Welcome, "admin"!')
    normbeep()
    mainmenu()
def help():
    normbeep()
    print('===============================HELP===============================')
    print('help: Displays this menu.')
    print('logon: Initiates log on protocol.')
    print('shutdown: Shuts down the computer.')
    bootupmenu()
def mainhelp():
    normbeep()
    print('===============================HELP===============================')
    print('help: Displays this menu.')
    print('list dir: Lists all files in current folder.')
    print('time: Shows time')
    print('reset: !Reset System!')
    print('iris: Starts the I.R.I.S Interface.')
    print('txtedit: Starts The Text Editor.')
    print('logoff: Logs Off.')
    mainmenu()

def logon():
    print('Initiating logon protocol...')
    time.sleep(1)
    print('Loading Successful!')
    normbeep()
    time.sleep(0.5)
    userlogon = input('User: ')
    if userlogon == 'admin':
        passlogon = input('Password: ')
        if passlogon == 'minecraft':
            logoncomplete()
        else:
            print('Wrong password')
            errorbeep()
            logon()
    if userlogon == 'mgserverremote':
        passserverlogon = input('Warning: You Are About To Activate The MG SERVER REMOTE CONNECTION. Continue? Y/N ')
        warnbeep()
        if passserverlogon == 'y':
            psl2 = input('Password:')
            if psl2 == 'pizza':
                normbeep()
                srmode()
            else:
                print('Incorrect Password.')
                errorbeep()
                logon()                    
        if passserverlogon == 'n':
            print('OK.')
            logon()
        else:
            print('Command Not Recognised.')
            errorbeep()
            logon()
    else:
        print('User not recognised')
        errorbeep()
        logon()


#MAIN


bootup()
