import code_example
import pytest
import mock


@pytest.mark.parametrize(
    "mocked_cond, mocked_loop_count",
    [
        pytest.param(True, 3, id="True with 3"),
        pytest.param(False, 3, id="False with 3"),
    ],
)
def test_simple_example(mocker, mocked_cond, mocked_loop_count):
    """Testing the simple example function"""
    import pudb

    pudb.set_trace()  # fmt: skip

    mocked_number_of_runs = mocker.patch.object(
        code_example, "number_of_runs", return_value=mocked_loop_count
    )
    mocked_print_hello_world = mocker.patch.object(code_example, "print_hello_world")

    code_example.simple_example(mocked_cond)

    mocked_number_of_runs.assert_called_with(mocked_cond)
    mocked_print_hello_world.assert_called_with(mocked_loop_count)
    assert mocked_number_of_runs.call_count == 1
