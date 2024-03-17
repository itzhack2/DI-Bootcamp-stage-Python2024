#Function

# def say_hello():
#     print(f'{username1} ,hello there!')

# username1 ='Daniel'
# say_hello()



# def say_hello_language(username:str, language:str):
#     "print a massage to the username in the specified language"
#     if language =='EN':
#         print(f'{username},hello there!')
#     elif language == 'PT':
#         print(f'{username}')
#     elif language == :
#          print(f'{username}')
#     elif language == :
#         print(f'{username}')   
#     elif language == :
#         print(f'{username}')
#     elif language == :
#         print(f'{username}')

# scope
#global conut
count= 100
def calculation(a,b):
    #local scope
    global count 
    result = a+b
    count += result
    return count
print(calculation(5,12))
print(count)



#passing list as arguments



def selector_heat(names:list):
    for name in names:
        if name == "luna":
            print(f'welcome to home,{name}')
        else:
            print(f'welcome to Hogwarts,{name}')
studnet = [ 'Harry','Hermione','Ron','luna']    
selector_heat(studnet)



matrix 

list_2d = [['7','i','i'],
           ['i','i','i'],
           ['','','']]