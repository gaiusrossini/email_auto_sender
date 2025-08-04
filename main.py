import argparse
from src.email_sender import send_emails

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Email Sender")
    parser.add_argument("--dry-run", action="store_true", help="Simulate email sending without actually sending")

    args = parser.parse_args()
    send_emails(dry_run=args.dry_run)
