def split_ip_address(ip_address):
    # 多个想要排除的IP地址，使用英文逗号进行分隔
    # excluded_ips = ["192.168.1.1", "192.168.2.1"]
    # 想要排除的IP地址段
    # excluded_ip_networks = ["192.168.0.0/24"]
    excluded_prefix = ("192.168.", "example")
    excluded_ips = []
    valid_ips = []

    for ip in ip_address.split(','):
        ip = ip.strip()  # 移除可能的空格
        if any(ip.startswith(prefix) for prefix in excluded_prefix):
            print("IP地址在白名单中，将被排除：", ip)
            excluded_ips.append(ip)
        if not any(ip.startswith(prefix) for prefix in excluded_prefix):
            valid_ips.append(ip)

    # 格式化输出
    formatted_ips = ','.join(valid_ips)

    return formatted_ips
