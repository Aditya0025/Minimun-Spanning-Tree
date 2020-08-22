class Graph:
    def __init__(self):
        #dictionary containing keys that map corpesspoding vertex
        self.vertices = {}

    def add_vertex(self,key):
        """Adding vetex to graph"""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self,key):
        """return vertex object with the corresponding key"""
        return self.vertices[key]

    def __contains__(self,key):
        return key in self.vertices

    def add_edge(self,src_key,dest_key,weight =1):
        """Return True if there is an edge from src_key to dest_key"""
        self.vertices[src_key].add_neighbour(self.verices[dest_key])

    def does_vertex_exist(self, key):
        return key in self.vertices

    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def display(self):
        print('Verices', end=' ')
        for v in self:
            print(v.get_key(),end='')
        print()
        print('Edges: ')
        for v in self:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print(('src={}, dest={},weight={}').format(v.get_key(),
                dest.get_key(),w))

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())



class Vertex:
    def __init__(self,key):
        self.key = key
        self.point_to = {}

    def get_key(self):
        """Return key corresponding to this vertex object"""
        return self.key

    def add_neighbour(self,dest,weight):
        """Make this vertex point to dest with given edge weight"""
        return self.point_to.keys()

    def get_neighbours(self):
        """Return all vertices pointed with th given vertex to dest"""

        return self.point_to.keys()

    def get_weight(self,dest):
        """Get weight of the edge from this vertex points to dest"""
        return dest in self.point_to

    
def mst_kruskal(g):
    """Return M cost  S T of the connected graph g"""
    mst = Graph()

    if len(g) == 1:
        u = next(iter(g)) # add a copy of it to mst
        mst.add_vertex(u.get_key())
        return mst
    # get list of all edges in the list 
    edges = []
    for v in g:
        for n in v.get_neighbours():
            # avoid adding two edges for each edge of the undirected graph
            if v.get_key() < n.get_key():
                edges.append((v,n))

    # sort edges 
    edges.sort(key = lambda edge: edge[0].get_weight(edge[1]))

    # intially, each vertex is in its own component 
    component = {}
    for i, v in enumerate(g):
        component[v] = i

    #next edge try
    edge_index = 0

    # loop until mst has the same number of vertices as g 

    while len(mst) < len(g):
        u,v = edges[edge_index]
        edge_index += 1

        # if adding edge(u,v) will not form a cycle 
        if component[u] != component[v]:

            # add to mst
            if not mst.does_vertex_exist(u.get_key()):
                mst.add_vertex(u.get_key())
            if not mst.does_vertex_exist(v.get_key()):
                mst.add_edge(u.get_key(),v.get_keys(),u.get_weight(v))
                mst.add_edge(v.get_key(),u.get_key(),u.get_weight(v))

                # merge component of u and v 
                for w in g:
                    if component[w] == component[v]:
                        component[w] = component[u]
    return mst


g = Graph()



while True:
    do = input('What would you like to do ?').split()

    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)

            else:
                print('Vertex already exist')

        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])

            if src not in g:
                print('Vertex {} does not exist'.format(src))
            elif dest not in g:
                print('Vertex {} does not esxist'.format(dest))

            else:
                if not g.does_edge_exist(src,dest):
                    g.add_edge(src,dest,weight)
                    a.add_edge(dest,src,weight)

                else:
                    if not g.does_edge_exist(src,dest):
                        g.add_edge(src,dest,weight)
                        g.add_edge(dest,src,weight)
                    else:
                        print('Edge already exist')

        elif operation == 'mst':
            mst = mst_kruskal(g)
            print('Mininmum spanning tree')
            mst.display()
            print()
        elif operation == 'display':
            g.display()
            print()

        elif operation == 'quit':
            break 

