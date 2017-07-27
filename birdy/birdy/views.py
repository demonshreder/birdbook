# URL & shortcuts
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, JsonResponse
# from intelligence import bird_id
import tensorflow as tf
import base64
import numpy as np
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
imagePath = sys.argv[1]
script_dir = os.path.dirname(os.path.abspath(__file__))
modelFullPath = script_dir + '/intelligence/output_graph.pb'
labelsFullPath = script_dir + '/intelligence/output_labels.txt'

"""Creates a graph from saved GraphDef file and returns a saver."""
with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

sess = tf.Session()


def run_inference_on_image(image_data):
    answer = None

    # print("Inside the script")
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predictions = sess.run(softmax_tensor,
                           {'DecodeJpeg/contents:0': image_data})
    predictions = np.squeeze(predictions)

    top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
    f = open(labelsFullPath, 'r')
    lines = f.readlines()
    labels = [str(w).replace("\n", "") for w in lines]
    for node_id in top_k:
        human_string = labels[node_id]
        score = predictions[node_id]
        # print('%s (score = %.5f)' % (human_string, score))
    result = {}
    result['bird'] = labels[top_k[0]].title()
    result['score'] = str(predictions[top_k[0]])
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
