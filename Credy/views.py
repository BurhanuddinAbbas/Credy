from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import threading

threadLock = threading.Lock()
global_counter = 0


def increment_counter():
    global global_counter
    with threadLock:
        global_counter += 1


@require_http_methods(['GET'])
def request_counter(request):
    global global_counter
    return JsonResponse({'requests': 'Number of requests served by this server till now is ' + str(global_counter)})


@require_http_methods(['GET'])
def request_counter_reset(request):
    global global_counter
    with threadLock:
        global_counter = 0
    return JsonResponse({'message': "Request count reset successfully"})
