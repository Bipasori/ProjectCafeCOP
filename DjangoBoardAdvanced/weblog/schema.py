import graphene
from graphene_django.types import DjangoObjectType
from .models import Weblog, WeblogUrl

from datetime import datetime

class LogType(DjangoObjectType):
    class Meta:
        model = Weblog
        fields = "__all__"

class WeblogCreate(graphene.Mutation):
    # 서버로 보낼 데이터
    class Arguments:
        serverDesc = graphene.String()
        userAgent = graphene.String()
        urlDesc = graphene.String()

    weblog = graphene.Field(LogType)

    # Mutation method : DB에 생성
    def mutate(self, info, serverDesc, userAgent, urlDesc):

        # print("session:", info.context.session)
        # print("keys:", info.context.session.keys())
        if 'member_no' in info.context.session:
            mno = info.context.session['member_no']
            memberNo = int(mno)
        else:
            memberNo = 0

        curtime = datetime.now()
        ymd = curtime.strftime("%Y%m%d")

        if WeblogUrl.objects.filter(url_desc=urlDesc, yyyymmdd=ymd).exists():
            rsTmp = WeblogUrl.objects.get(url_desc=urlDesc, yyyymmdd=ymd)
            rsTmp.click_cnt += 1
            rsTmp.save()
        else:
            WeblogUrl.objects.create(url_desc=urlDesc,
                                     yyyymmdd=ymd,
                                     click_cnt=1)

        weblog = Weblog.objects.create(
            member_no=memberNo,
            server_desc=serverDesc,
            useragent=userAgent,
            url_desc=urlDesc,
            log_date=curtime
        )
        return WeblogCreate(weblog=weblog)

