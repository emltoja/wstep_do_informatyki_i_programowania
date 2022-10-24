# Zadanie 2 Lista 3

import matplotlib.pyplot as plt

letters = 'qwertyuiopasdfghjklzxcvbnmąęóćżźłńść'

text = '''nauka dostarczająca narzędzi do otrzymywania ścisłych wniosków z przyjętych założeń[1], zatem dotycząca prawidłowości rozumowania. Ponieważ ścisłe założenia mogą dotyczyć najróżniejszych dziedzin myśli ludzkiej, a muszą być czynione w naukach ścisłych, technice, a nawet w naukach humanistycznych, zakres matematyki jest szeroki i stale się powiększa.
Wiele dziedzin nauki i technologii w pewnym momencie zaczyna definiować swoje pojęcia z dostatecznie dużą precyzją, aby można było stosować do nich metody matematyczne, co często zapoczątkowuje kolejny dział matematyki teoretycznej lub stosowanej. Tak stało się np. z mechaniką klasyczną, mechaniką statystyczną, ekonomią (ekonometria), lingwistyką (lingwistyka matematyczna), teorią gier, a nawet niektórymi działami politologii (teoria głosowań). Obecnie standardem w naukach eksperymentalnych jest potwierdzanie istnienia obserwowanych zależności za pomocą metod statystyki, będącej działem matematyki. Pomaga to odróżnić rzeczywiste zależności od przypadkowej zbieżności. Leonardo da Vinci stwierdził w Traktacie o malarstwie: „Żadne ludzkie badania nie mogą być nazywane prawdziwą nauką, jeśli nie mogą być zademonstrowane matematycznie”.
Matematyka teoretyczna, nazywana czasami matematyką czystą, jest często rozwijana bez wyraźnego związku z konkretnymi zastosowaniami. W tej odmianie jest ona przez niektórych matematyków uważana za formę sztuki[a]. Jednak niektóre działy matematyki teoretycznej znalazły swoje praktyczne zastosowanie, kiedy okazało się, że potrzebuje ich nowoczesna fizyka lub informatyka. Szkolne rozumienie matematyki jako nauki wyłącznie o liczbach i pojęciach geometrycznych zdezaktualizowało się już w XIX wieku wraz z postępami algebry i teorii mnogości.
•	Paul Dirac stwierdził: „Matematyka jest narzędziem stworzonym specjalnie do wszelkich abstrakcyjnych koncepcji i nie ma ograniczeń dla jej potęgi w tym zakresie”[2].
•	Benjamin Peirce nazwał ją „nauką, która wyciąga właściwe wnioski”[3].
•	Henri Poincaré określił matematykę jako „sztukę nadawania takich samych nazw różnym rzeczom”[4]. Oddaje to jedną z piękniejszych cech matematyki, zdolnej uogólniać właściwości i czynić analogie między bardzo odległymi i wydawałoby się mało ze sobą związanymi obiektami.
•	David Hilbert uznał, że „sztuka uprawiania matematyki zawiera się w znajdowaniu szczególnych przypadków, które zawierają w sobie zalążki uogólnień”[5].
•	Poeta William Wordsworth stwierdził: „Matematyka jest niezależnym światem stworzonym przez czystą inteligencję”[6].
•	Z czasem niektóre działy matematyki stały się odrębnymi światami, uprawianymi wyłącznie dla ich piękna, bez jakiegokolwiek związku z rzeczywistością. Henry John Stephen Smith stwierdził wprost „Czysta matematyka, oby nigdy nie była przez nikogo używana”[7].
•	Z drugiej strony Nikołaj Łobaczewski uznał, że „Nie ma gałęzi matematyki, choćby nie wiem jak abstrakcyjnej, która pewnego dnia nie zostałaby zastosowana do zjawisk realnego świata”[8]. Wyprzedził tą wypowiedzią o pół wieku postępy fizyki, która stosuje w praktyce działy matematyki, przed jej epoką uważane za domenę czystej myśli, niezbrukanej zastosowaniami.
•	Immanuel Kant stwierdził: „Matematyka jest najjaskrawszym przykładem, jak czysty rozum może skutecznie rozszerzać swoją domenę bez jakiejkolwiek pomocy doświadczenia”[9].
Matematyka jest sztuką wyciągania wniosków z założeń. Jeśli rozumowanie matematyczne jest poprawne, to przy poprawnych założeniach istnieje pewność otrzymania poprawnych wniosków. Jeśli w rozumowaniu jest jakakolwiek nieścisłość, takiej gwarancji nie ma. Stąd wynika olbrzymi nacisk, kładziony w matematyce na ścisłość rozumowania. W utrzymaniu tej ścisłości pomaga omawiany dalej formalizm logiczny oraz zapis matematyczny.
Nie znaczy to, że w matematyce wyobraźnia, głębia, czy intuicja nie są ważne. Matematyka nie może sensownie istnieć bez aparatu formalnego, ale formalizm tworzy tylko ramy dla inwencji i twórczego myślenia matematyka, podobnie jak gramatyka języka tworzy ramy dla inwencji pisarza. Formalizm, choćby w praktyce tylko przybliżony, jest metodą obiektywnego porozumiewania się matematyków. Można używać do omawiania pojęć matematycznych zwykłego języka naturalnego, jednak ma to sens tylko tak długo, jak długo da się taki opis jednoznacznie przetłumaczyć na formalizm (nawet jeśli to tłumaczenie nie jest w praktyce wykonane).
Formalna struktura matematyki wygląda następująco:
•	Wybierany jest tzw. alfabet złożony ze skończonej liczby rozróżnialnych znaków (np. liter, cyfr, znaków matematycznych itp.).
•	Tworzony jest język formalny, na który składają się słowa złożone ze znaków alfabetu.
•	Słowa tworzą wyrażenia, w tym zdania. Praktyczne teorie powinny pozwalać na mechaniczne (algorytmiczne) sprawdzanie, które ciągi symboli tworzą poprawnie zbudowane zdania oraz mieć jednoznaczną, dającą się algorytmicznie rozpoznać składnię[d].
•	Formalne języki służą za podstawę teoriom formalnym (wciąż ogólniejszym od matematycznych). Teoria formalna oprócz języka wprowadza pojęcie twierdzenia (specjalny rodzaj zdań poprawnie zbudowanych) i reguł dowodzenia.
•	Jedną z teorii formalnych jest logika matematyczna. Te z formalnych teorii, które zawierają logikę matematyczną, nazywane są teoriami matematycznymi. Większość teorii matematycznych zawiera też teorię mnogości. Wraz z logiką matematyczną (klasyczną) przychodzi formalne pojęcie prawdy, które można zdefiniować na wiele sposobów.
•	Teorią matematyczną nazywany jest formalnie dowolny niesprzeczny zbiór zdań. W praktyce z symboli języka formalnego wydziela się tzw. pojęcia pierwotne[e]. Na tym etapie o pojęciach pierwotnych nic jeszcze nie wiadomo. Na przykład pojęciami pierwotnymi dwuwymiarowej geometrii euklidesowej są punkt, prosta i relacja incydencji („punkt leży na prostej”, bądź „prosta zawiera punkt” – bez wyróżniania prostej, czy punktu).
•	Zwykle budowana jest tzw. aksjomatyka, czyli wyróżniany jest zestaw zdań zwanych aksjomatami, mówiących o relacjach między pojęciami pierwotnymi[f]. Dla geometrii euklidesowej jednym z aksjomatów jest zdanie: „Przez każde dwa punkty można przeprowadzić prostą”.
•	Używając reguł wnioskowania, można rozpoczynając od aksjomatów dowodzić rozmaitych twierdzeń danej teorii.
•	Teoria nie musi (i nie może) w żaden sposób odnosić się do innych cech pojęć pierwotnych niż te, które zostały wyrażone przez aksjomaty lub z nich wynikają. Jeśli jakieś pojęcia zostaną zdefiniowane w taki sposób, aby podstawione w miejsce pojęć pierwotnych teorii spełniały jej aksjomaty – operacja ta nazywa się interpretacją – twierdzenia teorii będą prawdziwe także dla tych nowo zdefiniowanych pojęć. Taki zestaw interpretacji pojęć pierwotnych nazywany jest modelem danej teorii. Modelem płaskiej geometrii euklidesowej jest np. kartezjański układ współrzędnych (ściślej tzw. przestrzeń kartezjańska), gdzie punkt interpretowany jest jako para liczb rzeczywistych (zwanych współrzędnymi), prosta – jako zbiór punktów   spełniających dla pewnych punktów   oraz   równanie   natomiast relację incydencji interpretuje się jako relację przynależności do tego zbioru.
•	Powyżej teoria matematyczna była opisywana z bardzo formalnego punktu widzenia, tzn. przez pryzmat operacji na symbolach matematycznych. Matematycy jednak zwykle nie wyobrażają sobie matematyki w ten sposób. Rozumują raczej w kategoriach przestrzeni i struktur, składających się z pewnego zbioru elementów (np. liczb) oraz działań i relacji między nimi (np. relacje porządku i działania algebraiczne). Zbiory wraz z różnego rodzaju powiązaniami pomiędzy ich elementami zwane są właśnie strukturami lub przestrzeniami. Na poziomie formalnym pojęcia te są synonimami pojęcia modelu, jednak koncepcyjnie podejście to ułatwia skoncentrowanie się na bardziej uchwytnych obiektach (elementach przestrzeni), niż na formalnych manipulacjach symbolami.
W praktyce matematycy nie przejmują się zanadto powyższym formalizmem podczas rozszerzania danej teorii (a więc, formalnie, tworzenia nowej). Poprawne (w sensie praktycznym) dowody matematyczne są jednak w odczuciu matematyków sprowadzalne do dowodów formalnych. Obecnie rozwija się formalizację matematyki opartą na metodach informatycznych, która pozwala na pełny formalny zapis dowodów dający się stosować w praktyce[g].
Chociaż działalność matematyczna polega na tworzeniu nowych pojęć matematycznych i dowodzeniu twierdzeń na temat pojęć już znanych, to taka definicja nie oddałaby wszelakich niuansów uprawiania matematyki. Jak stwierdził Gian-Carlo Rota: „Często słyszymy, że matematyka sprowadza się głównie do «dowodzenia twierdzeń». Czy praca pisarza sprowadza się głównie do «pisania zdań»?”[12]
'''

# Funkcja liczaca czestosc wystepowania danej litery w tekscie
def count_chars(text):
    text = text.lower()
    result = []
    for letter in letters:
        result.append([text.count(letter), letter])
    result.sort(reverse=True)
    return result

# Funkcja tworząca histogram 10 najczesciej wystepujacych liter w teksci
def plot_(values):
    xaxis = []
    yaxis = []
    for i in range(10):
        xaxis.append(values[i][1])
        yaxis.append(values[i][0])
    plt.bar(xaxis, yaxis)
    plt.show()

# Wyswietlenie wykresu
plot_(count_chars(text))
