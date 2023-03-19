# python3
# Daniels Raivo Ivanovs 211RMB021 15.grupa
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)
    
    
    for i in range (m):
        t, thread = heapq.heappop(threads)
        output.append((thread, t))
        heapq.heappush = (threads, (t + data[i], thread))
    return output

def main():
    n,m = map(int, input().split())
    assert 1 <= n <= 10**5
    assert 1 <= m <= 10**5
    data = list(map(int,input().split()))
    assert len(data) == m
    assert all(0 <= t <= 10**9 for t in data)
    
    result = parallel_processing(n, m, data)
    
    for thread, t in result:
        print(thread, t)
           
if __name__ == "__main__":
    main()
