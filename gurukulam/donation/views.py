from django.shortcuts import render

# Create your views here.
import razorpay
from .models import DonationGurukulam

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ammount = int(request.POST.get("ammount"))*100
        email = request.POST.get("email")
        print(name)
        print(ammount)
        client = razorpay.Client(auth=("rzp_test_NqMTyxGPRznNqZ","q5lpOYcSqvHq48MdyI610EOk"))
        payment = client.order.create({'ammount': ammount, 'currency': "INR","payment_capture": '1'})
        donateGurukul = DonationGurukulam(name=name, ammount = ammount, email = email, payment_id = payment['id'])
        print(payment)
        return render(request, "index.html", {'payment':payment})
    return render(request, "index.html")


def success(request):
    if request.method == "POST":
        a = request.POST
        print(a)
    return  render(request, "success.html")