import glob


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
