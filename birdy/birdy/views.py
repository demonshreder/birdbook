# URL & shortcuts
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from intelligence import bird_id
import tensorflow as tf
from .forms import BirdForm
import base64


def index(request):
    # bird_id.bird_test()
    if request.method == 'POST':
        image = request.FILES['bird_image']
        result = bird_id.run_inference_on_image(image.read())
        image.seek(0)
        image = base64.b64encode(image.read())
        return render(request, 'birdy/index.html', {'image': image, 'result': result})

    else:
        form = BirdForm()
        return render(request, 'birdy/index.html', {'form': form})
