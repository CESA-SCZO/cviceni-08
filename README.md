# Cvičení 8

**Klonování repozitáře:**
- Klávesa Windows + R -> cmd -> Enter
```
mkdir c:\SCZO_2026
cd C:\SCZO_2026
git clone https://cesta.ke.forked.git.repozitari
uv sync
```

**Úkol 1:**
- Načtěte obraz 'football.png'.
- Zobrazte si jednotlivé barevné složky tohoto obrazu zvlášť spolu s jejich histogramy.
- Na základě zobrazených informací vhodně zvolte práh pro prahování s jedním prahem tak, abyste vysegmentovali pouze čáry a branky fotbalového hřiště
- Pomocí zvoleného prahu vytvořte segmentační masku pro dané části hřiště
  - Jasovým hodnotám, které představují chtěné oblasti přiřaďte hodnotu 1 a zbylým hodnotu 0.


**Úkol 2:**
- Načtěte obraz 'Boulder_cropped.png' a uložte si pouze hodnoty RGB a převeďte jej do prostoru HSV.
- Zobrazte si jednotlivé barevné složky tohoto obrazu zvlášť spolu s jejich histogramy.
- Na základě Vašich vědomostí a zobrazených informací si vyberte kanál, pomocí kterého budete schopni vysegmentovat úchyty pouze jedné barvy a vynásobte jeho hodnoty 360.
- Vybraný kanál si zobrazte do jednoho figure spolu s původním obrazem, colormapou kanálu a jeho histogramem s horizontální orientací
- Zvolte vhodně prahy pro vysegmentování úchytů zelené barvy a vytvořte binární segmentační masku
- Zobrazte si do jednoho figure původní barevný obraz, segmentační masku a obraz, ve kterém budou mít pouze zelené úchyty svou původní barvu a všechno ostatní bude černé.

**Úkol 3:**
- Načtěte obraz ‘okruh.png’ a převeďte jej do šedotónového
- Nastavte vhodnou pozici semínka na vysegmentování cest okruhu
- Prozkoumejte přiložené funkce region_growing() a Exploration_of_neighbourhood(). Co je vstupem, co výstupem? 
- Porovnejte výslednou segmentační masku získané použitím přiložené funkce a masku získanou pomocí prahování se stejnou hodnotou prahu
- Upravte funkci tak, aby využívala na rozrůstání Vámi vybrané dynamické kritérium
- Měňte pozice semínka a pozorujte jeho vliv na výsledek segmentace

**Závěr cvičení:**
```
git add .
git commit –m „message“
git push origin main
```