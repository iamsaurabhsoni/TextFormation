from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")
def analyze(request):
    #Get the text
    djlist = request.POST.get('text', 'default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #check which checkbox is checked(on)
    if removepunc == "on":
        punctuations = '''!{}-[]():;"'\,<>./?@#$%^&*_+'''
        analyzed = ""
        for char in djlist:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif(fullcaps == "on"):
        analyzed = ""
        for char in djlist:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djlist):
            if not(djlist[index] == " " and djlist[index+1] == " "):
                analyzed = analyzed + char
        param = {'purpose': 'Erased Extra Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)

    elif(newlineremover == "on"):
        analyzed = ""
        for char in djlist:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        param = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
     else:
        return HttpResponse("Error")

