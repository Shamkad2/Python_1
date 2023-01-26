import model_div as m_div
import model_mult as m_mult
import model_sub as m_sub
import model_sum as m_sum
import model_pow as m_pow
import log 
import excep


def compl(op):
    if op == 1:
        print("Addition")
        log.log_operation("Addition")
        return m_sum.get_sum(complex(excep.is_number("Enter 1 real part: "), excep.is_number("Enter 1 imaginary part: ")), \
                            complex(excep.is_number("Enter 2 real part: "), excep.is_number("Enter 2 imaginary part: ")))
    elif op == 2:
        print("Subtraction")
        log.log_operation("Subtraction")
        return m_sub.get_sub(complex(excep.is_number("Enter 1 real part: "), excep.is_number("Enter 1 imaginary part: ")), \
                            complex(excep.is_number("Enter 2 real part: "), excep.is_number("Enter 2 imaginary part: ")))
    elif op == 3:
        print("Multiplication")
        log.log_operation("Multiplication")
        return m_mult.get_mult(complex(excep.is_number("Enter 1 real part: "), excep.is_number("Enter 1 imaginary part: ")), \
                            complex(excep.is_number("Enter 2 real part: "), excep.is_number("Enter 2 imaginary part: ")))
    elif op == 4:
        print("Division")
        log.log_operation("Division")
        return m_div.get_div(complex(excep.is_number("Enter 1 real part: "), excep.is_number("Enter 1 imaginary part: ")), \
                            complex(excep.is_not_zero("Enter 2 real part: "), excep.is_not_zero("Enter 2 imaginary part: ")))
    elif op == 5:
        print("Exponentiation")
        log.log_operation("Exponentiation")
        return m_pow.get_pow(complex(excep.is_number("Enter 1 real part: "), excep.is_number("Enter 1 imaginary part: ")), \
                            complex(excep.is_number("Enter 2 real part: "), excep.is_number("Enter 2 imaginary part: ")))   
