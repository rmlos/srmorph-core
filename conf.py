"""
Cofiguration file.
"""

import os
from os.path import expanduser
import tempfile

HOME = expanduser("~")
# Change this to your path(s): 
PATH = os.path.join(HOME, 'code', 'srmorph2')
PATH_TEXTS = os.path.join(PATH, 'data', 'texts')
PATH_PARSED = os.path.join(PATH, 'data', 'parsed')
PATH_TEMP = tempfile.gettempdir()
PATH_TMPPARSE = os.path.join(PATH, 'data', 'tempparse.txt')
PATH_SERBIAN = os.path.join(PATH, 'data', 'serbian.txt')

# Serbian hunspell data
HUNSPELL_PATH = os.path.join(PATH_TEXTS, 'hunspell-sr.txt')
# When comparing corpus with hunspell words, save the words which
# are not in hunspell into HUNSPELL_DIFF_PATH.
HUNSPELL_DIFF_PATH = os.path.join(PATH, 'data', 'hunspell-diff.txt') 

# Path to Goran Igaly's Dictionary of Croatian Languages
PATH_CROD = os.path.join(PATH, 'data', 'HR_Txt_538.txt')
# Igaly's Dictionatry uses several columns, but we need only one
# for corpus creation, so the prepared file is stored as NAME_PARSED_CRO.
NAME_PARSED_CRO = 'croatian.txt'
# If SETUSECRO is set to True, the program will convert
# Croatian words to Cyrillic and remove the ones containing
# non-Cyrillic letters. 
SETUSECRO = False

NAME_CORPUSGZ = 'srmorph-corpus.tar.gz'
PATH_EXPORT_CORPUS = os.path.join(PATH_TEMP, 'srmorph-corpus.txt')
PATH_EXPORT_README = os.path.join(PATH_TEMP, 'readme.txt')
PATH_EXPORT_TAR = os.path.join(HOME, NAME_CORPUSGZ)
PATH_DOWNLOAD_TAR = os.path.join(HOME, NAME_CORPUSGZ)
PATH_PARSE_LOG = os.path.join(PATH, 'data', 'parsing.log')
PATH_PARSE_ERRORLOG = os.path.join(PATH, 'data', 'errors-parsing.log')
PATH_TABLABELS = os.path.join(PATH, 'resource', 'labels.csv')

# Extensions to parse. All are lowercased during the indexing, so
# no need to specify other forms.
PARSE_EXTENSIONS = ('.txt',)

# Applies to web gui at http://srmorph.languagebits.com/
SETCACHEON = False
PATH_MO = r'/home/romeo/code/gui-srmorph/localize/translations'

corpus_sources = {'dict-sr': "Serbian (Cyrillic and Latin) Hunspell spelling dictionary by Goran Rakić.\nURL https://gitorious.org/dict-sr",

                  'HR.Txt':"'Rječnik hrvatskih jezika' by Goran Igaly, PhD\nURL http://www.igaly.org/rjecnik-hrvatskih-jezika/pages/.php?lang=HR",

                  'ask': \

"""
Antologija narodnih junačkih pesama  -  Đurić, Vojislav
Antologija narodnih pripovedaka  -  Đurić, Vojislav
ANTOLOGIJA NARODNIH UMOTVORINA  -  Knežević, Milivoje V.
ANTOLOGIJA NOVIJE SRPSKE LIRIKE  -  Popović, Bogdan
ANTOLOGIJA SRPSKE POEZIJE ZA DECU PREDZMAJEVSKOG PERIODA  -  Opačić, Zorana
Autobiografija  -  Nušić, Branislav
BAKONJA FRA BRNE  -  Matavulj, Simo
BASNE  -  Obradović, Dositej
Bašta sljezove boje  -  Ćopić, Branko
BELEŠKE JEDNE ANE  -  Kapor, Momo
Bespuće  -  Milićević, Vuk
BOŽJI LJUDI  -  Stanković, Borisav
DEČJA ZBIRKA PESAMA  -  Ilić, Vojislav J.
DNEVNIK JEDNOG DOBROVOLJCA  -  Todorović, Pera
DORĆOL  -  Velmar-Janković, Svetlana
DOROTEJ  -  Nenadić, Dobrilo
Doživljaji mačka Toše  -  Ćopić, Branko
DRUGA PEVANIJA  -  Jovanović, Jovan Zmaj
Dva srpska romana (studije o Seobama i Nečistoj krvi)  -  Petković, N
GAZDA MLADEN  -  Stanković, Borisav
GLASAM ZA LJUBAV  -  Olujić, Grozdana
GORSKI CAR  -  Ranković, Svetolik P.
GORSKI VIJENAC  -  Petrović, Petar Njegoš
GOSPOĐA MINISTARKA  -  Nušić, Branislav
IZ STAROG JEVANĐELJA I STARI DANI  -  Stanković, Borisav
IZABRANA DELA  -  Kočić, Petar
KORA  -  Popa, Vasko
Koreni  -  Ćosić, Dobrica
Kratka istorija srpske književnosti  -  Ivić, Pavle (sa grupom autora)
Najbolje godine i druge priče  -  Kapor, Momo
PRIPOVETKE  -  Glišić, Milovan
VEČITI MLADOŽENJA  -  Ignjatović, Jakov

URL http://www.antologijasrpskeknjizevnosti.rs/"""}

corpus_readme = """SRMORPH DATABASE README

This is a database of Serbo-Croatian words from 
<http://srmorph.languagebits.com/database>. Please check
the sources for credits.

This is an autogenerated file, and I cannot guarantee that
all entries are valid. The scripts are located at:

<https://bitbucket.org/marw/srmorph-core>  

Romeo Mlinar
mlinar [a] languagebits.com

CORPUS SOURCES

%(sources)s

PARSING LOG AND COUNT*

%(log)s

*will be zero if the sources are only packed 
--
end of autogenerated file
"""
