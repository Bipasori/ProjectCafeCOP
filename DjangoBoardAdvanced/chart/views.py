from django.shortcuts import render
from chart.models import salesPredict

def chart_bar(request):

    return render(request, "chart_bar.html", {
    })

def chart_bar2(request):

    import pymysql
    dbCon = pymysql.connect('223.194.46.212', 'root', '12345!', 'edudb')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute("SELECT yyyymm, sales_amt, sales_predict FROM sales_predict")
        rsSales = cursor.fetchall()

    return render(request, "chart_bar2.html", {
        'title' : '판매 예측',
        'dtitle1' : '실적',
        'dtitle2' : '예측',
        'rsSales' : rsSales
    })
