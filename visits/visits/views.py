from django.http import JsonResponse
from django.core.cache import cache

from rest_framework.decorators import api_view


@api_view(['GET',])
def snippet_list(request):
    if request.method == 'GET':
        visits = cache.get("visits")
    if not visits:
        cache.set("visits", 0)
    cache.incr("visits")
    return JsonResponse({"visitasds": cache.get("visits")})