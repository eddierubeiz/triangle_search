from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import TriangleIssue, TriangleArticle;
from django.template import loader
from django.shortcuts import render


def index(request):
    #years = TriangleIssue.objects.dates('pub_date','year', order='DESC')
    #issue_list = TriangleIssue.objects.order_by('-pub_date');
    issue_list = TriangleIssue.objects.filter(pub_date__year='1986').order_by('pub_date');
    start_year = 1900
    end_year = 2150
    issue_counts = {}
    for i in range (start_year, end_year):
        count_for_this_year =  TriangleIssue.objects.filter(pub_date__year=i).count()
        if count_for_this_year > 0:
            issue_counts[i] = count_for_this_year
    context = { 'issue_list': issue_list , 'issue_counts' : issue_counts}
    return render(request, 'browse/index.html', context)

def year(request, year):
    issue_list = TriangleIssue.objects.filter(pub_date__year=year).order_by('pub_date');
    context = { 'issue_list': issue_list, 'year': year }
    return render(request, 'browse/year.html', context)

def issue(request, issue_id):
    issue = get_object_or_404(TriangleIssue, pk=issue_id)
    year = issue.pub_date.strftime('%Y')
    return render(request, 'browse/issue.html', {'issue': issue, 'year': year})

def article(request, article_id):
    article = get_object_or_404(TriangleArticle, pk=article_id)
    year = article.issue.pub_date.strftime('%Y')
    return render(request, 'browse/article.html', {'article': article, 'year':year})

