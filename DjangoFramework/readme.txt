
Session 관리 *******************************************************************************************************

- makemigrations, migrate 하면 장고 Session 생성
- Session은 서버 cookie이지만 장고는 별도로 관리

# session 변수 생성
request.session['member_no'] = rsMember.member_no

# session 변수 읽기
if 'company_no' in request.session:
    companyno = request.session['company_no']

====================================================================
엑셀 업로드
====================================================================

pip install pymysql
pip install openpyxl

# https://blog.thereis.xyz/41
pip install django-cors-headers



https://icofont.com/icons
