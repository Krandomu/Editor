from django.shortcuts import render
# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.template import RequestContext, loader

from api.models import ContentHTML


def home_view(request):
	template = loader.get_template('home.html')
	
	if (ContentHTML.objects.all()):
		content = ContentHTML.objects.latest('created')
		context = {
			'page': content
		}
		regions = json.loads(content.regions)

		context.update(regions)
		
		context = context
	else:
		context = {}
	
	return HttpResponse(template.render(context))

