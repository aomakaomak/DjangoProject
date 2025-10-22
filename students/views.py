from ctypes.wintypes import HHOOK

from django.shortcuts import render
from django.http import HttpResponse

# def example_view(request):
#     return render(request, 'app/example.html')
#
# def show_data(request):
#     if request.method == 'GET':
#         return render(request, 'app/show_data.html')
#
# def submit_data(request):
#     if request.method == 'POST':
#         return HttpResponse('Данные отправлены')
#
# def show_item(request, item_id):
#     return render(request, 'app/item.html', {'item_id': item_id})


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'{name}, спасибо за сообщение')
    return render(request, 'students/contact.html')