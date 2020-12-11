from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from mahasiswa.models import Pkl
from . import models, forms
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/')
def index(req):
    return render(req, 'dosen/index.html')

# @login_required(login_url='/accounts/')
# def detail_dosen(req, id):
#     dosen = models.Dosen.objects.filter(pk=id).first()
#     catatans = Catatan.objects.filter(owner=dosen.owner) # mengambil semua object yang ada di models Catatan
#     return render(req, 'dosens/detail.html',{
#         'data': catatans,
#     })

@login_required(login_url='/accounts/')
def detail_staf(req, id):
    dosen = models.Catatan.objects.filter(pk=id).first()
    print(dosen)
    if group is not None and group.name == 'dosen':
        mahasiswa = models.Pkl.objects.all()
    catatans = Catatan.objects.filter(owner=dosen.nama_dosen) # mengambil semua object yang ada di models Catatan
    return render(req, 'dosens/detail.html',{
        'data': catatans,
        'data':mahasiswa,
    })

@login_required(login_url='/accounts/')
def index_staf(req):
    tasks = models.Dosen.objects.all()
    form_input = forms.DosenForm()
    form_user = forms.CreateUserForm()

    if req.POST:
        form_input = forms.DosenForm(req.POST, req.FILES)
        form_user = forms.CreateUserForm(req.POST)
        if form_input.is_valid() or form_user.is_valid():
            form_input.save()
            form_user.save()
            return redirect('/dosens/')

    return render(req, 'dosens/index.html',{
        'data': tasks,
        'form' : form_input,
        'form_user' : form_user,
    })

@login_required(login_url='/accounts/')
def catatan(req, id):
    dosen = models.Dosen.objects.all()

    group = req.user.groups.first(pk=id)
    if group is not None and group.name == 'dosen':
        mahasiswa = models.Pkl.objects.all()
    return render(req, 'dosen/catatan.html',{
        'data': dosen,
        'data': mahasiswa,
    })

@login_required(login_url='/accounts/')
def update_staf(req, id):
    if req.POST:
        mitra = models.Dosen.objects.filter(pk=id).update(nip=req.POST['nip'], nama_dosen=req.POST['nama_dosen'], fakultas=req.POST['fakultas'], jurusan=req.POST['jurusan'])
        return redirect('/dosens/')

    dosen = models.Dosen.objects.filter(pk=id).first()
    return render(req, 'dosens/update.html', {
        'data': dosen,
    })

@login_required(login_url='/accounts/')
def delete_staf(req, id):
    models.Dosen.objects.filter(pk=id).delete()
    return redirect('/dosens/')
