# python3
# Daniels Raivo Ivanovs 211RMB021 15.grupa
def parallel_processing(n, m, data):
    output = []
    thread = [(0,i) for i in range(n)]
    thread.sort()
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    
    for i in range (m):
        index, time = thread[0]
        output.append((index,time))
        thread[0] = (time + data[i], index)
        thread.sort()

    return output

def main():
    n,m = map(int, input().split())
    
    if not 1 <= n <= 10**5:
        pass
    elif not 1 <=m <= 10**5:
        pass
    else:
        
        data = list(map(int,input().split()))
        if len(data) !=m:
            pass
        elif not all (0 <= ti<=10**9 for ti in data):
            pass
        else:
            result = paralle_processing(n, m, data)
            
            for index, start_time in result:
                print(index, start_time)
            


if __name__ == "__main__":
    main()
