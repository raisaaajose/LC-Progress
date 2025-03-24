#1976. Number of Ways to Arrive at Destination
#Djikistra's algorithm + storing number of minimum path solutions in 'ways array'
#We only need count from source to n-1 th node
#priority queue 

import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
       
        MOD = 10**9 + 7
        ways = [0] * n
        adj=[[] for _ in range(n)]

        for (u, v, wt) in roads:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
            
        src=0
        pq=[]
        dist=[float('inf')]*n
        heapq.heappush(pq,(0,src))
        dist[src]=0
      #only one way to reach source from source
        ways[0] = 1
        
        while pq:
            distance, u =heapq.heappop(pq)

            if distance > dist[u]:
                continue
                
            for v, weight in adj[u]:
                if dist[v]>dist[u]+weight:
                    dist[v]=dist[u]+weight
                    heapq.heappush(pq,(dist[v],v))
                    ways[v] = ways[u]
                elif dist[v] == dist[u] + weight:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return (ways[n-1])
    
