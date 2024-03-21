
from argparse import ArgumentParser

parser = ArgumentParser(description='Hello baby..')

parser.add_argument("a_float",type=float)

parser.add_argument("-an_opt_float",type=float)

parser.add_argument("-an_opt_float_w_default",default=5.0,type=float)

parms = parser.parse_args()

print (vars(parms))

