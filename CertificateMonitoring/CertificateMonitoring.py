import ssl
import socket
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def get_certificate_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            return expiry_date
def check_certificate(hostname):
    expiry_date = get_certificate_expiry_date(hostname)
    days_to_expiry = (expiry_date - datetime.utcnow()).days
    print(f"The SSL certificate for {hostname} expires in {days_to_expiry} days on {expiry_date}.")
    return  hostname, days_to_expiry
if __name__ == "__main__":
   
    file_path = r'C:\Users\sahak\OneDrive\Desktop\google.com.txt'

    my_file = open(file_path,"r") 
    data = my_file.read() 
    WebSite = data.split("\n") 
    my_file.close() 
    


    for i in range(len(WebSite)):
       hostname,expiry_date = check_certificate(WebSite[i])
       if expiry_date < -1:
   
            from_email = 'sahakyanarthur023@gmail.com'
            to_email =   'sahakyanartur023@gmail.com'
            subject = f'Certification validation'
            body = f'Your website {hostname} certificate is expires in {expiry_date} days.'
  
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
   
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_user = 'sahakyanarthur023@gmail.com'
            smtp_password = 'ggpbtodayspwmdsw'

            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(smtp_user, smtp_password)
                server.sendmail(from_email, to_email, msg.as_string())
                server.quit()
                print("Email sent successfully!")
            except Exception as e:
                print(f"Failed to send email: {e}")


