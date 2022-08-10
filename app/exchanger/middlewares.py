"""
Module contain middlewares
see: django middlewares
"""
from time import time

from exchanger.models import ResponseLog


class ResponseLogCreate:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        # contain values to db
        response_time = end - start
        request_method = request.method
        query_params = request.GET
        ip_address = request.META.get('REMOTE_ADDR')
        path = request.path

        new_log = ResponseLog.objects.create(
            response_time=response_time,
            request_method=request_method,
            query_params=query_params,
            ip=ip_address,
            path=path
        )
        new_log.save()

        return response
