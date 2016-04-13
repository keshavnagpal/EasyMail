from django.shortcuts import render
from django.http import HttpResponse
from msg.models import sendmail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.
def index(request):
	if(request.POST):
		test=sendmail(sub=request.POST["sub"],sender=request.POST["sender"],reciever=request.POST["reciever"],message=request.POST["message"])
		test.save()
		s=test.sender
		r=test.reciever
		m=test.message
		p=request.POST["password"]
		sub=test.sub
		try:
			fromaddr = s
			toaddr = r
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = toaddr
			msg['Subject'] = sub
 
			body = m
			msg.attach(MIMEText(body, 'plain'))
 
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(fromaddr, p)
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()
			return HttpResponse("submitted succesfully to "+r)
		except:
			return HttpResponse("Oops something went wrong , working on it")

	return render(request,'index.html')
    