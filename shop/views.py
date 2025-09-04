from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, render

from .models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    # Option 1
    try:
        course = Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404

    # Option 2
    # course = get_list_or_404(Course, pk=course_id)
    # return render(request, 'shop/single_course.html', {'course': course})
