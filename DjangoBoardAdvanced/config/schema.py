import graphene
from board.schema import BoardQuery, BoardCreate, BoardDelete, BoardUpdate
from weblog.schema import WeblogCreate

class Query(
    BoardQuery,
    ):
    pass

# class Mutation(
#     BoardCreate,
#     CreatePerson,
#     ):
#     pass

# Resolve할 mutation class 생성
class Mutations(graphene.ObjectType):
    board_create = BoardCreate.Field()
    board_delete = BoardDelete.Field()
    board_update = BoardUpdate.Field()
    weblog_create = WeblogCreate.Field()

schema = graphene.Schema(
    query=Query,
    mutation=Mutations
)
