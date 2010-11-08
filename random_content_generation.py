# -*- coding: utf-8 -*-
# (C) Copyright 2010 CPS-CMS Community <http://cps-cms.org/>
# Authors:
# M.-A. Darche <ma.darche@cynode.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Utility script to create random content.

This is for developpers / testers only.
"""

import string
import re
from random import randint, sample, choice, randrange

USERNAMES = (
    "Adolphe Thiers",
    "Patrice de Mac-Mahon",
    "Jules Grévy",
    "Sadi Carnot",
    "Jean Casimir-Perier",
    "Félix Faure",
    "Émile Loubet",
    "Armand Fallières",
    "Raymond Poincaré",
    "Paul Deschanel",
    "Alexandre Millerand",
    "Gaston Doumergue",
    "Paul Doumer",
    "Albert Lebrun",
)

A_TEXT = """\
Aquariophilie d'eau douce

L'aquariophilie d'eau douce est réputée être la plus simple à gérer. Le bassin avec des poissons rouges en est l'exemple le plus simple et le plus connu.

Mais il existe des formes d'aquariophilie qui cherchent à reproduire le milieu naturel et qui sont beaucoup plus ardues à mettre en œuvre, notamment les reproductions en miniature du lac Malawi ou du lac Tanganyka.

Il est essentiel pour la survie des poissons que l'aquariophile maîtrise les paramètres de l'eau et le Cycle de l'azote. En effet, les déchets organiques (excréments des poissons, restes de nourriture etc.) se décomposent en produisant de l'ammoniac qui est hautement toxique pour les poissons. Cet ammoniaque est transformé en nitrites par une première famille de bactéries, mais les nitrites sont également hautement toxiques.

Les nitrites sont alors transformés en nitrates par une seconde famille de bactéries. Les nitrates ne sont pas toxiques à faible dose. Ces nitrates seront éliminés de l'aquarium lors des changements d'eau, ou bien consommés par les plantes qui s'y trouvent.

Afin que les populations de bactéries se constituent, il est indispensable d'attendre vingt à trente jours après la constitution de l'aquarium avant d'y mettre les premiers poissons. De même, il est indispensable de préserver ces populations de bactéries lors de l'entretien du bac.

Aquariophilie d'eau de mer

Celle-ci est réputée être plus difficile, et surtout réclame un matériel plus imposant. L'espèce la plus souvent montrée et reproduite en aquarium d'eau de mer est le poisson clown avec son anémone que l'on peut voir notamment dans le dessin animé de Walt Disney Le Monde de Némo. Les aquariums marins récifaux reproduisent les écosystèmes coralliens, alors que les bacs dits fish only se consacrent exclusivement à l'hébergement des poissons.

Comment devenir aquariophile ?

L'aquariophilie est un loisir passionnant et enrichissant, et de nombreux bienfaits découlent de cette passion. En plus d'acquérir le sens de responsabilités des enfants comme les adultes, l'aquariophilie apporte des notions pluridisciplinaires (notamment telles la biologie), des études tendent à démontrer que cet hobby contribue à diminuer le stress, ce qui explique que de nombreux centres médicaux ou maisons de repos, possèdent des aquariums.

Avant de commencer cette passion, il y a cependant des précautions à prendre.

Se renseigner avant de commencer

Sous peine de faire beaucoup d'erreurs en s'y lançant à l'aveuglette... et d'abandonner par déception.

En effet l'aquariophilie peut être un hobby très coûteux, quand on est débutant. Vous pourrez aussi remarquer qu'aucun vendeur ne répondra la même chose à la même question (ou presque). Certains sont sérieux, mais ils sont bien difficiles à distinguer des autres, au début.

Si vous avez besoin de conseils, reportez vous surtout aux livres, et aux forums de discussion aquariophiles, où les gens vous aideront à bien débuter. Petit à petit vous saurez sur quels matériels il vaut mieux mettre le prix, et sur quels autres vous pouvez faire bien des économies.

Quels poissons ?

L'aquariophilie d'eau de mer : elle nécessite des connaissances particulières, un gros investissement, et forcément un gros aquarium. Néanmoins les poissons d'eau douce sont eux aussi très beaux, et vous pourrez passer de longues heures à les regarder béatement.

Il faut bien choisir la population de poissons que vous voulez avoir : ils ont tous des besoins variés qu'il est important de respecter pour leur bonne santé. Il faut aussi veiller à associer des poissons compatibles entre eux : par exemple il vaudra mieux éviter de mettre ensemble des Archocentrus nigrofasciatus (couramment appelés nigros), qui sont des poissons très territoriaux et relativement agressifs, ou des oscars, avec de petits et calmes guppys (Poecilia reticulata) : ils ne feraient pas long feu avec les premiers.

Il faut aussi choisir la taille de l'aquarium en fonction des poissons que vous allez mettre dedans : il est d'usage de compter qu'un litre d'eau est nécessaire par cm de poisson à l'âge adulte (ce qui veut dire qu'un guppy adulte a besoin de 4 litres qui lui soient dédiés pour vivre, par exemple. Cependant, cela ne veut pas dire qu'on peut maintenir un guppy dans un volume de 4l - 60litres est un minimum pour la maintenance de ce poisson). Mais il faut aussi respecter leurs besoins « sociaux » : certains poissons vivent par couples, d'autres en bancs, d'autres en groupes de taille variable... Le non-respect des besoins de vos pensionnaires entraîne un stress, ce qui n'est pas vraiment visible, mais entraîne à la longue les maladies, car le poisson est affaibli. La règle du litre d'eau par cm de poisson est donc un premier repère, mais doit être adaptée aux autres besoins des poissons (pour des poissons comme les cichlidés par exemple il faut compter beaucoup plus d'eau par poisson). Une surpopulation du bac entraîne un surplus de pollution, donc plus de changements d'eau nécessaires.

Enfin, il faut veiller à mettre le poisson dans une qualité d'eau qui lui convienne. En effet selon la région où ils vivent, les poissons sont adaptés à vivre dans une eau dont les paramètres sont bien précis : pH, dureté... Vous avez ensuite le choix de vous servir de l'eau du robinet, ou de l'eau osmosée (une eau purifiée très peu minéralisée). L'eau osmosée s'achète en animalerie, ou se fabrique par osmoseur ; c'est donc un coût de plus : réfléchissez-y tout de suite. Vous pouvez aussi bien avoir des poissons en eau du robinet ; dans ce cas il vaut mieux tester d'abord son eau, pour savoir quels poissons s'y trouveront bien.

Les poissons d'eau douce vendus dans le commerce sont pour la plupart tropicaux : il va donc aussi leur falloir un combiné chauffant... toujours à associer à un thermomètre car leur régulation n'est pas toujours très fiable.

Si vous voulez rester en eau froide, il y a toutes sortes de poissons rouges : ils peuvent aussi être très beaux dans un aquarium planté, plutôt que dans une boule.

Il va donc falloir faire le point sur ce que vous pouvez fournir à vos futurs pensionnaires, puis les sélectionner selon ces paramètres. En général on commence par faire l'inverse, et... ça se passe mal !"""
# source: http://fr.wikipedia.org/wiki/Aquariophilie

G_TEXT = """\
Énoncés des deux théorèmes

Le premier théorème d'incomplétude peut être énoncé de la façon un peu approximative suivante.

    Dans n'importe quelle théorie récursivement axiomatisable, cohérente et capable de "formaliser l'arithmétique", on peut construire un énoncé arithmétique qui ne peut être ni prouvé ni réfuté dans cette théorie.

De tels énoncés sont dits indécidables dans cette théorie.

Toujours dans l'article de 1931, Gödel en déduit le second théorème d'incomplétude :

    Si T est une théorie cohérente qui satisfait des hypothèses analogues, la cohérence de T, qui peut s'exprimer dans la théorie T, n'est pas démontrable dans T.

Ces deux théorèmes ont été prouvés pour l'arithmétique de Peano, et donc pour les théories plus fortes que celle-ci, en particulier les théories destinées à fonder les mathématiques, telles que la théorie des ensembles, ou les Principia Mathematica...

Les conditions d'application des théorèmes

Pour fixer les idées, on considère dorénavant que les théories en question sont des théories du premier ordre de la logique classique, même si les théorèmes d'incomplétude restent valides, sous les mêmes conditions, par exemple en logique intuitionniste ou en passant à l'ordre supérieur.

    * Par théorie récursivement axiomatisable, on entend que la théorie peut être axiomatisée de façon qu'il soit possible de reconnaître de façon purement mécanique les axiomes parmi les énoncés du langage de la théorie. C'est le cas évidemment des théories utilisées pour formaliser tout ou partie des mathématiques usuelles.
    * Une théorie est cohérente si aucune contradiction ne peut être prouvée à partir de ses axiomes. On dit aussi qu'elle est consistante, ou non-contradictoire. Pour le premier théorème d'incomplétude, Gödel faisait une hypothèse de cohérence un peu plus forte. L'hypothèse de cohérence simple suffit de toute façon pour le second théorème, qui n'énonce que la non-démontrabilité de l'énoncé de cohérence. J. B. Rosser a donné en 1936 une démonstration du premier théorème d'incomplétude sous la simple hypothèse de cohérence. À proprement parler, l'énoncé du premier théorème d'incomplétude donné au début de cet article n'est donc pas exactement celui de Gödel. On le nomme souvent théorème de Gödel-Rosser.
    * Une théorie permet de formaliser l'arithmétique si, d'une part il est possible de définir (en un sens qu'il faudrait préciser) les entiers (donnés par zéro et la fonction successeur), avec les opérations usuelles, au moins l'addition et la multiplication, et si d'autre part un certain nombre d'énoncés sur les entiers sont prouvables dans la théorie. Les axiomes de Peano conviennent, mais, pour le premier théorème d'incomplétude une théorie arithmétique beaucoup plus faible suffit (la récurrence n'est essentiellement pas utile). Pour le second il faut un minimum de récurrence.
      Il est remarquable que pour formaliser l'arithmétique, l'addition et la multiplication suffisent (en plus de zéro et du successeur). C'est le tout premier pas vers la solution du dixième problème de Hilbert (voir théorème de Matiyasevich). L'addition seule ne suffit pas : l'arithmétique de Presburger, qui est la théorie obtenue en restreignant l'arithmétique de Peano au langage de l'addition (en plus de zéro et du successeur), est complète.

Conséquences immédiates du premier théorème d'incomplétude

On peut reformuler le premier théorème d'incomplétude en disant que si une théorie T satisfait les hypothèses utiles, il existe un énoncé tel que chacune des deux théories obtenues l'une en ajoutant à T cet énoncé comme axiome, l'autre en ajoutant la négation de cet énoncé, sont cohérentes.

Étant donné un énoncé G, notons non G sa négation. On montre facilement qu'un énoncé G n'est pas démontrable dans T si et seulement si la théorie T + non G (la théorie T à laquelle on ajoute l'axiome non G) est cohérente. En effet, si G est démontrable dans T, T + non G est évidemment contradictoire, et, réciproquement, de T + non G est contradictoire, on déduit que G est conséquence de T (c'est le raisonnement par l'absurde).

Il est donc équivalent de dire qu'un énoncé G est indécidable dans une théorie cohérente T, et de dire que les deux théories T + non G et T + G sont cohérentes. L'énoncé G n'étant évidemment pas indécidable dans chacune de ces deux théories, on voit que la notion d'énoncé indécidable est par nature relative à une théorie donnée.

Ainsi, si G est l'énoncé indécidable donné pour T par le premier théorème d'incomplétude, on aura, en appliquant à nouveau ce théorème, un nouvel énoncé indécidable dans la théorie T + G (et donc d'ailleurs indécidable aussi dans la théorie T).

De fait, quand le théorème d'incomplétude s'applique à une théorie T, il s'applique à toutes les extensions cohérentes de cette théorie, tant qu'elles restent récursivement axiomatisables : il n'y a aucun moyen effectif de compléter une telle théorie.

Il faut également noter que, quelle que soit la théorie en jeu, l'énoncé obtenu est arithmétique, c'est à dire qu'on peut l'exprimer dans le langage de l'arithmétique. Il s'agit même d'un énoncé de l'arithmétique logiquement assez simple (en un sens précis). Par exemple, on obtiendra par le théorème de Gödel appliqué à la théorie des ensembles de Zermelo-Fraenkel un énoncé arithmétique mais qui sera indécidable dans celle-ci.

Conséquences immédiates du second théorème d'incomplétude

Il peut être utile pour comprendre l'énoncé du second théorème d'incomplétude, de le reformuler par contraposée :

    Si T est une théorie récursivement axiomatisable qui permet de formaliser "suffisamment d'arithmétique", et si T prouve un énoncé exprimant qu'elle est cohérente, alors T est contradictoire.

Par contre une théorie qui démontre un énoncé exprimant qu'elle n'est pas cohérente, peut très bien ne pas être contradictoire, comme on le déduit du second théorème d'incomplétude lui-même !

Esquissons la preuve. Appelons cohT un énoncé qui exprime la cohérence de T dans la théorie T. D'après ce qui précède, le second théorème d'incomplétude affirme que, sous les hypothèses utiles sur T, si la théorie T est cohérente, la théorie T'=T + non cohT est encore cohérente. Rappelons que " T n'est pas cohérente ", signifie qu'il existe une preuve d'une contradiction dans T. Une preuve dans T est aussi une preuve dans T' , qui a juste un axiome supplémentaire. Il est donc simple de montrer dans une théorie telle que T, qui satisfait les hypothèses du théorème de Gödel, que non cohT a pour conséquence non cohT'. On a donc déduit du second théorème de complétude, et de l'existence d'une théorie cohérente T qui satisfait les hypothèses de ce théorème -- prenons par exemple l'arithmétique de Peano -- l'existence d'une théorie T' cohérente qui démontre non cohT', à savoir un énoncé exprimant qu'elle n'est pas cohérente.

A contrario une théorie incohérente, dans laquelle tous les énoncés sont prouvables, démontrera évidemment un énoncé exprimant qu'elle est cohérente.

On voit par ces diverses remarques que le second théorème d'incomplétude ne dit rien en défaveur de la cohérence d'une théorie à laquelle il s'applique, par exemple la cohérence de l'arithmétique de Peano. Tout ce qu'il dit de cette dernière, c'est qu'elle ne peut se prouver que dans une théorie logiquement plus forte.

Vérité et démontrabilité

La notion de vérité est parfois méconnue en dehors de la logique mathématique. Le théorème de Gödel établit justement qu'un énoncé arithmétique peut être vrai (pour les entiers) sans être démontrable. On définit la vérité relativement à un modèle, et nous allons dans la suite nous intéresser à la vérité dans le modèle standard de l'arithmétique, les entiers que "tout le monde connait", que l'on note N. Rappelons que si l'on démontre un énoncé à partir d'énoncés vrais dans un modèle, l'énoncé obtenu est vrai dans ce modèle, et que dans un modèle un énoncé (une formule close) est soit vrai soit faux, pas d'autre alternative. Par conséquent la théorie des énoncés vrais dans N est close par déduction et complète. On déduit immédiatement du premier théorème d'incomplétude que

    La théorie des énoncés vrais dans N n'est pas récursivement axiomatisable.

et donc

    Si T est une théorie récursivement axiomatisable qui permet de formaliser "suffisamment d'arithmétique", et dont tous les axiomes sont vrais dans N, il existe un énoncé vrai dans N qui n'est pas démontrable dans T.

C'est un théorème d'incomplétude, plus faible cependant que le premier théorème d'incomplétude de Gödel (il s'applique à moins de théories, on ne peut le formaliser dans l'arithmétique, pour en déduire le second théorème d'incomplétude). Tel quel il se déduit d'ailleurs du Théorème de Tarski (1933), qui est plus facile à démontrer que celui de Gödel. Comme l'énoncé non démontrable est vrai dans N et que la théorie ne démontre que des énoncés vrais dans N, la négation de cet énoncé n'est pas non plus démontrable. Par ailleurs comme la théorie T a un modèle, elle est cohérente. En précisant comme il faut la complexité logique de l'énoncé vrai non démontrable, on pourra ne supposer que la vérité dans N des théorèmes de cette complexité logique, et on obtiendra un théorème équivalent au premier théorème d'incomplétude (celui démontré par Gödel).

La notion de vérité utilisée se définit mathématiquement, mais, par exemple, la vérité d'une formule du premier ordre de l'arithmétique ne se définit pas dans l'arithmétique de Peano. Le vocabulaire utilisé correspond à l'intuition, la notion est très commode. Mais il n'est pas besoin d'attribuer une valeur excessive à cette notion pour l'utiliser. Par exemple, Gödel construit effectivement un énoncé dont il montre qu'il est vrai dans N, ce qui veut dire qu'on sait le prouver dans une théorie plus forte que celle de départ. La notion de vérité dans un modèle s'est précisée au cours de la première moitié du vingtième siècle. À l'époque où Gödel démontre son théorème, elle n'est pas vraiment formalisée, même s'il a démontré en 1929 le théorème de complétude et donc connait bien entendu cette notion. La définition utilisée actuellement est due à Alfred Tarski, on la trouve dans un article publié en 1956.

Définissons la vérité dans N. Le langage a pour seul symbole de constante 0, pour seuls symboles de fonction s (la fonction successeur, qui ajoute 1), + et ×, pour seul symbole de relation en plus de l'égalité, le symbole d'inégalité ¿.

Le modèle standard se définit simplement : les seuls éléments de l'ensemble de base du modèle sont les entiers usuels, tous décrits par les termes du langage de la forme s ... s 0 (où s est le signe pour la fonction successeur, "ajouter 1"), c'est à dire la notation unaire bien connue qui correspond à l'idée primitive d'entier. Dans la vie courante on utilise plutôt un petit bâton que la lettre s, et on n'éprouve pas le besoin de noter le zéro. Les termes du langage sont essentiellement des polynômes, les formules atomiques des égalités ou inégalités polynômiales. Pour définir le modèle il reste à décrire les formules atomiques closes, c'est à dire sans variable, vraies et fausses.

On définit facilement la vérité dans N des égalités et inégalités polynômiales sur les entiers (pas de variable !) notés de cette façon, et on peut même le faire mécaniquement, c'est à dire que la vérité des énoncés atomiques (égalités et inégalités polynômiales closes) est décidable au sens algorithmique. Les algorithmes en jeu sont essentiellement ceux de l'addition et de la multiplication en base 1 (des suites de "bâtons"), conceptuellement plus simples que ceux que l'on enseigne à l'école primaire pour la base 10 (mais plus fastidieux à utiliser).

A partir de là, on a défini le modèle, et donc on a la définition par induction de la vérité d'une formule quelconque dans ce modèle. Sans rentrer dans la définition formelle, observons quelques cas particuliers. Tout d'abord la vérité des formules closes sans quantificateurs reste décidable : on peut se ramener à des conjonctions et disjonctions d'égalités et d'inégalités (¿ et ¿) polynômiales. Passons aux quantificateurs, un énoncé du genre ¿x(P(x)=Q(x)) où P et Q sont des polynômes à une seule variable, est vrai quand on peut trouver un entier n tel que P(n)=Q(n). Remarquez que s'il existe un tel entier, une machine pourra le trouver, en essayant les entiers les uns après les autres par ordre croissant. Mais la machine ne s'arrêtera pas s'il n'existe pas de tel entier. Il n'y a pas d'évidence que la vérification de telles formules est algorithmiquement décidable (et elle ne l'est pas).

La situation est "pire" pour le quantificateur universel : un énoncé du genre ¿ x(P(x)=Q(x)) est vrai si pour chaque entier n, l'égalité P(n)=Q(n) est vraie : c'est bien défini, mais, si l'on suit la définition, cela demande une infinité de vérifications ! On voit bien la différence entre vérité et démontrabilité. Une preuve est nécessairement finie, et de plus on doit pouvoir reconnaître mécaniquement une preuve formelle. Pour démontrer un énoncé universel tel que celui-ci, habituellement on fait une récurrence. Sommairement, une preuve par récurrence est une façon finie de représenter une infinité de vérifications. Au passage on a perdu quelque chose, comme l'énonce précisément le théorème de Gödel.

Quand on a un moyen mécanique de décider la vérité de certaines classes d'énoncés, par exemple les énoncés sans quantificateurs, on a une preuve de ces énoncés, ou de leurs négations, au sens informel de cette notion. Dans les cas abordés ci-dessus, ces preuves sont effectivement formalisables dans les théories pour lesquelles on démontre les théorèmes de Gödel.

Des exemples de systèmes incomplets et d'énoncés indécidables

L'existence de théories incomplètes est banale. Beaucoup de théories, comme la théorie des groupes, des anneaux, des corps, ne sont pas complètes : par exemple on peut dire au premier ordre qu'un groupe ou un corps a 2 éléments, ou 3 éléments. C'est différent pour l'arithmétique, on aurait souhaité capturer par une axiomatique toutes les propriétés des entiers naturels. Pour les théories destinées à fonder les mathématiques, Principia Mathematica ou théorie axiomatique des ensembles, on peut s'attendre à ne pas avoir encore découvert tous les axiomes. Mais le théorème de Gödel affirme qu'il restera toujours des énoncés indécidables (tant que la théorie reste récursivement axiomatisable).

Il existe également des théories complètes intéressantes, comme l'arithmétique de Presburger déjà évoquée, la théorie des corps algébriquement clos d'une caractéristique donnée, la théorie des corps réels clos, et la géométrie élémentaire qui lui est associée.

Énoncés indécidables dans l'arithmétique de Peano

Appliqués à l'arithmétique, les théorèmes de Gödel fournissent des énoncés dont la signification est tout à fait intéressante, puisqu'il s'agit de la cohérence de la théorie. Cependant ces énoncés dépendent du codage choisi. Ils sont pénibles à écrire explicitement.

Paris et Harrington ont montré en 1977 qu'un renforcement du théorème de Ramsey fini, vrai dans N, n'est pas démontrable dans l'arithmétique de Peano. Il s'agit du premier exemple d'énoncé indécidable dans l'arithmétique qui n'utilise pas de codage du langage. Depuis, on en a découvert d'autres. Le théorème de Goodstein est un tel énoncé ; sa preuve est particulièrement simple (quand on connaît les ordinaux), mais utilise une induction jusqu'à l'ordinal dénombrable ¿0. Kirby et Paris ont démontré en 1982 que l'on ne peut pas prouver ce théorème dans l'arithmétique de Peano.

Les énoncés de ce genre qui ont été découverts sont des résultats de combinatoire. Leur preuve n'est pas nécessairement très compliquée, et en fait il n'y a aucune raison de penser qu'il y a un lien entre complexité technique d'une preuve et possibilité de formaliser celle-ci dans l'arithmétique de Peano.

Énoncés indécidables en théorie des ensembles

En théorie des ensembles, on a d'autres énoncés indécidables que ceux fournis par le théorème de Gödel qui peuvent être de nature différente. Ainsi, d'après des travaux de Gödel, puis de Paul Cohen, l'axiome du choix et l'hypothèse du continu sont des énoncés indécidables dans ZF la théorie des ensemble de Zermelo et Fraenkel, le second étant d'ailleurs indécidable dans ZFC (ZF plus l'axiome du choix). Mais d'une part, ce ne sont pas des énoncés arithmétiques. D'autre part, la théorie obtenue en ajoutant à ZF l'axiome du choix ou sa négation est équi-cohérente à ZF : la cohérence de l'une entraîne la cohérence de l'autre et réciproquement. De même pour l'hypothèse du continu. Ce n'est pas le cas pour un énoncé exprimant la cohérence de ZF, d'après justement le second théorème d'incomplétude. De même pour l'un des deux énoncés obtenus par les preuves usuelles du premier théorème d'incomplétude (il est équivalent à un énoncé de cohérence).

Dès que l'on peut montrer dans une théorie des ensembles T+A, qu'un ensemble (un objet de la théorie) est modèle de la théorie des ensembles T, c'est à dire la cohérence de T, on déduit par le second théorème d'incomplétude que, si T est cohérente, A n'est pas démontrable dans T. On montre ainsi que certains axiomes qui affirment l'existence de "grands" cardinaux, ne sont pas démontrables dans ZFC.

Théorèmes d'incomplétude et calculabilité

La notion de calculabilité intervient a divers titres à propos des théorèmes d'incomplétude. On l'a utilisé pour en définir les hypothèses. Elle intervient dans la preuve du premier théorème d'incomplétude (Gödel utilise les fonctions récursives primitives). Enfin incomplétude et indécidabilité de l'arithmétique sont liées.

Indécidabilité algorithmique

Il y a un lien étroit entre décidabilité algorithmique d'une théorie, l'existence d'une méthode mécanique pour tester si un énoncé est ou non un théorème, et complétude de cette théorie. Une théorie récursivement axiomatisable et complète est décidable. On peut donc prouver le premier théorème d'incomplétude en montrant qu'une théorie qui satisfait les hypothèses utiles est indécidable. Ce résultat, l'indécidabilité algorithmique des théories qui satisfont les hypothèses du premier théorème d'incomplétude, a été démontré indépendemment par Turing et Church en 1936 (voir problème de la décision), en utilisant les méthodes développées par Gödel pour son premier théorème d'incomplétude. Pour un résultat d'indécidabilité, qui est un résultat négatif, il faut avoir formalisé la calculabilité, et être convaincu que cette formalisation est correcte, conviction qui ne peut reposer seulement sur des bases mathématiques. En 1931, Gödel connaît un modèle de calcul que l'on dirait maintenant Turing-complet, les fonctions récursives générales, décrit dans une lettre que Jacques Herbrand lui a adressée, et qu'il a lui-même précisé et exposé en 1934. Cependant il n'est pas convaincu à l'époque d'avoir décrit ainsi toutes les fonctions calculables. À la suite de travaux de Kleene, Church, et Turing, ces deux derniers ont énoncé indépendemment en 1936 la thèse de Church-Turing : les fonctions calculables sont les fonctions récursives générales.

On peut être plus précis en donnant une classe restreinte d'énoncés pour laquelle la prouvabilité est indécidable. Si on reprend les arguments développés dans le paragraphe Vérité et démontrabilité ci-dessus, on voit par exemple que la classe des énoncés sans quantificateurs (et sans variables) est, elle, décidable.

En utilisant les arguments développés par Gödel, on montre que la prouvabilité des énoncés ¿1 est indécidable. Sans entrer dans le détail de la définition des formules ¿1 (faite ci-dessous), cela ne semble pas si loin d'une solution négative au dixième problème de Hilbert : l'existence d'un algorithme de décision pour la résolution des équations diophantiennes. Mais il fallu plusieurs dizaines d'années et les efforts successifs de plusieurs mathématiciens dont Martin Davis, Hilary Putnam, Julia Robinson et finalement Youri Matiiassevitch pour y arriver en 1970 (voir théorème de Matiiassevitch).

On peut tout à fait déduire le premier théorème de Gödel du théorème de Matiiassevitch. Cela peut paraître artificiel, puiqu'un résultat d'indécidabilité beaucoup plus facile à démontrer suffit. Mais on peut en déduire des énoncés indécidables d'une forme particulièrement simple. En effet, le théorème de Matiiassevitch équivaut à dire que la vérité des énoncés (formules closes) qui s'écrivent comme des égalités polynomiales quantifiées existentiellement, n'est pas décidable. Or :

    * on peut reconnaître mécaniquement de tels énoncés, et donc leurs négations ;

    * L'ensemble des tels énoncés vrais est récursivement énumérable, et donc, d'après le théorème de Matiiassevitch, l'ensemble des tels énoncés faux n'est pas récursivement énumérable ;

    * l'ensemble des théorèmes d'une théorie récursivement axiomatisable est récursivement énumérable (voir Théorie récursivement axiomatisable), et donc l'ensemble des théorèmes qui s'écrivent comme la négation d'une égalité polynômiale quantifiée existentiellement également ;

    * l'hypothèse de cohérence que fait Gödel pour son premier théorème d'incomplétude a pour conséquence directe que des égalités quantifiés existentiellement et fausses ne peuvent être démontrables.

On en déduit qu'il existe des énoncés vrais non démontrables, qui s'écrivent comme la négation d'une égalité polynômiale quantifiée existentiellement, ou plus simplement comme une inégalité polynômiale quantifiée universellement.

La mise en cause du mouvement formaliste

Pour répondre aux problèmes de la crise des fondements des mathématiques, Hilbert et ses élèves avaient développé un programme qui devait apporter une réponse définitive aux problèmes des fondements des mathématiques. Le programme de Hilbert reposait de façon essentielle sur la possibilité de prouver la cohérence des théories mathématiques par des méthodes finitaires : sans plus préciser, des méthodes qui devaient pouvoir se formaliser dans une théorie probablement plus faible que l'arithmétique de Peano. On déduit immédiatement du second théorème d'incomplétude que ce n'est pas possible pour toute théorie récursivement axiomatisable permettant de formaliser les mathématiques, et donc de définir l'arithmétique de Peano elle-même.

Il y eu des tentatives pour remédier à cette situation en précisant et en étendant la notion de méthode finitaire, même si, d'après le second théorème de Gödel, on ne peut espérer définir une fois pour toutes une théorie (récursivement axiomatisable) pour de telles méthodes finitaires. Ainsi Gentzen a prouvé en 1936 la cohérence de l'arithmétique en utilisant un principe de récurrence jusqu'à l'ordinal dénombrable ¿0, mais pour des formules de complexité logique très simple. Cette preuve développe des outils qui se sont révélés fondamentaux en théorie de la démonstration. Elle est indubitablement une preuve de cohérence relative. On l'interprètera plus volontiers aujourd'hui comme une façon de mesurer la "force" de l'arithmétique de Peano (par un ordinal).

Une preuve partielle du premier théorème d'incomplétude

La preuve par Gödel de son premier théorème d'incomplétude utilise essentiellement deux ingrédients :

    * le codage par des nombres entiers du langage et des fonctions qui permettent de le manipuler, ce que l'on appelle l'arithmétisation de la syntaxe ;

    * un argument diagonal qui fait apparaître un énoncé similaire au paradoxe du menteur : l'énoncé de Gödel est équivalent, via codage, à un énoncé affirmant sa propre non prouvabilité dans la théorie considérée.

L'énoncé de Gödel n'est pas paradoxal. Il est vrai dans N, car s'il était faux, il serait prouvable. Or cet énoncé est de complexité logique suffisamment simple pour que sa prouvabilité dans une théorie cohérente capable de coder l'arithmétique entraîne sa vérité dans N (on n'a pas besoin de supposer que N est modèle de la théorie). Il est donc vrai dans N. il n'est donc pas prouvable.

Pour montrer que la négation de l'énoncé de Gödel n'est pas non plus prouvable, il faut une hypothèse de cohérence plus forte, comme celle qu'a faite Gödel. Rosser a modifié astucieusement l'énoncé pour pouvoir utiliser simplement la cohérence. En ce qui concerne la preuve de Gödel l'argument est le suivant : l'énoncé étant vrai, sa négation est fausse. Si on supposait que N est modèle de la théorie, cela suffirait pour qu'elle ne soit pas démontrable. Mais Gödel a construit un énoncé d'une complexité logique suffisamment faible pour qu'une hypothèse beaucoup moins forte suffise : il s'agit essentiellement de dire que de tels énoncés faux ne peuvent être démontrables, et il peut l'exprimer de façon syntaxique.

Arithmétisation de la syntaxe

À l'époque actuelle, quiconque connait un peu d'informatique n'a aucun mal à imaginer que l'on puisse représenter les énoncés d'une théorie par des nombres. Cependant il faut également manipuler ces codages dans la théorie. La difficulté réside dans les restrictions du langage : une théorie du premier ordre avec essentiellement l'addition et la multiplication comme symboles de fonction. C'est la difficulté que Gödel résout pour montrer que la prouvabilité peut être représentée par une formule dans la théorie.

La suite est un peu technique. On peut simplifier l'argumentation en supposant que N est modèle de T, auquel cas on n'a pas besoin d'être attentif à la complexité logique de l'énoncé. La partie sur la fonction ¿ et la représentation de la récurrence reste utile. On précise également des notions, et des résultats qui ont été évoqués ou rédigés de façon approximative ci-dessus.

Codes

Il peut être amusant d'écrire soi même les codages, il l'est certainement beaucoup moins de lire ceux des autres. On trouve donc beaucoup de variété dans la littérature. Le choix du codage n'a pas grande importance, en soi. Éventuellement certains se "manieront" plus facilement dans la théorie. Comme les formules et les démonstrations peuvent être vues comme des suites finies de caractères, lettres, espace, ponctuation, et ceux-ci en nombre fini, on peut les coder par un nombre, celui étant écrit dans une base de la taille nombre de caractère nécessaire, ou par tout autre moyen qui permet de coder des suites finies d'entier. On peut également utiliser un codage des couples (voir ci-dessous) pour représenter, suites finies, arbres, et donc les structures syntaxiques utiles ...

Formules ¿0

Un problème plus important est d'avoir des fonctions pour manipuler ces structures, l'équivalent des programmes en informatique : il est à peu près clair que l'on ne peut se contenter de compositions de fonctions constantes, d'additions et de multiplications, c'est à dire de polynômes à coefficients entiers positifs. On va représenter les fonctions utiles par des formules. Voyons un exemple, par ailleurs fort utile pour les codages. La bijection de Cantor entre N×N et N est bien connue et tout à fait calculable : on énumére les couples d'entiers diagonale par diagonale (somme constante), par exemple en faisant croître la seconde composante :

Cette fonction n'est déjà plus représentée par un terme du langage, à cause de la division par 2, mais elle est représentée par la formule (on utilise "¿" pour la relation d'équivalence) :

Passons maintenant aux fonctions de décodage, c'est à dire à un couple de fonctions inverses. On aura besoin de quantificateurs :

On a donc représenté une fonction, plus exactement son graphe (la formule soulignée) par une formule du langage de l'arithmétique. Les formules ci-dessus sont bien particulières : la première est une égalité polynômiale, si on remplace les trois variables libres par des termes clos du langage, représentant des entiers (s¿s0), elle devient décidable. Les deux suivantes utilisent un quantificateur borné : "¿x¿z A" signifie "il existe un x plus petit ou égal à z tel que A". Là encore si on remplace les deux variables libres par des entiers cette formule devient décidable : pour vérifier une quantification existentielle bornée, il suffit de chercher jusqu'à la borne, soit on a trouvé, et l'énoncé est vérifié, soit on n'a pas trouvé et il ne l'est pas. Ce n'est plus le cas (pour la seconde partie de l'assertion) si la quantification existentielle n'est pas bornée. On pourra conserver cette propriété de décidabilité en ajoutant des quantifications universelles bornées, notée "¿ x¿ p A" ("pour tout x plus petit ou égal à p, A"). Les formules construites à partir des égalités polynômiales en utilisant les connecteurs booléens usuels, et des quantifications uniquement bornées sont appelées formules ¿0. Remarquez que la négation d'une formule ¿0 est ¿0.

On se convainc facilement, des arguments sont donnés juste ci-dessus et au paragraphe vérité et démontrabilité, que la vérité dans N des formules closes ¿0 est décidable : on a un moyen mécanique de savoir si elles sont vraies ou fausses. Pour démontrer le premier théorème d'incomplétude de Gödel (il faut un peu plus pour Gödel-Rosser, de la récurrence pour le second), la condition minimale sur la théorie, en plus d'être récursivement axiomatisable et d'une hypothèse de cohérence, est de démontrer toutes les formules ¿0 vraies dans N, et donc, par stabilité par négation des ¿0 et cohérence, de n'en démontrer aucune fausse. C'est ce que l'on a entendu par "formaliser suffisamment d'arithmétique". Remarquez que c'est une hypothèse sur les axiomes de la théorie. Par exemple l'ensemble des formules ¿0 vraies dans N étant décidable, on peut le choisir comme système d'axiomes pour une théorie qui sera bien récursivement axiomatisable (on peut évidemment le simplifier). En particulier on peut démontrer :

    Dans l'arithmétique de Peano, les formules closes ¿0 sont vraies dans N si et seulement si elles sont démontrables.

Résultat qui se démontre d'ailleurs sans véritablement utiliser de récurrence (ce qui est naturel puisqu'il n'y a pas véritablement de quantification universelle dans ces énoncés).

Il serait bien commode de se contenter de manipuler des fonctions représentables par des formules ¿0 : vérité et démontrabilité sont confondues, ces formules sont décidables, donc les fonctions représentées par des formules ¿0 sont calculables. Mais le "langage de programmation" induit n'est pas assez riche. On doit introduire les formules ¿1, qui sont les formules obtenues en plaçant un quantificateur existentiel en tête d'une formule ¿0. En général la négation d'une formule ¿1 n'est pas équivalente à une formule ¿1. On a la propriété suivante :

    Dans une théorie qui prouve toutes les formules ¿0 vraies dans N, les formules ¿1 vraies dans N sont prouvables.

En effet une formule ¿1 "¿ x A x" est vraie dans N signifie que pour un certain entier, que l'on peut écrire "s¿s0", la formule "A s¿s0" est vraie, or cette formule est ¿0.

Il existe de théories arithmétiques cohérentes, qui démontrent des formules closes ¿1 fausses, contrairement à ce qui se passe pour les ¿0. Il faut préciser que de telles théories arithmétiques sont assez pathologiques, comme celles qui démontrent un énoncé exprimant leur propre contradiction (voir début de l'article). L'hypothèse de cohérence supplémentaire utile pour le premier théorème d'incomplétude, que l'on va appeler ¿-cohérence, c'est justement de supposer que la théorie ne démontre aucune formule close ¿1 fausse. On suppose que certaines formules ne sont pas démontrables, donc la contradiction ne l'est pas : c'est bien une hypothèse de cohérence au moins aussi forte que la cohérence simple. Elle est vraiment plus forte : on peut exprimer la négation de la cohérence d'une théorie par une formule ¿1[1].

Fonctions définissables, fonctions représentables

Un sous-ensemble E de N, ou plus généralement de Np est définissable dans l'arithmétique s'il existe une formule F de l'arithmétique avec p variables libres telle que :

Un sous-ensemble E de Np est représentable dans une théorie T s'il existe une formule s'il existe une formule F de l'arithmétique avec p variables libres telle que :

Une fonction f à plusieurs variables sur N est définissable dans N si son graphe est défini dans N, représentable dans une théorie T' si son graphe est représentable dans T. Un ensemble, ou une fonction est définissable par une formule ¿1 si et seulement si il, ou elle, est représentable par cette formule dans une théorie ¿-cohérente où tous les énoncés ¿0 sont démontrables.

Il existe d'autres notions de représentabilité plus fortes, pour les ensembles comme pour les fonctions. Pour celle introduite ici on dit souvent faiblement représentable.

On notera y=f(x) une formule ¿1 définissant ou représentant f. Pour le théorème de Gödel c'est la notion de fonction ou d'ensemble représentable qui est utile, mais la notion de fonction ou d'ensemble définissable est plus simple à manipuler, et comme on s'intéresse aux cas où elles sont équivalentes, on va dans la suite parler de définissabilité par une formule ¿1.

On peut remarquer que la conjonction, la disjonction de deux formules ¿1, la quantification existentielle d'une formule ¿1, la quantification universelle bornée d'une formule ¿1, sont équivalentes dans N (on note ¿N) à une formule ¿1 :

L'ensemble de fonctions à notre disposition est donc stable par composition (on donne l'exemple pour une variable, on généralise sans peine à des fonctions de plusieurs variables) :

On définit également de façon naturelle :

Cependant, pour pouvoir avoir un langage suffisamment expressif pour définir les fonctions utiles sur la syntaxe, il manque une notion très utile : la définition par récurrence. L'idée pour l'obtenir est d'utiliser un codage des suites finies (les listes de l'informatique). Supposons que nous ayons un tel codage, notons l=[n0;¿;np] l'entier qui code la suite finie n0,¿,np. Il faut pouvoir décoder : notons ¿(l,i)=ni l'élément en place i de la suite codée par l (la valeur n'a pas d'importance si i est trop grand). Supposons que nous ayons une fonction g à valeur et image entière (une suite infinie d'entiers) définie par :

et que f soit définissable dans N. Alors on pourra définir la fonction g par :

formule qui est équivalente dans N à une formule ¿1 dès que le graphe de ¿ est ¿1. Ceci se généralise au schéma de récurrence utilisé pour les fonctions récursives primitives. Il suffit donc trouver une formule ¿1 qui définit une fonction ¿ : c'est la principale difficulté à résoudre pour le codage de la syntaxe.

Le nom de fonction ¿ est repris de l'article original de Gödel. Pour la définir, il a eu l'idée d'utiliser le théorème des restes chinois : pour coder n1,¿,np on va donner p entiers premiers entre eux eux à deux, engendrés à partir d'un seul entier d, et un entier a dont les restes des divisions par chacun de ces entiers sont n1,¿,np. La suite n1,¿,np sera donc codée par les deux entiers a et d, l'entier <a,d> si on en veut un seul. Plusieurs (une infinité !) entiers coderont la même suite, ce qui n'est pas gênant si on pense à l'objectif (coder les définitions par récurrence). Le principal est que l'on assure que toute suite finie a au moins un code.

Étant donnés les entiers n1,¿,np, on choisi un entier s, tel que s ¿ p et pour tout ni, s¿ni. Les entiers

sont alors premiers entre eux deux à deux. De plus ni < di. Par le théorème chinois on déduit l'existence d'un entier a tel que pour chaque entier ni de la suite finie, le reste de la division de a par di soit ni. On a donc, en posant d = s! :

On a bien une fonction ¿ définie par une formule ¿0.

On en déduit que :

    si une fonction se définit par récurrence primitive à partir de fonctions définissables par des formules ¿1, elle est définissable par une formule ¿1.

On peut faire beaucoup de choses avec les fonctions récursives primitives. Une fois ce résultat obtenu, le reste n'est plus qu'affaire de soin. On peut utiliser des méthodes plus ou moins astucieuses pour gérer les problèmes de liaison de variables. On montre que la fonction qui code la substitution d'un terme à une variable dans une formule est récursive primitive, que l'ensemble des (codes de) preuves d'une théorie T récursivement axiomatisable est récursif primitif, et enfin que la fonction qui extrait d'une preuve la conclusion de celle-ci est récursive primitive. Dire qu'une formule est prouvable dans T, c'est dire qu'il existe une preuve de cette formule dans T, ce qui, codé dans la théorie, reste ¿1 (bien que le prédicat "être démontrable" ne soit pas lui récursif primitif, ni même récursif).

En conclusion, pour une théorie récursivement axiomatisable T, on a deux formules ¿1, DemT(x) et z=sub(x,y), telles que :

    DemT(¿F¿) est vraie dans N si et seulement si F est prouvable dans T ;  pour une formule Fx, ¿Fn¿=sub(¿F¿,n).

On a noté ¿F¿ l'entier qui code la formule F.

Du fait que les formules sont ¿1, on peut remplacer "vrai" par "démontrable dans T" sous les hypothèses suffisantes.

Diagonalisation

La construction de l'énoncé de Gödel repose sur un argument diagonal. On construit tout d'abord la formule à une variable libre ¿(x) :

qui peut s'interpréter dans N par la formule de code x appliquée à son propre code n'est pas démontrable dans T, et on applique cette formule à l'entier ¿¿¿. On obtient G=¿(¿¿¿) , une formule qui dit bien d'elle même qu'elle n'est pas démontrable dans T. On reprend en la précisant l'argumentation déjà donnée au dessus. On suppose que T est récursivement axiomatisable, démontre toutes les formules ¿0 vraies dans N, donc toutes les formules ¿1 vraies dans N, et qu'elle est ¿-cohérente.

    * G=¿(¿¿¿) est une formule close, équivalente à la négation d'une formule ¿1 ;

    * si la formule G était démontrable, la négation de G étant ¿1 ne pourrait être vraie car alors elle serait démontrable, et donc cela contredirait la cohérence de T. La formule G serait donc vraie dans N, ce qui voudrait dire, par construction de G, que la formule G ne serait pas démontrable, contradiction. Donc G n'est pas démontrable.

    * si la négation de la formule G était démontrable dans T, par ¿-cohérence elle serait vraie, or elle est fausse d'après ce qui précède. Donc la négation de G n'est pas démontrable.

On voit donc bien, le dernier argument étant assez tautologique, que le premier théorème d'incomplétude de Gödel s'énonce aussi bien par :

    Si T est une théorie récursivement axiomatisable, cohérente, et qui démontre toutes les formules ¿0 vraies dans N, alors il existe une formule G, négation d'une formule ¿1, qui est vraie dans N, mais non démontrable dans T.

Argument de la preuve du second théorème d'incomplétude

Le second théorème d'incomplétude se prouve essentiellement en formalisant la preuve du premier théorème d'incomplétude pour une théorie T dans cette même théorie T. En effet, on a montré ci-dessus que, si la théorie était cohérente la formule G de Gödel (qui dépend de T), n'est pas prouvable. Mais la formule de Gödel est équivalente à sa non prouvabilité. On a donc montré que la cohérence de la théorie T entraîne G : si T est suffisante pour formaliser cette preuve, on a alors montré dans la théorie T que la cohérence de la théorie T entraîne G, formule qui n'est pas prouvable dans T, donc n'est pas prouvable dans T.

On utilise simplement la non-démontrabilité de G, donc l'hypothèse de cohérence simple suffit. Par contre la théorie T doit forcément être plus expressive que pour le premier théorème d'incomplétude. En particulier on a besoin de récurrence.

Les conditions que doivent vérifier la théorie T pour démontrer le second théorème d'incomplétude ont été précisées tout d'abord par Paul Bernays dans les Grundlagen der Mathematik (1939) co-écrit avec David Hilbert, puis par Martin Löb, pour la démonstration de son théorème, une variante du second théorème d'incomplétude. Les conditions de démontrabilité de Löb portent sur le prédicat de prouvabilité dans la théorie T, que l'on nomme comme ci-dessus DemT :

On s'est a de fait démontré la condition D1 pour démontrer le premier théorème d'incomplétude. La seconde condition D2 est une formalisation dans la théorie de D1. Enfin la dernière, D3, est une formalisation de la règle logique primitive dite de Modus Ponens. Notons cohT la formule qui exprime la cohérence de T, c'est à dire que l'absurde, que l'on note ¿, n'est pas démontrable :

Comme la négation d'une formule F, ¬F, équivaut à F entraîne l'absurde, F¿¿, on déduit de la condition D3 que

Pour déduire le second théorème d'incomplétude des trois conditions de Löb, il suffit de reprendre le raisonnement déjà fait ci-dessus. Soit G la formule de Gödel, qui, sous hypothèse de cohérence simple, entraîne ¬DemT(¿G¿). D'après D1 et la cohérence de la théorie T, G n'est pas démontrable dans T (premier théorème). On formalise maintenant ce raisonnement dans T. Supposons que dans T, DemT(¿G¿). Comme d'autre part on démontre dans T que DemT(¿G ¿ ¬DemT(¿G¿)¿), on déduit par D3 dans T, DemT(¿¬DemT(¿G¿)¿). Finalement par D'3 on a montré ¬cohT dans T. Récapitulons : on a montré dans T que DemT(¿G¿) ¿ ¬cohT, c'est à dire par définition de G, ¬G ¿ ¬cohT, et par contraposée cohT ¿ G. Or on a vu que G n'est pas démontrable dans T, donc cohT n'est pas démontrable dans T.

La preuve de D1 a été déjà été esquissée à propos du premier théorème d'incomplétude : il s'agit de formaliser proprement la démontrabilité, et on utilise que les formules closes ¿1 vraies sont démontrables.

La condition D3 formalise la règle de modus ponens, une règle que l'on a tout intérêt à avoir dans les système formel pour les démonstrations que l'on a choisi. Il faudrait rentrer dans le détail du codage pour donner la preuve de D3, mais elle ne sera pas bien difficile. Il faut faire attention à bien formaliser le résultat indiqué dans la théorie choisie : les variables en jeu (par exemple il existe un x qui est le code d'une preuve de F) sont les variables de la théorie. Il faudra quelques résultats sur l'ordre, savoir démontrer quelques résultats élémentaires sur les preuves dans la théorie.

C'est la condition D2 qui s'avère la plus délicate a démontrer. C'est un cas particulier de la propriété

qui formalise (dans T) que toute formule close ¿1 vraie est démontrable dans T. On n'a donné ci-dessus aucun détail sur la preuve de ce dernier résultat, T étant par exemple l'arithmétique de Peano. Si on en donnait, on se rendrait compte que l'on n'a pas besoin de l'axiome de récurrence de la théorie, mais que, par contre, l'on raisonne par récurrence sur la longueur des termes, la complexité des formules ... Comme il faut maintenant formaliser cette preuve dans la théorie, il faut de la récurrence. Pour résumer la situation : quand on a démontré sérieusement le premier théorème d'incomplétude pour l'arithmétique de Peano, on a fait cette preuve, qui est un peu longue, mais ne présente pas de difficulté. Pour le second théorème, la seule chose à faire consiste maintenant à montrer que cette preuve se formalise dans l'arithmétique de Peano elle-même, ce qui est intuitivement relativement clair (quand on a fait la preuve), mais très pénible à expliciter complètement.

On peut en fait démontrer le second théorème d'incomplétude pour une théorie plus faible que l'arithmétique de Peano, l'arithmétique primitive récursive. On étend le langage de façon à avoir des symboles de fonction pour toutes les fonctions primitives récursives, et on ajoute à la théorie les axiomes qui définissent ces fonctions. On restreint la récurrence aux formules sans quantificateurs, ce qui fait que celles-ci sont "immédiates". L'arithmétique primitive récursive est souvent considérée comme la formalisation des mathématiques finitaires, avec lesquelles Hilbert espérait pouvoir prouver la cohérence des théories mathématiques.
"""
# source: http://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_G%C3%B6del

GG_TEXT = """\
La Gaule et ses habitants

    Toute la Gaule est divisée en trois parties, dont l'une est habitée par les Belges, l'autre par les Aquitains, la troisième par ceux qui, dans leur langue, se nomment Celtes, et dans la nôtre, Gaulois. Ces nations diffèrent entre elles par le langage, les institutions et les lois. Les Gaulois sont séparés des Aquitains par la Garonne, des Belges par la Marne et la Seine. Les Belges sont les plus braves de tous ces peuples, parce qu'ils restent tout à fait étrangers à la politesse et à la civilisation de la province romaine, et que les marchands, allant rarement chez eux, ne leur portent point ce qui contribue à énerver le courage : d'ailleurs, voisins des Germains qui habitent au-delà du Rhin, ils sont continuellement en guerre avec eux. Par la même raison, les Helvètes surpassent aussi en valeur les autres Gaulois ; car ils engagent contre les Germains des luttes presque journalières, soit qu'ils les repoussent de leur propre territoire, soit qu'ils envahissent celui de leurs ennemis. Le pays habité, comme nous l'avons dit, par les Gaulois, commence au Rhône, et est borné par la Garonne, l'Océan et les frontières des Belges ; du côté des Séquanes et des Helvètes, il va jusqu'au Rhin ; il est situé au nord. Celui des Belges commence à l'extrême frontière de la Gaule, et est borné par la partie inférieure du Rhin ; il regarde le nord et l'orient. L'Aquitaine s'étend de la Garonne aux Pyrénées, et à cette partie de l'Océan qui baigne les côtes d'Espagne ; elle est entre le couchant et le nord.

Les Helvètes. Plans ambitieux d'Orgétorix. Sa mort

    Orgétorix était, chez les Helvètes, le premier par sa naissance et par ses richesses. Sous le consulat de M. Messala et de M. Pison, cet homme, poussé par l'ambition, conjura avec la noblesse et engagea les habitants à sortir du pays avec toutes leurs forces ; il leur dit que, l'emportant par le courage sur tous les peuples de la Gaule, ils la soumettraient aisément tout entière à leur empire. Il eut d'autant moins de peine à les persuader que les Helvètes sont de toutes parts resserrés par la nature des lieux ; d'un côté par le Rhin, fleuve très large et très profond, qui sépare leur territoire de la Germanie, d'un autre par le Jura, haute montagne qui s'élève entre la Séquanie et l'Helvétie ; d'un troisième côté, par le lac Léman et le Rhône qui sépare cette dernière de notre Province. Il résultait de cette position qu'ils ne pouvaient ni s'étendre au loin, ni porter facilement la guerre chez leurs voisins ; et c'était une cause de vive affliction pour des hommes belliqueux. Leur population nombreuse, et la gloire qu'ils acquéraient dans la guerre par leur courage, leur faisaient regarder comme étroites des limites qui avaient deux cent quarante milles de long sur cent quatre-vingts milles de large.

    Poussés par ces motifs et entraînés par l'ascendant d'Orgétorix, ils commencent à tout disposer pour le départ, rassemblent un grand nombre de bêtes de somme et de chariots, ensemencent toutes leurs terres, afin de s'assurer des vivres dans leur marche et renouvellent avec leurs voisins les traités de paix et d'alliance. Ils pensèrent que deux ans leur suffiraient pour ces préparatifs ; et une loi fixa le départ à la troisième année. Orgétorix est choisi pour présider à l'entreprise. Envoyé en qualité de député vers les cités voisines, sur sa route, il engage le Séquanais Casticos, fils de Catamantaloédis, et dont le père avait longtemps régné en Séquanie et avait reçu du peuple romain le titre d'ami, à reprendre sur ses concitoyens l'autorité suprême, précédemment exercée par son père. Il inspire le même dessein à l'Héduen Dumnorix, frère de Diviciacos, qui tenait alors le premier rang dans la cité et était très aimé du peuple ; il lui donne sa fille en mariage. Il leur démontre la facilité du succès de leurs efforts ; devant lui-même s'emparer du pouvoir chez les Helvètes, et ce peuple étant le plus considérable de toute la Gaule, il les aidera de ses forces et de son armée pour leur assurer l'autorité souveraine. Persuadés par ces discours, ils se lient sous la foi du serment. : ils espéraient qu'une fois maîtres du pouvoir, au moyen de cette ligue des trois peuples les plus puissants et les plus braves, ils soumettraient la Gaule entière.

    Ce projet fut dénoncé aux Helvètes ; et, selon leurs coutumes, Orgétorix fut mis dans les fers pour répondre à l'accusation. Le supplice du condamné devait être celui du feu. Au jour fixé pour le procès, Orgétorix fit paraître au tribunal tous ceux qui lui étaient attachés, au nombre de dix mille hommes ; il y réunit aussi tous ses clients et ses débiteurs dont la foule était grande : secondé par eux, il put se soustraire au jugement. Les citoyens, indignés de cette conduite, voulaient maintenir leur droit par les armes, et les magistrats rassemblaient la population des campagnes, lorsque Orgétorix mourut. Il y a lieu de penser, selon l'opinion des Helvètes, qu'il se donna lui-même la mort.

Préparatifs d'émigration des Helvètes

    Cet événement ne ralentit pas l'ardeur des Helvètes pour l'exécution de leur projet d'invasion. Lorsqu'ils se croient suffisamment préparés, ils incendient toutes leurs villes au nombre de douze, leurs bourgs au nombre de quatre cents et toutes les habitations particulières ; ils brûlent tout le blé qu'ils ne peuvent emporter, afin que, ne conservant aucun espoir de retour, ils s'offrent plus hardiment aux périls. Chacun reçoit l'ordre de se pourvoir de vivres pour trois mois. Ils persuadent aux Rauraques, aux Tulinges et aux Latobices, leurs voisins, de livrer aux flammes leurs villes et leurs bourgs, et de partir avec eux. Ils associent à leur projet et s'adjoignent les Boïens qui s'étaient établis au-delà du Rhin, dans le Norique, après avoir pris Noréia.

    Il n'y avait absolument que deux chemins par lesquels ils pussent sortir de leur pays : l'un par la Séquanie, étroit et difficile, entre le Jura et le Rhône, où pouvait à peine passer un chariot ; il était dominé par une haute montagne, et une faible troupe suffisait pour en défendre l'entrée ; l'autre, à travers notre Province, plus aisé et plus court, en ce que le Rhône, qui sépare les terres des Helvètes de celles des Allobroges, nouvellement soumis, est guéable en plusieurs endroits, et que la dernière ville des Allobroges. Genève, est la plus rapprochée de l'Helvétie, avec laquelle elle communique par un pont. Ils crurent qu'ils persuaderaient facilement aux Allobroges, qui ne paraissaient pas encore bien fermement attachés au peuple romain, de leur permettre de traverser leur territoire, ou qu'ils les y contraindraient par la force. Tout étant prêt pour le départ, ils fixent le jour où l'on doit se réunir sur la rive du Rhône. Ce jour était le 5 avant les calendes d'avril, sous le consulat de L. Pison et de A. Gabinius.

César s'apprête à leur barrer le passage

    César, apprenant qu'ils se disposent à passer par notre Province, part aussitôt de Rome, se rend à grandes journées dans la Gaule ultérieure et arrive à Genève. Il ordonne de lever dans toute la province le plus de soldats qu'elle peut fournir (il n'y avait qu'une légion dans la Gaule ultérieure), et fait rompre le pont de Genève. Les Helvètes, avertis de son arrivée, députent vers lui les plus nobles de leur cité, à la tête desquels étaient Namméios et Verucloétios, pour dire qu'ils avaient l'intention de traverser la province, sans y commettre le moindre dommage, n'y ayant pour eux aucun autre chemin, qu'ils le priaient d'y donner son consentement. César, se rappelant que les Helvètes avaient tué le consul L. Cassius et repoussé son armée qu'ils avaient fait passer sous le joug, ne crut pas devoir leur accorder cette demande. Il ne pensait pas que des hommes pleins d'inimitié pussent, s'ils obtenaient la permission de traverser la province, s'abstenir de violences et de désordres. Cependant, pour laisser aux troupes qu'il avait. commandées le temps de se réunir, il répondit aux députés qu'il y réfléchirait, et que, s'ils voulaient connaître sa résolution, ils eussent à revenir aux ides d'avril.

    Dans cet intervalle, César, avec la légion qu'il avait avec lui et les troupes qui arrivaient de la Province, éleva, depuis le lac Léman, que traverse le Rhône, jusqu'au mont Jura, qui sépare la Séquanie de l'Helvétie, un rempart de dix- neuf mille pas de longueur et de seize pieds de haut : un fossé y fut joint. Ce travail achevé, il établit des postes, fortifie des positions, pour repousser plus facilement les Helvètes, s'ils voulaient passer contre son gré. Dès que le jour qu'il avait assigné à leurs députés fut arrivé, ceux-ci revinrent auprès de lui. Il leur déclara que les usages et l'exemple du peuple romain lui défendaient d'accorder le passage à travers la Province, et que, s'ils tentaient de le forcer, il s'y opposerait. Les Helvètes, déçus dans cette espérance, essaient de passer le Rhône, les uns sur des barques jointes ensemble et sur des radeaux faits dans ce dessein, les autres à gué, à l'endroit où le fleuve a le moins de profondeur, quelquefois le jour, plus souvent la nuit. Arrêtés par le rempart, par le nombre et par les armes de nos soldats, ils renoncent à cette tentative.

Ils traversent le pays des Séquanes. Mesures de César

    Il leur restait un chemin par la Séquanie, mais si étroit qu'ils ne pouvaient le traverser malgré les habitants. N'espérant pas en obtenir la permission par eux-mêmes, ils envoient des députés à l'Héduen Dumnorix, pour le prier de la demander aux Séquanes. Dumnorix, puissant chez eux par son crédit et par ses largesses, était en outre l'ami des Helvètes, à cause de son mariage avec la fille de leur concitoyen Orgétorix. Excité d'ailleurs par le désir de régner, il aimait les innovations, et voulait s'attacher par des services un grand nombre de cités. Il consentit donc à ce qu'on lui demandait, et obtint des Séquanes que les Helvètes traverseraient leur territoire : on se donna mutuellement des otages ; les Séquanes s'engagèrent à ne point s'opposer au passage des Helvètes, et ceux-ci à l'effectuer sans violences ni dégâts.

    On rapporte à César que les Helvètes ont le projet de traverser les terres des Séquanes et des Héduens, pour se diriger vers celles des Santons, peu distantes de Toulouse, ville située dans la province romaine. II comprit que, si cela arrivait, cette province serait exposée à un grand péril, ayant pour voisins, dans un pays fertile et découvert, des hommes belliqueux, ennemis du peuple romain. Il confie donc à son lieutenant T. Labiénus la garde du retranchement qu'il avait élevé. Pour lui, il va en Italie à grandes journées, y lève deux légions, en tire trois de leurs quartiers d'hiver, aux environs d'Aquilée, et prend par les Alpes le plus court chemin de 1a Gaule ultérieure, à la tête de ces cinq légions. Là, les Ceutrons, les Graïocèles et les Caturiges, qui s'étaient emparés des hauteurs, veulent arrêter la marche de son armée. II les repousse dans plusieurs combats, et se rend, en sept journées, d'Océlum, dernière place de la province citérieure, au territoire des Voconces, dans la province ultérieure ; de là il conduit ses troupes dans le pays des Allobroges, puis chez les Ségusiaves. C'est le premier peuple hors de la province, au-delà du Rhône.

    Déjà les Helvètes avaient franchi les défilés et le pays des Séquanes ; et, arrivés dans celui des Héduens, ils en ravageaient les terres. Ceux-ci, trop faibles pour défendre contre eux leurs personnes et leurs biens, députent vers César, pour lui demander du secours : "Dans toutes les circonstances, ils avaient trop bien mérité du peuple romain pour qu'on laissât, presque à la vue de notre armée, dévaster leurs champs, emmener leurs enfants en servitude, prendre leurs villes. Dans le même temps, les Ambarres, amis et alliés des Héduens, informent également César que leur territoire est ravagé et qu'ils peuvent à peine garantir leurs villes de la fureur de leurs ennemis. Enfin les Allobroges, qui avaient des bourgs et des terres au-delà du Rhône, viennent se réfugier auprès de lui, et lui déclarent qu'il ne leur reste rien que le sol de leurs champs. César, déterminé par ce concours de plaintes, crut ne devoir pas attendre que tous les pays des alliés fussent ruinés, et les Helvètes arrivés jusque dans celui des Santons.

Les Helvètes passent la Saône. Défaite des Tigurins

    La Saône est une rivière dont le cours, entre les terres des Héduens et celles des Séquanes et jusqu'au Rhône, est si paisible que l'oeil ne peut en distinguer la direction. Les Helvètes la passaient sur des radeaux et des barques jointes ensemble. César, averti par ses éclaireurs que les trois quarts de l'armée helvète avaient déjà traversé la Saône, et que le reste était sur l'autre rive, part de son camp, à la troisième veille, avec trois légions, et atteint ceux qui n'avaient pas encore effectué leur passage. Il les surprend en désordre, les attaque à l'improviste et en tue un grand nombre. Les autres prennent la fuite, et vont se cacher dans les forêts voisines. Ils appartenaient au canton des Tigurins ; car tout le territoire de l'Helvétie est divisé en quatre cantons. C'étaient ceux de ce canton qui, dans une excursion du temps de nos pères, avaient tué le consul L. Cassius et fait passer son armée sous le joug. Ainsi, soit effet du hasard, soit par la volonté des dieux immortels, cette partie des citoyens de l'Helvétie, qui avait fait éprouver une si grande perte au peuple romain, fut la première à en porter la peine. César trouva aussi dans cette vengeance publique l'occasion d'une vengeance personnelle ; car l'aïeul de son beau-père, L. Pison, lieutenant de Cassius, avait été tué avec lui par les Tigurins, dans la même bataille.

Ambassade de Divico

    Après ce combat, César, afin de poursuivre le reste des Helvètes, fait jeter un pont sur la Saône et la traverse avec son armée. Ceux-ci, effrayés de son arrivée soudaine, et voyant qu'il lui avait suffi d'un seul jour pour ce passage qu'ils avaient eu beaucoup de peine à effectuer en vingt jours, lui envoient des députés ; à la tête de cette députation était Divico, qui commandait les Helvètes à la défaite de Cassius. Il dit à César que, "si le peuple romain faisait la paix avec eux, ils se rendraient et s'établiraient dans les lieux que leur aurait assignés sa volonté ; mais que, s'il persistait à leur faire la guerre, il eût à se rappeler l'échec passé de l'armée romaine et l'antique valeur des Helvètes ; que pour s'être jeté à l'improviste sur un seul canton, lorsque leurs compagnons, qui avaient passé la rivière, ne pouvaient lui porter secours, il ne devait nullement attribuer cet avantage à son courage, ni concevoir du mépris pour eux ; qu'ils avaient appris de leurs pères et de leurs ancêtres à se fier à leur valeur plutôt qu'à la ruse et que d'avoir recours aux embuscades ; qu'il prît donc garde que ce lieu où ils se trouvaient, marqué par le désastre des Romains et la destruction de leur armée, n'en tirât son nom et n'en transmit le souvenir à la postérité."

    À ce discours César répondit "qu'il était loin d'avoir oublié les choses que lui rappelaient les députés helvètes, et que son ressentiment en était d'autant plus vif que les Romains avaient moins mérité leur malheur ; que s'ils eussent pu se douter de quelque injure, il leur était facile de se tenir sur leurs gardes ; mais qu'ils avaient été surpris parce que, n'ayant rien fait qui dût leur inspirer des craintes, ils ne pouvaient en concevoir sans motif. Quand même César voudrait bien oublier cette ancienne injure, pourrait-il aussi effacer de son souvenir celles qui étaient récentes ; les efforts qu'ils avaient faits pour traverser malgré lui la province romaine, et leurs ravages chez les Héduens, chez les Ambarres, chez les Allobroges ? L'insolente vanité qu'ils tiraient de leur victoire, et leur étonnement de voir leurs outrages si longtemps impunis, lui démontraient que les dieux immortels, afin de rendre, par un revers subit, un châtiment plus terrible, accordent souvent à ceux-là même qu'ils veulent punir des succès passagers et une plus longue impunité. Quoi qu'il en soit, s'ils lui livrent des otages comme garants de leurs promesses, et s'ils donnent aux Héduens, à leurs alliés et aux Allobroges, satisfaction du tort qu'ils leur ont fait, il consent à conclure avec eux la paix." Divico répondit "qu'ils tenaient de leurs pères la coutume de recevoir des otages, et de n'en point donner ; que le peuple romain devait le savoir."

César suit les Helvètes. Combats d'arrière-garde

    Après cette réponse, il se retira. Le lendemain, ils lèvent leur camp ; César en fait autant, et envoie en avant toute sa cavalerie, au nombre de quatre mille hommes, qu'il avait levés dans la province entière, chez les Héduens et chez leurs alliés. Elle devait observer la direction que prendraient les ennemis. Cette cavalerie, ayant poursuivi leur arrière-garde avec trop d'ardeur, en vint aux mains avec la cavalerie helvète dans un lieu désavantageux et éprouva quelque perte. Les Helvètes, fiers d'avoir dans cette rencontre repoussé avec cinq cents chevaux un si grand nombre de cavaliers, nous attendirent plus hardiment, et nous inquiétèrent quelquefois avec leur arrière-garde. César retenait l'ardeur de ses soldats, et se contentait pour le moment de s'opposer aux rapines, au pillage et aux dévastations de l'ennemi. On fit route ainsi durant quinze jours, sans que l'arrière-garde des Helvètes fût séparée de notre avant-garde de plus de cinq ou six mille pas.

Mauvaise volonté des Héduens. Diviciacos et Liscos dénoncent Dumnotrix

Cependant César pressait chaque jour les Héduens de lui livrer le blé qu'ils lui avaient promis ; car le climat froid de la Gaule, située au nord, comme il a été dit précédemment, faisait non seulement que la moisson n'était pas parvenue, dans les campagnes, à sa maturité, mais que le fourrage même y était insuffisant ; quant au blé qu'il avait fait charger sur la Saône, il pouvait d'autant moins lui servir, que les Helvètes s'étaient éloignés de cette rivière, et il ne voulait pas les perdre de vue. Les Héduens différaient de jour en jour, disant qu'on le rassemblait, qu'on le transportait, qu'il était arrivé. Voyant que ces divers discours se prolongeaient trop, et touchant au jour où il fallait faire aux soldats la distribution des vivres, César convoqua les principaux Héduens, qui étaient en grand nombre dans le camp, entre autres Diviciacos et Liscos. Ce dernier occupait la magistrature suprême que les Héduens appellent vergobret, fonctions annuelles et qui confèrent le droit de vie et de mort. César se plaint vivement à eux de ce que, ne pouvant acheter des vivres ni en prendre dans les campagnes, il ne trouve, dans un besoin si pressant et presque en présence de l'ennemi, aucun secours dans des alliés ; l'abandon où ils le laissaient était d'autant plus coupable, que c'était en grande partie à leur prière qu'il avait entrepris la guerre.
"""


# building the corpus

RAW_TEXTS = (
    ('aquariophilie', A_TEXT),
    ('godel', G_TEXT),
    ('guerre', GG_TEXT),
)
# Corpus plural is "Corpora"
# CORPORA has the following structure:
# {'corpus_name': ("Sentence1", "Sentence2"),
# }
CORPORA = {}
for corpus_name, text in RAW_TEXTS:
    paragraphs = text.split('\n\n')
    sentences = []
    for p in paragraphs:
        sentences += (p.split('. '))
    sentences = tuple(sentences)
    CORPORA[corpus_name] = sentences

def randomSentences(corpus=None):
    """Returns a list of sentences as a list object.
    """
    if corpus is None:
        corpus_name = choice(CORPORA.keys())
        corpus = CORPORA[corpus_name]
    start = randint(0, len(corpus))
    end = start + 3
    return corpus[start:end]

def randomSentence(corpus=None):
    """Returns a sentence as a string.
    """
    if corpus is None:
        corpus_name = choice(CORPORA.keys())
        corpus = CORPORA[corpus_name]
    return choice(corpus)

def randomWords(n=None, corpus=None):
    """Returns n words as a list object.
    """
    if n is None:
        n = randint(3, 10)
    sentence = randomSentence(corpus=corpus)
    sentence = sentence.strip()
    sentence = [not l in string.punctuation and l or ' ' for l in sentence ]
    sentence = ''.join(sentence)
    words = sentence.split()
    return words[:n]

def randomWord(corpus=None):
    words = randomWords(corpus=corpus)
    return choice(words)

def randomParagraph(n=None, corpus=None):
    if n is None:
        n = randint(3, 10)
    return '. '.join([randomSentence(corpus=corpus) for _ in xrange(n)])

def randomText(n=3, corpus=None):
    return '\n\n'.join([randomParagraph(randint(3, 6), corpus=corpus)
                        for _ in xrange(n)])

def randomCorpus(self):
    return choice(CORPORA.keys())

