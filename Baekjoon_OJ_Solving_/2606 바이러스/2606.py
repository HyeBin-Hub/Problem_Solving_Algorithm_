n=int(input())
m=int(input())
con={node:set() for node in range(1,n+1)}

for i in range(m):
    a,b=map(int,input().split())
    con[a].add(b)
    con[b].add(a)

# 깊이 우선 탐색
def DFS(start_node,visited):
    visited.append(start_node)
    for node in con[start_node]:
        if node not in visited:
            DFS(node,visited)
    return visited

print(len(DFS(1,[]))-1)
    
