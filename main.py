"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
    
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
  xvec, yvec = pad(x.binary_vec, y.binary_vec)
  if(x.decimal_val <= 1 and y.decimal_val <= 1):
    return BinaryNumber(x.decimal_val*y.decimal_val)
  else:
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    n = len(xvec)
    
    lefts = subquadratic_multiply(x_left, y_left)
    leftFin = bit_shift(lefts, n)

    xSums = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    ySums = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
    #xySums = xSums.decimal_val + ySums.decimal_val
    #xyFin = bit_shift(BinaryNumber(xySums), n//2)

    rightFin = subquadratic_multiply(x_right, y_right)
    
    middle = bit_shift(BinaryNumber(subquadratic_multiply(xSums, ySums).decimal_val-lefts.decimal_val-rightFin.decimal_val), n//2)

    final = middle.decimal_val + leftFin.decimal_val + rightFin.decimal_val

  return BinaryNumber(final)
    ###

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)).decimal_val == 2*2

def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

