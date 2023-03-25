def bfs_modified(graph, s, t):

    visited={}
    visited[0]= [False] * graph[3]
    visited[1]= [False] * graph[3]
    visited[2]= [False] * graph[3]

    no_of_edges={}
    for i in range(graph[3]):
        no_of_edges[i]=[None,None,None]

    queue=[(s,2)]
    visited[0][s]=True
    no_of_edges[s][2]=0
    next_color={0:1,1:2,2:0}
    prev_color={0:2,1:0,2:1}
    color={0:'red',1:'yellow',2:'blue'}

    parent={}
    for i in range(graph[3]):
        parent[i]=[None,None,None]

    while len(queue) != 0:
        node=queue.pop(0)
        next=next_color[node[1]]
        for i in graph[next][node[0]]:
            if visited[next][i] == False:
                visited[next][i] = True
                queue.append((i,next))
                no_of_edges[i][next]=no_of_edges[node[0]][node[1]]+1
                parent[i][next]=node[0]
    
    #print(parent)
    path=[]

    if(no_of_edges[t][2]==None):
        print('No path exists from s with red edge and ends at t with blue edge by satisfying the rules of the maze.')

    else:

        print('\n1.Path exists from s with red edge and ends at t with blue edge by satisfying the rules of the maze.')
        print('2.minimum no.of edges required to go from s to t is: '+str(no_of_edges[t][2])+' edges')


        num=no_of_edges[t][2]
        path.append((t,None))
        temp=parent[t][2]
        temp_path=2
        num=num-1
        while(num>0):
            num=num-1
            path.append((temp,color[temp_path]))
            temp_path=prev_color[temp_path]
            temp=parent[temp][temp_path]
        path.append((s,color[0]))
        path.reverse()
        #print(path)
        print('3.The path from s to t is: ')

        for i in path[:-1]:
            print(str(i[0])+'--'+i[1]+'-->',end=' ')
        print(path[-1][0])
    return