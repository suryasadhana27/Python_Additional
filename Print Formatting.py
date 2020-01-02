# Print Formating #
print('This is a print function')


#Method 1: Putting variables into string

x='String'
print('Place my variable here: %s' %(x)) # Note: %s stands for string

y=123
print('Place my variable here: %s' %(y)) #Note: %s converts the objects into string and prints

#Method 2: Floating point Numbers

print('This is a Floating point Number: %1.2f' %(14.125)) 
#Note: the .2f says how may decimal points are required. Here in this example its 2 digits afer the deciaml point

print('This is a Floating point Number: %1.0f' %(14.125)) 
# Note: 0f represents zero decimal values


print('This is a Floating point Number: %1.5f' %(14.125)) 
# Note: .5f says 5 decimal points, it adds 2 aditional zeros to the esisting number 
# as the number contains only 3 decimal points. ANS: 14.12500

print('This is a Floating point Number: %10.2f' %(14.125)) 
# Note: It prints the values after 10 blank space

# Alternative #
print('Place my variable here: %r' %(y)) 
# %s and %r works similar and converts the value into string

#passing Multiple value object
print ('First: %s, Second: %s, Third:%s' %('hi','Two','3'))
#python follows the order in printing the objects

#####  Best pythonick way is to use string.format methiod ###

print('First: {x}, Second: {x}'.format(x='inserted'))
#Note: here we find the variable once and inserted multiple times, as the object value of x is used 2 times

print('First: {x}, Second: {y}, Third: {x}'.format(x='inserted', y='Surya'))
#Irrespective to the order we can plave the vales as per the requirement

