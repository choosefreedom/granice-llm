Analiza - tu mój disclaimer konta użytkownika są fikcyjne i stworzone wcześniej na potrzeby zrozumienia mechanizmu nadawania uprawnień.

To najciekawszy wynik z trzech pokoi — /etc/passwd ujawnił coś konkretnego.

Trzy rzeczy ustawione dobrze

1. Tylko mimson jest w grupie sudo — ani lekarz, ani rejestratorka nie mają uprawnień administracyjnych. Zgodne z zasadą najmniejszych uprawnień — personel medyczny nie powinien mieć pełnej kontroli nad systemem.
2. Konta usługowe/systemowe mają /usr/sbin/nologin albo /bin/false (avahi, cups, sssd, dnsmasq, itd.) — nie da się nimi normalnie zalogować, co ogranicza powierzchnię ataku.
3. Personel ma oddzielne, imienne konta (lekarz, rejestratorka) zamiast jednego współdzielonego — dobra praktyka pod kątem rozliczalności: wiadomo, kto był zalogowany, gdy coś się stanie z kartoteką.

Trzy ustawione źle albo budzące wątpliwość

1. cryptsetup w ogóle nie jest zainstalowany ("command not found") — nie da się nawet SPRAWDZIĆ, czy dysk z kartotekami jest zaszyfrowany, bo brakuje samego narzędzia. To bardzo mocna poszlaka, że pełne szyfrowanie dysku (LUKS) najprawdopodobniej nie jest tu w ogóle skonfigurowane — czyli odpowiedź na pytanie z karty wygląda źle, jeszcze zanim w ogóle zdążycie ją formalnie potwierdzić.
2. Konta lekarz i rejestratorka mają pełną powłokę /bin/bash (interaktywne logowanie), a nie sprawdziliście jeszcze, czy mają dostęp tylko do tego, czego potrzebują — w szczególności czy rejestratorka (z założenia bez dostępu do dokumentacji medycznej) nie może odczytać tych samych plików co lekarz.
3. Nie sprawdzono jeszcze /home/lekarz ani /home/rejestratorka — dotychczasowe ls -la pokazało tylko folder projektu ćwiczenia, a to właśnie w katalogach domowych tych dwóch kont najprawdopodobniej leżą realne kartoteki.

Jedna rzecz do naprawy w pierwszej kolejności — i dlaczego

Doinstalować/sprawdzić narzędzia szyfrowania i faktycznie zweryfikować stan dysku: sudo apt install cryptsetup, potem lsblk -f (LUKS pokaże się jako crypto_LUKS przy partycji) i sudo blkid. Równolegle: sudo ls -la /home/lekarz /home/rejestratorka, żeby ustalić, gdzie faktycznie leżą kartoteki i jakie mają uprawnienia. To priorytet, bo pytanie z karty dotyczy wprost ryzyka wycieku danych medycznych (kategoria szczególna RODO) w razie kradzieży sprzętu — a obecnie nie ma nawet potwierdzenia, że narzędzie do sprawdzenia szyfrowania jest zainstalowane, nie mówiąc o samym szyfrowaniu.