from pyramid.response import Response
import random
from pyramid import request
from pyramid.view import view_config
from pyramid.view import view_defaults
import transaction


from .. import models

queue = {}
job_id = 123



@view_defaults(route_name='rest')
class RESTView(object):
    def __init__(self, req: request.Request):
        self.request = req # request.Request
        self.dbsession = req.dbsession

    @view_config(request_method='GET')
    def get(self):
        body = self.request.json_body
        job_id = body['job_id']
        print(queue)
        if job_id in queue:
            return Response(json_body=queue[job_id])
        return Response(json_body={})

    @view_config(request_method='POST')
    def post(self):
        print(self.request.json_body)
        # TODO Validate all params there
        job_id = random.randint(0, 10)
        new_data = {'python_script': self.request.json_body['python_script'],
                    'queue_name': self.request.json_body['queue_name'],
                    'date_submitted': '20240918',
                    'status': 'SUBMITTED',
                    'time_submitted':  '2:39 PM PST',
                    }
        queue[job_id] = new_data
        new_data['success'] = 'true '
        new_data['job_id'] = job_id
        print(queue)
        return Response(json_body=new_data)

        # newModel = models.MyModel(name='two', value=2)
        # self.dbsession.add(newModel)
        # transaction.commit()
        return Response(json_body={'success': 'true'})

    @view_config(request_method='PUT')
    def put(self):
        return Response(json_body={'success': 'true'})

    @view_config(request_method='PATCH')
    def patch(self):
        return Response(json_body={'success': 'true'})

    @view_config(request_method='DELETE')
    def delete(self):
        body = self.request.json_body
        job_id = body['job_id']
        print(queue)
        if job_id in queue:
            del queue[job_id]
            print(queue)
            return Response(json_body={'success': 'true', 'date_deleted': 'YYYYMMDD', 'time_deleted': 'TODO: get time'})
        return Response(json_body={'success': 'false'})