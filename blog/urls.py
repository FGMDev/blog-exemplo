from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('mensagens/', views.mensagens, name='mensagens'),
    path('mensagens/<int:mensagem_id>/edit', views.editar_mensagem, name='editar_mensagem'),
    path('mensagem/<int:mensagem_id>/delete', views.deletar_mensagem, name='deletar_mensagem'),
    path('register/', views.register, name='register')
]