<h2>Zespół nr: 1 </h2>
<b>
Skład zespołu wraz z funkcjami:<br />
Jakub Obarowski – przywódca<br />
Dorota Harasimiuk - sekretarz<br />
Marcel Tutak - zastępca<br /><br />
![kraina](https://github.com/obarowskij/AiSD/assets/146991219/70d9dfba-e964-468b-bb6d-59a82b36d572)
(obraz autorstwa Doroty Harasimiuk)

 <table>
  <tr>
    <th>L.p</th>
    <th>Specyfikacja problemu (dane i wyniki)</th>
    <th>Do jakich treści w zadaniu odnosi się algorytm</th>
    <th>Zastosowane struktury danych </th>
    <th>Informacje o zastosowanym algorytmie</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Dane: zbiór punktów orientacyjnych tworzących obszar Krainy <br />
     Wynik: bliczenie otoczki wypukłej Krainy</td>
    <td>Zdefiniowanie obszaru w którym żyją płaszczaki na Stronie</td>
    <td>stos, klasa, listy</td>
    <td>Algorytm Grahama - wpierw losujemy punkty obserwacyjne i sortujemy je biegunowo. Później wkładamy je na stos i mamy gotową wypukłą otoczkę, którą zwizualiujemy biblioteką matplotlib</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Dane: Tragarze przedstawieni jako punkty w przestrzeni, gdzie każdy tragarz reprezentowany jest przez dwa punkty (np. jeden punkt to położenie tragarza, a drugi to położenie jego rąk, przy założeniu pewnej ustalonej odległości między nimi)<br />
     Wynik: Lista tragarzy, którzy mogą współpracować ze sobą przy transporcie odcinków z fabryki</td>
    <td>Dobranie tragarzy do transportu odcinków z fabryki</td>
    <td>listy?</td>
    <td>Geometria obliczeniowa na płaszczyźnie</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>Dane: Otoczka wypukła Krainy oraz lista tragarzy gotowych do współpracy<br />
     Wynik: Minimalny czas potrzebny do zbudowania płotu wokół Krainy</td>
    <td>Zbudowanie płotu wokół Krainy</td>
    <td>kolejka, klasa</td>
    <td>Mając otoczkę grahama przedstawiamy to jako sieć przepływową i aby znaleźć, ile razy płaszczaki muszą się zbierać do budowy płotu, możemy użyć algorytmu Forda-Fulkersona, aby znaleźć maksymalny przepływ z punktu źródłowego (gdzie zaczynają się prace budowlane) do punktu ujściowego (gdzie prace się kończą), uwzględniając ograniczenia przepustowości na krawędziach.
Ostatecznie, maksymalny przepływ w tej sieci przepływowej będzie reprezentować maksymalną liczbę tragarzy, które mogą być przenoszone od fabryki do miejsca budowy płotu, co pośrednio może odzwierciedlać, ile razy płaszczaki muszą się zbierać, aby zbudować płot.</td>
  </tr>
  <tr>
    <td>4.</td>
    <td>Dane: Ciąg znaków reprezentujący zmienioną melodię (opowieść-melodia) oraz ciąg znaków zawierający zmienioną wersję melodi, gdzie jedna litera została zastąpiona przez inną (koszmarna-melodia)<br />
    Wynik: Oryginalna melodia</td></td>
    <td>Znalezienie oryginalnej melodii</td>
    <td>Lista</td>
    <td>Algorytm Rabina-Karpa, Algorytm KMP</td>
  </tr>
  <tr>
    <td>5.</td>
    <td>Dane: Ciąg znaków a1a2...an reprezentujący opowieść-melodię<br />
     Wynik: Ustalenie kodowania dla ciągu znaków, umożliwiającego kompresję danych</td>
    <td>Problem niewystarczającej ilości pamięci na komputerze informatyka płaszczaka</td>
    <td>słowniki</td>
    <td>Huffman - polega na analizie częstotliwości występowania liter w zdaniu i na tej podstawie przypisywaniu skróconych kodów dla symboli</td>
  </tr>
  <tr>
    <td>6.</td>
    <td>Dane: opowieść-melodia <br />
     Wynik: indeks potencjalnego podmienionego znaku w melodii</td>
    <td>ewentualnej zamiana innych fragmentów opowieści-melodii</td>
    <td>-----------</td>
    <td>-----------</td>
  </tr>
   <tr>
    <td>7.</td>
    <td>Dane: Lista strażników wraz z ich datami urlopu<br />
     Wynik: Harmonogram pracy strażników ustawiany według minimalnej liczby odsłuchań melodii w trakcie pracy</td>
    <td>Potrzeba ochrony płotu</td>
    <td>-----------</td>
    <td>-----------</td>
  </tr>
</table> 
<br />
input krainy: GRAF - lista punktów <br />
tragarz: 1) rece: przod/tyl 2) lista kogo lubi (wiemy ilu wygenerowalismy tutaj)<br />
strażnik: 1) energia 2) urlop?<br />
Potencjalnie dodać płaszczaki klase z której te dwie dziedziczą i dodać imiona(jakąś identyfikacje)<br /><br />
<h1> Sekcja Problemów z problemami....... </h1>

<h2> Problem 4 </h2><br />
Informatyk próbował już zapisać te melodie na kompa tylko mu nie starczylo miejsca. zakładamy że znamy te melodie? i pewnie też znamy aktualną popsutą piosenkę. Więc po co nam wyszukiwanie wzorca. idk do zapytania <br/ >
clueless???<br />
</b>

