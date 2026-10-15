from colorama import Fore, Back, Style, init
import time
import sys

print ("""
[0;34m▄▄▄[0;34;47m▀▀▀[0;34m█[0;37m                [0;34m▄▄▄[0;34;47m▀▀▀[0;34m█[0;37m    [0;34m▄▄▄[0;34;47m▀▀▀[0;34m█[0;37m                 [0m
[0;37m [0;34m█[0;34;47m   [0;34m█[0;37m                  [0;34m█[0;34;47m   [0;34m█[0;37m      [0;34m█[0;34;47m   [0;34m█[0;37m                  [0m
[0;37m [0;34m█[0;34;47m ░ [0;34m█[0;37m    [0;34m▄[0;34;47m▀▀[0;37;44m█▀▀█[0;34;47m▀[0;37;44m▄[0;34m▄[0;37m    [0;34m█[0;34;47m ░ [0;34m█▄[0;37;44m▄[0;34m▄[0;37m   [0;34m█[0;34;47m ░ [0;34m█▄[0;37;44m▄[0;34m▄[0;37m    [0;30;44m▀[0;37;44m▄▄▄▄▄▄▄[0;30;44m▀[0;37m  [0m
[0;37m [0;34m█[0;34;47m░▒░[0;34m█[0;37m   [0;34m█[0;34;47m ░[0;37;44m▒[0;34m█[0;37m  [0;37;44m▒█▓█[0;35;44m░[0;37m   [0;34m█[0;34;47m░▒░[0;37;44m▀▓█▀[0;34m▀[0;37m  [0;34m█[0;34;47m░▒░[0;37;44m▀▓█▀[0;34m▀[0;37m  [0;34m█[0;37;44m█▓█[0;34m█▀█[0;37;44m█▓█[0;34m█[0;37m [0m
[0;37m [0;34m█[0;34;47m▒▓▒[0;34m█[0;37m  [0;34m█[0;34;47m▒░▒[0;37;44m░[0;37m   [0;37;44m░▓▀▀[0;34m▀[0;37m   [0;34m█[0;34;47m▒▓▒[0;34m██[0;37;44m░[0;34m█[0;37m   [0;34m█[0;34;47m▒▓▒[0;34m██[0;37;44m░[0;34m█[0;37m  [0;34m█[0;37;44m▓▒▓ [0;37m   [0;37;44m ▓▒▓[0;34m█[0m
[0;37m [0;34m█[0;34;47m▓█▓[0;35;44m░[0;37m  [0;34m█[0;34;47m▒▓▒[0;34m█▀■▀▀▀[0;37m      [0;34m█[0;34;47m▓█▓[0;35;44m░[0;34m▒▀[0;37m    [0;34m█[0;34;47m▓█▓[0;35;44m░[0;34m▒▀[0;37m   [0;34m█[0;37;44m▒░▒[0;34m▓[0;37m   [0;34m▓[0;37;44m▒░▒[0;34m█[0m
[0;37m [0;34m█[0;34;44m [0;94;44m░ [0;35;44m▒[0;37m  [0;34m█[0;34;47m▓█▓[0;35;44m░[0;37m    [0;34m▄▄■▄[0;37m   [0;34m█[0;34;44m [0;94;44m░ [0;35;44m▒[0;34m░[0;37m     [0;34m█[0;34;44m [0;94;44m░ [0;35;44m▒[0;34m░[0;37m    [0;34m█[0;37;44m░ ░[0;34m▓[0;37m   [0;34m▓[0;37;44m░ ░[0;34m█[0m
[0;37m [0;34m█[0;94;44m░▒░[0;35;44m▓[0;37m   [0;34m█[0;34;44m [0;94;44m░[0;35;44m▒[0;34m▄[0;37m [0;34m▄[0;94;44m▒░░▒[0;35;44m▓[0;35m▌[0;37m  [0;34m█[0;94;44m░▒░[0;35;44m▓[0;34m▓[0;35;44m▄■▄[0;37m  [0;34m█[0;94;44m░▒░[0;35;44m▓[0;34m▓[0;35;44m▄■▄[0;37m  [0;34m█[0;34;44m [0;94;44m░▒ [0;34m▄[0;94;44m ▒░[0;34;44m [0;34m█[0;37m [0m
[0;37m [0;34m█[0;34;45m▀▀▀ [0;37m     [0;35m▀[0;35;44m▄▄▄▄[0;35m▀▀▀▀[0;37m    [0;35;44m■[0;34;45m▀▀▀[0;35;44m▄▀[0;34m▀▀▀[0;37m  [0;35;44m■[0;34;45m▀▀▀[0;35;44m▄▀[0;34m▀▀▀[0;37m   [0;35m▀[0;35;44m▄▄▄[0;35m■[0;35;44m▄▄▄[0;35m▀[0;37m  [0m           Developed by BoKu~
[0;34m▀▀[0;37m                     [0;34m▀▀[0;37m         [0;34m▀▀[0;37m                      [0m
""")

total_mails = []
unique_mails = []

def show_options():
    print(Fore.BLUE + "[01]  Process emails\n[02]  Remove Duplicate emails\n[03]  Remove Invalid emails\n[04]  Remove both Duplicate and Invalid emails\n[05]  Line up emails to send\n[06]  Personalized Email Sender Automation\n[07]  Show Options\n[08]  Help\n[09]  Exit\n")

# Example: 01 emails.txt emails2.txt emails3.txt
def help_function():
    print("Pressed Help Function.")
    pass

def process_mails(email_files):
    for i in email_files:
        with open(i, "r", encoding="utf-8") as file:
            for line in file:
                total_mails.append(line.strip().lower())
    print(Fore.GREEN + f"[=]   Processed Mails (uncleaned): {len(total_mails)}\n" + Style.RESET_ALL)

def unique_mails():
    
    try:
        global total_mails
        unique_emails = list(dict.fromkeys(total_mails))
        print(f"[=]   Unique Mails (removed duplicates): {len(unique_emails)}")
        print(f"[=]   Removed Mails (duplicates): {len(total_mails) - len(unique_emails)}\n")
        total_mails = unique_emails

    except Exception as e:
        print(Fore.RED + f"[-]   Error: {e}")

    except KeyboardInterrupt:
        print(Fore.RED + "\n[-]   Keyboard Interrupt Detected. Quitting..." + Style.RESET_ALL)
        sys.exit()

def main():
    show_options()
    while True:
        try:
            userInput = input(Fore.GREEN + "[+]   Your Input: ")
            if userInput[:2] == "01":
                try:
                    email_files = userInput[3:].split(", ")
                    process_mails(email_files)
                except Exception as e:
                    print(Fore.RED + f"[-]   Error: {e}\n" + Style.RESET_ALL)
        
            elif userInput[:2] == "02":
                unique_mails()
        
            elif userInput[:2] == "03":
                print("03 pressed")
                break
        
            elif userInput[:2] == "04":
                print("04 pressed")
                break
        
            elif userInput[:2] == "05":
                print("05 pressed")
                break
        
            elif userInput[:2] == "06":
                print("06 pressed")
                break
        
            elif userInput[:2] == "07":
                show_options()
                continue
    
            elif userInput[:2] == "08":
                help_function()
                continue
        
            elif userInput[:2] == "09":
                print("[=]   Existing..." + Style.RESET_ALL)
                break
        
            else:
                print("Invalid Input. Enter [06] to see options.\n")
                continue
    
        except KeyboardInterrupt:
            print(Fore.RED + "\n[-]   Keyboard Interrupt Detected. Quitting..." + Style.RESET_ALL)
            break

if __name__ == "__main__":
    main()