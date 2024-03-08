from django.shortcuts import redirect, render
from accounts.models import User
from core.models import Video, Article
from django.db.models import Sum

def dashboard(request):
    users = User.objects.all()
    videos = Video.objects.all()
    articles = Article.objects.all()
    # all_views = Video.objects.aggregate(Sum('view'))['view__sum'] or 0
    # total_users = User.objects.count()
    # total_videos = Video.objects.count()
    context = {
        'users': users,
    #     'total_users': total_users,
         'videos': videos,
         'articles': articles,
    #     'total_videos': total_videos,
    #     'all_views': all_views
     }
    return render(request, "admin/dashboard.html", context)

def addVideo(request):
    return render(request,"admin/video/add-video.html")


def video_list(request):
    videos = Video.objects.all()
    context = {
         'videos': videos,
     }
    return render(request, "admin/video/video-list.html", context)

def add_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        full_name = request.POST.get('full_name', '')
        telephone = request.POST.get('telephone', '')

        # Create a new user instance using CustomUser model and manager
        user = User.objects.create_user(email=email, password=password)
        user.full_name = full_name
        user.telephone = telephone
        if user.is_superuser:
            user.role = 'admin'
        else:
            user.role = 'Guardian'

        user.save()
        return redirect('user_list')  # Redirect to a page displaying the list of users

    return render(request, 'admin/add_user.html')