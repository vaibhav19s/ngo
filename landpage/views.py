from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Ngo,Event
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    all_ngos=Ngo.objects.all()
    all_events=Event.objects.all()
    context={
        'all_ngos':all_ngos,
        'all_events':all_events,
    }
    return render(request, 'landpage/index.html' , context)

def homepage(request):
    return render(request, 'landpage/homepage.html')


def detail(request):
    #ngo = get_object_or_404(Ngo,pk=ngo_id)
    all_ngos = Ngo.objects.all()
    all_events = Event.objects.all()
    context = {
        'all_ngos': all_ngos,
        'all_events': all_events,
    }
    return render(request, 'landpage/detail.html',context)

def favorite(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    try:
        if event.is_favorite:
            event.is_favorite = False
        else:
            event.is_favorite = True
        event.save()
    except (KeyError, Event.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def delete_event(request, ngo_id, event_id):
    ngo = get_object_or_404(Ngo, pk=ngo_id)
    event = Event.objects.get(pk=event_id)
    event.delete()
    return render(request, 'landpage/detail.html', {'ngo': ngo})




def create_ngo(request):
    if not request.user.is_authenticated():
        return render(request, 'landpage/login.html')
    else:
        form = NgoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            ngo = form.save(commit=False)
            ngo.user = request.user
            ngo.ngo_logo = request.FILES['ngo_logo']
            file_type = ngo.ngo_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'ngo': ngo,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'landpage/create_ngo.html', context)
            ngo.save()
            return render(request, 'landpage/detail.html', {'ngo': ngo})
        context = {
            "form": form,
        }
        return render(request, 'landpage/create_ngo.html', context)


def create_event(request, ngo_id):
    form = EventForm(request.POST or None, request.FILES or None)
    ngo = get_object_or_404(Ngo, pk=ngo_id)
    if form.is_valid():
        ngos_events = ngo.event_set.all()
        for s in ngos_events:
            if s.event_title == form.cleaned_data.get("event_title"):
                context = {
                    'ngo': ngo,
                    'form': form,
                    'error_message': 'You already added that event',
                }
                return render(request, 'landpage/create_event.html', context)
        event = form.save(commit=False)
        event.ngo = ngo
        event.audio_file = request.FILES['audio_file']
        file_type = event.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'ngo': ngo,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'landpage/create_event.html', context)

        event.save()
        return render(request, 'landpage/detail.html', {'ngo': ngo})
    context = {
        'ngo': ngo,
        'form': form,
    }
    return render(request, 'landpage/create_event.html', context)


def delete_ngo(request, ngo_id):
    ngo = Ngo.objects.get(pk=ngo_id)
    ngo.delete()
    ngos = Ngo.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'ngos': ngos})



def favorite(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    try:
        if event.is_favorite:
            event.is_favorite = False
        else:
            event.is_favorite = True
        event.save()
    except (KeyError, Event.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_ngo(request, ngo_id):
    ngo = get_object_or_404(Ngo, pk=ngo_id)
    try:
        if ngo.is_favorite:
            ngo.is_favorite = False
        else:
            ngo.is_favorite = True
        ngo.save()
    except (KeyError, Ngo.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'landpage/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                ngos = Ngo.objects.filter(user=request.user)
                return render(request, 'landpage/index.html', {'ngos': ngos})
            else:
                return render(request, 'landpage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'landpage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'landpage/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                ngos = Ngo.objects.filter(user=request.user)
                return render(request, 'landpage/index.html', {'ngos': ngos})
    context = {
        "form": form,
    }
    return render(request, 'landpage/register.html', context)


def events(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'landpage/login.html')
    else:
        try:
            event_ids = []
            for ngo in ngo.objects.filter(user=request.user):
                for event in ngo.event_set.all():
                    event_ids.append(event.pk)
            users_events = Event.objects.filter(pk__in=event_ids)
            if filter_by == 'favorites':
                users_events = users_events.filter(is_favorite=True)
        except Ngo.DoesNotExist:
            users_events = []
        return render(request, 'landpage/events.html', {
            'event_list': users_events,
            'filter_by': filter_by,
        })
