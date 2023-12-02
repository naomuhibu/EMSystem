from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
#from django.contrib.auth.models import auth
#from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions
from .models import Earthquake
from .serializers import EarthquakeSerializer
#from .forms import CreateUserForm, LoginForm

class IndexView(TemplateView):
    template_name = 'index.html'

    def earthquakes(self):
        earthquakes = Earthquake.objects.all()
        serializer = EarthquakeSerializer(earthquakes, many=True)
        geojson_data = serializer.data
        return JsonResponse({'earthquakes': geojson_data}, content_type='application/json', safe=False)

class EarthquakeList(generics.ListCreateAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer

class EarthquakeAPI(generics.ListAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer  

class EarthquakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Earthquake.objects.all()
    serializer_class = EarthquakeSerializer
    
'''
def Register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_vaild():
            form.save()
            return HttpResponse("The user was registerd.")
        
    context = {'form':form}

    return render(request, 'register.html', context=context)

def Login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return HttpResponse("You have logged in.")
            

    context = {'form': form}
    return render(request, 'login.html', context=context)
    '''