Python 가상환경 설정  Django 설치

django-admin startproject config .
python manage.py startapp users
users에 models.py – profile사용
마이그레이션 makemigrations, migrate

pip install graphene-django
pip install Django-graphql-jwt
 PyJWT 다시 설치 pip install PyJWT==1.7.1         : 2021년 2월 에러

마이그레이션 migrate
python manage.py createsuperuser

pip install mjango-graphql-auth                  : 2020년 11월 16일 release
마이그레이션 migrate

config.urls.py
schema.py  settings.py에 GRAPHENE, INSTALLED_APPS ‘django_filters’
admin.py
/admin에서 user등록

API :
schema.py
- settings.py - GRAPHQL_JWT

http://127.0.0.1:8000/graphql
