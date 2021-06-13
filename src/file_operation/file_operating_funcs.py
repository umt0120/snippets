import glob
import re
import shutil


def list_all_files(target_directory: str) -> list[str]:
    """指定したディレクトリ以下を再帰的に検索し、全ディレクトリ、ファイルを持つリストを返す

    Args:
        target_directory (str): 対象ディレクトリ

    Returns:
        list[str]: 全ファイルのリスト
    """
    return glob.glob(target_directory + "**", recursive=True)


def list_files_by_extension(target_directory: str, extension: str) -> list[str]:
    """指定したディレクトリ以下から、特定の拡張子を持つファイルを再帰的に検索してリストにして返す

    Args:
        target_directory (str): 対象ディレクトリ
        extension (str): 拡張子（.txt, .md, ...）

    Returns:
        list[str]: 対象ファイルのリスト
    """
    return glob.glob(target_directory + "**/*" + extension, recursive=True)


def replace_string_by_regexp(
        target_directory_specified_in_glob_format: str, recursive: bool, regexp: str,
        replacing_str: str, encoding: str = "utf-8", backup: bool = True) -> bool:
    """globで検索したファイルに対し、正規表現で文字列置換を行う。

    Args:
        target_directory_specified_in_glob_format (str): 対象ディレクトリ。globの形式で指定する。
        recursive (bool): 再帰的に検索するかどうか。
        regexp (str): 置換対象を指定する正規表現。
        replacing_str (str): 置換する文字列。
        encoding (str): ファイルエンコード。Defaults to UTF-8.
        backup (bool, optional): バックアップファイルを残すかどうか。 Defaults to True.

    Returns:
        bool: 処理成否
    """
    # 対象のファイル一覧を取得
    target_files: list[str] = glob.glob(target_directory_specified_in_glob_format, recursive=recursive)

    for target_file in target_files:

        if backup:
            # バックアップファイルを作成
            backup_file = target_file + ".back"
            shutil.copy(target_file, backup_file)

        replaced_results: list[str] = []
        with open(target_file, encoding=encoding) as file:
            # 全行読み込み
            lines: list[str] = file.readlines()
    
            for line in lines:
                # 正規表現でマッチした文字列を置換
                replaced_results.append(re.sub(regexp, replacing_str, line))

        with open(target_file, mode="w", encoding=encoding) as file:
            file.writelines(replaced_results)

    return True
