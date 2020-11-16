from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ConvertView(APIView):
    """
    Convert an integer based string to an enlish
    readable snippet representing that integer.
    """

    def get(self, request, number, format=None):
        breakpoint()
        return Response(
            {
                'status': 'ok',
                'num_in_english': 'one hundo',
            }, status=status.HTTP_200_OK,
        )