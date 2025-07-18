						Welcome to the Scanner PLC README file!    

Scanner PLC v1.0
=============

Scanner simples para detectar e coletar informações básicas de CPUs de PLC Siemens S7 em uma rede, testando diferentes racks e slots.

Compatível com qualquer distro Linux.

![descrição](/scanner_plc.png)  

Instalação
-----------

Atualize sua distro:
 
    $ sudo pacman -Syyu

Baixe o repositório e crie um ambiente virtual:

    $ git clone https://github.com/whoami-a51/scanner_plc.git
    $ python3 -m venv venv
    $ source venv/bin/activate
  
Uso:

    $ cd scanner_plc/
    $ python3 scanner_plc.py

Desinstalação
--------------

    $ deactivate
    $ cd .. && sudo rm -rf scanner_plc venv 


Como ele funciona
-----------

- Varre racks de 0 a 5 e slots de 0 a 5
- Tenta se conectar a cada combinação no PLC no IP especificado
- Se conectar, coleta e exibe informações do CPU, como:
  - Tipo do módulo
  - Número serial
  - Nome do sistema (AS Name)
  - Copyright
- Exibe mensagens indicando sucesso, falha ou erros na conexão

## Exemplo de saída

```
[OK] Conectado com rack=0, slot=2
Informações do CPU:
  Module Type Name: CPU 315-2 PN/DP
  Serial Number: XYZ12345678
  AS Name: PLC1
  Copyright: Siemens AG
[FAIL] Não conectado rack=0, slot=3
[ERRO] rack=1, slot=0: Connection timed out
```

---

## Requisitos

- Python 3.x
- Biblioteca `python-snap7`


---

## Aviso

Use este script apenas em redes e dispositivos que você tem autorização para acessar.

---
