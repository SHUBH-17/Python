# Declare and Assign Variables in python

int_var = 10
float_var = 18.25
string_var = 'Shubham' # or another way is by using double quotes -> "Shubham"  
bool_var = True # or False when we need to assign false


# Function in Python for output
# Function might or might not take parameters
# Print variable values
print('Hello World!!')
print('Value of int_var = ' , int_var, '- Result done !!')
print('Value of float_var = ' , float_var, '- Result done !!')
print('Value of string_var = ' , string_var, '- Result done !!')
print('Value of bool_var = ' , bool_var, '- Result done !!')

# Adding int_var and float_var
print('int_var + float_var = ' ,int_var + float_var)

# Checking data type of any variable in Python : type()
print('Type of int_var ? ',type(int_var) )
print('Type of float_var ? ',type(float_var) )
print('Type of string_var ? ',type(string_var) )
print('Type of bool_var ? ',type(bool_var) )
print('Type of int_var + float_var ? ',type(int_var + float_var) )

# type casting in python : int(), float(), str(), bool()
int_var = int_var + 10 
casted_int_var = float(int_var)
print('Printing casted_int_var ->' , casted_int_var)
print('Type of casted_int_var ? ',type(casted_int_var) )
casted_float_var = int(float_var)
print('Casting float into int ->' , casted_float_var)

numeric_str = '123'
# numeric_str = numeric_str + 50 -> typecasting required
numeric_str = int(numeric_str) + 50
print('value of numeric_str = ', numeric_str)



# taking inputs in python
name = input('Enter Name: ')
age = int(input('Enter age: ')) # converting age to int during input itself as input takes everything as string
print("User Name =",name)
print("User Age =",age )

print("type(name) =", type(name))
print("type(age) =", type(age) )

