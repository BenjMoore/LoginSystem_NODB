from cgi import print_environ_usage
from distutils.log import error
import time
import datetime
import sys
import os
import platform

## Banner Var
currentDT = datetime.datetime.now()
cred = 'Benjamin James Moore'
usercount = 0

# Clear Screen Functions
class clear_Screen():
    os_Detected = platform.system()
    if os_Detected == "Linux" or "Darwin":
        os.system("clear")
    if os_Detected == "Windows":
        os.system("cls")
    else:
        print("OS Not Supported\n Some Functionality May Not Be Available!")


class splash:
    def banner_ASCII():
        print("")
        print("\033[1;36;40m         :::        ::::::::   :::::::: ::::::::::: ::::    :::\033")
        print("\033[1;36;40m        :+:       :+:    :+: :+:    :+:    :+:     :+:+:   :+:\033")  
        print("\033[1;36;40m       +:+       +:+    +:+ +:+           +:+     :+:+:+  +:+\033")  
        print("\033[1;36;40m      +#+       +#+    +:+ :#:           +#+     +#+ +:+ +#+\033")    
        print("\033[1;36;40m     +#+       +#+    +#+ +#+   +#+#    +#+     +#+  +#+#+#\033")     
        print("\033[1;36;40m    #+#       #+#    #+# #+#    #+#    #+#     #+#   #+#+#\033")      
        print("\033[1;36;40m   ########## ########   ######## ########### ###    ####\033")       
        print("\033[1;36;40m")               
        print("\033[1;36;40m                       \033")
        print("")


    def Account():     
        welcome = input("_\033[1;36;40mDo you have an acount? \033[1;32;40my\033\033[1;36;40m/\033\033[1;36;40m\033[1;31;40mn\033\033[1;36;40m:\033\033[1;35;40m ")

        if welcome == "y":
            while True:
                login1 = input("\033[1;36;40mLogin:\033\033[1;35;40m")
                login2 = input("\033[1;36;40mPassword:\033\033[1;35;40m")
                try:
                    file = open(login1+".txt", "r")
                    data = file.readline()
                    file.close()
                except FileNotFoundError:
                    file = open("Log.txt" , "a")
                    file.write("[Server] Attempted Login From: ")
                    file.write(login1+"@"+login2)
                    file.write(" {Account Does Not Exist, Or Wrong Password}\n")
                    file.close()
                    clear_Screen()
                    print("\033[1;36;40m[+] Error, Wrong Username/Pass [+]\033")
                    time.sleep(1)
                    print("\033[1;36;40m[+] Restarting [+]\033")
                    time.sleep(1)
                    import src.login as login
                
                
                if data == login1+":"+login2:
                    try:
                        file = open(login1+"online.txt", "r")
                        online = file.readline()
                        if online == 'True':
                            print("Already Logged in..")
                            time.sleep(2)
                            sys.exit()
                        if online == 'False':
                            file.close()
                            file = open(login1+"online.txt", "w")
                            file.write("True")
                            file.close()
                            file = open("Log.txt" , "a")
                            file.write("[Server] Acc Login From ")
                            file.write(login1+"@"+login2)
                            file.write('\n')
                            file.close()
                            clear_Screen()
                            time.sleep(1)
                            print("\033[1;36;40m[+] Login Sucsessful [+]\n[+] Welcome To Lewd [+]\033")
                            time.sleep(2)
                            import main
                        
                
                        
                    except FileNotFoundError:
                        file = open("Log.txt" , "a")
                        file.write("[Server] Attempted Login From: ")
                        file.write(username+"@"+password)
                        file.write(" {Account Does Not Exist, Or Wrong Password}\n")
                        file.close()
                        clear_Screen()
                        print("\033[1;36;40m[+] Error, Wrong Username/Pass [+]\033")
                        time.sleep(1)
                        print("\033[1;36;40m[+] Restarting [+]\033")
                        time.sleep(1)
                        import Login
                        
                    
                    break
                print("\033[1;36;40mIncorrect username or password.\033")

        if welcome == "n":
                
            username  = input("\033[1;36;40m[+] Username:\033\033[1;35;40m")
            password  = input("\033[1;36;40m[+] Password:\033\033[1;35;40m")
            try:
                file = open(username+".txt", "x")
                file.write(username+":"+password)
                file.close()
                file = open(username+"online.txt", "x")
                file.write("False")
                file.close()
                clear_Screen()
                        
            except FileExistsError:
                clear_Screen()
                time.sleep(0.5)
                print("\033[1;36;40m[+] Error - Username Already Exists :/ [+]\033")
                time.sleep(1)
                print("\033[1;36;40m[Restarting]\033")
                time.sleep(1)
                import src.login as login
                        
        print("\033[1;36;40m[+] Acc Added [+]\033\033[1;35;40m")
        key = input("\033[1;36;40mAutho Key:\033\033[1;35;40m ")
        try:
                file = open(key+".txt", "r")
                dataa = file.readline()
                file.close()
                    #error Handler
        except FileNotFoundError:
                file = open("Log.txt" , "a")
                file.write("[Server] Wrong/Fake Autho Key From : ")
                file.write(username+"@"+password)
                file.write(" Using Key:")
                file.write(key)
                file.write("{Key Dosnt Exist}\n")
                file.close()
                clear_Screen()
                os.remove(username+".txt") ## Deletes Account 
                print("\033[1;36;40m[+] Error, Wrong Authentication Key [+]\033\033[1;36;40m\033")
                time.sleep(1)
                print("\033[1;36;40m[+] Restarting [+]\033")
                time.sleep(1)
                import exit_file
                    
        if dataa == key+"@ClamLq":
                clear_Screen()
                print("\033[1;36;40m[+] Account Authorised.. Please Wait [+]")
                time.sleep(1)
                clear_Screen()
                print("\n════════════════════════════                         [+] Acc Details [+]")
                print(" [+] Username:", username)
                print("════════════════════════════ ")
                print(" [+] Password:", password)
                print("════════════════════════════ ")
                print(" [+] AuthCode:", key)
                print("════════════════════════════ ")
                print(" [+] Date:",currentDT.day,"/",currentDT.month,"/",currentDT.year)
                print("════════════════════════════ ")
                print(" [+] Time:",currentDT.hour,":",currentDT.minute)
                print("════════════════════════════ ")
                print("════════════════════════════ ")
                print(" [+] Made By:",cred)
                print("════════════════════════════ ")
                print("\n")
                print("                                                      [+] WARNING [+]\n")
                print("\033[1;36;40m[+] By Typing Y, One Time AuthCode Will be Deleted [+]")
                accept = input("\033[1;36;40m[+] I Accept The Agreement and Accept that We are Not Reliable For Refund Upon forgeting of password [y/n]:\033\033[1;35;40m ")
                                
                if accept == 'y':
                    usercount = usercount + 1
                    file.close()
                    os.remove(key+".txt")
                    clear_Screen()
                    file = open("Log.txt" , "a")
                    file.write("[Server] Acc Creation From ")
                    file.write(username+"@"+password)
                    file.write(" Using Key:")
                    file.write(key)
                    file.write(" {Key Deleted Sucsessfuly}\n")
                    file.close()
                    file = open(username+"online.txt", "w")
                    file.write("True")
                    file.close()
                    file = open("users.txt", "a")
                    file.write(username+"@"+password)
                    file.write("\n")
                    file.close()
                    print("[+] Welcome, Loading.. [+]")
                    time.sleep(2)
                    
                
                    
                        
                if accept == 'n':
                    clear_Screen()
                    print("\033[1;36;40m[+] Please Accept Agereement, {Acc Creation Terminated} [+]\033")
                    os.remove(username+".txt")
                    time.sleep(2)
                    import Login