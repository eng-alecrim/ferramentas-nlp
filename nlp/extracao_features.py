# =============================================================================
# BIBLIOTECAS E MÓDULOS
# =============================================================================

from pathlib import Path
from typing import Dict, Iterable, List, Optional

import numpy as np
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from spacy.lang.en.stop_words import STOP_WORDS as STOP_WORDS_EN
from spacy.lang.es.stop_words import STOP_WORDS as STOP_WORDS_ES
from spacy.lang.pt.stop_words import STOP_WORDS as STOP_WORDS_PT

from .utils import get_path_projeto

# =============================================================================
# CONSTANTES
# =============================================================================

DIRETORIO_PROJETO = get_path_projeto()
assert isinstance(DIRETORIO_PROJETO, Path)
DIRETORIO_DADOS = DIRETORIO_PROJETO / "data"

# -----------------------------------------------------------------------------
# Modelos de linguagem
# -----------------------------------------------------------------------------

nlp_pt = spacy.load("pt_core_news_sm")
nlp_es = spacy.load("es_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

STOP_WORDS = {
    "pt": list(STOP_WORDS_PT),
    "es": list(STOP_WORDS_ES),
    "en": list(STOP_WORDS_EN),
}

# =============================================================================
# FUNÇÕES
# =============================================================================

# -----------------------------------------------------------------------------
# Extração das principais palavras
# -----------------------------------------------------------------------------


def get_contagem_palavras(
    textos: Iterable[str],
    idioma_stop_words: Optional[str] = None,
    palavras_indesejadas: List[str] = [],
    **kwargs,
) -> Dict[str, int]:
    """
    **kwargs:
    -preprocessor: callable, default=None
        - Override the preprocessing (strip_accents and lowercase)
    - strip_accents: "unicode"
    - lowercase: bool True/False
    - ngram_range: tuple(min_n, max_n), default=(1, 1)
    """

    stop_words = (
        STOP_WORDS.get(idioma_stop_words) if idioma_stop_words else None
    )
    if stop_words:
        palavras_indesejadas += stop_words
    vetorizador_contagem = CountVectorizer(
        stop_words=palavras_indesejadas, **kwargs
    )
    matriz_contagem = vetorizador_contagem.fit_transform(textos).toarray()
    palavras = vetorizador_contagem.get_feature_names_out()
    contagem_palavras = np.sum(matriz_contagem, axis=0)

    return dict(zip(palavras, contagem_palavras))


# -----------------------------------------------------------------------------
# Extração das principais palavras de uma coluna textual de um dataframe
# -----------------------------------------------------------------------------


def get_contagem_palavras_dataframe(
    dataframe: pd.DataFrame, coluna_textos: str, **kwargs
) -> Dict[str, int]:
    """
    **kwargs:
    - idioma_stop_words: Optional[str] = None,
    - palavras_indesejadas: List[str] = [],
    - preprocessor: callable, default=None
        - Override the preprocessing (strip_accents and lowercase)
    - strip_accents: "unicode"
    - lowercase: bool True/False
    - ngram_range: tuple(min_n, max_n), default=(1, 1)
    """
    return get_contagem_palavras(
        dataframe.loc[:, coluna_textos].values, **kwargs
    )
