from django.urls import path
from wiki.views import PageList, PageDetailView

app_name = 'wiki'
urlpatterns = [
    path('', PageList.as_view(), name='wiki-list-page'),
    path('<slug:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
