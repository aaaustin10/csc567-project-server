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
        start = request.GET.get('start')
        if start:
            start = int(start)

        amount = request.GET.get('amount')
        if amount:
            amount = int(amount)

        end = amount
        if start and end:
            end += start

        entries = Entry.objects.filter(owner_id=1).order_by('-timestamp').select_related('owner')[start : end]
        return HttpResponse(Entry.iterable_to_json(entries))

    def post(self, request):
        contents = request.body
        e = Entry.json_to_entry(contents)
        e.save()
        return HttpResponse(Entry.iterable_to_json([e]))
