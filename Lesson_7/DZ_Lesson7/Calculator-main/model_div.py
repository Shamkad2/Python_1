import log


def get_div(num_1, num_2):
    log.log_result(num_1 / num_2)
    return num_1 / num_2


def get_int_div(num_1, num_2):
    log.log_result(num_1 // num_2)
    return num_1 // num_2


def get_remain_div(num_1, num_2):
    log.log_result(num_1 % num_2)
    return num_1 % num_2
