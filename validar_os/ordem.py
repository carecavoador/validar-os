from dataclasses import dataclass


@dataclass
class OrdemDeServico:
    num_os: int
    num_pedido: int
    versao: int
    cliente: str
    nome: str
    perfil: str
    oc: str
    fechamento: float
    pistas: int
    repeticoes: int
    passo: float
    passo_horiz: float
    camada: str
    espessura: float
