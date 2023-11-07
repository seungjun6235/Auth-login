from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): #올바른 입력한 경우: 흔한비밀번호 X
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'signup.html',context)