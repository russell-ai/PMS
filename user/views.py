from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.urls import reverse_lazy


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{username}, Giriş BAŞARILI!')
            return redirect('landing-page')
        else:
            messages.success(request, "Giriş BAŞARIZSIZ!, kullanıcı adı veya parola yanlış, tekrar deneyin.")
            return redirect('user:login')
    else:
        return render(request, 'user/login.html')


@login_required
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.success(request, "Bu kullanıcı adı sistemde kayıtlı. Başka bir kullanıcı adı deneyin")
                return redirect('user:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.success(request, "Bu email sistemde kayıtlı. Başka bir email adı deneyin")
                    return redirect('user:register')
                else:
                    user = User(username=username, password=password, email=email)
                    user.save()
                    messages.success(request, f'Kayıt BAŞARILI! {username}, hesabı oluşturuldu.')
                    return redirect('user:login')

        else:
            messages.success(request, "Parolalar eşleşmedi!")
            return redirect('user:register')
    else:
        return render(request, 'user/register.html')


@login_required
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        messages.success(request, "Oturum kapatıldı!")
        return redirect('user:login')


class MyPasswordChangeView(PasswordChangeView):
    template_name = "user/password-change.html"
    success_url = reverse_lazy('user:password-change-done')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "user/password-reset-done.html"
