from django.shortcuts import render, redirect
from . import models, forms
from django.shortcuts import render, redirect
from django.db.models.functions import ExtractWeekDay
from django.forms.models import model_to_dict
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/')
def index(req):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/catatan/')

    tasks = models.Catatan.objects.filter(owner=req.user).annotate(week=ExtractWeekDay('waktu'))
    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.annotate(week=ExtractWeekDay('waktu'))
    return render(req, 'catatan/index.html',{
        'data': tasks,
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,

    })
    
@login_required(login_url='/accounts/')
def detail(req, id):
    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/detail.html', {
        'data': task,
    })
    
@login_required(login_url='/accounts/')
def delete(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/catatan/')

@login_required(login_url='/accounts/')
def index_dosen(req):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/catatan.d/')
    tasks = models.Catatan.objects.filter(owner=req.user).annotate(week=ExtractWeekDay('waktu'))
    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.annotate(week=ExtractWeekDay('waktu'))
    return render(req, 'catatan.d/index.html',{
        'data': tasks,
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,

    })

@login_required(login_url='/accounts/')
def detail_dosen(req):

    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'dosen': # mendefinisikan bahwa ini adalah dosen
        catatans = models.Catatan.objects.filter(owner=req.user)
    return render(req, 'dosenah/index.html',{
        'data': catatans,
    })
@login_required(login_url='/accounts/')
def new(req, *args, **kwargs):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/catatan/')
    return render(req, 'catatan.d/index.html',{
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,
    })
