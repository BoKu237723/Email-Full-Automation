def convert_to_ready_to_send():
    try:
        with open('cleaned.txt', 'r', encoding='utf8') as f:
            emails = [line.strip() for line in f if line.strip()]

        if not emails:
            print("No emails found in cleaned.txt")
            return

        # Let's send 300bcc per mail
        with open('rdy_to_send.txt', 'w', encoding='utf-8') as f:
            for i in range(0, len(emails), 300):
                # A chunk of up to 300 emails
                chunk = emails[i:i+300]

                # Join with space (for email sending)
                line = ' '.join(chunk)
                f.write(line + '\n')


        # Printing
        total_emails = len(emails)
        total_lines = (total_emails + 299) // 300 # Ceiling devision

        print(f"Conversion complete!")
        print(f"Total emails processed: {total_emails}")
        print(f"Total lines created: {total_lines}")
        print(f"Emails per line: 300 (last line may have fewer)")
        print(f"Output saved to: rdy_to_send.txt")

    except FileNotFoundError:
        print("Error: cleaned.txt not found in current directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_to_ready_to_send()