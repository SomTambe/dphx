from django.urls import path

from . import views

urlpatterns = [
    path('startTemp', views.startTempLogs.as_view(), name='startTemp'),
    path('stopTemp', views.stopTempLogs.as_view(), name='stopTemp'),
    path('writeTemp', views.writeTempLatest.as_view(), name='writeTemp'),
    path('getTempFlow', views.getTempFlowLatest.as_view(), name='getTempFlow'),
    path('startFlowRate', views.startFlowLogs.as_view(), name='startFlow'),
    path('stopFlowRate', views.stopFlowLogs.as_view(), name='stopFlow'),
    path('writeFlowRate', views.writeFlowLatest.as_view(), name='writeFlow'),
    path('getTstptLive', views.getLiveSetPt.as_view(), name='getSetPoint'),
    path('setPointTemp', views.setPointTemp.as_view(), name='setPoint'),
    path('startRelay', views.startRelay.as_view(), name='startRelay'),
    path('stopRelay', views.stopRelay.as_view(), name='stopRelay'),
]
