from src.file_operation.file_operating_funcs import list_all_files, list_files_by_extension, replace_string_by_regexp
import os
import tempfile
import filecmp
import re


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
        

def test_replace_string_by_regexp() -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        # ディレクトリ名に末尾のスラッシュを追加
        tmp_dir = os.path.join(tmp_dir, "")
        # サブディレクトリ作成
        sub_dir: str = os.path.join(tmp_dir, "sub_dir") 
        os.mkdir(sub_dir)
        tmp_file1: str = os.path.join(sub_dir, "tmp_file")
        tmp_file2: str = os.path.join(sub_dir, "tmp_file.txt")
        tmp_file3: str = os.path.join(sub_dir, "tmp_file.md")

        with open(tmp_file1, mode="w", encoding="utf-8") as f:
            f.write("abc123def456efg")
        with open(tmp_file2, mode="w", encoding="utf-8") as f:
            f.write("abc123def456efg")
        with open(tmp_file3, mode="w", encoding="utf-8") as f:
            f.write("abc123def456efg")
        
        result: bool = replace_string_by_regexp(
            tmp_dir + "**/*.txt", recursive=True, regexp=r"[a-z]+", replacing_str="0", encoding="utf-8", backup=True)

        # 処理成否
        assert result is True

        # バックアップファイルが存在すること
        result_list: list[str] = list_all_files(tmp_dir)
        assert len(list(filter(lambda str: re.findall(r"tmp_file.txt.back", str), result_list))) > 0

        with open(tmp_file1, mode="r", encoding="utf-8") as f:
            file_content: str = f.read()
            raw_str: list[str] = re.findall(r"abc123def456efg", file_content)
            replaced_str: list[str] = re.findall(r"012304560", file_content)
            assert "".join(map(str, raw_str)) == "abc123def456efg"
            assert len(replaced_str) == 0
                
        with open(tmp_file2, mode="r", encoding="utf-8") as f:
            file_content: str = f.read()
            raw_str: list[str] = re.findall(r"abc123def456efg", file_content)
            replaced_str: list[str] = re.findall(r"012304560", file_content)
            assert len(raw_str) == 0
            assert "".join(map(str, replaced_str)) == "012304560"

        with open(tmp_file3, mode="r", encoding="utf-8") as f:
            file_content: str = f.read()
            raw_str: list[str] = re.findall(r"abc123def456efg", file_content)
            replaced_str: list[str] = re.findall(r"012304560", file_content)
            assert "".join(map(str, raw_str)) == "abc123def456efg"
            assert len(replaced_str) == 0
