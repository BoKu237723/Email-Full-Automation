import re

ALLOWED_DOMAINS = {
    '@gmail.com',
    '@outlook.com',
    '@hotmail.com',
    '@proton.me',
    '@icloud.com',
    '@yahoo.com'
}

def is_valid_email(email):
    email = email.strip().lower()

    # Check if email ends with any of the allowed domains.
    for domain in ALLOWED_DOMAINS:
        if email.endswith(domain):
            # Basic email validation: should have something before the @
            local_part = email[:-len(domain)]
            if local_part and '@' not in local_part:
                return True
    return False

def process_emails():
    try:
        with open('emails.txt', 'r', encoding='utf-8') as f:
            raw_emails = [line.strip() for line in f if line.strip()]

        cleaned_set = set()
        duplicates = []
        removed = []

        for email in raw_emails:
            email_lower = email.lower()
            
            if is_valid_email(email_lower):
                if email_lower in cleaned_set:
                    # This is a duplicate of a valid email
                    duplicates.append(email)
                else:
                    # New valid email
                    cleaned_set.add(email_lower)
            else:
                # Invalid email format
                removed.append(email)

         # Write cleaned emails (unique valid ones)
        with open('cleaned.txt', 'w', encoding='utf-8') as f:
            for email in sorted(cleaned_set):
                f.write(email + '\n')

        # Write duplicated emails
        with open('duplicate.txt', 'w', encoding = 'utf-8') as f:
            for email in duplicates:
                f.write(email+'\n')

        # Write removed emails (invalud ones)
        with open('removed.txt', 'w', encoding = 'utf-8') as f:
            for email in removed:
                f.write(email + '\n')

        # print summary
        print(f"Processing complete!")
        print(f"Total emails processed: {len(raw_emails)}")
        print(f"Unique valid emails saved to cleaned.txt: {len(cleaned_set)}")
        print(f"Duplicate emails saved to duplicate.txt: {len(duplicates)}")
        print(f"Invalid emails saved to removed.txt: {len(removed)}")
        
    except FileNotFoundError:
        print("[-] Error: emails.txt not found in current directory")
    except Exception as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    process_emails()