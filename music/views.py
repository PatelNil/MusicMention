from django.http import request,Http404
from django.http.response import JsonResponse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import context
from .models import Album, Song
from django.template import loader
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.views.generic import View
from .forms import UserForm
import lyricsgenius as lg
class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name = 'all_album'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class Album_create(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class Album_update(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class Album_delete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #returns user object if credentials are corrects
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user) #login step
                    return redirect('music:index')
        return render(request, self.template_name,{'form':form})

class Song_add(CreateView):
    model = Song
    fields = ['album','file_type','song_title']
class Song_delete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:details')
def make_album_fav(request):
    id = request.GET['id']
    a1 = Album.objects.get(id=id)
    a1.is_favorite = True
    a1.save()
    return JsonResponse({'fav':'Favorite'})

def Show_lyrics(request):
    genius = lg.Genius('4x-nTc-nUzekdFO6SyL2U_IJ93xxvTtztp_ox4hfqOBoEnZolVv6jEDMvj_F0M_B',skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    artist = genius.search_artist(request.POST['artist'], max_songs=0, sort="title")
    song = genius.search_song(request.POST['id'])
    s1 = song.lyrics
    s1 = list(s1.split('\n'))
    return render(request,'music/lyrics.html',{'context':s1})


# Create your views here.
"""
def index(request):
    #return HttpResponse("<h1>HomePage</h1>")#you can enter plane text too.
    html = ''
    all_album = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_album':all_album
    }
    for album in all_album:
        url = str(album.id)+'/'
        html += '<a href="'+url+'">'+album.album_title+'</a><br>'
    return HttpResponse(html)
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',context)
def details(request,album_id):
    album = get_object_or_404(Album,id=album_id)
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exsits")
    return render(request,'music/detail.html',{'album':album})

def fav(request,album_id):
    album = get_object_or_404(Album,id=album_id)
    try:
        song = album.song_set.get(id=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not select valid song!!"
        })
    else:
        song.is_fav = True
        song.save()
        return render(request,'music/detail.html',{'album':album})
"""