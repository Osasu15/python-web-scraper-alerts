from alerts.email_alert import send_email_alert

send_email_alert(
    subject="Test Alert",
    body="If you received this, your email alerts work."
)

print("Email sent!")
