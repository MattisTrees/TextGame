from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.

@csrf_exempt
def sms_response(request):
	print(str(request))

	# Start the TwiML response
	resp = MessagingResponse()

	if request.method == "POST":

		# Add a text message
		msg = resp.message("Hello Lauren! This is a message from the Django App!!!")

		return HttpResponse(str(resp))
	if request.method == "GET":
		msg = resp.message("The Django server has recieved a GET request and doesn't know what to do with it! Ask Matt!")
		return HttpResponse(str(resp))
