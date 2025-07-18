# PLC Scanner - snap7

Scanner simples para detectar e coletar informações básicas de CPUs de PLC Siemens S7 em uma rede, testando diferentes racks e slots.

---

## Sobre

Este script em Python utiliza a biblioteca [snap7](https://github.com/gijzelaerr/python-snap7) para se conectar a PLCs Siemens S7, tentando várias combinações de rack e slot para identificar dispositivos ativos e obter informações do CPU.

---

## Como usar

1. Instale a biblioteca snap7, se ainda não tiver:

```bash
pip install python-snap7
```

2. Configure o IP do PLC alvo no arquivo `scanner_plc.py`:

```python
ip = 'xx.xxx.xxx.xxx'  # Substitua pelo IP do PLC que deseja escanear
```

3. Execute o script:

```bash
python scanner_plc.py
```

---

## O que o script faz?

- Varre racks de 0 a 5 e slots de 0 a 5
- Tenta se conectar a cada combinação no PLC no IP especificado
- Se conectar, coleta e exibe informações do CPU, como:
  - Tipo do módulo
  - Número serial
  - Nome do sistema (AS Name)
  - Copyright
- Exibe mensagens indicando sucesso, falha ou erros na conexão

---

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

## Contato

Quem fez: whoami-a51  
Email: whoami.a51@protonmail.com

---

## Aviso

Use este script apenas em redes e dispositivos que você tem autorização para acessar.

---

Já é, qualquer coisa só chamar! Não fode.
