# 使用说明
《调用微步情报社区API生成IP详情的Excel表格》
调用微步情报社区API时，需在https://x.threatbook.com/v5/myApi绑定可信的访问IP。同时，在check_malicious_ip.py中填入对应的APIkey。
在使用时，需关闭代理等。每个用户单日IP信誉的查询上限为50。
可在ip_split.py中配置白名单，批量检查过程中会自动跳过白名单内容，不占用当日的API调用次数。
在Excel表格中，存在“添加时间”一列，可快速筛选出最近一次查询的IP信息。
