from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context

# import datetime
#
#
# def hello(request):
#     return HttpResponse('Hello World!')
#
#
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><head><title>Current date&time</title></head><body>Now: %s.</body></html>" % now
#     return HttpResponse(html)
#
#
# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     date_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     html = "<html><head><title>Current date&time</title></head><body>Time in %s hours: %s.</body></html>" % (offset, date_time)
#     return HttpResponse(html)