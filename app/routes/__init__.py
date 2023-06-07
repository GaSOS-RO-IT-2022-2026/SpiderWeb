from .www import www as blWWW
from .api.v1 import v1 as blV1
routes: list[tuple] = [(blWWW, "/"), (blV1, "/api/v1/")]
