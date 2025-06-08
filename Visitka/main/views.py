from django.shortcuts import render




def home(request):
    return render (request, 'main/home.html')

def about(request):
    return render (request, 'main/about.html')

def portfolio(request):
    projects = [
        {
            'title': 'Проект 1',
            'description': 'Краткое описание первого проекта',
            'image': 'project1.jpg',
            'link': '#',
            'technologies': ['HTML', 'CSS', 'JavaScript']
        },
        {
            'title': 'Проект 2',
            'description': 'Краткое описание второго проекта',
            'image': 'project2.jpg',
            'link': '#',
            'technologies': ['Python', 'Django', 'PostgreSQL']
        },
        {
            'title': 'Проект 3',
            'description': 'Краткое описание третьего проекта',
            'image': 'project3.jpg',
            'link': '#',
            'technologies': ['React', 'Node.js', 'MongoDB']
        }
    ]
    return render(request, 'main/portfolio.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        # Здесь будет обработка формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Обычно здесь отправка email или сохранение в БД
        return render(request, 'main/contact_success.html')
    return render(request, 'main/contact.html')






