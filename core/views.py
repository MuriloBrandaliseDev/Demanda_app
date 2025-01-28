from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Demanda
from .forms import DemandaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def home(request):
    demandas = Demanda.objects.filter(is_concluded=False).order_by('-data_demanda')
    return render(request, 'core/home.html', {'demandas': demandas})

@login_required
# core/views.py

@login_required
def demanda_detail(request, pk):
    demanda = get_object_or_404(Demanda, pk=pk)
    return render(request, 'core/demanda_detail.html', {'demanda': demanda})

@login_required
def concluir_demanda(request, pk):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        demanda = get_object_or_404(Demanda, pk=pk)
        demanda.is_concluded = True
        demanda.save()
        return JsonResponse({'success': True})
    return HttpResponseForbidden()


@login_required
def demanda_create(request):
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            demanda = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'redirect_url': f'/demanda/{demanda.pk}/'
                })
            else:
                return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
    else:
        form = DemandaForm()
    return render(request, 'core/demanda_form.html', {'form': form})

@login_required
def demanda_update(request, pk):
    demanda = get_object_or_404(Demanda, pk=pk)
    if request.method == 'POST':
        form = DemandaForm(request.POST, instance=demanda)
        if form.is_valid():
            demanda = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'redirect_url': f'/demanda/{demanda.pk}/'
                })
            else:
                return redirect('demanda_detail', pk=demanda.pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
    else:
        form = DemandaForm(instance=demanda)
    return render(request, 'core/demanda_form.html', {'form': form})

@login_required
def calendar_view(request):
    return render(request, 'core/calendar.html')

@login_required
def get_events(request):
    # Filtra apenas as demandas não concluídas
    demandas = Demanda.objects.filter(is_concluded=False)
    events = []
    for demanda in demandas:
        events.append({
            'title': demanda.titulo,
            'start': demanda.data_demanda.strftime('%Y-%m-%d'),
            'url': f'/demanda/{demanda.pk}/',
        })
    return JsonResponse(events, safe=False)