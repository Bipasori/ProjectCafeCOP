from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('waadmin', views.waadmin, name="waadmin"),
    path('waresult', views.waresult, name="waresult"),
    path('make_session', views.make_session, name="make_session"),
    path('reset_session', views.reset_session, name="reset_session"),
    path('select_answer', views.select_answer, name="select_answer"),

    path('create_qheader', views.create_qheader, name="create_qheader"),
    path('change_qheader', views.change_qheader, name="change_qheader"),

    path('create_question', views.create_question, name="create_question"),
    path('change_question', views.change_question, name="change_question"),
    path('delete_question', views.delete_question, name="delete_question"),

    path('waresult_read', views.waresult_read, name="waresult_read"),
    path('create_qresult', views.create_qresult, name="create_qresult"),
    path('change_qresult', views.change_qresult, name="change_qresult"),
    path('delete_qresult', views.delete_qresult, name="delete_qresult"),

]

