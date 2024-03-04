from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def dashboard(request):
    return render(request,"base.html")
def profile_list(request):
    profiles=Profile.objects.exclude(user=request.user)
    return render(request,"whisper/profile_list.html",{"profiles":profiles})
def profile(request,pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    profile=Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request,"whisper/profile.html",{"profile":profile})
def dashboard(request):
    form = WhisperForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("whisper:dashboard")
    followed_whisper = Whisper.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    form=WhisperForm()
    return render(request,"whisper/dashboard.html",{"form":form,"whisper":followed_whisper})
