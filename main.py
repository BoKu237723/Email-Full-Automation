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

ALLOWED_DOMAINS = {
    '@gmail.com',
    '@outlook.com',
    '@hotmail.com',
    '@proton.me',
    '@icloud.com',
    '@yahoo.com'
}

total_mails = []
unique_mails = []
valid_mails = []

def show_options():
    print(Fore.BLUE + "\n[01]  Process emails\n[02]  Remove Duplicate emails\n[03]  Remove Invalid emails\n[04]  Remove both Duplicate and Invalid emails\n[05]  Line up emails to send (chunks.txt)\n[06]  Personalized Email Sender Automation\n[07]  Show Options\n[08]  Help\n[09]  Exit\n")

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
        print(f"[=]   Unique Mails (Final): {len(unique_emails)}")
        print(f"[=]   Duplicate Mails (Removed): {len(total_mails) - len(unique_emails)}\n")
        total_mails = unique_emails

    except Exception as e:
        print(Fore.RED + f"[-]   Error: {e}")

    except KeyboardInterrupt:
        print(Fore.RED + "\n[-]   Keyboard Interrupt Detected. Quitting..." + Style.RESET_ALL)
        sys.exit()

def is_valid_email():
    global valid_mails, total_mails
    for domain in ALLOWED_DOMAINS:
        for mail in total_mails:
            if mail.endswith(domain):
                local_part = mail[:-len(domain)]
                if local_part and '@' not in local_part and ' ' not in local_part:
                    valid_mails.append(mail)

    print(f"[=]   Valid Mails (Final): {len(valid_mails)}")
    print(f"[=]   Invalid Mails (Removed): {len(total_mails) - len(valid_mails)}\n")    

    total_mails = valid_mails

def email_chunking(amount):
    # Let's send 300bcc per mail
    with open('chunks.txt', 'w', encoding='utf-8') as f:
        total_lines = 0
        for i in range(0, len(total_mails), amount):
            chunk = total_mails[i:i+amount]
            # Join with space (for email sending)
            line = ' '.join(chunk)
            f.write(line + '\n')
            total_lines += 1

    print(f"[=]   Amount of Lines: {total_lines}")
    print(f"[=]   The Data is Generated in 'chunks.txt' \n")


def help_function():
    print("Pressed Help Function.")
    pass

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
                is_valid_email()
        
            elif userInput[:2] == "04":
                unique_mails()
                is_valid_email()
        
            elif userInput[:2] == "05":
                try:
                    amount = userInput[2:].split(" ")
                    print(f"Amount: {amount[1]}")
                    email_chunking(int(amount[1]))

                except Exception as e:
                    print(Fore.RED + f"[-]   Error: {e}\n" + Style.RESET_ALL)
                
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