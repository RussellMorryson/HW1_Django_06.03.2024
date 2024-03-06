from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
   logger.info('Index page accessed')
   main_index = """<!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            </head>
            <body>
                <h1>Главная страница</h1>
                <h2>Еще один заголовок!</h2>
                <a href= 'about'>Обо мне</a>
                </body>
            </html>"""
   return HttpResponse(main_index)

def about(request):
    logger.info('About page accessed')
    about = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Обо мне</h1>
    <h2>Привет всем меня зовут Руслан</h2>
    <a href='index'>Главная</a>
</body>
</html>"""
    return HttpResponse(about)
