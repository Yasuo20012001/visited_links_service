from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Visit
import json
from django.utils import timezone

@csrf_exempt
def visited_links(request):
    try:
        data = json.loads(request.body)
        links = data.get('links', [])

        for link in links:
            visit = Visit(link=link)
            visit.save()

        return JsonResponse({'status': 'ok'})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'status': str(e)}, status=500)


def visited_domains(request):
    try:
        from_time = int(request.GET.get('from'))
        to_time = int(request.GET.get('to'))

        visits = Visit.objects.filter(timestamp__range=[timezone.datetime.fromtimestamp(from_time), timezone.datetime.fromtimestamp(to_time)])
        domains = list(set([visit.link.split('//')[-1].split('/')[0] for visit in visits]))

        return JsonResponse({'domains': domains, 'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': str(e)}, status=500)
