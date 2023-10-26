from ..resource import Resource

class Animals(Resource):
    def get(self):
        return self._get("/v1/rest/animal/search")