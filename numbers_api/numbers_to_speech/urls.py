# from django.contrib import admin
from django.urls import re_path
from numbers_to_speech.views import ConvertView

urlpatterns = [
    # we do not need the admin site for this api at this point.
    # path('admin/', admin.site.urls),
    re_path(
        r'api/v1/convert/(?P<number>\d+)$',
        ConvertView.as_view(), name='convert'),
]