from django.shortcuts import render
from django.views.generic import View
from payment.utils import *
from .conf import *


class GenerateCV(View):
    def post(self, request):
        return renderPdf(CV_PATH, "CV", "inline")
    def get(self, request):
        return renderPdf(CV_PATH, "CV", "inline")