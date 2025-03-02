from django.shortcuts import render

# Create your views here.
# advanced_features_and_security/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import YourModel

@permission_required('app_name.can_edit', raise_exception=True)
def edit_model(request, pk):
    model_instance = YourModel.objects.get(pk=pk)
    # Your edit logic here
    return render(request, 'edit_model.html', {'model_instance': model_instance})

@permission_required('app_name.can_create', raise_exception=True)
def create_model(request):
    if request.method == 'POST':
        # Your create logic here
        return redirect('model_list')
    return render(request, 'create_model.html')
