from django.conf.urls import url
from django.conf import settings

from open_edx_api_extension import views


COURSE_ID_PATTERN = settings.COURSE_ID_PATTERN
USERNAME_PATTERN = '(?P<username>[\w.@+-]+)'

urlpatterns = [
    url(r'^courses/$', views.CourseList.as_view()),
    url(r'^courses/{}/(?P<username>\w+)/$'.format(COURSE_ID_PATTERN), views.CourseUserResult.as_view()),
    url(r'^enrollment$', views.SSOEnrollmentListView.as_view(), name='courseenrollments'),
]
