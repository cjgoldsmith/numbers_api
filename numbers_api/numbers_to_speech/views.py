from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from textwrap import wrap
import math


class ConvertView(APIView):
    """
    Convert an integer based string to an enlish
    readable snippet representing that integer.
    """
    ONES = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    TENS = {
        '0': '',
        '1': 'ten',
        '2': 'twenty',
        '3': 'thirty',
        '4': 'fourty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety',
    }

    # 10^{key * 3}
    MAGNITUDE = {
        0: '',
        1: 'thousand',
        2: 'million',
        3: 'billion',
        4: 'trillion',
        5: 'quadrillion',
        6: 'quintillion',
        7: 'sextillion',
        8: 'septillion',
        9: 'octillion',
        10: 'nonillion',
        11: 'decillion',
        12: 'undecillion',
        13: 'duodecillion',
        14: 'tredecillion',
    }

    def get(self, request, number, format=None):
        return Response(
            {
                'status': 'ok',
                'num_in_english': self.parse_hundred(number),
            }, status=status.HTTP_200_OK,
        )

    @classmethod
    def parse_number(cls, number_string):
        parsed = ''

        # We require full hundreds sets in each magnitude.
        padded_length = math.ceil(len(number_string)/3) * 3
        number_string = number_string.zfill(padded_length)

        number_by_magnitude = wrap(number_string, 3)
        idx = len(number_by_magnitude) - 1
        for hundreds_string in number_by_magnitude:
            parsed += f'{cls.parse_hundred(hundreds_string)} {cls.MAGNITUDE[idx]}'.strip()
            parsed += ' '
            idx -= 1
        return parsed.rstrip()


    @classmethod
    def parse_hundred(cls, hundreds_string):
        # programming error, do not continue.
        if len(hundreds_string) != 3:
            raise ValueError("parse_hundred called with less than hundreds value string")

        hundreds = cls.ONES[hundreds_string[0]]
        if hundreds:
            hundreds = f'{hundreds} hundred'

        tens = cls.TENS[hundreds_string[1]]
        ones = cls.ONES[hundreds_string[2]]
        return ' '.join([hundreds, tens, ones]).strip()
