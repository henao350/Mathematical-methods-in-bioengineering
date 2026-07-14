# Create venv by exit() in vscode or directly in cmd or powershell
# cd "C:\Users\JP\Documents\GitHub\dcbi_mathmethods_2026s1" #Thats a folder in my own (JP) GitHub
# python -m venv .venv
# Now python again in the terminal

####This code is NOT OPTIMIZED, as it creates huge lists, and also uses all three left mid and right evaluation####

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

n_subdivisions = [5,10,100,1000,10000,100000,1000000] 
#Because this script is not optimized for memory its not recommended to go higher than 10e6
#You can also replace by n_subdivisions = range(1000) but it will spam the text below

#The procedure of this code is:
# 0. Creates an outside loop to iterate for n_subdivisions
# 1. Calculate (b-a)/n and that would be the "length of each rectangle" and store into a list
# 2. Assess f(x) from a to b in a n-stepwise manner using the x-list, then multiply by x to obtain the rectangle area and store that into a grand total variable
# 3. Finally, sum all of the new area list and it gets the approximate area under the curve for all three approximations :D
# 4. Compares with the analytical solution using the defined integral

#0. Create a loop
for subdivision in n_subdivisions:
    length_of_rectangle = (point_2 - point_1) / subdivision

    #Define parameters necessary for a loop of evaluating the function in length_of_rectangle up to point 2
    list_of_x = []
    iteration = point_1

    #1. Loop to create a list with all possible X values, this should be a list of length equal to subdivision
    while iteration < point_2:
        list_of_x.append(iteration)
        iteration += length_of_rectangle


    #print(list_of_x)

    #2. Takes the list that contains all possible x values and evaluates for each one of them
    #Creates a set of empty values to be added later in each approach
    total_left = 0
    total_mid = 0
    total_right = 0

 ######Loops for every approach
    for x in list_of_x:
        dx = length_of_rectangle #Change of variable name to not 
        left_x = x
        mid_x = x + dx/2
        right_x = x + dx

    #3. The += sums every value of rectangle area to get a total area using n subdivisions
        total_left  += assessed_function(left_x)  * dx
        total_mid   += assessed_function(mid_x)   * dx
        total_right += assessed_function(right_x) * dx

 #####Ends loop for every approach


    #4. To check accuracy, we can do the defined integral check
    #If f(x) = x^2 + 5x + 6
    #F'(b) - F'(a)= (x^3)/3 + 5/2(x^2) + 6x

    exact_area = integral(point_2) - integral(point_1)

    #Show total area from 0 to 3 in the form of a phrase
    print("The total area computed from " + str(point_1) + " to " + str(point_2) + " was " + str(total_left)+  " from the left, " + str(total_mid)+" in the middle and " + str(total_right)+" from the right, using subdivisions of " + str(length_of_rectangle) + " while the analytical area using the defined integral was " + str(exact_area))


print("Please note that middle values converge much quicker than left or right ones.")




