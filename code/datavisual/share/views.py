from django.shortcuts import render
from .models import share
from .forms import shareform,userRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def share_list(request):
    shares=share.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'shares':shares})

@login_required
def share_create(request):
    if request.method=="POST":
        form=shareform(request.POST)
        if form.is_valid():
            share=form.save(commit=False)
            share.user=request.user
            share.save()
            return redirect('share_list')
    else:
        form=shareform()
        
    #for empty forms
    return render(request,'tweet_form.html',{'form':form})
@login_required
def share_edit(request, share_id):
    share_instance = get_object_or_404(share, pk=share_id, user=request.user)
    if request.method == "POST":
        form = shareform(request.POST, instance=share_instance)
        if form.is_valid():
            form.save()
            return redirect('share_list')
    else:
        form = shareform(instance=share_instance)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def share_delete(request,share_id):
    share_instance=get_object_or_404(share,pk=share_id,user=request.user)
    if request.method=='POST':
        share_instance.delete()
        return redirect('share_list')
    return render(request,'tweet_confirm_delete.html',{'share':share_instance})




def register(request):
    if request.method=='POST':
        form=userRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('share_list')
    else:
        form=userRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def see(request,share_id):
    share_instance = get_object_or_404(share,pk=share_id)
    if share_instance.type_of_link == '3d':
        template_name = 'see_data.html'
    elif share_instance.type_of_link == 'Geo':
        template_name = 'see_data_second.html'
    return render(request, template_name, {'share_instance': share_instance})


