<h2>Zespół nr: 1 </h2>
<b>
Skład zespołu wraz z funkcjami:<br />
Jakub Obarowski – przywódca<br />
Dorota Harasimiuk - sekretarz<br />
Marcel Tutak - zastępca<br /><br />

 <table>
  <tr>
    <th>L.p</th>
    <th>Specyfikacja problemu (dane i wyniki)</th>
    <th>Do jakich treści w zadaniu odnosi się algorytm</th>
    <th>Zastosowane struktury danych | Informacje o zastosowanym algorytmie</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Dane: tragarze <br />
     Wynik: tragarze dobrani w pary</td>
    <td>Dobranie tragarzy do transportu odcinków z fabryki</td>
    <td>listy?</td>
    <td>Geometria obliczeniowa na płaszczyźnie</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Dane: odcinki, świat(graf, punkty) <br />
     Wynik: najkrótsza droga</td>
    <td>Budowa płotu</td>
    <td>listy?</td>
    <td>Algorytm Jarvisa, Algorytm Grahama</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>Dane: ciag znakow „a1a2a3…an” <br />
     Wynik: ciag znakow zamieniony „ba2a3…an”</td>
    <td>Zapisanie melodii w komputerze</td>
    <td>-----------</td>
    <td>-----------</td>
  </tr>
  <tr>
    <td>4.</td>
    <td>Dane: ciag znakow  <br />
     Wynik: : ciag znakow zamieniony nie tylko pierwszy znak</td>
    <td>Inne zmiany w melodii</td>
    <td>-----------</td>
    <td>-----------</td>
  </tr>
  <tr>
    <td>5.</td>
    <td>Dane: strażnik, droga(graf) <br />
     Wynik: grafik strażników dla najmniejszej ilości odsłuchań</td>
    <td>Pilnowanie płotu przed inwazją</td>
    <td>-----------</td>
    <td>-----------</td>
  </tr>
</table> 
<br />
input krainy: GRAF - lista punktów <br />
tragarz: 1) rece: przod/tyl 2) lista kogo lubi (wiemy ilu wygenerowalismy tutaj)<br />
strażnik: 1) energia 2) urlop?<br />
Potencjalnie dodać płaszczaki klase z której te dwie dziedziczą i dodać imiona(jakąś identyfikacje)<br /><br />

<h2>Problem 1</h2><br />
Dobieramy tragarzy po listach kto kogo lubi i ich zwrot.<br />
Dajemy do listy<br />
Specyfikacja: Chociaż jedna para tragarzy musi się lubić i mieć zwrot, który pozwala im współpracować<br /><br />

<h2>Problem 2</h2> <br />
Znajdujemy punkty graniczne które określają kształt krainy, liczymy odległości pomiędzy nimi – wielkość płotu. Losujemy miejsce fabryki(nie może znajdować się na obszarze tekstu) i obliczamy po kolei odległości do punktów granicznych i ile odcinków trzeba wysłać żeby zbudować płot.<br />
Założenia: z jednego punktu granicznego można zbudować płot w dwóch kierunkach, tzn. gdy punkty ABC, są sąsiednie to z punktu B można zbudować drogę do A i do C. Zaczynamy od najkrótszych dróg.<br />
Specyfikacja: Fabryka znajduje się w Krainie<br />
</b>


