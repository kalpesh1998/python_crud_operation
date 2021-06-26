from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Student_form
from .forms import Student_info

# Create your views here.
def create_view(request):
    context = {}
    form = Student_info(request.POST)
    if form.is_valid():
        form.save()

    context["form"] = form

    # logic
    return render(request, "base.html", context)

# list_view
def list_view(request):
    context = {}
    context["dataset"]= Student_form.objects.all()

    return render(request,'list_view.html',context)

# detail_view
def detail_view(request,pid):
    context={}
    context["data"]=Student_form.objects.get(id=pid)
    return render(request,'detail_view.html',context)

# update
def update_view(request,id):
    context = {}
    obj =get_object_or_404(Student_form,id=id)
    form = Student_info(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('info')

    context["form"]=form
    return render(request,'update.html',context)


# delete view
def delete_view(request,id):
    context={}
    obj=get_object_or_404(Student_form,id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,'delete.html',context)