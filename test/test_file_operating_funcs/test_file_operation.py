from src.file_operation.file_operating_funcs import list_all_files


def test_list_all_files() -> None:
    assert type(list_all_files("D://")) is list
