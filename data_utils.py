class DataUtils:
    @staticmethod
    def merge_dicts(dict1: dict, dict2: dict):
        common_keys = set(dict1.keys()) & set(dict2.keys())
        if common_keys:
            raise ValueError(
                f"Key(s) {common_keys} are present in both dictionaries and would be overwritten"
            )

        return {**dict1, **dict2}

