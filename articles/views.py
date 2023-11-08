from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request,'index.html',context)

@login_required #@ create전에 이거 먼저 실행해야 되게 만듬
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form
    }    
    
    return render(request,'form.html', context)

def detail(request,id):
    article = Article.objects.get(id=id)

    context={
        'article':article
    }

    return render(request,'detail.html',context)