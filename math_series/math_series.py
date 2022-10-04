
def lucas(limit):
    '''This function takes an int as a limit for the array 
       length and returns the last number  of the Fibonacci numbers Starting from 2,1\n
       Takes :
       limit (int)
       returns 
       a list of numbers'''
    list = [2, 1]
    try:

        if(limit < 0):
            return "Enter a vaild number(Not a string , not below 0)"

        if limit == 0:
            return 2
        elif limit == 1:
            return 1

        for i in range(limit+1):
            if i >= 2:
                list.append(list[i-1] + list[i-2])
        return list[limit]
    except:
        return "Enter a vaild number(Not a string , not below 0)"


def Fibonacci(limit: int):
    '''This function takes an int as a limit for the array 
       length and returns he last number of the Fibonacci numbers Starting from 0,1 \n
       Takes :
       limit (int)
       returns 
       a list of numbers 

       '''
    try:
        if(limit < 0):
            return "Enter a vaild number(Not a string , not below 0)"

        list = [0, 1]

        if limit == 0:
            return 0
        elif limit == 1:
            return 1

        for i in range(limit+1):
            if i >= 2:
                list.append(list[i-1] + list[i-2])

        return list[limit]
    except:
        return "Enter a vaild number(Not a string , not below 0)"


def sum_series(limit, num1=0, num2=1):
    '''This function takes an int as a limit for the array 
       length and returns a list of the Fibonacci numbers Starting from 0,1 \n
       Takes :
       limit (Required)
       num1 : first element of the Fibonacci array(0 by default so it optional )
       num2 : second element of the Fibonacci array(1 by default optional)
       returns 
       a list of numbers along with its type 

       '''
    try:

        if(num2 < 0 or num2 < 0 or limit < 0 or type(num1) != int or type(num2) != int or type(limit) != int ):
            return "Enter a vaild number(Not a string , not below 0)"
        list = [num1, num2]
        if 1 and 0 in list:
            return Fibonacci(limit)
        elif 2 and 1 in list:
            return lucas(limit)
        else:
            for i in range(limit+1):
                if i >= 2:
                    list.append(list[i-1] + list[i-2])
            return list[limit]
    except:
        return "Enter a vaild number(Not a string , not below 0)"
    

print(sum_series(1, "hi", 2))

# if __name__  == '__main__':
