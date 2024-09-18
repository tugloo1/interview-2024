from pyramid.response import Response
from pyramid import request
from pyramid.view import view_config
from pyramid.view import view_defaults
import transaction


from .. import models


@view_defaults(route_name='rest')
class RESTView(object):
    def __init__(self, req: request.Request):
        self.request = req # request.Request
        self.dbsession = req.dbsession

    @view_config(request_method='GET')
    def get(self):
        query = self.request.dbsession.query(models.MyModel)
        one = query.filter(models.MyModel.name == 'one').one()
        print(one.name)
        print(one.value)
        # return Response(json_body={'name': 'Piyush'})
        return Response(json_body={'name': one.name, 'value': one.value})

    @view_config(request_method='POST')
    def post(self):
        print(self.request.json_body)
        newModel = models.MyModel(name='two', value=2)
        self.dbsession.add(newModel)
        transaction.commit()
        return Response(json_body={'success': 'true'})

    @view_config(request_method='PUT')
    def put(self):
        return Response(json_body={'success': 'true'})

    @view_config(request_method='PATCH')
    def patch(self):
        return Response(json_body={'success': 'true'})

    @view_config(request_method='DELETE')
    def delete(self):
        return Response('delete')