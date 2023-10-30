from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/services')
def services():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('index.html')


# Load email configuration from environment variables or a config file.

@app.route('/contact-submit', methods=['POST'])
def contact_submit():
    if request.method == 'POST':
        name = request.form['name']
        email_user = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        # Handle the form data, save to a database, etc.
        try:
                    # Access email configuration from environment variables
            # email_host = os.environ.get('SSN_PROJECT_EMAIL_ADDRESS')
            # email_password = os.environ.get('SSN_PROJECT_EMAIL_PASS')
            email_port = 587
            email_host =  "smtp.gmail.com" 
            email_password = "muanlosmmbtztfzi"
            email_from = "ssnmentorshipprojectmailsender@gmail.com"
            email_server = smtplib.SMTP(email_host, email_port)
            email_server.starttls()
            email_server.login(email_from, email_password)
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = email_user
            msg['Subject'] = "Confirmation Mail"
            email_message = '''
                Hello,

                Thank you for booking a session with us. We have received your details, and you will hear from us soon.

                Best regards,
                Your Company
                Indian Infra
                '''
            msg.attach(MIMEText(email_message, 'plain'))

            email_server.sendmail(email_from, email_user, msg.as_string())
            email_server.quit()

            # Redirect to a thank-you page or display a success message.
            return render_template('confirmation.html')

        except Exception as e:
            # Log the error and redirect to an error page or display an error message.
            print(f"Email sending error: {e}")
            return render_template('error.html')

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)





if __name__ == '__main__':
    app.run(debug=True)


