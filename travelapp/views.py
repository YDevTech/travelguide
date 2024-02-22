from django.shortcuts import render, get_object_or_404, redirect,
from .models import Experience,
from .forms import ExperienceForm 

# Create your views here.
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'experience_list.html', {'experiences': experiences})

def experience_detail(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    return render(request, 'experience_detail.html', {'experience': experience})

def create_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            new_experience = form.save()
            return redirect('experience_detail', experience_id=new_experience.id)
    else:
        form = ExperienceForm()

    return render(request, 'create_experience.html', {'form': form})
