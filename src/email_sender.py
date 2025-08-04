
import smtplib
from email.message import EmailMessage
import openpyxl
from jinja2 import Template
import os
import csv
from datetime import datetime

def send_emails(dry_run=False):
    from dotenv import load_dotenv
    load_dotenv()

    email_address = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASSWORD")

    wb = openpyxl.load_workbook("data/recipients.xlsx")
    sheet = wb.active

    with open("templates/email_template.html", "r", encoding="utf-8") as f:
        template = Template(f.read())

    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file = "logs/sent_emails.csv"
    log_exists = os.path.exists(log_file)

    with open(log_file, mode="a", newline="", encoding="utf-8") as log:
        log_writer = csv.writer(log)
        if not log_exists:
            log_writer.writerow(["Timestamp", "Email", "Status", "Message"])

        for row in sheet.iter_rows(min_row=2, values_only=True):
            name, email, service, price = row
            subject = f"Proposal for {service}"
            body = template.render(name=name, service=service, price=price)

            print(f"📨 Preview for: {email}")
            print(f"Subject: {subject}\n")
            print(body)
            print("-" * 60)

            if dry_run:
                print(f"[DRY-RUN] Would send to: {email}\n")
                log_writer.writerow([datetime.now(), email, "DRY-RUN", "Previewed"])
                continue

            confirm = input("Send this email? (y/n): ").strip().lower()
            if confirm != "y":
                print(f"❌ Skipped: {email}")
                log_writer.writerow([datetime.now(), email, "SKIPPED", "User chose not to send"])
                continue

            try:
                msg = EmailMessage()
                msg["Subject"] = subject
                msg["From"] = email_address
                msg["To"] = email
                msg.set_content(body, subtype="html")

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(email_address, email_password)
                    smtp.send_message(msg)

                print(f"✅ Email sent to {email}\n")
                log_writer.writerow([datetime.now(), email, "SENT", "Success"])
            except Exception as e:
                print(f"❌ Error sending to {email}: {e}\n")
                log_writer.writerow([datetime.now(), email, "ERROR", str(e)])
