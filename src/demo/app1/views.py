import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger('django')

def home(request):
    msg = "Hello world from homepage."
    logger.warn(msg)
    return HttpResponse(msg)

def subpage(request):
    msg = "Hello world from subpage."
    logger.error(msg)
    return HttpResponse(msg)
