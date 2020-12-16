from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from mahasiswa.models import Pkl
# from catatan.models import Gambar
from . import models, forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/')
def index_sem1(req):
    forum = req.user.mahasiswa.first().nama_mitra

    return redirect(f'/forumsem1/{forum.id}')


@login_required(login_url='/accounts/')
def delete_forum(req, id):
    models.Forum.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/forumsem1/')


@login_required(login_url='/accounts/')
def detail_forum_sem1(req, id):
    forum = models.Forum.objects.filter(pk=id).first()
    komen = models.Komen.objects.filter(pk=id).first()
    form_input = forms.PostingForm()
    form_komen = forms.KomenForm()
    form_balas = forms.BalasForm()

    if req.POST:
        form_input = forms.PostingForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.instance.forum = forum
            form_input.save()
        return redirect(f'/forumsem1/{id}')

    print(forum.posting.first())

    return render(req, 'forumsem1/detail.html', {
        'form': form_input,
        'form_komen': form_komen,
        'form_balas': form_balas,
        'data': forum,
    })


@login_required(login_url='/accounts/')
def delete_posting_sem1(req, id, id_posting):
    models.Posting.objects.filter(pk=id_posting).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forumsem1/{id}')
    
@login_required(login_url='/accounts/')
def delete_komen_sem1(req, id, id_posting, id_komen):
    models.Komen.objects.filter(pk=id_komen).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect(f'/forumsem1/{id}')

@login_required(login_url='/accounts/')
def sem1_komen(req, id, id_posting):
    posting = models.Posting.objects.filter(pk=id_posting).first() 

    if req.POST:
        form_komen = forms.KomenForm(req.POST, req.FILES)
        if form_komen.is_valid():
            form_komen.instance.pengguna = req.user
            form_komen.instance.posting = posting
            form_komen.save()

    return redirect(f'/forumsem1/{id}')
