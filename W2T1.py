def highestPerfSquare(n):
    x = 0
    squares = []
    if n > 0:
        xy = x**2
        while x < n :
            xy = x**2
            x += 1
            squares.append(xy)
            print(xy)
    	
    elif xy != n:
        nhps = squares[-2]
    
        print ("%s is the next highest perfect square.." % nhps)

    else:
        print ("%s is a perfect square" % xy) 

n = 26
highestPerfSquare(n)
