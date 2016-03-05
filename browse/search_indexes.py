import datetime
from haystack import indexes
from .models import TriangleIssue, TriangleArticle


class TriangleIssueIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    
    
    #indexing these breaks  when you run build_solr_schema -- TrieIntField isn't supported or something.
    #volume = indexes.TrieIntField(model_attr='volume')
    #number = indexes.TrieIntField(model_attr='number')
    issue_url = indexes.CharField(model_attr='issue_url')

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return TriangleIssue.objects.all()

    def get_model(self):
        return TriangleIssue

class TriangleArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    keywords = indexes.CharField(model_attr='keywords')
    genre = indexes.CharField(model_attr='genre')

    def get_model(self):
        return TriangleArticle

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return TriangleArticle.objects.all()
