#scanner_plc.py by whoami-a51 (whoami.a51@protonmail.com)

import snap7

#IP do PLC via terminal
ip = input("PLC alvo: ").strip()

client = snap7.client.Client()

for rack in range(6):   # racks de 0 a 5
    for slot in range(6):  # slots de 0 a 5
        try:
            client.connect(ip, rack, slot)
            if client.get_connected():
                print(f'[OK] Conectado com rack={rack}, slot={slot}')
                info = client.get_cpu_info()
                print("Informações do CPU:")
                print(f"  Module Type Name: {getattr(info, 'ModuleTypeName', 'N/A')}")
                print(f"  Serial Number: {getattr(info, 'SerialNumber', 'N/A')}")
                print(f"  AS Name: {getattr(info, 'ASName', 'N/A')}")
                print(f"  Copyright: {getattr(info, 'Copyright', 'N/A')}")
                client.disconnect()
            else:
                print(f'[FAIL] Não conectado rack={rack}, slot={slot}')
        except Exception as e:
            print(f'[ERRO] rack={rack}, slot={slot}: {e}')
