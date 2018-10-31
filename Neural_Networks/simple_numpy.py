import numpy as np



def sigmoid(x):
    s = 1/(1 + np.exp(-x))
    return s



def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s*(1-s)
    return ds    
    
x = np.array([1, 2, 3])
print x
print(np.exp(x)) # result is (exp(1), exp(2), exp(3))


print 'x = np.array([1, 2, 3])'
x = np.array([1, 2, 3])
print (x + 3)



print x
print sigmoid(x), '\n'*5 

x = np.array([1, 2, 3])

print 'sigmoid_derivative(x):'
print sigmoid_derivative(x)



#Exercise: Implement image2vector() that takes an input of shape (length, height, 3) and returns a vector of shape (length*height*3, 1). For example, if you would like to reshape an array v of shape (a, b, c) into a vector of shape (a*b,c) you would do:
#v = v.reshape((v.shape[0]*v.shape[1], v.shape[2])) # v.shape[0] = a ; v.shape[1] = b ; v.shape[2] = c
#Please don't hardcode the dimensions of image as a constant. Instead look up the quantities you need with image.shape[0], etc.

def image2vector(image):
    v = image.reshape((image.shape[0]*image.shape[1] * image.shape[2]),1)    
    return v

image = np.array([[[ 0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])


print ("image2vector(image) = " + str(image2vector(image)))



def softmax(x):
   
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    x_sum = np.sum(x_exp, axis = 1, keepdims = True)
    
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    s = x_exp/x_sum

    ### END CODE HERE ###
    
    return s
