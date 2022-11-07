# Peszt-Balint

Ez egy szám kitalálgatós program amely visszajelzést ad hogy a szám nagyobb vagy kissebb.
A bemutatandó modulhoz szükséges 3 föggvény miatt egy értékelést is bekér.


A program 1 ellenőrző ciklust tartalmaz amely segíségével eldönthetjük hogy a megadott érték jó-e vagy újra be kell kérni.

A következő ciklus csak egyszerűen eldönti hogy a szám nagyobb, kissebb vagy egyenlő.

A feladatmegoldás érdekében beletettem egy osztályt ami igazából csak feleslegesen bonyolítja a programot. Ennek az osztálynak csak annyi a szerepe hogy a program végén ezen keresztül írjuk ki az értékelés adatait.

A következő 2 ciklus bekér egy értékelés és eldönti hogy az megfelelő formátumú-e?

Végül a program az előbb említett osztályon keresztül kiírja az eredményt.

//////////////////////////////////////////////////////////////////////
Modulok:

Saját:

 - modul1
 
    'greetings': Az indításkor szükséges adatok kiírása
   
    'rating': A felhasználó által megadott értékelés formázása
    
    'textArt': Az 5 csillagos értékelésre megadott speciális szöveg kiírása
   
Külső:
 - string
   (Az elfogadható számok kilistázásáért)
 - random
   (Random szám generálás)
 - getpass
   (A jelenlegi felhasználó nevének megszerzése)
