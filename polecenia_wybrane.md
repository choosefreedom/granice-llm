# Polecenia do Rundy 1 — pokoje 14, 16, 19

Wybrane z `03_Polecenia_na_trzech_systemach.pdf` — tylko te wiersze z tabeli
odpowiedników, które pasują do ogniska śledztwa z danej karty. Wybierz kolumnę
swojego systemu.

## Pokój 14 — Deweloper Nadwiślańska Inwestycje

Ognisko z karty: **"poczta i reguły: czy ktoś ustawił przekierowanie wiadomości"**.

**Uwaga:** w tabeli PDF nie ma osobnego wiersza o regułach przekierowania
poczty — to ustawienie żyje wewnątrz klienta pocztowego / poczty webowej
(Outlook, Gmail, serwer pocztowy), a nie w samym systemie operacyjnym. Poniżej
najbliższe polecenia z tabeli, które pomogą znaleźć COŚ, co mogłoby taką
regułę wymuszać na poziomie systemu (podejrzany proces, skrypt startowy,
podmieniony plik konfiguracyjny) — ale samą regułę trzeba sprawdzić w
ustawieniach konta pocztowego, nie w terminalu.

| Co sprawdzacie | Ubuntu | macOS | Windows 11 |
|---|---|---|---|
| Co teraz działa (procesy) — czy nie ma podejrzanego skryptu/procesu przekierowującego pocztę | `ps aux` | `ps aux` | `Get-Process` |
| Co uruchamia się przy starcie — czy coś automatycznie uruchamia się i mogło ustawić regułę | `systemctl list-unit-files --state=enabled` | `launchctl list` | `Get-CimInstance Win32_StartupCommand` |
| Kto ma prawa administratora — kto w ogóle mógł to zmienić | `getent group sudo` | `dscl . -read /Groups/admin GroupMembership` | `Get-LocalGroupMember -SID S-1-5-32-544` |
| Uprawnienia do pliku — jeśli znajdziecie plik konfiguracyjny reguł (np. `.forward`, plik klienta pocztowego) | `ls -l plik` | `ls -l plik` | `icacls plik` |
| Suma kontrolna pliku — czy plik konfiguracyjny nie został podmieniony | `sha256sum plik` | `shasum -a 256 plik` | `Get-FileHash plik` |

## Pokój 16 — Przedszkole Bajkowa Kraina

Ognisko z karty: **"udostępnianie plików: gdzie trafiają zdjęcia z zajęć"**.

| Co sprawdzacie | Ubuntu | macOS | Windows 11 |
|---|---|---|---|
| Gdzie jestem — punkt startowy do znalezienia folderu ze zdjęciami | `pwd` | `pwd` | `pwd` |
| Co jest w katalogu — przeszukanie folderów ze zdjęciami z zajęć | `ls -la` | `ls -la` | `ls -Force` |
| Uprawnienia do pliku — czy folder/zdjęcia są dostępne dla innych niż trzeba | `ls -l plik` | `ls -l plik` | `icacls plik` |
| Zmiana uprawnień — jeśli trzeba to naprawić | `chmod 644 plik` | `chmod 644 plik` | `icacls plik /grant *S-1-5-32-545:R` |
| Co nasłuchuje na portach — czy nie działa jakiś niezamierzony serwer plików (FTP/SMB/HTTP) serwujący zdjęcia na zewnątrz | `sudo ss -tulpn` | `sudo lsof -iTCP -sTCP:LISTEN -n -P` | `Get-NetTCPConnection -State Listen` |
| Co uruchamia się przy starcie — czy nie działa automatycznie jakaś aplikacja do synchronizacji w chmurze | `systemctl list-unit-files --state=enabled` | `launchctl list` | `Get-CimInstance Win32_StartupCommand` |

## Pokój 19 — Gabinet weterynaryjny Cztery Łapy

Ognisko z karty: **"kopie i szyfrowanie: gdzie leżą kartoteki i czy są zaszyfrowane"**.

To jedyny z trzech pokoi, gdzie tabela ma bezpośrednie trafienie (wiersz
"Czy dysk jest zaszyfrowany").

| Co sprawdzacie | Ubuntu | macOS | Windows 11 |
|---|---|---|---|
| Czy dysk jest zaszyfrowany — **kluczowe pytanie z karty** | `sudo cryptsetup status /dev/mapper/*` | `fdesetup status` | `manage-bde -status` |
| Gdzie jestem / co jest w katalogu — znalezienie folderu z kartotekami | `pwd` / `ls -la` | `pwd` / `ls -la` | `pwd` / `ls -Force` |
| Uprawnienia do pliku — kto może odczytać kartoteki | `ls -l plik` | `ls -l plik` | `icacls plik` |
| Suma kontrolna pliku — weryfikacja integralności kopii zapasowych kartotek | `sha256sum plik` | `shasum -a 256 plik` | `Get-FileHash plik` |
| Lista kont użytkowników / kto ma prawa administratora — kto w ogóle ma dostęp do maszyny z kartotekami | `cat /etc/passwd` / `getent group sudo` | `dscl . -list /Users UniqueID` / `dscl . -read /Groups/admin GroupMembership` | `Get-LocalUser` / `Get-LocalGroupMember -SID S-1-5-32-544` |
