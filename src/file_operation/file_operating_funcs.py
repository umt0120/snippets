import glob


def list_all_files(target_directory: str) -> list[str]:
    """指定したディレクトリ以下の全ファイルのリストを取得する

    Args:
        target_directory (str): 対象ディレクトリ

    Returns:
        list[str]: 全ファイルのリスト
    """
    return glob.glob(target_directory + "**", recursive=True)
