# python3
# Daniels Raivo Ivanovs 211RMB021 15.grupa
import heapq

def parallel_processing(n, m, data):
    output = []
    thread = [(0,i) for i in range(n)]
    heapq.heapify(thread)
    
    
    for i in range (m):
        time, thread = heapq.heappop(thread)
        output.append((thread, time))
        heapq.heappush = (thread, (time + data[i], thread))
    return output

def main():
    n,m = map(int, input().split())
    assert 1 <= n <= 10**5,
    assert 1 <= m <= 10**5,
    data = list(map(int,input().split()))
    assert len(data) == m,
    assert all(0 <= t <= 10**9 for t in data),
    
    result = parallel_processing(n, m, data)
    
    for thread, time in result:
        print(thread, time)
    

            


if __name__ == "__main__":
    main()
