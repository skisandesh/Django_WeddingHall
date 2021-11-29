from django.shortcuts import render
from .forms import FeedbackForm
from django.contrib.auth import get_user_model
from django.views import generic
from .models import HallDetail,UserProfile

def home(request):
    return render(request,'sites/home.html')

class detailview(generic.ListView):
    template_name = 'sites/detail.html'
    model = HallDetail
    context_object_name = 'data'
    def get_queryset(self):
        return HallDetail.objects.filter(name = self.kwargs['hall_name'])



def hall_data(request):
    users = get_user_model().objects.all().values_list('username',flat=True)
    if request.method == 'POST':
        global location, excluded
        global data
        date = request.POST.get('date')
        request.session['date'] = date
        location = request.POST['locations']
        if HallDetail.objects.filter(location__contains= location):
            excludes = []
            for user in users:
                if UserProfile.objects.filter(profile__contains=user):
                    value = UserProfile.objects.filter(profile__contains=user).values_list('list',flat=True)
                    excludes.append(value)

            if not excludes:
                print("true")
                data = HallDetail.objects.filter(location=location)
            else:

                for exclude in excludes:
                     excluded = HallDetail.objects.filter(name__in=exclude).values_list('name',flat=True)
                data = HallDetail.objects.filter(location=location).exclude(name__in=excluded)

            return render(request,'sites/hall_list.html',{'data':data,'date':date})
        else:
            return render(request,'sites/search.html')

def contact(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        print(form)
        form.save()
        return render(request,'sites/home.html')
    context = {'form':form}
    return render(request,'sites/contact.html',context)

def book_hall(request,hall_name):
    return render(request,'sites/booking.html',{'data':hall_name})

def my_list(request):
    # if request.session['date'] == None:
    #     print('true')
    user = request.user
    if 'pay' in request.POST:
        list = request.POST.get('pay')
        date = request.session['date']

        if UserProfile.objects.filter(profile__contains=user):
            a = UserProfile(profile=user,list=list,booked_date=date)
            a.save()

        else:
            userprofile = UserProfile(profile=user,list=list,booked_date=date)
            userprofile.save()

    elif 'release' in request.POST:
        if UserProfile.objects.filter(profile__contains=user):
            hall = request.POST.get('release')
            UserProfile.objects.filter(profile=user,list=hall).delete()


    values = UserProfile.objects.filter(profile__contains=user).values_list('list', flat=True)
    hall_list = HallDetail.objects.filter(name__in=values)

    profile = UserProfile.objects.filter(profile__contains=user)
    # print(profile,hall_list)
    return render(request, 'sites/my_list.html', {'data': hall_list,'profile':profile})




