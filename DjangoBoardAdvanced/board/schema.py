import graphene
from graphene_django.types import DjangoObjectType
from .models import Board

from datetime import datetime

class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        # fields = "__all__"
        fields = ("b_no", "b_title", "b_note", "b_writer", "b_count", "b_date")

class BoardQuery(graphene.ObjectType):
    Board_all = graphene.List(BoardType)
    Board_detail = graphene.Field(BoardType, b_no=graphene.Int(required=True))

    def resolve_Board_all(self, info, **kwargs):
        return Board.objects.filter(usage_flag='1').order_by('-b_no')

    def resolve_Board_detail(self, info, b_no):
        # Querying a single question
        return Board.objects.get(b_no=b_no)

# schema = graphene.Schema(query=BoardQuery)

# https://docs.graphene-python.org/projects/django/en/latest/mutations/

class BoardCreate(graphene.Mutation):
    # 서버로 보낼 데이터
    class Arguments:
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    board = graphene.Field(BoardType)

    # Mutation method : DB에 생성
    def mutate(self, info, bTitle, bWriter, bNote):
        board = Board.objects.create(
            b_title=bTitle,
            b_writer=bWriter,
            b_note=bNote,
            b_date=datetime.now()
        )
        return BoardCreate(board = board)


class BoardDelete(graphene.Mutation):
    # 서버로 보낼 데이터
    class Arguments:
        bNo = graphene.Int()

    board = graphene.Field(BoardType)

    # Mutation method : DB에 생성
    def mutate(self, info, bNo):
        board = Board.objects.get(b_no=bNo)
        board.usage_flag = '0'
        board.save()
        return BoardDelete(board = board)

class BoardUpdate(graphene.Mutation):
    # 서버로 보낼 데이터
    class Arguments:
        bNo = graphene.Int()
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    board = graphene.Field(BoardType)

    # Mutation method : DB에 생성
    def mutate(self, info, bNo, bTitle, bWriter, bNote):
        board = Board.objects.get(b_no=bNo)
        board.b_title = bTitle
        board.b_writer = bWriter
        board.b_note = bNote
        board.save()
        return BoardUpdate(board = board)