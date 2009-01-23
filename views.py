from models import Case
from utils import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from forms import UpdateCaseForm


def index(request):
    return render(request, "index.html", {'cases': Case.objects.all()})

def new(request):
    case = Case(source="Hello World")
    case.save()
    return HttpResponseRedirect(case.get_absolute_url())
    
def case(request, id):
    case = get_object_or_404(Case, pk=id)
    context = { 'case': case }
    if request.method == 'POST':
        form = UpdateCaseForm(request.POST, instance=case)
        if form.is_valid():
            form.process(request)
            return HttpResponseRedirect(case.get_absolute_url())
    else:
        form = UpdateCaseForm(instance=case)    
    context['form'] = form
    return render(request, "case.html", context)

def runcase(request, id):
    case = get_object_or_404(Case, pk=id)
    return render(request, "runcase.html", {'case':case})
    