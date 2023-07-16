import strawberry
from typing import Annotated

from .types import RandomModelType


@strawberry.type
class CreateRandomModelSuccess:
    message: str = "RandomModel created successfully"
    random_model: RandomModelType


@strawberry.type
class CreateRandomModelError:
    message: str = "RandomModel creation failed"

CreateRandomModelPayload = Annotated[
    CreateRandomModelSuccess | CreateRandomModelError,
    strawberry.union(name="CreateRandomModelPayload")
    ]
