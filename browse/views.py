from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import TriangleIssue, TriangleArticle;
from django.template import loader
from django.shortcuts import render

def index(request):
    issue_list = TriangleIssue.objects.order_by('-pub_date');
    context = { 'issue_list': issue_list, }
    return render(request, 'browse/index.html', context)

def issue(request, issue_id):
    issue = get_object_or_404(TriangleIssue, pk=issue_id)
    return render(request, 'browse/issue.html', {'issue': issue})

def article(request, article_id):
    article = get_object_or_404(TriangleArticle, pk=article_id)
    return render(request, 'browse/article.html', {'article': article})

