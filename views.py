from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context

import datetime


def hello(request):
    return HttpResponse('Hello World!')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><head><title>Current date&time</title></head><body>Now: %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    date_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><head><title>Current date&time</title></head><body>Time in %s hours: %s.</body></html>" % (offset, date_time)
    return HttpResponse(html)


def home(request):
    breadcrumbs = [
        {
            'title': 'Home',
            'link': '/',
            'active': False,
        },
        {
            'title': 'Posts',
            'link': '/posts/',
            'active': False,
        },
        {
            'title': 'Installing LAMP in Ubuntu 12.04',
            'link': '#',
            'active': True,
        },
    ]

    posts = [
        {
            'title': 'Post title',
            'thumbnail': 'img/pika_pika.jpg',
            'link': '/installing-lamp-on-ubuntu-12.04/',
            'date': '12 january 2014',
            'comments_count': 15,
            'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '
                    'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                    'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                    'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                    'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                    'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                    'Lorem Ipsum.',
        },
        {
            'title': 'Post title',
            'thumbnail': 'img/pika_pika.jpg',
            'link': '/installing-lamp-on-ubuntu-12.04/',
            'date': '12 january 2014',
            'comments_count': 15,
            'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '
                    'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                    'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                    'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                    'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                    'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                    'Lorem Ipsum.',
        },
        {
            'title': 'Post title',
            'thumbnail': 'img/pika_pika.jpg',
            'link': '/installing-lamp-on-ubuntu-12.04/',
            'date': '12 january 2014',
            'comments_count': 15,
            'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '
                    'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                    'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                    'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                    'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                    'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                    'Lorem Ipsum.',
        },
    ]

    tags = [
        {
            'title': 'Google',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Fish',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Chips',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Salt',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Vinegar',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Fish',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Chips',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Salt',
            'link': 'http://www.google.com',
        },
        {
            'title': 'Vinegar',
            'link': 'http://www.google.com',
        },
    ]

    template = get_template('post_list.html')
    context = Context({
        'activePage': 'contact',
        'breadcrumbs': breadcrumbs,
        'tags': tags,
        'posts': posts,
    })
    html = template.render(context)
    return HttpResponse(html)