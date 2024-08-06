# =============================================================================
# BIBLIOTECAS E FUNÇÕES
# =============================================================================

import os
from pathlib import Path
from typing import Callable, Union

from dotenv import find_dotenv, load_dotenv

# =============================================================================
# CONSTANTES
# =============================================================================

# -----------------------------------------------------------------------------
# Retorna o path da raiz do projeto
# -----------------------------------------------------------------------------

load_dotenv(find_dotenv())
NOME_PROJETO = os.getenv("NOME_PROJETO")
assert NOME_PROJETO is not None


def get_path_projeto(
    dir_atual: Path = Path.cwd(), nome_projeto: str = NOME_PROJETO
) -> Union[Callable, Path]:
    if dir_atual.name == nome_projeto:
        return dir_atual

    return get_path_projeto(dir_atual.parent, nome_projeto)
