from django.shortcuts import render,get_object_or_404
from  article.models import Article
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})
def detail(request,slug):
    #article = Article.objects.filter(id = id).first()   
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    return render(request,"detail.html")