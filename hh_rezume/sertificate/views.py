from django.shortcuts import render


def sertificate(request):
    template_name = 'sertificate/sertificate.html'
    return render(request, template_name)
