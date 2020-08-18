from django.shortcuts import render
from .models import Topic

def index(request):
    """Main page"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Вывовит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

