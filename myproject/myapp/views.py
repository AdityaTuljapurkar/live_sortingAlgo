from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

from django.http import JsonResponse

def get_data(request):
    data = request.GET.get('array', '')
    if not data.strip():
        return JsonResponse({'error': 'Please enter a comma-separated list of numbers.'}, status=400)

    try:
        array = [int(x.strip()) for x in data.split(',') if x.strip()]
    except ValueError:
        return JsonResponse({'error': 'Invalid input. Please enter only numbers separated by commas.'}, status=400)

    steps = [array.copy()]  # Start with the initial array state

    arr = array.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps.append(arr.copy())  # Record step even if no swap

    return JsonResponse({'steps': steps})
