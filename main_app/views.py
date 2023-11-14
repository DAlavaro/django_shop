from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(name, email, message)
    return render(request, 'main_app/index.html')


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        contact = [{'name': name, 'phone': phone}]
        print(contact)
    return render(request, 'main_app/about.html')