'''
Created on 20/08/2017

@author:
'''
import logging
import sys

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

def ass_core(numeros, cacantidad):
    tam_nums = len(numeros)
    num_formas = 0
    cacas = [[0] * (251)]
    for _ in range(251):
        cacas.append([0] * 251)
    cacas[0][0] = 1
    numeros_ord = sorted(numeros)
#    for num in numeros_ord:
#        cacas[num][num] = 1
    logger_cagada.debug("las monedas {}, la cantidad {}".format(numeros_ord, cacantidad))
    for tam_actual in range(numeros_ord[0], cacantidad + 1):
        num_formas = 0
        logger_cagada.debug("tam act {}".format(tam_actual))
        for moneda_act in numeros_ord:
            num_formas_act = 0
            if(moneda_act > tam_actual):
                break
            logger_cagada.debug("moneda act {}".format(moneda_act))
            comp_moneda_act = tam_actual - moneda_act
            logger_cagada.debug("comp moneda act {}".format(comp_moneda_act))
            logger_cagada.debug("puta mierda i {}".format(cacas[2][2]))
            if(comp_moneda_act):
                for moneda_final_comp in numeros_ord:
                    if(moneda_final_comp > comp_moneda_act):
                        break
                    if(moneda_final_comp > moneda_act):
                        break
                    logger_cagada.debug("comp {} terminando en {} ai {} formas".format(comp_moneda_act, moneda_final_comp, cacas[comp_moneda_act][moneda_final_comp]))
                    num_formas_act += cacas[comp_moneda_act][moneda_final_comp]
                    logger_cagada.debug("puta mierda c {}".format(cacas[2][2]))
            else:
                logger_cagada.debug("whoa no ai comp")
                num_formas_act += 1
            cacas[tam_actual][moneda_act] = num_formas_act
            logger_cagada.debug("puta mierda {}".format(cacas[2][2]))
            logger_cagada.debug("tam act {}, moneda ultima {} formas {}".format(tam_actual, moneda_act, cacas[tam_actual][moneda_act]))
            num_formas += num_formas_act
        logger_cagada.debug("para cantidad {} el num de formas {}".format(tam_actual, num_formas))
    return num_formas

def ass_main():
    lineas = list(sys.stdin)
    cacantidad, _ = [int(x) for x in lineas[0].strip().split(" ")]
    numeros = [int(x) for x in lineas[1].strip().split(" ")]
    mierda = ass_core(numeros, cacantidad)
    print("{}".format(mierda))
    

if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    ass_main()
