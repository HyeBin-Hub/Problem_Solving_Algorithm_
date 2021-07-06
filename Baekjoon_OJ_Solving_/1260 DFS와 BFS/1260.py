from collections import deque    

def DFS(node,visit):
    print(node,end=" ")
    visit.append(node)

    for next_node in sorted(connections[node]):
        if next_node not in visit:
            DFS(next_node,visit)
def BFS():
    queue=deque([V])
    visit=[0]*(n+1)
    visit[V]=1
    while queue: 
        node=queue.popleft()
        print(node,end=" ")
        for next_node in sorted(connections[node]):
            if not visit[next_node]:
                queue.append(next_node)
                visit[next_node]=1
n,m,V=map(int,input().split())
connections={node:set() for node in range(1,n+1)}
for _ in range(m):
    A,B=map(int,input().split())
    connections[A].add(B)
    connections[B].add(A)
DFS(V,[])
print()
BFS()