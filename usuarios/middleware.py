from django.utils.cache import add_never_cache_headers


class DisableHtmlCacheMiddleware:
    """Evita el cacheo de respuestas HTML (mismo comportamiento previo).

    Se colocó aquí para que `PruebaDjango/settings.py` apunte a
    `usuarios.middleware.DisableHtmlCacheMiddleware` en lugar de `blog.middleware`.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        content_type = response.get('Content-Type', '')
        if content_type.startswith('text/html'):
            add_never_cache_headers(response)
        return response
