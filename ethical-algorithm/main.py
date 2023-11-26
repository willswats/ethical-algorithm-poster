# Try it on replit: https://replit.com/@willswats/Ethical-Algorithm

from math import sqrt

from graphics import Point

zones = [
    {"colour": "green", "starting_amount": 0, "building_multiplier": 2},
    {"colour": "blue", "starting_amount": 50, "building_multiplier": 4},
    {"colour": "red", "starting_amount": 100, "building_multiplier": 6},
]


def distance_between_points(p1, p2):
    distance = sqrt(
        (p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2
    )
    return distance


def check_points_equality(p1, p2):
    if p1.getX() == p2.getX() and p1.getY() == p2.getY():
        return True
    return False


class GraphEdgeSide:
    def __init__(self, colour: str, buildings_amount: int) -> None:
        self.colour = colour
        self.buildings_amount = buildings_amount


class GraphEdge:
    def __init__(
        self, graph_nodes: list[Point], edge_sides: list[GraphEdgeSide]
    ) -> None:
        self.graph_nodes = graph_nodes
        self.edge_sides = edge_sides

    def get_distance(self):
        distance = distance_between_points(
            self.graph_nodes[0], self.graph_nodes[1]
        )
        return distance

    def get_risk(self):
        colours_risk = 0
        buildings_risk = 0
        for edge_side in self.edge_sides:
            if edge_side.colour == zones[0]["colour"]:
                colours_risk += zones[0]["starting_amount"]
                buildings_risk += (
                    edge_side.buildings_amount
                    * zones[0]["building_multiplier"]
                )
            elif edge_side.colour == zones[1]["colour"]:
                colours_risk += zones[1]["starting_amount"]
                buildings_risk += (
                    edge_side.buildings_amount
                    * zones[1]["building_multiplier"]
                )
            elif edge_side.colour == zones[2]["colour"]:
                colours_risk += zones[2]["starting_amount"]
                buildings_risk += (
                    edge_side.buildings_amount
                    * zones[2]["building_multiplier"]
                )
        return colours_risk + buildings_risk

    def get_combined_distance_risk(self):
        risk = self.get_risk()
        distance = self.get_distance()
        return risk + distance


class Graph:
    def __init__(self, graph_edges: list[GraphEdge]) -> None:
        self.graph_edges = graph_edges

    def get_adjacent_nodes(self, graph_node: Point):
        adjacent_nodes = []
        for graph_edge in self.graph_edges:
            if check_points_equality(graph_node, graph_edge.graph_nodes[0]):
                adjacent_nodes.append(graph_edge.graph_nodes[1])
        return adjacent_nodes

    def get_adjacent_edges(self, graph_node: Point):
        adjacent_edges = []
        for graph_edge in self.graph_edges:
            if check_points_equality(graph_node, graph_edge.graph_nodes[0]):
                adjacent_edges.append(graph_edge)
        return adjacent_edges

    def print_all_combined_distance_risk(self):
        for graph_edge in self.graph_edges:
            print(graph_edge.get_combined_distance_risk())

    def print_all_adjacent_nodes(self, node_start: Point):
        adjacent_nodes_start = self.get_adjacent_nodes(node_start)
        adjacent_nodes_two = []
        for adjacent_nodes in adjacent_nodes_start:
            print(adjacent_nodes)
            adjacent_nodes_two.append(self.get_adjacent_nodes(adjacent_nodes))

        for adjacent_nodes in adjacent_nodes_start:
            print(self.get_adjacent_nodes(adjacent_nodes))


def main():
    graph = Graph(
        [
            GraphEdge(
                [Point(222, 256), Point(193, 206)],
                [
                    GraphEdgeSide(zones[0]["colour"], 7),
                    GraphEdgeSide(zones[2]["colour"], 1),
                ],
            ),
            GraphEdge(
                [Point(222, 256), Point(222, 206)],
                [
                    GraphEdgeSide(zones[2]["colour"], 1),
                    GraphEdgeSide(zones[2]["colour"], 1),
                ],
            ),
            GraphEdge(
                [Point(222, 256), Point(254, 206)],
                [
                    GraphEdgeSide(zones[2]["colour"], 1),
                    GraphEdgeSide(zones[0]["colour"], 5),
                ],
            ),
            GraphEdge(
                [Point(193, 206), Point(173, 152)],
                [
                    GraphEdgeSide(zones[1]["colour"], 4),
                    GraphEdgeSide(zones[2]["colour"], 2),
                ],
            ),
            GraphEdge(
                [Point(222, 206), Point(222, 152)],
                [
                    GraphEdgeSide(zones[2]["colour"], 2),
                    GraphEdgeSide(zones[2]["colour"], 4),
                ],
            ),
            GraphEdge(
                [Point(254, 206), Point(283, 152)],
                [
                    GraphEdgeSide(zones[2]["colour"], 4),
                    GraphEdgeSide(zones[1]["colour"], 1),
                ],
            ),
            GraphEdge(
                [Point(173, 152), Point(222, 152)],
                [
                    GraphEdgeSide(zones[2]["colour"], 4),
                    GraphEdgeSide(zones[2]["colour"], 2),
                ],
            ),
            GraphEdge(
                [Point(283, 152), Point(222, 152)],
                [
                    GraphEdgeSide(zones[2]["colour"], 2),
                    GraphEdgeSide(zones[2]["colour"], 4),
                ],
            ),
        ]
    )

    graph.print_all_combined_distance_risk()
    graph.print_all_adjacent_nodes(Point(222, 256))


main()
