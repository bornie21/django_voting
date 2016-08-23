from django.conf.urls import url

from . import views

# app_name = 'polls'
urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='index'),
    url(r'^create_question/$', views.QuestionCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/question/$', views.QuestionDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update_question/$', views.QuestionUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete_question/$', views.QuestionDelete.as_view(), name='delete'),
    url(r'^choice_list$', views.ChoiceList.as_view(), name='index'),
    url(r'^create_choice/$', views.ChoiceCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/choice/$', views.ChoiceDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update_choice/$', views.ChoiceUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete_choice/$', views.ChoiceDelete.as_view(), name='delete'),

    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]