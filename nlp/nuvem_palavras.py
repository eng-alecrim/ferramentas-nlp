# =============================================================================
# BIBLIOTECAS E MÓDULOS
# =============================================================================

from pathlib import Path
from typing import Dict
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import os

# =============================================================================
# CONSTANTES
# =============================================================================

DIRETORIO_ATUAL = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
DIRETORIO_PROJETO = Path(DIRETORIO_ATUAL).parent
DIRETORIO_DADOS = DIRETORIO_PROJETO / "data"
DIRETORIO_NUVEM_PALAVRAS = DIRETORIO_DADOS / "nuvens_palavras"
DIRETORIO_NUVEM_PALAVRAS.mkdir(exist_ok=True, parents=True)

# =============================================================================
# FUNÇÕES
# =============================================================================

# -----------------------------------------------------------------------------
# Função que gera uma nuvem de palavras e salva em data/nuvens_palavras
# -----------------------------------------------------------------------------


def gera_nuvem(
    frequencia_palavras: Dict[str, int],
    numero_palavras: int = 10,
    nome_img: str = "nuvem",
) -> None:

    wordcloud = WordCloud(
        max_font_size=100,
        max_words=numero_palavras,
        background_color="white",
        width=800,
        height=400,
    ).generate_from_frequencies(frequencies=frequencia_palavras)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(DIRETORIO_NUVEM_PALAVRAS / f"{nome_img}.png", dpi=500)
    plt.show()

    return None
