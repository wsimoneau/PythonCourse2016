"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# TODO: define a function countEdges



def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

n = 16
for i in range(1,16):
	for z in range(1,16):
	#if G % 16 == 0
	G = makeLink(ring,i,i+1)
	G = makeLink(ring,i,n+i)
	G = makeLink(ring,(1 * n) +i,(1 * n)+i+1)
	G = makeLink(ring,(1 * n)+i,(2 * n)+i)
	G = makeLink(ring,(2 * n)+i,(2 * n)+i+1)
	G = makeLink(ring,(2 * n)+i,(3 * n)+i)
	G = makeLink(ring,(3 * n)+i,(3 * n)+i+1)
	G = makeLink(ring,(3 * n)+i,(4 * n)+i)
	G = makeLink(ring, (4 * n)+i, (4 * n)+i+1)
	G = makeLink(ring, (4 * n)+i, (5 * n)+i)
	G = makeLink(ring, (5 * n)+i, (5 * n)+i+1)
	G = makeLink(ring, (5 * n)+i, (6 * n)+i)
	G = makeLink(ring, (6 * n)+i, (6 * n)+i+1)
	G = makeLink(ring, (6 * n)+i, (7 * n)+i)
	G = makeLink(ring, (7 * n)+i, (7 * n)+i+1)
	G = makeLink(ring, (7 * n)+i, (8 * n)+i)
	G = makeLink(ring, (8 * n)+i, (8 * n)+i+1)
	G = makeLink(ring, (8 * n)+i, (9 * n)+i)
	G = makeLink(ring, (9 * n)+i, (9 * n)+i+1)
	G = makeLink(ring, (10 * n)+i, (10 * n)+i)


def make_square(n):
	square = {}
	`for i in range(1,n ** 2):
		if i%n !=0:
		makeLink(square,i,i+1)
	if (i-1)/n<n-1:
		makeLink(square,i,i+n)
	return square



def count_edges(graph):
	return reduce((lambda x, y : x + y), map
(len, graph.values()))/2

print "There are %d edges in the square"%
count_edges(square)




# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hdhoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
# How many edges in movies?

def tour(graph, nodes):
  for i in range(len(nodes)):
    node = nodes[i] 
    if node in graph.keys():
      print node 
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 



actors2 = [jr, ah, ms, rd, dh, ss, kb] 


# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [] 
def tour(graph, actors):
  for i in range(len(actors)): 
  	actor = actors[i]
  	if actor in graph.keys():
  		print actor
  	else:
  		print "Actor not found!"
  		break
  	if i+1 < len(actors):
  		next_actor = actors[i+1]
  		if next_actor in graph.keys():
  			if next_actor in graph[actor].keys():
  				pass
  			else:
  				print "Can't get there from here!"
  				break
    
    
   


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = findPath(graph, node, end, path)
                if newpath: test_path.append(newpath)
        for actor in test_path:
        	newpath = findPath(graph, actor, end, path)
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()
# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes
# allPaths = findAllPaths(movies, jr, ms)
# for path in allPaths:
#   print path

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.