from icecream import ic

from ordem import OrdemDeServico


INFO_OS = {
    'num_os': 965426,
    'num_pedido': 1,
    'versao': 1,
    'cliente': 'INPLAC',
    'nome': 'Maxima - Cimento Max pronto 1 kg',
    'perfil': '6458_Inplac_GE_Maq8F03_ESXR_XPS_WSI_PE_PIG_EXT_INX_sBco_54lpc_DL',
    'oc': '0020251',
    'fechamento': 495.0,
    'pistas': 1,
    'repeticoes': 3,
    'passo': 165.0,
    'passo_horiz': 520.0,
    'camada': 'Externa',
    'espessura': 1.14
}

ordem = OrdemDeServico(**INFO_OS)
ic(ordem)
