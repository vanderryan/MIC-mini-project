import sys
import logging
from webgme_bindings import PluginBase
from graph import Graph, Graph3D

# Setup a logger
logger = logging.getLogger('graph_theory')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class GraphTheory(PluginBase):
    def main(self):
        core = self.core
        root_node = self.root_node
        META = self.META
        active_node = self.active_node # we assume the active node is the state machine node

        visited = set()
        states = set()
        graph = {}

        # we build the most simple graph representation possible
        nodes = core.load_children(active_node)
        for node in nodes:
            if core.is_type_of(node, META['State']):
                states.add(core.get_path(node))
            if core.is_type_of(node, META['Init']):
                visited.add(core.get_path(node))
        for node in nodes:
            if core.is_type_of(node, META['Transition']):
                if core.get_pointer_path(node, 'src') in graph:
                    graph[core.get_pointer_path(node, 'src')].append(core.get_pointer_path(node, 'dst'))
                else:
                    graph[core.get_pointer_path(node, 'src')] = [core.get_pointer_path(node, 'dst')]

        g = Graph(graph)
        start = list(graph.keys())[0]
        end = list(graph.keys())[length - 2]

        self.send_notificaiton('Your graph details:')
        self.send_notificaiton('Adjacent matrix:')
        self.send_notificaiton(g.adjacency_matrix())
        self.send_notificaiton('Shortest Paths of all Paths:')
        self.send_notificaiton(g.all_pairs_shortest_paths())
        self.send_notificaiton('Graph as a list:')
        self.send_notificaiton(g.to_list())
        self.send_notificaiton('Shortest Path from node to node:')
        self.send_notificaiton(g.breadth_first_search(start, end))





