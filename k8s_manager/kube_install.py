# -*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators import csrf
from django.http import HttpResponseRedirect
import logging
import json

from .models import KubeConfig, KubeCluster
from .forms import KubeConfigForm
from . import common

from k8s_manager.celery import app
from k8s_manager.tasks import k8s_prepare_install_env

logger = logging.getLogger('django')


def build_context():
    context = {}
    return context


# 安装命令
def install_command(request,pk,step_id):

    logging.debug("---------install_command(%s,%s)-------------" % (pk,step_id))
    context = build_context()
    # result = {"status":"ok","data":"","city":"北京"}
    # return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")


    k8s_prepare_install_env.delay();

    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")














