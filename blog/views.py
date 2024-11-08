from django.shortcuts import render
from .models import Post, Blog, Mensagem

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first()
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
        "blog": Blog.objects.first()
    }
    return render(request, "post.html", context)

def about(request):
    context = {
        "blog": Blog.objects.first()
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
        "blog": Blog.objects.first(),
    }

    if request.method == "POST":
        print(request.POST['nome'])
        print(request.POST['email'])
        print(request.POST['telefone'])
        print(request.POST['mensagem'])
        print(request.POST['cidade'])
        
        if not request.POST['nome']:
            context['errp'] = "O usuario não digitou o nome"
            return render(request, "contact.html", context)

        mensagem = Mensagem(nome = request.POST['nome'],
                            email = request.POST['email'],
                            telefone = request.POST['telefone'],
                            mensagem = request.POST['mensagem'],
                            cidade = request.POST['cidade'])
        
        mensagem.save()

        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html", context)