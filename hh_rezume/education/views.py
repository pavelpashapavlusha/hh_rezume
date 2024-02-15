from django.shortcuts import render


def education(request):
    template_name = 'education/education.html'
    return render(request, template_name)
