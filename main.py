# python3
# Daniels Raivo Ivanovs 211RMB021 15.grupa
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)
    
    
    for i in range(m):
        time, index = heapq.heappop(threads)
        output.append((index, time))
        heapq.heappush(threads, (time + data[i], index))
        
    return output

def main():
  
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    assert 1 <= n <= 10**5
    assert 1 <= m <= 10**5
    assert len(data) == m
    assert all(0 <= ti <= 10**9 for ti in data)

    result = parallel_processing(n, m, data)

    for index, starting_time in result:
        print(index, starting_time)

if __name__ == "__main__":
    main()
