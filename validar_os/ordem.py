from dataclasses import dataclass, field


@dataclass
class OrdemDeServico:
    num_os: int = field(default=None)
    num_pedido: int = field(default=None)
    versao: int = field(default=None)
    cliente: str = field(default=None)
    nome: str = field(default=None)
    perfil: str = field(default=None)
    oc: str = field(default=None)
    fechamento: float = field(default=None)
    pistas: int = field(default=None)
    repeticoes: int = field(default=None)
    passo: float = field(default=None)
    passo_horiz: float = field(default=None)
    camada: str = field(default=None)
    espessura: float = field(default=None)
    cod_barras: str = field(default=None)


if __name__ == '__main__':
    pass
