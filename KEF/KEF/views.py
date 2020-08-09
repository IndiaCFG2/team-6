from django.shortcuts import render, redirect

def workshops(request):
    return render(request, 'main_page/video-page.html')

def about(request):
    return render(request, 'main_page/about.html')

def contact(request):
    return render(request, 'main_page/contact.html')
