from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from mahasiswa.models import Pkl
from catatan import models, forms
from forum.models import Forum
from dosen.models import Dosen
from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/')
def index(req):
    tasks = models.Catatan.objects.filter(owner=req.user)
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
        return redirect('/')

    group = req.user.groups.first()
    if group is not None and group.name == 'dosen':
        return render(req, 'dosen/index.html')
    elif group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.all()
        return render(req, 'staf/index.html')
    elif group is not None and group.name == 'dosensem1':
        return render(req, 'dosensem1/index.html')
    elif group is not None and group.name == 'stafsem1':
        tasks = models.Catatan.objects.all()
        return render(req, 'stafsem1/index.html')
    else:
        return render(req, 'home/index.html', {
            'data': tasks,
            'form_catatan' : form_catatan,
            'form_gambar' : form_gambar,
        })
    return render(req, 'staf/index.html')

@login_required(login_url='/accounts/')
def delete_catatan(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/')

@login_required(login_url='/accounts/')
def cetak(req):
    cetak = models.Catatan.objects.filter(owner=req.user)
    forum = Forum.objects.filter().first()
    pkl = Pkl.objects.filter().first()
    dosen = Dosen.objects.filter().first()

    return render(req, 'home/cetak.html', {
        'cetak' : cetak,
        'forum' :forum, 
        'pkl' :pkl,
        'dosen':dosen,  
    })

@login_required(login_url='/accounts/')
def cetak_sem1(req):
    cetak = models.Catatan.objects.filter(owner=req.user)
    forum = Forum.objects.filter().first()
    pkl = Pkl.objects.filter().first()
    dosen = Dosen.objects.filter().first()

    return render(req, 'sem1/cetak.html', {
        'cetak' : cetak,
        'forum' :forum, 
        'pkl' :pkl,
        'dosen':dosen,  
    })


@login_required(login_url='/accounts/')
def cetak_dosen(req):
    cetak = models.Catatan.objects.filter(owner=req.user)
    forum = Forum.objects.filter().first()
    pkl = Pkl.objects.filter().first()
    dosen = Dosen.objects.filter().first()

    return render(req, 'dosen/cetak.html', {
        'cetak' : cetak,
        'forum' :forum, 
        'pkl' :pkl,
        'dosen':dosen,  
    })

@login_required(login_url='/accounts/')
def cetak_dosen_sem1(req):
    cetak = models.Catatan.objects.filter(owner=req.user)
    forum = Forum.objects.filter().first()
    pkl = Pkl.objects.filter().first()
    dosen = Dosen.objects.filter().first()

    return render(req, 'dosensem1/cetak.html', {
        'cetak' : cetak,
        'forum' :forum, 
        'pkl' :pkl,
        'dosen':dosen,  
    })

@login_required(login_url='/accounts/')
def cetak_staf(req):
    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'staf': # mendefinisikan bahwa ini adalah dosen
        cetak = models.Catatan.objects.filter(owner=req.user)
    # return redirect(f'/home/{id}')
    return render(req, 'staf/cetak.html', {
        'cetak' : cetak,
    })
@login_required(login_url='/accounts/')
def cetak_staf_sem1(req):
    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'staf': # mendefinisikan bahwa ini adalah dosen
        cetak = models.Catatan.objects.filter(owner=req.user)
    # return redirect(f'/home/{id}')
    return render(req, 'stafsem1/cetak.html', {
        'cetak' : cetak,
    })