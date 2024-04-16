############################

### Check item not install 

## status red or green


############################# COLOR CODE 

G="$(printf '\033[1;32m')"
Y="$(printf '\033[1;33m')"
W="$(printf '\033[1;37m')"
C="$(printf '\033[1;36m')"
R="$(printf '\033[1;31m')"


####################### CODE 


figlet_c() { # check install figlet 
    if ! which figlet > /dev/null; then
    	
    	echo ${R} "[0] ${W}Not install figlet  " 
    	echo 
    	echo " Debian/Ubuntu : sudo apt install figlet -y " 
    	echo " Arch          : sudo pacman -S figlet" 
    	echo " Redhat/Fedora : sudo yum install figlet " 
    	echo
    	read -p "Enter to continue..."
    	
    	
    	#echo " Fedora        : sudo dnf install figlet " 
    	
    else
    	echo ${G} "[+] ${W} installed figlet  " 

fi
}
############################################### END 
lolcat_c() { # check install lolcat
    if ! which lolcat > /dev/null; then
    	
    	echo ${R} "[0] ${W}Not install lolcat  " 
    	echo 
    	echo " Debian/Ubuntu : sudo apt install lolcat -y " 
    	echo " Arch          : sudo pacman -S lolcat" 
    	echo " Redhat        : sudo yum install lolcat " 
    	echo " Fedora        : sudo dnf install lolcat " 
    	echo
    	read -p "Enter to continue..."

    	
    else
    	echo ${G} "[+] ${W} installed lolcat  " 

fi
}
#################################################### END
meta_c() { # check install metasploit-framework
    if ! which msfconsole > /dev/null; then
    	
    	echo ${R} "[0] ${W}Not install metasploit  "
    	echo 
    	echo " Ubuntu        : sudo snap install metasploit-framework " 
    	echo " Debian        : ?  "
    	echo " Arch          : sudo pacman -S metasploit" 
    	echo " Redhat        : ? " 
    	echo " Fedora        : ?" 
    	echo
    	read -p "Enter to continue..."
    	
    else
    	echo ${G} "[+] ${W} installed metasploit  " 
fi
}
############################## END CODE 

##### __MAIN__
clear
figlet_c
lolcat_c
meta_c

### __END_MAIN__

