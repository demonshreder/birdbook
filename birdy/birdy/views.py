# URL & shortcuts
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse
from birdy.models import Bird
# from intelligence import bird_id
import tensorflow as tf
import base64
import numpy as np
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
imagePath = sys.argv[1]
script_dir = os.path.dirname(os.path.abspath(__file__))
modelFullPath = script_dir + '/intelligence'
labelsFullPath = script_dir + '/intelligence'

"""Creates a graph from saved GraphDef file and returns a saver."""
with tf.gfile.FastGFile(modelFullPath + '/output_graph.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

sess1 = tf.Session()

# with tf.gfile.FastGFile(modelFullPath + '2/output_graph.pb', 'rb') as g:
#     graph_def = tf.GraphDef()
#     graph_def.ParseFromString(f.read())
#     _ = tf.import_graph_def(graph_def, name='')

# sess2 = tf.Session()


def run_inference_on_image(image_data):

    softmax_tensor = sess1.graph.get_tensor_by_name('final_result:0')
    predictions = sess1.run(
        softmax_tensor, {'DecodeJpeg/contents:0': image_data})
    predictions = np.squeeze(predictions)
    pred_1 = predictions.argsort()[-5:][::-1]
    # print(pred_1, predictions)

    # softmax_tensor = sess2.graph.get_tensor_by_name('final_result:0')
    # predictions = sess2.run(
    #     softmax_tensor, {'DecodeJpeg/contents:0': image_data})
    # predictions = np.squeeze(predictions)
    # pred_2 = predictions.argsort()[-5:][::-1]
    # print(pred_2, predictions)

    f = open(labelsFullPath + '/output_labels.txt', 'r')
    lines = f.readlines()
    labels = [str(w).replace("\n", "") for w in lines]
    labels = labels[pred_1[0]]
    score = predictions[0]

    result = {}
    result['bird'] = labels.title()
    result['score'] = str(score)
    bird = Bird.objects.get(name__icontains=result['bird'])
    result['desc'] = bird.desc
    result['url'] = bird.url
    # print(result)
    return result


def index(request):
    if request.method == 'POST':
        image = request.FILES['file']
        result = run_inference_on_image(image.read())
        return JsonResponse(result)
        # return render(request, 'birdy/index.html', {'result': result})

    else:
        return render(request, 'birdy/index.html')


def bird_list(request):
    name_list = Bird.objects.values('name')
    count = Bird.objects.count()
    return render(request, 'birdy/list.html', {'list': name_list, 'count': count})


def about(request):
    return render(request, 'birdy/about.html')
