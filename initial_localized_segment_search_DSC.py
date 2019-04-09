import math

''' f(x) Quasiconvex function on R. Find first localized segment x* є [a,b] '''

def dsk_min(f, x_0, h_0, epsilon=10**(-5)):


    # if x is to close to x+h 
    if (f(x_0) + abs(h_0)>f(x_0)) and (f(x_0) - abs(h_0)>f(x_0)) and abs(h_0)<epsilon:
        return (x_0-h_0, x_0+h_0)
    
    # choose which side to go to us
    if (f(x_0) < f(x_0+h_0)):
        h_0 = -h_0
        if f(x_0) + abs(h_0) < f(x_0) or f(x_0) + abs(h_0) < f(x_0):
            raise ValueError('ERROR f(x_0) + abs(h_0) < f(x_0) or f(x_0) + abs(h_0) < f(x_0)')

    x_points = [x_0]
    h_values = [h_0]

    while (f(x_points[-1]) > f(x_points[-1]+h_values[-1])):
        x1 = x_points[-1] + h_values[-1]
        h1 = 2*h_values[-1]
        x_points.append(x1)
        h_values.append(h1)


        # only if function does not exist at f(x+h) point we will reduce by hals h
        check_if_exsist = False
        while check_if_exsist is False:
            try:
                f(x_points[-1])
                f(x_points[-1]+h_values[-1])
            except ValueError:
                h_values[-1] /= 2.0
                if abs(h_values[-1]) < epsilon:
                    break
            else:
                check_if_exsist = True

    if (f(x_points[-1]) < f(x_points[-1] + h_values[-1])) and len(x_points)>1:  
        # choose section from 4 points (remove one of them)
        # [x_m, x_m+1, x_m-1, x_m-2] --> posible section

        x_m = x_points[-1] + h_values[-1]
        x_m_min_1 = x_points[-1]
        x_m_min_2 = x_points[-2]
        h_k_add_1 =  h_values[-1] / 2.0
        x_m_add_1 = x_m - h_k_add_1

        if (f(x_m_min_2) > f(x_m)):
            return (x_m, x_m_min_1)
        else:
            return (x_m_add_1, x_m_min_2)
    else: # smth wrong with x_0 or h_o
        print(x_points)
        print(h_values)
        return (x_points[-1] + h_values[-1], x_points[-1])


func_1 = lambda x: 2*x**2 - 12*x
func_2 = lambda x: 3*x**2 + 6*x - 2
func_3 = lambda x: x**2 + 2*(x*math.log10(x/math.e) - 2.0)
func = func_2

print(dsk_min(func, h_0 = 0.005, x_0=5))
