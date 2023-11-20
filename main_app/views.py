from django.shortcuts import render

from main_app.models import Product

menu = [
    {'title': 'Инфо', 'url_name': 'info'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Доставка', 'url_name': 'delivery'},
    {'title': 'Отзывы', 'url_name': 'reviews'},
]
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'main_app/index.html', context=context)


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        contact = [{'name': name, 'phone': phone}]
        print(contact)
    return render(request, 'main_app/about.html')