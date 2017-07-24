# URL & shortcuts
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse
from intelligence import bird_id
import tensorflow as tf
import base64


def index(request):
    # bird_id.bird_test()
    if request.method == 'POST':
        image = request.FILES['file']
        result = bird_id.run_inference_on_image(image.read()).title()
        # image.seek(0)
        # image = base64.b64encode(image.read())
        print(result)
        return HttpResponse(result)
        # return render(request, 'birdy/index.html', {'result': result})

    else:
        return render(request, 'birdy/index.html')
