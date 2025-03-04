import smtplib
import os
import zipfile
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = 'your_smtp_server.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

EXCEL_FILE = "./data/email_address_book.xlsx"
ATTACHMENTS_DIR = "./output/"
TEMP_ZIP_DIR = "./temp_zips"

def zip_attachments(categories):
    """Create a zip file for the specified categories."""
    os.makedirs(TEMP_ZIP_DIR, exist_ok=True)
    zip_file_path = os.path.join(TEMP_ZIP_DIR, "attachments.zip")
    
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for category in categories.split(','):
            category_path = os.path.join(ATTACHMENTS_DIR, category.strip())
            if os.path.exists(category_path):
                for file in os.listdir(category_path):
                    file_path = os.path.join(category_path, file)
                    if os.path.isfile(file_path):
                        zipf.write(file_path, arcname=f"{category.strip()}/{file}")
    
    return zip_file_path

def send_email(to_email, subject, body, attachments):
    """Send an email with attachments."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        for file_path in attachments:
            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                msg.attach(part)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    df = pd.read_excel(EXCEL_FILE)
    
    for _, row in df.iterrows():
        to_email = row['Email']
        categories = row['Categories']
        subject = "Monthly Analysis Report"
        body = f"""
            <html>
                <body>
                    <p>Dear {row['Fullname']},</p>
                    <p>Please find attached the latest analysis reports.</p>
                    <p>Best regards,</p>
                    <p>Your Team</p>
                </body>
            </html>
        """
        
        zip_path = zip_attachments(categories)
        send_email(to_email, subject, body, [zip_path])

    # Cleanup
    for file in os.listdir(TEMP_ZIP_DIR):
        os.remove(os.path.join(TEMP_ZIP_DIR, file))
    os.rmdir(TEMP_ZIP_DIR)

if __name__ == "__main__":
    main()
