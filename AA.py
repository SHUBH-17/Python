
list_a = [9,-1,2,-5,1,10,-6]
print ('Given list: ',list_a)

print('Printing positive no.s first then negative no.s')
result = [ x for x in list_a if x>0 ] + [ x for x in list_a if x<0 ]
print (result)

print('Printing positive no.s first then negative no.s but in sorted way')
list_a = list(set(list_a))
result = [ x for x in list_a if x>0 ] + [ x for x in list_a if x<0 ]
print (result)

print('adding all elements > 0 and adding all elements < 0 sepearately')
import functools
res = [functools.reduce(lambda x,y : x+y,list(filter(lambda x : x > 0, list_a)))] +[functools.reduce(lambda x,y : x+y,list(filter(lambda x : x < 0, list_a)))]
print (res)
