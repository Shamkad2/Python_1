from math import sqrt
import log


def get_sqrt(num_1):
    log.log_result(round(sqrt(num_1), 2))
    return round(sqrt(num_1), 2)
