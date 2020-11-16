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

    POST_PROCESS_TEENS = {
        'ten one': 'eleven',
        'ten two': 'twelve',
        'ten three': 'thirteen',
        'ten four': 'fourteen',
        'ten five': 'fifteen',
        'ten six': 'sixteen',
        'ten seven': 'seventeen',
        'ten eight': 'eighteen',
        'ten nine': 'nineteen',
    }

    def get(self, request, number, format=None):
        return Response(
            {
                'status': 'ok',
                'num_in_english': self.parse_number(number),
            }, status=status.HTTP_200_OK,
        )

    @classmethod
    def _post_process_teens(cls, parsed):
        """
        Post process a parsed string and remove
        the oddity of teens phrasing.
        e.g. 'one hundred ten one' is 'one hundred eleven'.
        """
        for val in cls.POST_PROCESS_TEENS:
            if val in parsed:
                # TODO - think about optimizing this with in place replacement re.sub
                parsed = parsed.replace(val, cls.POST_PROCESS_TEENS[val])
        return parsed

    @classmethod
    def parse_number(cls, number_string):
        """
        Parses a string representation of a number
        ( n digits with no commas or other characters.)
        and returns the human readable representation of
        that number.
        """
        parsed = ''

        # handle negative
        if number_string[0] == '-':
            parsed += 'negative '
            number_string = number_string[1:]

        # We require full hundreds sets in each magnitude.
        padded_length = math.ceil(len(number_string)/3) * 3
        number_string = number_string.zfill(padded_length)

        number_by_magnitude = wrap(number_string, 3)
        idx = len(number_by_magnitude) - 1
        for hundreds_string in number_by_magnitude:
            parsed += f'{cls.parse_hundred(hundreds_string)} {cls.MAGNITUDE[idx]}'.strip()
            parsed += ' '
            idx -= 1
        return cls._post_process_teens(parsed.rstrip())

    @classmethod
    def parse_hundred(cls, hundreds_string):
        """
        Parses a set of three numbers into a hundreds
        human readable representation.

        Hundreds string must be padded to 3 characters if
        value is under the hundreds spot.
        """
        # programming error, do not continue.
        if len(hundreds_string) != 3:
            raise ValueError("parse_hundred called with less than hundreds value string")

        hundreds = cls.ONES[hundreds_string[0]]
        if hundreds:
            hundreds = f'{hundreds} hundred'

        tens = cls.TENS[hundreds_string[1]]
        ones = cls.ONES[hundreds_string[2]]
        return ' '.join([hundreds, tens, ones]).strip()
