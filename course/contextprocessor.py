from jdatetime import datetime
from extension.utils import persian_number_converter


def time_now(request):
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    return {'current_date': current_date}
