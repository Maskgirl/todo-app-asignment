from django.shortcuts import render,redirect
from .models import *
from .form import *


def listTask(request):
	queryset = task.objects.order_by('complete','due')
	form = TaskForm()
	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		# return redirect('/')
	context = {
		'tasks':queryset,
		'form':form,
		}
	return render(request, 'list.html', context)
def updateTask(request, pk):
	queryset = task.objects.get(id=pk)
	form = UpdateForm(instance=queryset)
	if request.method == 'POST':
		form = UpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'form':form
		}

	return render(request, 'update_task.html', context)

def deleteTask(request, pk):
	queryset = task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/')

	context = {
		'item':queryset
		}
	return render(request, 'delete_task.html', context)
