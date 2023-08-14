import pandas as pd


def json_to_excel(data):
    # 解析JSON数据为DataFrame
    df = pd.DataFrame.from_dict(data["data"], orient="index")

    # 重新命名列名
    column_mapping = {
        "severity": "severity",
        "judgments": "judgments",
        "tags_classes": "tags_classes",
        "basic": "basic",
        "carrier": "carrier",
        "location": "location",
        "asn": "asn",
        "scene": "scene",
        "confidence_level": "confidence_level",
        "is_malicious": "is_malicious",
        "update_time": "update_time"
    }

    df.rename(columns=column_mapping, inplace=True)

    return df
