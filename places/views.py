from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView, DetailView
from .models import Place, FeedBack
from .forms import PlaceForm, FeedBackForm


def places(request):
    place_objects = Place.objects.all()
    return render(request, 'places/places.html', {"places":place_objects})

def create_place(request):
    if request.method == "POST":
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect(places)

    place_form = PlaceForm()
    return render(request, 'places/form.html', {'place_form':place_form})


def place(request, id):
    place_object = Place.objects.get(id=id)
    return render(request, 'places/place.html', {'place_object': place_object})

def edit_place(request, id):
    place_object = Place.objects.get(id=id)

    if request.method == "POST":
        place_form = PlaceForm(data=request.POST, instance=place_object)
        if place_form.is_valid():
            place_form.save()
            return redirect(place, id=id)

    place_form = PlaceForm(instance=place_object)
    return render(request, 'places/form.html', {'place_form':place_form})


def delete_place(request, id):
    place_object = Place.objects.get(id=id)
    place_object.delete()
    return redirect(places)


class FeedBackView(FormView):
    template_name = 'places/feedback_form.html'
    form_class = FeedBackForm
    success_url = '/places/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class FeedBackDetailView(DetailView):
    queryset = FeedBack.objects.all()
    template_name = 'places/feedback.html'

