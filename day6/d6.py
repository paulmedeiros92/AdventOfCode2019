class Node:
  def __init__(self, parent):
    self.parent = parent
    self.parents = []
    self.children = []

f = open("day6/input.txt", "r")
inputs = f.read().split("\n")  # no empty space at the end of input file
nodes = { 'COM': Node('NONE') }
count = 0

def findParents(node, parents):
  if node.parent != 'NONE' and node.parent in nodes.keys(): # hides the orphan problem
    parents.append(node.parent)
    findParents(nodes[node.parent], parents)
  return parents

def shortestPath(sParents, dParents):
  s = [ parent for parent in sParents if parent not in dParents ]
  d = [ parent for parent in dParents if parent not in sParents ]
  s.extend(d)
  return len(s)


def countOrbits(orbits, children, level, count):
  for child in children:
    count += level
    if child in orbits:
      count = countOrbits(orbits, orbits[child].children, level + 1, count)
  return count

for x in inputs:
  parent, child = x.split(')')
  if parent in nodes:
    nodes[parent].children.append(child)
  if child not in nodes:
    nodes[child] = Node(parent)

for node in nodes.values():
  if node.parent != 'NONE' and node.parent in nodes.keys():
    node.parents = findParents(nodes[node.parent], [ node.parent ]) # hides the orphan problem

print(countOrbits(nodes, nodes['COM'].children, 1, 0))
print(shortestPath(nodes['YOU'].parents, nodes['SAN'].parents))