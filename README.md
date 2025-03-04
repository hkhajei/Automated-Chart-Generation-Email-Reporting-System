# 📊 Automated Chart Generation & Email Reporting System

This project automates the process of generating data visualizations, saving them as PDF reports, and emailing them to relevant recipients. The system reads an address book from an Excel file, generates category-based reports, and sends emails with zipped attachments.

## 🚀 Features

- **🌟 Chart Generation**: Creates and saves charts using `matplotlib.backends.backend_pdf.PdfPages`.
- **📂 Organized Storage**: Saves reports in category-based folders.
- **📧 Automated Email Sending**: Reads an address book from Excel and sends emails with relevant attachments.
- **📦 File Compression**: Zips files before sending emails.

---

## 📂 Project Structure

```
project/
│️── data/
│️   └️── email_address_book.xlsx   # Excel file with recipient details
│️── output/                       # Generated PDF reports by category
│️   ├️── AC/
│️   │️   ├️── outliers.pdf
│️   │️   └️── trends.pdf
│️   ├️── HP/
│️   │️   ├️── outliers.pdf
│️   │️   └️── trends.pdf
│️── scripts/
│️   ├️── generate_charts.py        # Generates charts and saves PDFs
│️   └️── send_email.py             # Handles email sending with attachments
│️── main.py                        # Runs the entire workflow
│️── README.md                      # Project documentation
```

---

## 🔧 Installation & Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2. Install Dependencies**

Ensure you have Python installed, then install the required libraries:

```bash
pip install matplotlib pandas openpyxl smtplib zipfile
```

### **3. Create Sample Address Book**

If the `data/email_address_book.xlsx` file does not exist, run:

```bash
python scripts/create_email_book.py
```

*(You can replace **`create_email_book.py`** with the script you used to generate the Excel file.)*

---

## 📊 Usage

### **1. Generate Charts**

```bash
python scripts/generate_charts.py
```

- This will create category-based PDF reports inside the `output/` directory.

### **2. Send Emails**

```bash
python scripts/send_email.py
```

- Reads recipients from `email_address_book.xlsx`
- Zips related files
- Sends emails with attachments

### **3. Run Everything**

```bash
python main.py
```

- Generates charts
- Sends emails automatically

---

## 📌 Configuration

- Modify `SMTP_SERVER`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` in `send_email.py` before running.
- Adjust `CATEGORIES` in `generate_charts.py` as per your needs.

---

## 🤝 Contributing

Feel free to contribute! Open issues, submit PRs, or share suggestions.

---

## 📩 Contact

For questions or feedback, reach out at:

- **Email**: [h.khajei@gmail.com](mailto\:.khajei@gmail.com)
- **GitHub**: [hkhajei](https://github.com/hkhajei)

