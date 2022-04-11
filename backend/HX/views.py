from urllib import request
from django.http import HttpResponse, JsonResponse
from .utils import *
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializer import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
import json

pcid_temp = 0
pcid_flow1 = 0
pcid_flow2 = 0
pcid_relay = 0

class getTempFlowLatest(APIView):
    def get(self, request):
        h = HX.objects.get(id=1)
        ser = GetHX(h)
        print(ser.data)
        return Response(ser.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class writeTempLatest(APIView):
    def get(self, request):
        l = getLastLine('temp.csv')
        writeCurrTempValues(l)
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class startTempLogs(APIView):
    def get(self, request):
        global pcid_temp
        pcid_temp = startTempReading()
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class stopTempLogs(APIView):
    def get(self, request):
        global pcid_temp
        stopTempReading(pcid_temp)
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class startFlowLogs(APIView):
    def get(self, request):
        global pcid_flow1, pcid_flow2
        pcid_flow1, pcid_flow2 = startFlowReading()
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class stopFlowLogs(APIView):
    def get(self, request):
        global pcid_flow1, pcid_flow2
        stopFlowReading(pcid_flow1, pcid_flow2)
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class writeFlowLatest(APIView):
    def get(self, request):
        l1 = getLastLine('fhot_rate.csv')
        l2 = getLastLine('fcold_rate.csv')
        writeCurrFlowValues(l1 + ',' + l2)
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class getLiveSetPt(APIView):
    def get(self, request):
        h = liveSetPt('relay.py')
        return Response({'Tsetpt_live':h}, status=status.HTTP_200_OK)

    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class startRelay(APIView):
    def get(self, request):
        global pcid_relay
        pcid_relay = startRel()
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        return HttpResponse("Bad Request.", status=406)

class setPointTemp(APIView):
    def get(self, request):
        return HttpResponse("Bad Request.", status=406)

    def post(self, request):
        dat = json.loads(request.body)
        h = HX.objects.get(id=1)
        h.Tsetpt = dat['Tsetpt']
        h.save()
        return Response(status=status.HTTP_200_OK)

class stopRelay(APIView):
    def get(self, request):
        global pcid_relay
        stopRel(pcid_relay)
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        return HttpResponse("Bad Request.", status=406)
