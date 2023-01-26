import model_div as m_div
import model_mult as m_mult
import model_sub as m_sub
import model_sum as m_sum
import model_pow as m_pow
import model_sqrt as m_sqrt
import compl
import user_interface as u_i
import log
import excep 


def calc():
    print("Calculator welcomes you!")
    
    while True:
        print()
        u_i.main_menu()
        num = excep.wrong_input()
        
        if num == 1:
            print('-' * 50)
            print("Working with rational")

            while True:
                u_i.operations_rational()
                op = excep.wrong_input()
                print('-' * 50)
                
                if op == 1:
                    print("Addition")
                    log.log_operation("Addition")
                    print(m_sum.get_sum(excep.is_number("Enter 1 number: "), excep.is_number("Enter 2 number: ")))
                    break
                elif op == 2:
                    print("Subtraction")
                    log.log_operation("Subtraction")
                    print(m_sub.get_sub(excep.is_number("Enter 1 number: "), excep.is_number("Enter 2 number: ")))
                    break
                elif op == 3:
                    print("Multiplication")
                    log.log_operation("Multiplication")
                    print(m_mult.get_mult(excep.is_number("Enter 1 number: "), excep.is_number("Enter 2 number: ")))
                    break
                elif op == 4:

                    while True:
                        u_i.div_operations()
                        div_op = excep.wrong_input()
                        print('-' * 50)
                        
                        if div_op == 1:
                            print("Division")
                            log.log_operation("Division")
                            print(m_div.get_div(excep.is_number("Enter 1 number: "), excep.is_not_zero("Enter 2 number: ")))
                            break
                        elif div_op == 2:
                            print("Integer division")
                            log.log_operation("Integer division")
                            print(m_div.get_int_div(excep.is_number("Enter 1 number: "), excep.is_not_zero("Enter 2 number: ")))
                            break
                        elif div_op == 3:
                            print("Get remainder of the division")
                            log.log_operation("Get remainder of the division")
                            print(m_div.get_remain_div(excep.is_number("Enter 1 number: "), excep.is_not_zero("Enter 2 number: ")))
                            break
                        else:
                            print("Incorrect entry! Please, choose something from the list!")
                    break

                elif op == 5:
                    print("Exponentiation")
                    log.log_operation("Exponentiation")
                    print(m_pow.get_pow(excep.is_number("Enter 1 number: "), excep.is_number("Enter 2 number: ")))
                    break
                elif op == 6:
                    print("Calculating the square root")
                    log.log_operation("Calculating the square root")
                    print(m_sqrt.get_sqrt(excep.is_number("Enter a number: ")))
                    break
                else:
                    print("Incorrect entry! Please, choose something from the list!")
        
        elif num == 2:
            print('-' * 50)
            print("Working with complex")
            
            while True:
                u_i.operations_complex()
                op = excep.wrong_input()
                print('-' * 50)
                
                if 1 <= op <= 5:
                    print(compl.compl(op))
                    break
                else:
                    print("Incorrect entry! Please, choose something from the list!")

        elif num == 0:
            return "The program has finished working."
        
        else:
            print("Incorrect entry! Please, choose something from the list!")
