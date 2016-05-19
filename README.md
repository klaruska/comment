## Spustenie 

1. terminál: `python manage.py runserver`
2. prehliadač: http://127.0.0.1:8000/post/1/

## Riešenie

- skript `script.py` vygeneruje komentáre *(11172 komentárov)* k 3 článkom, pričom vnorenie má hodnotu 3
- stránka pozostáva z názvu blogu, článku a jeho komentárov a zo zoznamu všetkých článkov, ktoré sa nachádzajú v tabuľke napravo
- názov článku, meno autora, samotný článok, meno autora komentára a komentár je generovaný pomocou rozšírenia `django.utils.lorem_ipsum` a to konkrétne použitím `words`, `sentence` a `paragraphs`
- k jednému článku prislúcha 19 hlavných komentárov, pričom v ďalších vnoreniach sa počet komentárov zmenšuje 
- komentáre sú zobrazované po 10, s možnosťou načítať ďalšie (vo všetkých vnoreniach)
- zobrazenie komentárov zabezpečujú súbory `ajax.py`, ktorý generuje elementy pre zobrazenie komentárov a tlačidiel pre načítanie ďalších komentárov  a `ajax.js`, ktorý zabezpečuje načítanie ďalších komentárov na základe predtým vygenerovaných id, prislúchajúcich k jednotlivým tlačidlám
- `ajax.js` tiež obsahuje funkciu **like** a **dislike**, ktoré zabezpečujú pripočítanie, resp. odpočítanie hlasu ku komentáru
- pre zobrazenie ikony používateľa a tlačidiel plus a mínus je využívaný Font Awesome Icons 
- pod ikonou **user** sa nachádza hodnota, ktorá označuje kvalitu komentára *(kvalita = pocet_kladnych_hodnoteni - pocet_zapornych_hodnoteni)*
- komentáre sú zoradené podľa kvality, počnúc najvyššou
- komentáre je možné hodnotiť, kliknutím na ikonu **+**, resp. **-**
- pre zobrazenie dátumu a času vytvorenia (v zozname článkov a pri komentároch) vo formáte *xx ago* bol vytvorený filter `timeago`, ktorý sa nachádza v *commenting/templatetags/custom_tags.py*
- po prejdení myšou na takto formátovaný dátum a čas vytvorenia článku, resp. komentára je zobrazený dátym vo formáte **dd.mm.yyyy** a čas vo formáte **hh:mm**
