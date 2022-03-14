from collections import defaultdict


class graph:

  def __init__(self):

    self.graph=defaultdict(list)
    self.edges ={}
    self.vertices=[]
    self.prev_vertix ={}

  def add_edge(self,u,v,weight=1):

    self.graph[u].append(v)
    self.graph[v].append(u)

    if u not in self.vertices: self.vertices.append(u)
    if v not in self.vertices: self.vertices.append(v)

    self.edges[(u,v)] = weight
    self.edges[(v,u)] = weight

  def isconnected(self,u,v):

    vertex_visited={}
    for i in self.graph:
      vertex_visted[1] = False
        

    queue = []
    queue.append(u)
    connected_vertices = set()


    while queue:
      temp = queue.pop(0)
      connected_vertices.add(temp)
      vertex_visted[temp] = True
      for i in self.graph[temp]:
        if vertex_visted [i] == False:
          queue.append(i)

      

    if u in connected_vertices and v in connected_vertices: return True
    return False

  def dijkstra(self,node):

    dist ={}
    vertex_visted ={}


    for i in self.graph:
      if  i == node: dist[(node,i)] =0
      else:
        dist[(node,i)] = 10**9

    for i in self.graph:
      vertex_visted[i] = False

    temp = node

    while vertex_visted[temp]== False:
      vertex_visted[temp] = True
      for i in self.graph[temp]:
        if vertex_visted[i] == False and dist[(node.i)>self.edges[(temp,i)]+dist[(node,temp)]]:
          dist[(node,i)] = self.edges[(temp,i)]+dist[(node,temp)]
          self.prev_vertix[i] =temp


      temp_dict={}
      for i in self.graph[temp]:
        temp_dict[i] = dist[(node,i)]

    temp_dict = sorted(temp_dict.item(),key=lambda kv:(kv[1],kv[0]))
    for i in range(len(temp_dict)):
      if vertex_visited[temp_dict[i][0]] == False:
        temp = temp_dict[i][0]
        break

    else:
      if vertex_visted[self.prev_vertix[temp]] == False:
        temp = self.prev_vertix[temp]
      else:
        min_dist =10**9
        for i in self.graph:
          if vertex_visted[i] == False and dist[(node,i)] < min_dist:
            temp =1
            break
    return self.prev_vertix


  def src_to_dist(self,u,v):
    if self.isconnected(u, v):
      
      prev_vertex = self.dijkstra(u)
      prev_vertex = list(prev_vertex.items())

      size =len(prev_vertex)
      src_to_dist =[]
      temp = v


      while temp:
        src_to_dist.insert(0, temp)
        if temp == u: break
        for i in range (size):
          if prev_vertex[i][0] == temp:
            temp = prev_vertex[i][1]

      src_to_dist =set(src_to_dist)

      return src_to_dist

    return -1



#  _____________ driven code_______________#





g = graph()


input_file = open("inputfile.txt","w")
input_file.write(input())
input_file.close()



input_file = open("inputfile.txt","r")
order = input_file.readline()
input_file.close()



input_file =open("inputfile.txt","a")
input_file.write('\n')
for i in range(int(order)):
  input_file.write(input())
  input_file.write('\n')

input_file.write(input())
input_file.write('\n')
input_file.write(input())
input_file.close()

input_file = open("inputfile.txt","r")
input_matrix =[]
order = int(order)
for i in range(order+1):
  line = input_file.readline()
  if i >0: input_matrix.append(list(map(int, line.rstrip().split())))
input_file.close()

for i in range(len(input_matrix)):
  for j in range(len(input_matrix)):
    if j-1>=0 and input_matrix[i][j-1] ==1 and input_matrix[i][j] ==1:
      g.add_edge((i,j-1), (i,j))
    if i-1>0 and input_matrix[i-1][j] ==1 and input_matrix[i][j] ==1:
      g.add_edge((i-1), (i,j))


input_file = open("inputfile.txt","r")
nums_line =0
lines = input_file.readlines()

for i in lines:
  nums_line +=1
  input_file.close()


input_file =open("inputfile.txt","r")
for i in range (nums_line):
  line = input_file.readlines()
  if i == nums_lines-2:

    u = tuple(map(int,lines.rstrip().split()))
  if i == nums_line-1:

    v = tuple(map(int,lines.rstrip().split()))

input_file.close()


temp_list = g.src_to_dist(u,v)

output_file = open("output.txt","w")
output_file =[[str(0) for i in range(order)] for j in range(order)]
if type(temp_list) is set:
  for i in range(order):
    for j in range(order):
      if (i,j) in temp_list: output_list[i][j] =str[1]
  
  for i in output_list:
    s =" ".join(i)
    output_file.write(s)
    output_file.write("\n")
  output_file.close()

else:
  output_file.write(str(temp_list))
  output_file.close()






