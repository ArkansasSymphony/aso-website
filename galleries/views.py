from django.shortcuts import render_to_response
from arkansassymphony.galleries.models import Gallery, Photo, Audio
from django.template import RequestContext

def galleries_view(request, media_type):
	if media_type == "photo":
		gallery_list = Gallery.objects.all().order_by('-order_date')
		return render_to_response('gallery/photos.html', {'gallery_list': gallery_list,}, context_instance=RequestContext(request))
	elif media_type == "video":
		return render_to_response('gallery/video.html', context_instance=RequestContext(request))
	elif media_type == "audio":
		audio = Audio.objects.all()
		return render_to_response('gallery/audio.html', {'audio': audio}, context_instance=RequestContext(request))
		
	
def photos_view(request, gallery_url):
	photos_list = Photo.objects.filter(gallery__url_name = gallery_url)
	gallery_list = Gallery.objects.filter(url_name = gallery_url)
	for i in gallery_list:
		gallery_object = i
	
	return render_to_response('gallery/gallery-display.html', {'photos_list': photos_list, 'gallery_object': gallery_object}, context_instance=RequestContext(request))
	
def single_photo(request, photo_name):
	photos_list = Photo.objects.filter(photo=photo_name)
	for photo in photos_list:
		photo_object = photo
	return render_to_response('gallery/photo-display.html', {'photo_object': photo_object}, context_instance=RequestContext(request))
