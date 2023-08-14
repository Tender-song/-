from check_malicious_ip import check_malicious_ip
from into_excel import json_to_excel
from datetime import datetime
import pandas as pd
from ip_split import split_ip_address
import os


def main():
    # 指定路径下创建Excel文件
    output_file = "C:/path"  # 指定文件路径

    # 检查文件是否存在
    if not os.path.exists(output_file):
        # 创建一个空的DataFrame
        data = pd.DataFrame()

        # 保存到桌面，文件名为test.xlsx
        data.to_excel(output_file, index=False)

        print("已创建新的Excel表格：", output_file)

    # 运行前需关闭已有Excel表格
    print("\n请检查是否已经关闭对应excel表格!\n")

    # 用户输入要查询的IP地址
    ip_address = input("请输入要查询的IP地址：")

    # 对ip进行检查，清除白名单内的ip
    formatted_ips = split_ip_address(ip_address)

    # 使用模块中的函数进行查询
    result = check_malicious_ip(formatted_ips)

    # 假设你有以上JSON数据
    data = result

    # 读取Excel文件
    template_file = "C:/path/example.xlsx"
    existing_data_df = pd.read_excel(template_file, sheet_name="Sheet1", index_col="IP地址")

    # 调用函数将JSON数据转换为DataFrame，并将IP地址作为索引
    new_data_df = json_to_excel(data)

    # 新增一个以添加时间为准的索引列
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data_df["添加时间"] = now

    # 合并现有数据和新的数据，并保留现有索引列中的时间
    merged_df = pd.concat([existing_data_df, new_data_df])

    # 输出合并后的DataFrame到Excel文件
    output_file = "C:/path/example.xlsx"
    merged_df.to_excel(output_file, index=True, index_label="IP地址")

    excel_file_path = "C:/path/example.xlsx"

    os.startfile(excel_file_path)


if __name__ == "__main__":
    main()
