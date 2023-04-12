import graphene
from graphene_django.types import DjangoObjectType
from .models import Board, Person

class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        # fields = "__all__"
        fields = ("b_no", "b_title", "b_note", "b_writer", "b_count", "b_date")

class BoardQuery(graphene.ObjectType):
    Board_all = graphene.List(BoardType)
    Board_detail = graphene.Field(BoardType, b_no=graphene.Int(required=True))

    def resolve_Board_all(self, info, **kwargs):
        return Board.objects.all()

    def resolve_Board_detail(self, info, b_no):
        # Querying a single question
        return Board.objects.get(b_no=b_no)

# schema = graphene.Schema(query=BoardQuery)

# https://docs.graphene-python.org/projects/django/en/latest/mutations/

class BoardCreate(graphene.Mutation):
    # Mutation결과로 표시할 항목
    bNo = graphene.Int()
    bTitle = graphene.String()
    bWriter = graphene.String()
    bNote = graphene.String()

    # 서버로 보낼 데이터
    class Arguments:
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    # Mutation method : DB에 생성
    def mutate(self, info, bTitle, bWriter, bNote):
        rsBrd = Board(
            b_title=bTitle,
            b_writer=bWriter,
            b_note=bNote
        )
        rsBrd.save()

        return BoardCreate(
            bTitle=rsBrd.b_title,
            bWriter=rsBrd.b_writer,
            bNote=rsBrd.b_note,
        )

# Resolve할 mutation class 생성
class Mutation(graphene.ObjectType):
    board_create = BoardCreate.Field()


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(root, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)

class Person(graphene.ObjectType):
    name = graphene.String()

class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()

# We must define a query for our schema
class Query(graphene.ObjectType):
    person = graphene.Field(Person)

schema = graphene.Schema(query=Query, mutation=MyMutations)