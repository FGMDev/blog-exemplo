from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Blog, Mensagem
from .forms import MensagemForm
from django.forms.models import model_to_dict

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
        form = MensagemForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                form.save()
                return redirect('mensagens')
            else: context["form"] = form
    else:
        context["form"] = MensagemForm()
        
    return render(request, "contact.html", context)
    
def mensagens(request):
    context = {
        "mensagens": Mensagem.objects.all()
    }
    return render(request, "mensagens.html", context)

def editar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    context = {
        "blog": Blog.objects.first,
        "form": MensagemForm(initial=model_to_dict(mensagem))
    }
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem.save()
            return redirect('mensagens')
        
    return render(request, "contact.html", context)


def deletar_mensagem(request, mensagem_id):
    context = {
        "blog": Blog.objects.first,
        "mensagem": get_object_or_404(Mensagem, pk=mensagem_id)
    }
    
    if request.method == 'POST':
        context["mensagem"].delete()
        return redirect('mensagens')
    else:
        return render(request, "delete_contact.html", context)

def register(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, "register.html", context)