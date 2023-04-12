=========================================================================================
초기 작업
=========================================================================================
pip install django
python manage.py runserver

bootstrapmade.com 에서
Vesperr 디자인 템플릿 적용

https://icofont.com/icons

python manage.py makemigrations
python manage.py migrate

=========================================================================================
Features
=========================================================================================
- 게시판
- ajax 적용하여 삭제...
- 게시판 조회에서 count증가 적용되어 있음...
- 앨범 업로드 게시판 - portfolio 디자인 활용, 파일업로드
- GraphQL API - 장고 graphene

=========================================================================================
설치
=========================================================================================
pip install mysqlclient
pip install pymysql
pip install graphene-django

# pip install django-encrypted-fields

===============================================================================
시각화
=========================================================================================
https://www.chartjs.org/samples/latest/
https://stackoverflow.com/questions/51003311/django-and-chartjs

# GraphQL error - Method Not Allowed
https://adamj.eu/tech/2020/06/29/why-does-python-raise-modulenotfounderror-when-modifying-installed-apps/
https://github.com/adamchainz/django-cors-headers
python -m pip install django-cors-headers
