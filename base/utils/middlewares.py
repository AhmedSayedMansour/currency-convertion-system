import logging

logger = logging.getLogger(__name__)

class LogResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        logger.info(str(response.content))
        return response
