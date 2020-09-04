from django.shortcuts import render
from school_track.models import Subject, Assignment
from django.http import HttpResponseRedirect
from django.urls import reverse
from school_track.forms import SubjectForm, AssignmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404

# Create your views here.
@login_required
def home(request):
    subjects = Subject.objects.filter(owner=request.user)
    context = {'subjects': subjects}
    return render(request, 'school_track/home.html', context)

@login_required
def subjects(request, subject_id):
    subjects = Subject.objects.get(id=subject_id)
    #MAKE SURE THE SUBJECT BELONGS TO THE CURRENT USER:
    if subjects.owner != request.user:
        raise Http404
    assignments = subjects.assignment_set.order_by('due_date')
    context = {'subjects': subjects, 'assignments': assignments}
    return render(request, 'school_track/subjects.html', context)

@login_required
def new_subject(request):
    form_class = SubjectForm
    #Add a new subject:
    form = form_class(request.POST or None)
    if request.method != 'POST':
        form = SubjectForm
    else:
        # POST data submitted; process data
        if form.is_valid():
            new_subj = form.save(commit=False)
            new_subj.owner = request.user
            new_subj.save()
            return HttpResponseRedirect(reverse('home'))
    
    context = {'form': form}
    return render(request, 'school_track/new_subject.html', context)

@login_required
def new_assignment(request, subject_id):
    form = AssignmentForm(request.POST or None)
    subjects = Subject.objects.get(id=subject_id)
    if request.method != 'POST':
        form = AssignmentForm()
    else:
        form = AssignmentForm(data=request.POST)
        if form.is_valid():
            new_assignment = form.save(commit=False)
            new_assignment.subjects = subjects
            new_assignment.save()
            return HttpResponseRedirect(reverse('subjects', args=[subject_id]))

    context = {'subjects': subjects, 'form': form}
    return render(request, 'school_track/new_assignment.html', context)

@login_required
def edit_assignment(request, assignment_id):
    #Edit an existing assignment:
    assignment = Assignment.objects.get(id=assignment_id)
    subjects = assignment.subjects
    if subjects.owner != request.user:
        raise Http404
    form = AssignmentForm(request.POST or None)
    if request.method != 'POST':
        form = AssignmentForm(instance=assignment)
    else:
        form = AssignmentForm(instance=assignment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subjects', args=[subjects.id]))

    context = {'assignment': assignment, 'subjects': subjects, 'form': form}
    return render(request, 'school_track/edit_assignment.html', context)

@login_required
def delete_assignment(request, assignment_id):
    ass_delete = Assignment.objects.get(id=assignment_id)
    subjects = ass_delete.subjects
    #assignments = subjects.assignment_set.order_by('due_date')
    form = AssignmentForm(request.POST or None)
    if request.method == 'POST':
        ass_delete.delete()
        return HttpResponseRedirect(reverse('subjects', args=[subjects.id]))
    
    context = {'ass_delete': ass_delete, 'subjects': subjects}
    return render(request, 'school_track/delete_assignment.html', context)

