class SecurityHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response["X-Frame-Options"] = "ALLOWALL"
        response["Content-Security-Policy"] = (
            "frame-src https://www.youtube.com https://www.youtube-nocookie.com;"
        )
        return response
