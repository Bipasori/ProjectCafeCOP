import graphene
from graphene_django.types import DjangoObjectType
from .models import Board

class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        fields = "__all__"

class BoardQuery(graphene.ObjectType):
    allBoard = graphene.List(BoardType)

    def resolve_allBoard(self, info, **kwargs):
        return Board.objects.all()

    def resolve_allBoard_by_id(self, info, id):
        # Querying a single question
        return Board.objects.get(b_no=id)

# https://docs.graphene-python.org/projects/django/en/latest/mutations/


class BoardMutation(graphene.Mutation):
    class Arguments:
        btitle = graphene.String(required=True)
        bwriter = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    question = graphene.Field(BoardType)

    def mutate(self, info, text, id):
        question = Board.objects.get(pk=id)
        question.b_title = btitle
        question.b_writer = bwriter
        question.save()

        return BoardMutation(question=question)

class Mutation(graphene.ObjectType):
    create_board = BoardMutation.Field()
