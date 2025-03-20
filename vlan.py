from netmiko import ConnectHandler

# Cấu hình kết nối đến Switch
SW9 = {
    'device_type': 'cisco_ios',  # Sửa thành 'cisco_ios' nếu là switch Cisco
    'ip': '10.215.27.89',
    'username': 'vnpro',
    'password': 'vnpro#123',
    'secret': 'vnpro#321',
}

# Kết nối SSH
net_connect = ConnectHandler(**SW9)
net_connect.enable()  # Vào chế độ enable

# Vòng lặp tạo VLAN và gán IP cho từng VLAN
for n in range(10, 31):  # VLAN từ 10 đến 30
    config_commands = [
        f'vlan {n}',
        f'interface vlan {n}',
        f'ip address 172.16.{n}.1 255.255.255.0',
        'no shutdown'
    ]
    net_connect.send_config_set(config_commands)
net_connect
# Đóng kết nối
net_connect.disconnect()

print("Cấu hình VLAN và IP hoàn tất.")
