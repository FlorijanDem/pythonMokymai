Tikslas
Išmokti naudoti super() ir papildyti paveldėtą klasę naujais atributais.
Užduotis
Sukurkite klasę Employee, kuri saugotų:
vardą;
pavardę;
mėnesinį atlyginimą.
Klasėje sukurkite metodus:
display_info();
calculate_monthly_salary().
Sukurkite dvi paveldinčias klases:
Manager
Papildomai saugo mėnesinį priedą.
Vadovo mėnesinis atlyginimas:
bazinis atlyginimas + priedas
HourlyEmployee
Papildomai saugo:
valandinį atlyginimą;
per mėnesį dirbtų valandų skaičių.
Darbuotojo atlyginimas:
valandinis atlyginimas × dirbtos valandos
Sukurkite kelis skirtingus darbuotojus ir apskaičiuokite jų atlyginimus.
Papildomas reikalavimas
Visus darbuotojus laikykite viename sąraše ir jų atlyginimus apskaičiuokite naudodami tą patį metodą.
Patarimai
Tai yra polimorfizmo pavyzdys.
Abiejų vaikų klasių metodas gali vadintis vienodai, nors skaičiavimas skiriasi.


3. Figūrų plotų skaičiuotuvas
Tikslas
Sukurti bendrą klasės struktūrą objektams, kurių skaičiavimai skiriasi.
Užduotis
Sukurkite bazinę klasę Shape, turinčią metodus:
calculate_area();
calculate_perimeter();
display_info().
Sukurkite paveldinčias klases:
Rectangle;
Square;
Circle;
Triangle.
Kiekviena klasė turi turėti tik jai reikalingus matmenis ir tinkamai apskaičiuoti plotą bei perimetrą.
Sudėkite visas figūras į bendrą sąrašą. Programa turi:
parodyti kiekvienos figūros informaciją;
apskaičiuoti kiekvienos figūros plotą;
apskaičiuoti kiekvienos figūros perimetrą;
surasti didžiausią plotą turinčią figūrą;
apskaičiuoti bendrą visų figūrų plotą.
Papildomas reikalavimas
Programa neturi kiekvienai figūrai rašyti atskiro tikrinimo:
if isinstance(shape, Rectangle):
Skaičiavimai turi veikti dėl vienodai pavadintų metodų.
Patarimai
Apskritimo skaičiavimams naudokite math.pi.
Prieš skaičiuodami trikampio plotą patikrinkite, ar toks trikampis gali egzistuoti.
Pagalvokite, ką turėtų daryti bazinės klasės metodai, jeigu jie nėra perrašyti.




4. Banko sąskaitų sistema
Tikslas
Praktiškai panaudoti enkapsuliaciją ir kontroliuoti objekto duomenų keitimą.
Užduotis
Sukurkite klasę BankAccount, turinčią:
savininko vardą;
sąskaitos numerį;
privatų balansą.
Balansas negali būti tiesiogiai keičiamas iš objekto išorės.
Sukurkite metodus:
deposit(amount) – papildyti sąskaitą;
withdraw(amount) – išimti pinigus;
get_balance() – gauti dabartinį balansą;
display_info() – parodyti sąskaitos informaciją.
Sukurkite dvi paveldinčias klases:
SavingsAccount
turi metinę palūkanų normą;
turi metodą, kuris prideda vienų metų palūkanas.
CreditAccount
gali turėti neigiamą balansą;
turi nustatytą kredito limitą;
negali viršyti kredito limito.
Programos veikimas
Sukurkite bent keturias sąskaitas ir atlikite skirtingas operacijas:
sėkmingą įnešimą;
sėkmingą išėmimą;
bandymą išimti per daug pinigų;
palūkanų pridėjimą;
kredito limito patikrinimą.
Patarimai
Patikrinkite, ar įnešama suma yra teigiama.
Negalima leisti naudotojui parašyti account.__balance = 100000.
Paveldinčiai klasei gali reikėti naudotis tėvinės klasės metodais, o ne tiesiogiai keisti privatų atributą.
5. Pranešimų siuntimo sistema
Tikslas
Suprasti, kaip vienodas metodas gali turėti visiškai skirtingas realizacijas.
Užduotis
Sukurkite klasę Notification, turinčią metodą:
send(message)
Sukurkite paveldinčias klases:
EmailNotification;
SMSNotification;
PushNotification.
Kiekviena klasė turi:
saugoti jai reikalingą gavėjo informaciją;
skirtingai realizuoti metodą send();
patikrinti, ar žinutė nėra tuščia;
parodyti, kokiu kanalu ir kam pranešimas buvo siunčiamas.
Pavyzdžiui, el. pašto pranešimas gali turėti gavėjo adresą ir temos pavadinimą, o SMS – telefono numerį.
Programos veikimas
Sukurkite kelių tipų pranešimų objektus.
Sudėkite juos į bendrą sąrašą.
Naudodami ciklą išsiųskite tą patį pranešimą visais kanalais.
Suskaičiuokite, kiek pranešimų buvo išsiųsta sėkmingai.
Papildoma dalis
Vienas pranešimo kanalas kartais turi nepavykti. Tokiu atveju metodas turi grąžinti informaciją, ar siuntimas pavyko.
Patarimai
Metodas gali ne tik spausdinti tekstą, bet ir grąžinti True arba False.
Pagrindinė programa neturi žinoti, kaip techniškai veikia kiekvienas pranešimų tipas.


6. Bibliotekos leidinių valdymas
Tikslas
Sujungti paveldėjimą, enkapsuliaciją, objektų būsenas ir polimorfizmą.
Užduotis
Sukurkite bazinę klasę LibraryItem, kuri saugotų:
unikalų ID;
pavadinimą;
išleidimo metus;
informaciją, ar leidinys šiuo metu paskolintas;
asmenį, kuris jį pasiskolino.
Sukurkite paveldinčias klases:
Book;
Magazine;
AudioBook.
Papildomi atributai:
knyga turi autorių ir puslapių skaičių;
žurnalas turi leidimo numerį;
audioknyga turi autorių ir trukmę minutėmis.
Sukurkite metodus:
borrow(reader_name);
return_item();
display_info();
get_late_fee(days_late).
Baudos skaičiavimo taisyklės turi skirtis pagal leidinio tipą.
Programos veikimas
Sukurkite bibliotekos kolekciją, kuri leistų:
pridėti leidinį;
pašalinti leidinį;
ieškoti pagal pavadinimą;
išduoti leidinį skaitytojui;
grąžinti leidinį;
parodyti visus laisvus leidinius;
parodyti visus paskolintus leidinius;
apskaičiuoti vėlavimo baudą.
Svarbios taisyklės
Jau paskolinto leidinio negalima paskolinti dar kartą.
Nepaskolinto leidinio negalima grąžinti.
Dviejų leidinių ID negali sutapti.
Leidinio būsenos neturėtų būti galima nekontroliuojamai pakeisti iš išorės.
Patarimai
Atskirai sukurkite klasę Library, kuri valdytų leidinių sąrašą.
LibraryItem atsako už vieną leidinį, o Library – už visą kolekciją.
Tai padeda atskirti objektų atsakomybes.
7. Internetinės parduotuvės prekių ir nuolaidų sistema
Tikslas
Išmokti projektuoti kelias bendradarbiaujančias klases ir vengti didelių if konstrukcijų.
Užduotis
Sukurkite bazinę klasę Product, kuri turėtų:
produkto ID;
pavadinimą;
kainą;
sandėlyje esantį kiekį.
Sukurkite paveldinčias klases:
PhysicalProduct;
DigitalProduct;
SubscriptionProduct.
Papildomos savybės:
fizinė prekė turi svorį ir pristatymo kainą;
skaitmeninė prekė turi failo dydį;
prenumerata turi galiojimo laikotarpį mėnesiais.
Kiekviena prekė turi turėti metodą:
calculate_final_price()
Galutinė kaina turi būti apskaičiuojama skirtingai:
fizinei prekei pridedamas pristatymas;
skaitmeninei prekei pristatymas netaikomas;
prenumeratai kaina gali priklausyti nuo mėnesių skaičiaus.
Sukurkite klasę ShoppingCart
Ji turi leisti:
pridėti produktą ir jo kiekį;
pašalinti produktą;
pakeisti produkto kiekį;
apskaičiuoti bendrą kainą;
patikrinti sandėlio likutį;
atlikti pirkimą;
sumažinti nupirktų prekių likučius.
Papildomos sąlygos
Neleiskite nupirkti daugiau fizinių prekių, nei yra sandėlyje.
Skaitmeninėms prekėms sandėlio ribojimas gali būti netaikomas.
Neleiskite įvesti neigiamos kainos arba kiekio.
Krepšelis turi veikti su visais produktų tipais.
Sudėtingesnė dalis
Sukurkite atskirą nuolaidų sistemą:
procentinė nuolaida;
fiksuotos sumos nuolaida;
nemokamas fizinių prekių pristatymas.
Nuolaidos neturi būti įrašytos kaip vienas didelis if blokas ShoppingCart klasėje.
Patarimai
Nuolaidą taip pat galima vaizduoti kaip objektą.
Prekės objektas turi apskaičiuoti savo kainą.
Krepšelis turi valdyti produktų rinkinį, o ne spręsti kiekvieno produkto vidines taisykles.
8. Transporto parko valdymo sistema
Tikslas
Sukurti platesnę sistemą, kurioje panaudojami beveik visi šiandien nagrinėti objektinio programavimo principai.
Užduotis
Sukurkite transporto parko sistemą įmonei, kuri valdo:
automobilius;
motociklus;
sunkvežimius;
elektrines transporto priemones.
Bazė turi būti klasė Vehicle.
Kiekviena transporto priemonė turi saugoti:
unikalų ID;
gamintoją;
modelį;
pagaminimo metus;
dabartinę ridą;
informaciją, ar transporto priemonė šiuo metu naudojama;
kuro arba baterijos likutį.
Skirtingos klasės
Car
turi durų skaičių;
naudoja kurą.
Motorcycle
gali turėti šoninę priekabą;
naudoja kurą.
Truck
turi didžiausią krovinio svorį;
turi saugoti dabartinį krovinio svorį.
ElectricCar
turi baterijos talpą;
turi įkrovimo metodą;
neturi naudoti kuro.
Bendri metodai
Visos transporto priemonės turi turėti vienodai pavadintus metodus:
start_trip(distance);
finish_trip();
calculate_trip_cost(distance);
refuel_or_charge(amount);
display_info().
Tačiau jų veikimas gali skirtis.
Sukurkite klasę Fleet
Ji turi:
pridėti transporto priemonę;
pašalinti transporto priemonę;
surasti transporto priemonę pagal ID;
pradėti kelionę;
užbaigti kelionę;
parodyti visas laisvas transporto priemones;
parodyti šiuo metu naudojamas transporto priemones;
apskaičiuoti bendrą transporto parko ridą;
rasti seniausią transporto priemonę;
apskaičiuoti planuojamos kelionės kainą.
Taisyklės
Naudojama transporto priemonė negali pradėti kitos kelionės.
Kelionė negali prasidėti, jeigu nepakanka kuro arba baterijos.
Rida negali sumažėti.
Kuro ir baterijos kiekis negali tapti neigiamas.
Sunkvežimio krovinys negali viršyti leidžiamos ribos.
Transporto priemonių ID negali kartotis.