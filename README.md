![GitHub last commit](https://img.shields.io/github/last-commit/gaiusrossini/email_auto_sender?style=flat-square)

# 📧 Email Auto Sender

Automate personalized email sending based on data from an Excel spreadsheet using Python.

This bot reads recipient information (name, email, service, price) from an `.xlsx` file, builds a custom message using Jinja2 templates, and sends emails via SMTP.

## 🚀 Features

- Reads data from Excel (`openpyxl`)
- Uses Jinja2 to generate personalized messages
- Sends real emails via `smtplib`
- Environment variables with `.env` for security
- Clean project structure, ready for production or freelance work

## 📸 Demo

```
✅ Email sent to alice@example.com
✅ Email sent to bob@example.com
✅ Email sent to charlie@example.com
```

## ⚙️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email_auto_sender.git
   cd email_auto_sender
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:
   ```
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

4. Fill the `data/recipients.xlsx` with recipient info.

5. Customize the `templates/message_template.txt` message.

6. Run the script:
   ```bash
   python main.py
   ```

## 🧱 Project Structure

```
email_auto_sender/
├── main.py
├── .env
├── requirements.txt
├── src/
│   └── email_sender.py
├── data/
│   └── recipients.xlsx
├── templates/
│   └── message_template.txt
```

## 📊 Example: recipients.xlsx

| name   | email               | service         | price |
|--------|---------------------|------------------|--------|
| Alice  | alice@example.com   | Website Design   | 500    |
| Bob    | bob@example.com     | SEO Optimization | 300    |

## 📝 Example: message_template.txt

```
Hello {{ name }},

Here is your personalized proposal:

Service: {{ service }}
Price: ${{ price }}

Best regards,
Gaius Rossini
```

## 👤 Author

**Gaius Rossini**  
Freelance Python Developer  
[github.com/gaiusrossini](https://github.com/gaiusrossini)

---

Feel free to use or modify this bot for your own needs. Pull requests are welcome!
