from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('boardheroku', views.boardheroku, name="boardheroku"),

    path('board', views.board, name="board"),
    path('board_write', views.board_write, name="board_write"),
    path('board_insert', views.board_insert, name="board_insert"),
    path('board_view', views.board_view, name="board_view"),
    path('board_edit', views.board_edit, name="board_edit"),
    path('board_update', views.board_update, name="board_update"),
    path('board_delete', views.board_delete, name="board_delete"),

    path('board_ajax', views.board_ajax, name="board_ajax"),
    path('board_deleteajax', views.board_deleteajax, name="board_deleteajax"),
    path('board_updatepost', views.board_updatepost, name="board_updatepost"),

    path('portfolio', views.portfolio, name="portfolio"),
    path('portfolio_detail', views.portfolio_detail, name="portfolio_detail"),

    path('boardapi', views.boardapi, name="boardapi"),
    path('boardapi_view', views.boardapi_view, name="boardapi_view"),
    path('boardapi_edit', views.boardapi_edit, name="boardapi_edit"),
    path('boardapi_update', views.boardapi_update, name="boardapi_update"),
    path('boardapi_write', views.boardapi_write, name="boardapi_write"),
    path('boardapi_insert', views.boardapi_insert, name="boardapi_insert"),
    path('boardapi_deleteajax', views.boardapi_deleteajax, name="boardapi_deleteajax"),

]
