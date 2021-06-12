from src.file_operation.file_operating_funcs import list_all_files, list_files_by_extension
import os
import tempfile
import filecmp


def test_list_all_files() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        # ディレクトリ名に末尾のスラッシュを追加
        tmp_dir = os.path.join(tmp_dir, "")
        # サブディレクトリ作成
        sub_dir: str = os.path.join(tmp_dir, "sub_dir") 
        os.mkdir(sub_dir)
        # 一時ファイル作成
        tmp_file: str = os.path.join(sub_dir, "tmp_file")
        open(tmp_file, mode="w")

        # 対象メソッドの実行
        result_list: list[str] = list_all_files(tmp_dir)

        # assertion
        assert len(result_list) == 3
        # ディレクトリ名は、末尾にスラッシュを付与した状態で比較
        assert filecmp.dircmp(os.path.join(result_list[0], ""), os.path.join(tmp_dir, ""))
        assert filecmp.dircmp(os.path.join(result_list[1], ""), os.path.join(sub_dir, ""))
        # ファイル名の比較
        assert filecmp.cmp(result_list[2], tmp_file)

def test_list_files_by_extension() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        # ディレクトリ名に末尾のスラッシュを追加
        tmp_dir = os.path.join(tmp_dir, "")
        # サブディレクトリ作成
        sub_dir: str = os.path.join(tmp_dir, "sub_dir") 
        os.mkdir(sub_dir)
        # 一時ファイル作成
        tmp_file1: str = os.path.join(sub_dir, "tmp_file")
        tmp_file2: str = os.path.join(sub_dir, "tmp_file.txt")
        tmp_file3: str = os.path.join(sub_dir, "tmp_file.md")
        open(tmp_file1, mode="w")
        open(tmp_file2, mode="w")
        open(tmp_file3, mode="w")

        # 対象メソッドの実行
        result_list: list[str] = list_files_by_extension(tmp_dir, ".txt")
        print(result_list)

        # assertion
        assert len(result_list) == 1
        # ファイル名の比較
        assert filecmp.cmp(result_list[0], tmp_file2)
        