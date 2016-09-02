from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.template.context_processors import csrf
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import UserProfile, User


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


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
            context = {'profile': profile}
            return render(request, 'userprofile/your_profile.html', context)
        return render(request, 'userprofile/update_profile.html', {'form': form})


@login_required()
def your_profile(request):
    profile = UserProfile.objects.all()
    context = {'profile': profile, }
    return render(request, 'userprofile/your_profile.html', context)


@login_required()
def user_profile(request):
    return render(request, HttpResponse("Hello biatches"))








