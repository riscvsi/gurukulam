from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ammount = request.POST.get("ammount")
        print(name)
        print(ammount)
    return render(request, "index.html")


def success(request):
    return  render(request, "success.html")