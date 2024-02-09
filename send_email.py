import smtplib
import ssl
from email.message import EmailMessage

# Define email parameters
subject = "Email From Python"
body = "This is a test email from Python!"
sender_email = "your_email@gmail.com"  # Replace with your email address
receiver_email = "recipient_email@gmail.com"  # Replace with recipient's email address
password = input("Enter your email password: ")  # Prompt the user for their password
#Accept App's in Gmail and create a Password APP https://myaccount.google.com/u/4/apppasswords

# Create an EmailMessage object
message = EmailMessage()
message.set_content(body)
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

# Create the HTML content of the email
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

# Add the HTML content to the message as an alternative
message.add_alternative(html, subtype="html")

# Create an SSL context
context = ssl.create_default_context()

# Try to send the email
try:
    print("Sending Email...")

    # Connect to the Gmail SMTP server using SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Log in to the SMTP server
        server.login(sender_email, password)

        # Send the email message
        server.send_message(message)

    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure "Process completed" is printed even if there is an error
    print("Process completed.")
