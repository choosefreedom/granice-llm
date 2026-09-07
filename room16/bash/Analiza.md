Analiza

Trzy rzeczy ustawione dobrze

1. Ollama i CUPS nasłuchują wyłącznie na localhost (127.0.0.1:11434, 127.0.0.1:631/[::1]:631) — nie są wystawione na sieć lokalną, więc nikt z zewnątrz nie dostanie się do nich bezpośrednio.
2. Brak jawnie otwartego portu do udostępniania plików — nie ma FTP (:21), nie ma serwera HTTP na plikach (:80/:8080), nie ma SMB (:445/:139) w stanie LISTEN. W tej chwili nic aktywnie nie serwuje plików na zewnątrz.
3. ls -la w katalogu roboczym nie pokazuje żadnych "przypadkowych" plików ze zdjęciami leżących w folderze projektu — dane ćwiczenia są oddzielone od ewentualnych realnych danych.

Trzy ustawione źle albo budzące wątpliwość

1. Proces python3 (WSDD — Web Services Dynamic Discovery, protokół używany do wykrywania się w sieciach Windows/Samba) nasłuchuje nie tylko lokalnie, ale na adresie sieci lokalnej 192.168.0.102:3702 i adresie multicastowym 239.255.255.250:3702. To znaczy, że ten komputer aktywnie OGŁASZA SIĘ w całej sieci lokalnej jako potencjalny host udostępniania plików — dokładnie ten typ mechanizmu, przez który "zdjęcia z zajęć" mogłyby stać się widoczne dla innych urządzeń w sieci, gdyby obok działał udział Samby.
2. Sam smbd/Samba nie pojawia się na liście enabled usług — czyli nie wiadomo, czy Samba w ogóle jest zainstalowana, czy uruchomiona ręcznie/inaczej. WSDD działa "sam", bez jasności co dokładnie ogłasza — to niejasna, nie do końca wytłumaczona sytuacja.
3. avahi-daemon nasłuchuje na porcie 5353 na wszystkich interfejsach (0.0.0.0 i [::], nie tylko localhost) — to kolejny mechanizm "ogłaszania się" w sieci (mDNS/Bonjour, używany m.in. przy AirDrop-podobnym udostępnianiu i drukarkach sieciowych), widoczny dla całej sieci lokalnej, a nie tylko zaufanych hostów.

Jedna rzecz do naprawy w pierwszej kolejności — i dlaczego

Sprawdzić, co dokładnie robi WSDD i czy towarzyszy mu realny udział plików: sudo systemctl status wsdd, dpkg -l | grep -i samba, sudo smbstatus, oraz jeśli istnieje — przejrzeć /etc/samba/smb.conf pod kątem udostępnionych ścieżek. To jedyny element z tej tury, który bezpośrednio dotyka pytania z karty — trzeba ustalić, czy przez tę usługę cokolwiek (potencjalnie zdjęcia) jest faktycznie widoczne dla całej sieci lokalnej, czy to tylko nieużywany, zapomniany komponent po instalacji systemu.

Zastrzeżenie takie samo jak przy pokoju 14: pwd/ls -la pokazały folder projektu ćwiczenia, a nie prawdziwy folder ze zdjęciami fikcyjnego przedszkola — to naturalne w tym ról-play, ale znaczy, że odpowiedź "gdzie trafiają zdjęcia" musi opierać się na analizie mechanizmów sieciowych (WSDD/Samba/avahi), a nie na tym, co dosłownie zobaczyliście w ls.