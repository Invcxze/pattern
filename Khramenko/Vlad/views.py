from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    data = {"ФИО": "ФИО", "ИНИЦ" : "Храменко Владислав Владимирович", "РОСТ": "Рост", "САНТИМЕТРЫ":"175см", "ВЕС": "ВЕС", "КИЛОГРАММЫ":"60кг","ВОЗРАСТ": "ВОЗРАСТ", "ЛЕТ":"17"}
    return render(request,"about.html", context=data)
def contacts(request):
    data = {"phone":"+79872275017", "telegram":"@napluseW", "GitHub":"https://github.com/Invcxze", "VK":"https://vk.com/slavakh"}
    return render(request, "contacts.html", context={'data':data})
def form(request):
    return render(request, "form.html")