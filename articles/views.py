from django.shortcuts import render,redirect
from .forms import ArticleForm,CommentForm
from .models import Article, Comment
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
    form = CommentForm()

    context={
        'article':article,
        'form': form
    }

    return render(request,'detail.html',context)


@login_required
def delete(request,id):
    article = Article.objects.get(id=id)

    if request.user == article.user:
        article.delete()

    return redirect('articles:index')


@login_required
def update(request, id):
    article = Article.objects.get(id=id)

    if request.user != article.user:
        return redirect('articles:detail',id=id)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) #기존정보 + 새로운정보 덮어씌우기
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
    else:
        form = ArticleForm(instance=article) # 기존 정보

    context = {
        'form': form
    }

    return render(request,'form.html',context)


@login_required
def comment_create(request, article_id):
    form = CommentForm(request.POST)
    # article = Article.objects.get(id=id)

    if form.is_valid():
        comment =form.save(commit=False)
        # comment.user = request.user
        # comment.article = article

        comment.user_id = request.user.id
        comment.article_id= article_id

        comment.save()

        return redirect('articles:detail',id=article_id)

@login_required
def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)

    if request.user == comment.user:
        comment.delete()    

    return redirect('articles:detail',id=article_id)