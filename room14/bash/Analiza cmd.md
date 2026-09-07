Analiza 

Trzy rzeczy ustawione dobrze

1. Grupa sudo ma tylko jednego użytkownika (sudo:x:27:mimson) — brak rozproszonych uprawnień administracyjnych. Mniej osób, które mogłyby (świadomie lub nie) ustawić nieautoryzowane przekierowanie.
2. Brak działającego serwera pocztowego w ps aux (żadnego postfix/exim/dovecot) — nic lokalnie nie obsługuje poczty na poziomie serwera, więc nie ma oczywistego wektora przekierowania "po stronie MTA" na tej maszynie.
3. unattended-upgrades.service jest włączony — aktualizacje bezpieczeństwa instalują się automatycznie, to dobra higiena podstawowa.

Trzy ustawione źle albo budzące wątpliwość

1. openvpn.service jest enabled, ale w ps aux nie widać żadnego działającego procesu openvpn. Włączona, ale pozornie nieużywana usługa VPN to coś do wyjaśnienia — czy ktoś ją kiedyś skonfigurował i po co, i czy nie tuneluje/przekierowuje ruchu (w tym poczty) w sposób, o którym reszta zespołu nie wie.
2. sssd.service jest enabled — to usługa integracji z zewnętrznym systemem tożsamości (LDAP/AD/FreeIPA). Na stacji roboczej biura sprzedaży to nietypowe i warte zapytania: czy maszyna jest podpięta pod jakąś centralną domenę, a jeśli tak — kto z zewnątrz mógłby przez nią zarządzać kontami czy regułami.
3. Same te trzy komendy w ogóle nie sprawdzają niczego związanego z pocztą — nie ma tu crontab -l, nie ma zawartości ~/.forward, nie ma ustawień żadnego klienta pocztowego. To dziura w samym rozpoznaniu, nie w konfiguracji maszyny — ale trzeba to jasno zaznaczyć w notatce, żeby nikt nie wywnioskował "wszystko OK", skoro naprawdę nie sprawdzono tego, o co pytała karta.

Jedna rzecz do naprawy w pierwszej kolejności — i dlaczego

Sprawdzić realną konfigurację poczty, a konkretnie Evolution. W ps aux widać aktywne procesy evolution-source-registry, evolution-calendar-factory, evolution-addressbook-factory, evolution-alarm-notify — to dowód, że na tej maszynie skonfigurowany jest klient pocztowy GNOME Evolution. To właśnie TAM (Edycja → Wiadomości → Filtry / ustawienia konta) może żyć reguła przekierowania, a nie w żadnym systemowym pliku. Dodatkowo warto odpalić crontab -l, żeby wykluczyć automatyczne zadanie, które co jakiś czas wysyła/przekazuje pocztę dalej. To priorytet, bo bez tego pytanie z karty ("czy ktoś ustawił przekierowanie wiadomości") pozostaje formalnie bez odpowiedzi — macie tylko poszlaki (VPN, sssd), ale nie sprawdziliście jeszcze samego miejsca, gdzie taka reguła realnie by siedziała.

Zastrzeżenie: to wszystko dotyczy Twojej rzeczywistej maszyny (VirtualBox, Ubuntu) używanej jako "komputer biura sprzedaży" na potrzeby ćwiczenia — nie prawdziwej infrastruktury dewelopera, więc traktujcie VPN/sssd jako punkty do zapytania/przećwiczenia metody, a nie realny alarm bezpieczeństwa.