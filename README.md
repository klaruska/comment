## Spustenie 

1. terminál: `python manage.py runserver`
2. prehliadač: http://127.0.0.1:8000/post/1/

## Riešenie

- skript `script.py` vygeneruje komentáre *(11172 komentárov)* k 3 článkom, pričom vnorenie má hodnotu 3
- komentáre sú zobrazované po 10, s možnosťou načítať ďalšie
- pod ikonou **user** sa nachádza hodnota, ktorá označuje kvalitu komentára *(kvalita = pocet_kladnych_hodnoteni - pocet_zapornych_hodnoteni)*
- komentáre sú zoradené podľa kvality, počnúc najvyššou
- komentáre je možné hodnotiť, kliknutím na ikonu **+**, resp. **-**
