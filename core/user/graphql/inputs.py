import strawberry


@strawberry.input
class CreateRandomModelInput:
    name: str
