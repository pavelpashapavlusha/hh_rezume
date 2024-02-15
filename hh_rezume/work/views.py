from django.shortcuts import render


def work(request):
    template_name = 'work/work.html'
    return render(request, template_name)
