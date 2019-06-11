from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, HttpResponseNotFound


def renderPdf(pdfSrc):
    fs = FileSystemStorage()
    if fs.exists(pdfSrc):
        with fs.open(pdfSrc) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename = "summary_of_summary.pdf" '
            return response
    else:
        return HttpResponseNotFound('This pdf was not found in out server!')
