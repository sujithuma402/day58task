import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Request vandha odane time note pannu
        start_time = time.time()
        
        response = self.get_response(request)
        
        # Response pogum munadi time calculate pannu
        duration = time.time() - start_time
        
        # Log adichudu
        logger.info(f"Request to {request.path} took {duration:.3f} seconds")
        
        # Header la um add pannalam - optional
        response['X-Request-Duration'] = f"{duration:.3f}s"
        return response