from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from clipboard.models import *

class ClipboardView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ClipboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        entries = Entry.objects.filter(owner_id=1)
        return HttpResponse(Entry.iterable_to_json(entries))

    def post(self, request):
        contents = request.POST['json']
        e = Entry.json_to_entry(contents)
        e.save()
        return HttpResponse("Success")
