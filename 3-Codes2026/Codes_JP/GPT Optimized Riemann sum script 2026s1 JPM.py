####This code is OPTIMIZED FOR MEMORY by ChatGPT, and it no longer creates huge lists. Also uses all three left mid and right evaluation####

#Example function x^2 + 5x + 6 or also (x+2)(x+3), evaluated from 0 to 3
def assessed_function(x):
    return (x+2)*(x+3) #Change this when changing the assessed function

#Define also the integral of the above function
def integral(x):
    return (x**3)/3 + (5/2)*(x**2) + 6*x #Change this when changing the assessed function

#Define the points we want to assess
point_1 = 0
point_2 = 3

#In this case we use 10e1 to 10e6 points as an example

n_subdivisions = [1,10,100,1000,10000,100000,1000000,10000000] 
#Its not recommended to go higher than 10e7
#You can also replace by n_subdivisions = range(1000) but it will spam the text below


#The procedure of this code is:
# 0. Creates an outside loop to iterate for n_subdivisions
# 1. Assess f(x) from a to b in a n-stepwise manner and multiplies in the spot by dx to obtain the rectangle area and store that into a grand total variable
# 2. Sum all of the new area and it gets the approximate area under the curve for all three approximations :D
# 3. Compares with the analytical solution using the defined integral

#0. Create an outside loop to iterate
for subdivision in n_subdivisions:
    #Define delta x as:
    length_of_rectangle = (point_2 - point_1) / subdivision

    #Create empty values to sum later
    total_left = 0
    total_mid = 0
    total_right = 0

    #Creates a while loop that counts from i to n subdivisions
    i = 0
    while i < subdivision:
        dx = length_of_rectangle

        #Starts from point 1 and increments x each time by i rectangles of dx width
        x = point_1 + i * dx

        #Calculates each x at any given x inside the loop to pass along to f(x)
        left_x = x
        mid_x = x + dx/2
        right_x = x + dx

        #2. Sums each calculated f(x)*dx to a grand total per approximation
        total_left  += assessed_function(left_x)  * dx
        total_mid   += assessed_function(mid_x)   * dx
        total_right += assessed_function(right_x) * dx

        i += 1  # count rectangles, not distance

    exact_area = integral(point_2) - integral(point_1)

    print(
        f"Left={total_left:.6f}, Mid={total_mid:.6f}, Right={total_right:.6f}, Exact={exact_area:.6f}"
    )


    #4. To check accuracy, we can do the defined integral check
    #If f(x) = x^2 + 5x + 6
    #F'(b) - F'(a)= (x^3)/3 + 5/2(x^2) + 6x

    exact_area = integral(point_2) - integral(point_1)

    #Show total area from 0 to 3 in the form of a phrase
    print("The total area computed from " + str(point_1) + " to " + str(point_2) + " was " + str(total_left)+  " from the left, " + str(total_mid)+" in the middle and " + str(total_right)+" from the right, using subdivisions of " + str(length_of_rectangle) + " while the analytical area using the defined integral was " + str(exact_area))


print("Please note that middle values converge much quicker than left or right ones.")
