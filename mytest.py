import json
import pathlib


def pytest_generate_tests(metafunc):
    row_data = pathlib.Path(metafunc.module.__file__).with_name('data.json')
    test_data = json.loads(row_data.read_text())

    arg_values = []
    arg_names = []
    id_list = []

    for scenario in test_data:
        id_list.append(scenario.get("id"))
        items = scenario.get("data").items()
        arg_names = [x[0] for x in items]
        arg_values.append([x[1] for x in items])
    metafunc.parametrize(arg_names, arg_values, ids=id_list, scope="class")


class TestSampleWithScenarios:

    def test_check_data_types(self, params, result):
        assert isinstance(params, list), "Params type is not list"
        assert isinstance(result, int), "Result is not empty"  # Adding extra assertion to an existing scenario

