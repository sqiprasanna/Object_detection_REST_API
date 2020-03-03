from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import Http404

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from webapp.models import Employees
# Permission Classes
from rest_framework.permissions import AllowAny
# Rest Framework
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# serializers
# from webapp.serializers import EmployeesSerializer
# from webapp.sketch.src.classes.inference.predict import predict
from webapp.YOLO.Detector import Detector 
from webapp.serializers import MBTISerializer
import cv2
import os

class MBTIAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = MBTISerializer

    def post(self, request, format=None):
        # try:
        serializer = MBTISerializer(data=request.data)
        if serializer.is_valid():
            image = request.data.get("image", None)
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)
            image_path = settings.MEDIA_ROOT + filename
            config_path = './webapp/YOLO/yolov3-spp.cfg'
            weights_path = './webapp/YOLO/yolov3-spp.weights'
            classes_path = './webapp/YOLO/coco.names'
            det_obj = Detector(weights_path,config_path,classes_path)
            img,class_id = det_obj.detectObject(image_path)
            cv2.imwrite(os.path.join(settings.MEDIA_ROOT,'detection.jpg'),img)
            # output = predict(image_path, filename)
            context = {
                "result": {"Big 5": class_id},
                "statusCode": 200,
            }
            return Response(context, status=HTTP_200_OK)
        else:
            context = {
                "statusCode": 400,
                "message": serializer.errors,
            }
            return Response({"error": context}, status=HTTP_400_BAD_REQUEST)