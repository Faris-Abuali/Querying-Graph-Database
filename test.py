from json_parser import JSONParser
from data_utils import DataUtils


def parse_json_file(file_path: str):
    return JSONParser(file_path).parse()


file_path0 = "example1.json"  # Path to your JSON file
graph0, attributes0, automaton0, global_vars0 = parse_json_file(file_path0)

file_path1 = "example4.json"  # Path to your JSON file
graph1, attributes1, automaton1, global_vars1 = parse_json_file(file_path1)
file_path2 = "example5.json"  # Path to your JSON file
graph2, attributes2, automaton2, global_vars2 = parse_json_file(file_path2)
file_path3 = "example6.json"  # Path to your JSON file
graph3, attributes3, automaton3, global_vars3 = parse_json_file(file_path3)


def test_graph_exploration():
    # print(f"{sorted(graph1.get_paths(1, 5))=}")

    assert sorted(graph1.get_paths(1, 5)) == [
        (1, 2, 3, 4, 5),
        (1, 2, 3, 5),
        (1, 2, 4, 5),
        (1, 2, 5),
        (1, 3, 4, 5),
        (1, 3, 5),
        (1, 4, 5),
        (1, 5),
    ]
    assert sorted(graph2.get_paths(1, 4)) == [(1, 2, 4)]
    assert sorted(graph3.get_paths(2, 5)) == [(2, 3, 4, 5), (2, 5)]
    print(f"test_graph_exploration: OK")


def test_naive_algorithm():
    assert not DataUtils.query_with_naive_algorithm(
        attributes0, automaton0, graph0, global_vars0, 1, 3
    )
    return
    assert DataUtils.query_with_naive_algorithm(
        attributes1, automaton1, graph1, global_vars1, 1, 5
    )
    assert not DataUtils.query_with_naive_algorithm(
        attributes1, automaton1, graph1, global_vars1, 1, 4
    )
    assert DataUtils.query_with_naive_algorithm(
        attributes1, automaton1, graph1, global_vars1, 2, 5
    )
    assert not DataUtils.query_with_naive_algorithm(
        attributes1, automaton1, graph1, global_vars1, 2, 3
    )
    assert not DataUtils.query_with_naive_algorithm(
        attributes2, automaton2, graph2, global_vars2, 2, 4
    )
    assert DataUtils.query_with_naive_algorithm(
        attributes2, automaton2, graph2, global_vars2, 2, 3
    )
    assert DataUtils.query_with_naive_algorithm(
        attributes3, automaton3, graph3, global_vars3, 4, 5
    )
    assert not DataUtils.query_with_naive_algorithm(
        attributes3, automaton3, graph3, global_vars3, 2, 5
    )
    assert not DataUtils.query_with_naive_algorithm(
        attributes3, automaton3, graph3, global_vars3, 2, 3
    )


def test_macro_state_algorithm():
    assert DataUtils.query_with_macro_state(
        attributes1, automaton1, graph1, global_vars1, 1, 5
    )
    assert not DataUtils.query_with_macro_state(
        attributes1, automaton1, graph1, global_vars1, 1, 4
    )
    assert DataUtils.query_with_macro_state(
        attributes1, automaton1, graph1, global_vars1, 2, 5
    )
    assert not DataUtils.query_with_macro_state(
        attributes1, automaton1, graph1, global_vars1, 2, 3
    )
    assert not DataUtils.query_with_macro_state(
        attributes2, automaton2, graph2, global_vars2, 2, 4
    )
    assert DataUtils.query_with_macro_state(
        attributes2, automaton2, graph2, global_vars2, 2, 3
    )
    assert DataUtils.query_with_macro_state(
        attributes3, automaton3, graph3, global_vars3, 4, 5
    )
    assert not DataUtils.query_with_macro_state(
        attributes3, automaton3, graph3, global_vars3, 2, 5
    )
    assert not DataUtils.query_with_macro_state(
        attributes3, automaton3, graph3, global_vars3, 2, 3
    )

if __name__ == "__main__":
    test_graph_exploration()
    test_naive_algorithm()