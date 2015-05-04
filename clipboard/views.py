from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from clipboard.models import *
import json

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

        entries = Entry.objects.filter(owner_id=request.GET.get('owner_id')).order_by('-timestamp').select_related('owner')[start : end]
        return HttpResponse(Entry.iterable_to_json(entries))

    def post(self, request):
        contents = request.body
        e = Entry.json_to_entry(contents)
        e.save()
        return HttpResponse(Entry.iterable_to_json([e]))

class LoginView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        create = bool(request.GET.get('create'))
        contents = request.body
        json_contents = json.loads(contents)

        user = User.objects.filter(username=json_contents['username'])
        if create and len(user) == 0:
            user = User.objects.create(username=json_contents['username'])
            user.set_password(json_contents['passkey'])
            user.save()
            return HttpResponse(user.id)
        elif user.get().check_password(json_contents['passkey']):
            return HttpResponse(user.get().id)
        return HttpResponse(-1)

class ClipView(TemplateView):
    template_name = "clipboard/clip.html"
