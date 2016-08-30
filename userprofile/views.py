from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.template.context_processors import csrf
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import UserProfile, User


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

'''
@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, request.Files or None, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('userprofile/home.html')
        else:
            user = request.user
            profile = user.profile
            form = UserProfileForm(instance=profile)

            args = {}
            args.update(csrf(request))  # Add cross site forgery here

            args['form'] = form

        return render_to_response('userprofile/update_profile.html', args)
    return render(request, 'userprofile/update_profile.html')


'''


@login_required()
def update_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'posts/login_user.html')
    else:
        form = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        '{% csrf_token %}'
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.avatar = request.FILES['avatar']
            file_type = profile.avatar.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'profile': profile,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'userprofile/update_profile.html', context)
            profile.save()
            context_prof = {
                "profile": profile,
            }
            return render(request, 'userprofile/your_profile.html', context_prof)
        return render(request, 'userprofile/update_profile.html', {'form': form})





@login_required()
def your_profile(request):
    profile = UserProfile.objects.all()
    context = {'profile': profile, }
    return render(request, 'userprofile/your_profile.html', context)



@login_required()
def user_profile(request):
    return render(request, HttpResponse("Hello biatches"))

'''
def home(request, pk):
    profile = User.objects.get(pk=pk)
    context = {'profile': profile, }
    return render(request, 'userprofile/home.html', context)
'''






