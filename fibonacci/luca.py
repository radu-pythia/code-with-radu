def fibonacci(N):
    series = [1, 1,]
    if N <= 2:
        return series[N-1]
    else:
        for i in range(1, N):
            n = series[i] + series[i-1]
            #print(n)
            series.append(n)
        return series[N-1]
    

#fibonacci(6)

print(fibonacci(100))
