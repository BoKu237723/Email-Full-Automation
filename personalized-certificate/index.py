import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

from dotenv import load_dotenv, dotenv_values
load_dotenv()

def send_certificate_emails():
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    YOUR_EMAIL = os.getenv("MYEMAIL")  # fill your email here
    YOUR_PASSWORD = os.getenv("MYPASSWORD")  # fill your app password here
    
    EMAIL_SUBJECT = "Your Certificate is Here!"
    EMAIL_BODY = r"""Dear Participant,

I hope this message finds you well.
Please find attached your certificate, which recognizes your "achievement, e.g., successful completion of the recent training program" with our organization. 
We hope you will proudly display this certificate as a testament to your hard work and dedication. Congratulations on your accomplishment!
Best regards,
"RiseUp"
"Testing"
"Your Organization Name etc etc"
"Your Contact Information"
"""
    
    # Paths
    CERTIFICATES_FOLDER = "certificates"
    EMAILS_JSON = "emails.json"
    
    try:
        with open(EMAILS_JSON, 'r') as f:
            email_data = json.load(f)
    except FileNotFoundError:
        print(f"[-] Error: {EMAILS_JSON} file not found!")
        return
    except json.JSONDecodeError:
        print(f"[-] Error: {EMAILS_JSON} contains invalid JSON!")
        return
    
    if not os.path.exists(CERTIFICATES_FOLDER):
        print(f"[-] Error: '{CERTIFICATES_FOLDER}' folder not found!")
        return
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(YOUR_EMAIL, YOUR_PASSWORD)
        print("[+] Successfully connected to Gmail SMTP server")
    except Exception as e:
        print(f"[-] Failed to connect to Gmail: {e}")
        return
    
    successful_emails = 0
    failed_emails = 0
    
    for entry in email_data:
        recipient_email = entry.get('email')
        png_filename = entry.get('png')
        
        if not recipient_email or not png_filename:
            print(f"[-]  Skipping invalid entry: {entry}")
            failed_emails += 1
            continue
        
        png_path = os.path.join(CERTIFICATES_FOLDER, png_filename)
        
        if not os.path.exists(png_path):
            print(f"[-] PNG file not found: {png_path}")
            failed_emails += 1
            continue
        
        try:
            msg = MIMEMultipart()
            msg['From'] = YOUR_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = EMAIL_SUBJECT
            
            # email body
            msg.attach(MIMEText(EMAIL_BODY, 'plain'))
            
            # PNG file
            with open(png_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {png_filename}'
            )
            msg.attach(part)
            
            # Send
            server.send_message(msg)
            print(f"[+] Sent certificate to: {recipient_email} ({png_filename})")
            successful_emails += 1
            
        except Exception as e:
            print(f"[-] Failed to send to {recipient_email}: {e}")
            failed_emails += 1
    
    server.quit()
    print(f"\n[=] Summary:")
    print(f"[+] Successful: {successful_emails}")
    print(f"[-] Failed: {failed_emails}")
    print(f"[=] Total processed: {successful_emails + failed_emails}")

if __name__ == "__main__":
    print("[=] Starting certificate email sender...")
    send_certificate_emails()
