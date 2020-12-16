from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    # path('staf/', include('staf.urls')),
    path('catatan/', include('catatan.urls')),
    path('catatan.d/',include('catatan.urls_dosen')),
    path('catatan.sem1/',include('catatan.urls_sem1')),
    path('accounts/', include('accounts.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('sem1/', include('mahasiswa.urls_sem1')),
    path('mahasiswas/', include('mahasiswa.urls_staf')),
    path('staf_sem1/', include('mahasiswa.urls_staf_sem1')),
    path('dosenah/', include('mahasiswa.urls_dosen')),

    # path('dosen/', include('dosen.urls')),
    path('dosens/', include('dosen.urls_staf')),
    path('mitras/', include('mitra.urls_staf')),
    path('forums/', include('forum.urls_staf')),
    path('forumsem1/', include('forum.urls_sem1')),
    path('forumd/', include('forum.urls_dosen')),
    path('forum/', include('forum.urls')),
    path('forumsem1/', include('forum.urls_sem1')),
    path('admin/', admin.site.urls),
    # path("edit_profile/",views.edit_profile,name="edit_profile"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = home.views.error_404
# handler500 = home.views.error_500


