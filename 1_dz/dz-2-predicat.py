def predicat(x,y,z):

    a = ( bool( not(x or y or z) ) )
    b = ( bool( not(x) and not(y) and not(z) ) )
    print(bool(a == b) )

predicat(0,0,0)
predicat(0,1,0)
predicat(0,0,1)
predicat(0,1,1)
predicat(1,1,1)
predicat(1,1,0)
predicat(1,0,0)
predicat(1,0,1)

# Искал решение (изучал Python без доступа к Интернету)

# print(type(y) , bool(y)) #<class 'int'> False
# print ( bool(not x) ) # True
# print(not (x) or not (y)) # True

# print( not( x or y or z ) )
# print( not(x) and not(y) and not(z) )

# print( bool( not( x or y or z )  ) == bool( not(x) and not(y) and not(z) ) )
# print( (not (x or y or z)) == (not (x) and not (y) and not (z)))
