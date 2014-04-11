from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context


def post_list(request):

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

    template = get_template('post_list.html')
    context = Context({
        'activePage': 'home',
        'breadcrumbs': False,
        'tags': tags,
        'posts': posts,
    })
    html = template.render(context)
    return HttpResponse(html)


def post(request, post_name):
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
            'title': post_name,
            'link': '#',
            'active': True,
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

    post_data = {
        'title': 'Post title',
        'thumbnail': 'img/pika_pika.jpg',
        'link': '/installing-lamp-on-ubuntu-12.04/',
        'date': '12 january 2014',
        'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '
                'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                'Lorem Ipsum.',
    }

    template = get_template('post.html')
    context = Context({
        'breadcrumbs': breadcrumbs,
        'tags': tags,
        'post': post_data,
    })
    html = template.render(context)
    return HttpResponse(html)


def contact(request):
    breadcrumbs = [
        {
            'title': 'Home',
            'link': '/',
            'active': False,
        },
        {
            'title': 'Contact me',
            'link': '#',
            'active': True,
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

    template = get_template('contact.html')
    context = Context({
        'activePage': 'contact',
        'breadcrumbs': breadcrumbs,
        'tags': tags,
    })
    html = template.render(context)
    return HttpResponse(html)


def about(request):
    breadcrumbs = [
        {
            'title': 'Home',
            'link': '/',
            'active': False,
        },
        {
            'title': 'About me',
            'link': '#',
            'active': True,
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

    template = get_template('about.html')
    context = Context({
        'activePage': 'about',
        'breadcrumbs': breadcrumbs,
        'tags': tags,
    })
    html = template.render(context)
    return HttpResponse(html)


def portfolio(request):
    breadcrumbs = [
        {
            'title': 'Home',
            'link': '/',
            'active': False,
        },
        {
            'title': 'Portfolio',
            'link': '#',
            'active': True,
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

    template = get_template('portfolio.html')
    context = Context({
        'activePage': 'portfolio',
        'breadcrumbs': breadcrumbs,
        'tags': tags,
    })
    html = template.render(context)
    return HttpResponse(html)