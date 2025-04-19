import logging

logger = logging.getLogger("api_requests")


class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith("/api/"):
            logger.info(
                f"{request.method} {request.path} - {response.status_code} "
                f"Headers: {dict(request.headers)}"
            )

        return response
