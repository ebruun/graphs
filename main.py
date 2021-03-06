import networkx as nx
from src.build import (
    build_full_graph,
    build_member_subgraph,
    build_joined_subgraph,
    build_joined_subgraph2,
)


def check_list():
    pass


def calculate_sequence(K):

    print("\nCALCULATING DISASSEMBLY SEQUENCE")

    nodes = list(K.nodes)
    sequence = []

    print(nodes)

    remove = []
    # check for any start/end nodes
    for n in nodes:

        c = K.nodes[n]["color"]

        if c == "tab:green":
            print("{} is a START node".format(n))
            sequence.append(n)
            remove.append(n)
        elif c == "black":
            print("{} is a END node".format(n))
            remove.append(n)

    nodes_left = list(set(nodes) - set(remove))

    print("remaining is {}".format(nodes_left))
    print("sequence is {}".format(sequence))


if __name__ == "__main__":

    G = build_full_graph(
        folder="P2_data_in",
        filename="_full_structure.png",
        scale=1,
        draw=False,
        show=False,
    )

    remove_members = ["SP1_2", "SP1_3", "SP1_4", "EP1_6"]
    subgraphs = []
    nodes_check_support = []

    for remove_member in remove_members:
        K, n = build_member_subgraph(
            G=G,
            rm=remove_member,
            scale=1.2,
            draw=True,
            show=False,
        )

        subgraphs.append(K)
        nodes_check_support.extend(n)

    nodes_check_support = list(set(nodes_check_support))

    print(subgraphs)
    print(nodes_check_support)

    # build_joined_subgraph(
    #     G=G,
    #     K1=K1,
    #     K2=K2,
    #     remove_members=m1 + m2,
    #     nodes_check_support=n1 + n2,
    #     name=m1[0] + "_" + m2[0],
    #     scale=1.2,
    #     draw=True,
    #     show=False,
    # )

    build_joined_subgraph2(
        G=G,
        Ks=subgraphs,
        rms=remove_members,
        nodes_check_support=nodes_check_support,
        name="_test",
        scale=1.2,
        draw=True,
        show=False,
    )
