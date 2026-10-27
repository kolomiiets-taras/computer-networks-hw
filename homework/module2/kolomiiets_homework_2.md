# Домашнє завдання 2. Транспортний рівень та служби мережі

**Студент:** Коломієць Тарас
**Модуль:** 2 — Транспортний рівень та служби мережі
**ОС:** Ubuntu 24.04.5 LTS

---

## Завдання 1. Аналіз відкритих портів

### Команда

```bash
ss -tuln
```

Ключі: `-t` — TCP-сокети, `-u` — UDP-сокети, `-l` — лише ті, що слухають (очікують підключень), `-n` — показувати номери портів, а не назви служб.

### Результат

```text
Netid State  Recv-Q Send-Q      Local Address:Port  Peer Address:PortProcess
udp   UNCONN 0      0              127.0.0.54:53         0.0.0.0:*
udp   UNCONN 0      0           127.0.0.53%lo:53         0.0.0.0:*
udp   UNCONN 0      0             224.0.0.251:5353       0.0.0.0:*
udp   UNCONN 0      0             224.0.0.251:5353       0.0.0.0:*
udp   UNCONN 0      0             224.0.0.251:5353       0.0.0.0:*
udp   UNCONN 0      0             224.0.0.251:5353       0.0.0.0:*
udp   UNCONN 0      0             224.0.0.251:5353       0.0.0.0:*
udp   UNCONN 0      0                 0.0.0.0:5353       0.0.0.0:*
udp   UNCONN 0      0                 0.0.0.0:38472      0.0.0.0:*
udp   UNCONN 0      0                    [::]:5353          [::]:*
udp   UNCONN 0      0                       *:41676            *:*
udp   UNCONN 0      0                       *:8976             *:*
udp   UNCONN 0      0                       *:8976             *:*
udp   UNCONN 0      0                       *:8976             *:*
udp   UNCONN 0      0                       *:44761            *:*
udp   UNCONN 0      0                    [::]:46881         [::]:*
udp   UNCONN 0      0                       *:48358            *:*
tcp   LISTEN 0      1               127.0.0.1:45905      0.0.0.0:*
tcp   LISTEN 0      1024            127.0.0.1:6188       0.0.0.0:*
tcp   LISTEN 0      1024            127.0.0.1:6190       0.0.0.0:*
tcp   LISTEN 0      512             127.0.0.1:5211       0.0.0.0:*
tcp   LISTEN 0      151             127.0.0.1:3306       0.0.0.0:*
tcp   LISTEN 0      1               127.0.0.1:36255      0.0.0.0:*
tcp   LISTEN 0      70              127.0.0.1:33060      0.0.0.0:*
tcp   LISTEN 0      4096            127.0.0.1:631        0.0.0.0:*
tcp   LISTEN 0      4096        127.0.0.53%lo:53         0.0.0.0:*
tcp   LISTEN 0      4096              0.0.0.0:5001       0.0.0.0:*
tcp   LISTEN 0      4096              0.0.0.0:5432       0.0.0.0:*
tcp   LISTEN 0      4096           127.0.0.54:53         0.0.0.0:*
tcp   LISTEN 0      4096              0.0.0.0:6379       0.0.0.0:*
tcp   LISTEN 0      50     [::ffff:127.0.0.1]:6189             *:*
tcp   LISTEN 0      50     [::ffff:127.0.0.1]:6191             *:*
tcp   LISTEN 0      50     [::ffff:127.0.0.1]:33847            *:*
tcp   LISTEN 0      511    [::ffff:127.0.0.1]:33969            *:*
tcp   LISTEN 0      511    [::ffff:127.0.0.1]:34321            *:*
tcp   LISTEN 0      511                     *:3000             *:*
tcp   LISTEN 0      4096   [::ffff:127.0.0.1]:63344            *:*
tcp   LISTEN 0      4096   [::ffff:127.0.0.1]:63343            *:*
tcp   LISTEN 0      4096   [::ffff:127.0.0.1]:63342            *:*
tcp   LISTEN 0      512                 [::1]:5211          [::]:*
tcp   LISTEN 0      4096                 [::]:5001          [::]:*
tcp   LISTEN 0      4096                 [::]:5432          [::]:*
tcp   LISTEN 0      4096                 [::]:6379          [::]:*
tcp   LISTEN 0      4096                [::1]:631           [::]:*
```

### Розбір відкритих портів

| Протокол | Порт | Стан | Адреса | Служба |
|---|---|---|---|---|
| TCP | 53 | LISTEN | `127.0.0.53` | DNS — локальний DNS-резолвер `systemd-resolved` |
| UDP | 53 | UNCONN | `127.0.0.53` | DNS — той самий `systemd-resolved`, приймає DNS-запити по UDP |
| TCP | 631 | LISTEN | `127.0.0.1` | CUPS — служба друку (IPP) |
| UDP | 5353 | UNCONN | `0.0.0.0`, `224.0.0.251` | mDNS — пошук пристроїв у локальній мережі (Avahi, Chrome) |
| TCP | 3306 | LISTEN | `127.0.0.1` | MySQL — сервер бази даних |
| TCP | 5432 | LISTEN | `0.0.0.0` | PostgreSQL — база даних у Docker-контейнері |
| TCP | 6379 | LISTEN | `0.0.0.0` | Redis — база даних у Docker-контейнері |
| TCP | 3000 | LISTEN | `*` | Локальний веб-сервер Next.js (розробка) |

### Пояснення

**Чому в TCP стан `LISTEN`, а в UDP `UNCONN`.** TCP — протокол зі встановленням з'єднання. Сокет у стані `LISTEN` чекає на вхідний SYN, щоб почати тристоронній handshake (SYN → SYN-ACK → ACK). В UDP з'єднань немає взагалі, тому сокет просто відкритий і приймає датаграми від будь-кого. `ss` показує для нього стан `UNCONN` (unconnected).

**Що означає адреса прослуховування:**
- `127.0.0.1` або `[::1]` — порт доступний **лише з цього комп'ютера** (loopback). Наприклад, MySQL (3306) і CUPS (631) з мережі недоступні.
- `0.0.0.0`, `[::]` або `*` — порт слухає **на всіх інтерфейсах**, тобто до нього можна підключитися з інших пристроїв локальної мережі. Так відкриті PostgreSQL (5432) і Redis (6379), бо Docker публікує порти контейнерів на всі інтерфейси.
- `224.0.0.251` — це не адреса пристрою, а multicast-група mDNS. Усі пристрої в мережі, що підтримують mDNS, приймають пакети на цю адресу.

**Колонки `Recv-Q` і `Send-Q` для LISTEN-сокета.** `Send-Q` показує розмір черги очікування (backlog): скільки нових з'єднань ядро може тримати, поки програма їх не прийняла. Наприклад, у MySQL це 151, у CUPS — 4096. `Recv-Q` = 0 означає, що в черзі зараз немає з'єднань, які чекають на обробку.

---

## Завдання 2. Аналіз процесів, що слухають порти

### Команда

```bash
sudo ss -tulpn
```

Ключ `-p` додає колонку `Process`: який процес відкрив сокет. Команду я запускав через `sudo`, бо без нього `ss` показує лише процеси поточного користувача (пояснення нижче).

### Результат

```text
Netid     State       Recv-Q      Send-Q                Local Address:Port            Peer Address:Port     Process
udp       UNCONN      0           0                        127.0.0.54:53                   0.0.0.0:*         users:(("systemd-resolve",pid=1743,fd=16))
udp       UNCONN      0           0                     127.0.0.53%lo:53                   0.0.0.0:*         users:(("systemd-resolve",pid=1743,fd=14))
udp       UNCONN      0           0                       224.0.0.251:5353                 0.0.0.0:*         users:(("chrome",pid=6730,fd=339))
udp       UNCONN      0           0                       224.0.0.251:5353                 0.0.0.0:*         users:(("chrome",pid=6730,fd=294))
udp       UNCONN      0           0                       224.0.0.251:5353                 0.0.0.0:*         users:(("chrome",pid=6730,fd=260))
udp       UNCONN      0           0                       224.0.0.251:5353                 0.0.0.0:*         users:(("chrome",pid=6785,fd=56))
udp       UNCONN      0           0                       224.0.0.251:5353                 0.0.0.0:*         users:(("chrome",pid=6785,fd=55))
udp       UNCONN      0           0                           0.0.0.0:5353                 0.0.0.0:*         users:(("avahi-daemon",pid=1851,fd=12))
udp       UNCONN      0           0                           0.0.0.0:38472                0.0.0.0:*         users:(("avahi-daemon",pid=1851,fd=14))
udp       UNCONN      0           0                              [::]:5353                    [::]:*         users:(("avahi-daemon",pid=1851,fd=13))
udp       UNCONN      0           0                                 *:41676                      *:*         users:(("webstorm",pid=8070,fd=55))
udp       UNCONN      0           0                                 *:8976                       *:*         users:(("pycharm",pid=83755,fd=70))
udp       UNCONN      0           0                                 *:8976                       *:*         users:(("rider",pid=16706,fd=111))
udp       UNCONN      0           0                                 *:8976                       *:*         users:(("webstorm",pid=8070,fd=57))
udp       UNCONN      0           0                                 *:44761                      *:*         users:(("pycharm",pid=83755,fd=67))
udp       UNCONN      0           0                              [::]:46881                   [::]:*         users:(("avahi-daemon",pid=1851,fd=15))
udp       UNCONN      0           0                                 *:48358                      *:*         users:(("rider",pid=16706,fd=36))
tcp       LISTEN      0           1                         127.0.0.1:45905                0.0.0.0:*         users:(("Rider.Backend",pid=16774,fd=645))
tcp       LISTEN      0           1024                      127.0.0.1:6188                 0.0.0.0:*         users:(("cef_server",pid=17170,fd=86))
tcp       LISTEN      0           1024                      127.0.0.1:6190                 0.0.0.0:*         users:(("cef_server",pid=24142,fd=90))
tcp       LISTEN      0           512                       127.0.0.1:5211                 0.0.0.0:*         users:(("Api",pid=27007,fd=936))
tcp       LISTEN      0           151                       127.0.0.1:3306                 0.0.0.0:*         users:(("mysqld",pid=3494,fd=23))
tcp       LISTEN      0           1                         127.0.0.1:36255                0.0.0.0:*         users:(("Rider.Backend",pid=16774,fd=750))
tcp       LISTEN      0           70                        127.0.0.1:33060                0.0.0.0:*         users:(("mysqld",pid=3494,fd=21))
tcp       LISTEN      0           4096                      127.0.0.1:631                  0.0.0.0:*         users:(("cupsd",pid=1549536,fd=7))
tcp       LISTEN      0           4096                  127.0.0.53%lo:53                   0.0.0.0:*         users:(("systemd-resolve",pid=1743,fd=15))
tcp       LISTEN      0           4096                        0.0.0.0:5001                 0.0.0.0:*         users:(("docker-proxy",pid=26905,fd=8))
tcp       LISTEN      0           4096                        0.0.0.0:5432                 0.0.0.0:*         users:(("docker-proxy",pid=848725,fd=8))
tcp       LISTEN      0           4096                     127.0.0.54:53                   0.0.0.0:*         users:(("systemd-resolve",pid=1743,fd=17))
tcp       LISTEN      0           4096                        0.0.0.0:6379                 0.0.0.0:*         users:(("docker-proxy",pid=26797,fd=8))
tcp       LISTEN      0           50               [::ffff:127.0.0.1]:6189                       *:*         users:(("rider",pid=16706,fd=187))
tcp       LISTEN      0           50               [::ffff:127.0.0.1]:6191                       *:*         users:(("webstorm",pid=8070,fd=304))
tcp       LISTEN      0           50               [::ffff:127.0.0.1]:33847                      *:*         users:(("rider",pid=16706,fd=40))
tcp       LISTEN      0           511              [::ffff:127.0.0.1]:33969                      *:*         users:(("rider",pid=16706,fd=173))
tcp       LISTEN      0           511              [::ffff:127.0.0.1]:34321                      *:*         users:(("webstorm",pid=8070,fd=242))
tcp       LISTEN      0           511                               *:3000                       *:*         users:(("next-server (v1",pid=80142,fd=22))
tcp       LISTEN      0           4096             [::ffff:127.0.0.1]:63344                      *:*         users:(("pycharm",pid=83755,fd=65))
tcp       LISTEN      0           4096             [::ffff:127.0.0.1]:63343                      *:*         users:(("rider",pid=16706,fd=80))
tcp       LISTEN      0           4096             [::ffff:127.0.0.1]:63342                      *:*         users:(("webstorm",pid=8070,fd=74))
tcp       LISTEN      0           512                           [::1]:5211                    [::]:*         users:(("Api",pid=27007,fd=937))
tcp       LISTEN      0           4096                           [::]:5001                    [::]:*         users:(("docker-proxy",pid=26912,fd=8))
tcp       LISTEN      0           4096                           [::]:5432                    [::]:*         users:(("docker-proxy",pid=848732,fd=8))
tcp       LISTEN      0           4096                           [::]:6379                    [::]:*         users:(("docker-proxy",pid=26803,fd=8))
tcp       LISTEN      0           4096                          [::1]:631                     [::]:*         users:(("cupsd",pid=1549536,fd=6))
```

### Процеси

```text
tcp LISTEN 0 4096 127.0.0.53%lo:53 users:(("systemd-resolve",pid=1743,fd=15))
udp UNCONN 0 0    127.0.0.53%lo:53 users:(("systemd-resolve",pid=1743,fd=14))
```
- **Процес:** `systemd-resolved` — локальний DNS-резолвер Ubuntu (у колонці ім'я обрізане до 15 символів: `systemd-resolve`)
- **PID:** 1743
- **Порт:** 53, і TCP, і UDP. Один процес відкрив два окремі сокети з різними дескрипторами (`fd=15` і `fd=14`), бо DNS працює по обох протоколах

```text
tcp LISTEN 0 151 127.0.0.1:3306 users:(("mysqld",pid=3494,fd=23))
tcp LISTEN 0 70  127.0.0.1:33060 users:(("mysqld",pid=3494,fd=21))
```
- **Процес:** `mysqld` — сервер бази даних MySQL
- **PID:** 3494
- **Порт:** 3306 (TCP), класичний протокол MySQL. Той самий процес слухає ще й 33060 — X Protocol MySQL. Обидва порти доступні лише локально (`127.0.0.1`)

```text
tcp LISTEN 0 4096 127.0.0.1:631 users:(("cupsd",pid=1549536,fd=7))
```
- **Процес:** `cupsd` — служба друку CUPS
- **PID:** 1549536
- **Порт:** 631 (TCP), протокол IPP

```text
tcp LISTEN 0 4096 0.0.0.0:5432 users:(("docker-proxy",pid=848725,fd=8))
```
- **Процес:** `docker-proxy` — допоміжний процес Docker
- **PID:** 848725
- **Порт:** 5432 (TCP). Насправді PostgreSQL працює всередині контейнера, а `docker-proxy` приймає з'єднання на порту хоста і пересилає їх у контейнер. Тому в колонці Process видно не `postgres`, а `docker-proxy`

```text
tcp LISTEN 0 511 *:3000 users:(("next-server (v1",pid=80142,fd=22))
```
- **Процес:** `next-server` — сервер розробки Next.js (веб-застосунок)
- **PID:** 80142
- **Порт:** 3000 (TCP)

### Різниця між запуском з `sudo` і без нього

Спершу я запустив `ss -tulpn` без `sudo`. Тоді колонка Process була порожня для портів 53, 631, 3306, 5353 (`0.0.0.0`), 5432, 6379 і 5001. Процеси моїх програм (`chrome`, `webstorm`, `next-server`, `Api`) було видно, а системних служб — ні.

Причина в тому, що ці служби працюють від імені інших користувачів: `systemd-resolve`, `mysql`, `avahi`, `root`. Щоб дізнатися, якому процесу належить сокет, `ss` читає `/proc/<PID>/fd/`, а читати чужі дескриптори звичайному користувачу заборонено. Так система захищає себе: користувач не повинен бачити деталі системних служб. Через `sudo` `ss` виконується від `root`, якому доступні всі процеси, тому колонка Process заповнена повністю.

---

## Завдання 3. Перевірка TCP-з'єднання

### Команда 1: nc

```bash
nc -vz google.com 80
```

```text
Connection to google.com (142.250.75.174) 80 port [tcp/http] succeeded!
```

Ключі: `-v` — детальний вивід, `-z` — лише перевірити, чи відкритий порт, без надсилання даних.

### Команда 2: telnet (для порівняння)

```bash
telnet google.com 80
```

```text
Trying 142.250.75.174...
Connected to google.com.
Escape character is '^]'.
Connection closed by foreign host.
```

### Результат

- **Тип з'єднання:** TCP
- **Порт:** 80 (HTTP)
- **IP сервера:** `142.250.75.174` (спершу `nc` визначив його через DNS)
- **Результат:** з'єднання встановлено

### Пояснення

`succeeded!` означає, що пройшов повний тристоронній handshake TCP:

1. Мій комп'ютер надіслав **SYN** на `142.250.75.174:80`.
2. Сервер Google відповів **SYN-ACK**: порт відкритий, і сервер готовий прийняти з'єднання.
3. Мій комп'ютер надіслав **ACK**, і з'єднання встановилося.

Після цього `nc` з ключем `-z` одразу закрив з'єднання. `telnet` теж підключився (`Connected to google.com`), але чекав, поки я щось введу. Я надіслав рядок, який не є HTTP-запитом, тому сервер Google закрив з'єднання (`Connection closed by foreign host`).

---

## Завдання 4. Порівняння TCP vs UDP

### Команди та результати

```bash
nc -vz 8.8.8.8 53
```
```text
Connection to 8.8.8.8 53 port [tcp/domain] succeeded!
```

```bash
nc -u -vz 8.8.8.8 53
```
```text
Connection to 8.8.8.8 53 port [udp/domain] succeeded!
```

На перший погляд результати однакові. Щоб перевірити, чи можна довіряти результату UDP, я виконав ту саму перевірку для порту **54**, на якому DNS-сервер Google нічого не слухає:

```bash
nc -u -vz -w 3 8.8.8.8 54
```
```text
Connection to 8.8.8.8 54 port [udp/*] succeeded!
```

```bash
nc -vz -w 3 8.8.8.8 54
```
```text
nc: connect to 8.8.8.8 port 54 (tcp) timed out: Operation now in progress
```

### Порівняння

| | TCP (`nc -vz`) | UDP (`nc -u -vz`) |
|---|---|---|
| Порт 53 (DNS працює) | `succeeded!` | `succeeded!` |
| Порт 54 (нічого не слухає) | `timed out` — помилка | `succeeded!` — хибний успіх |
| Що реально відбувається | Тристоронній handshake SYN → SYN-ACK → ACK | Відправляється датаграма без підтвердження |
| Чи можна довіряти результату | Так | Ні |

### Висновок

- **TCP: є підтвердження з'єднання.** `succeeded` означає, що сервер відповів на SYN пакетом SYN-ACK. Якщо порт закритий або пакети блокує фаєрвол, TCP повідомляє про помилку. На порту 54 саме так: відповіді на SYN не прийшло, і через 3 секунди спрацював тайм-аут.
- **UDP: немає гарантії відповіді (connection-less).** UDP не встановлює з'єднання, тому `nc` просто відправляє датаграму і вважає це успіхом. Про закритий порт він дізнався б лише з ICMP-повідомлення «port unreachable», але Google таких повідомлень не надсилає (або їх відкидає фаєрвол). Тому `succeeded!` для порту 54 — хибний результат: `nc` не отримав жодної помилки, і цього вистачило, щоб вважати перевірку успішною.
- **Різниця:** TCP встановлює сесію і гарантує, що інша сторона на зв'язку. UDP сесії не встановлює і нічого не гарантує, зате він швидший і простіший. Тому DNS-запити зазвичай йдуть по UDP: це один короткий запит і одна відповідь. TCP для DNS використовують, коли відповідь завелика для однієї UDP-датаграми або для передачі зон між DNS-серверами.

---

## Завдання 5. DNS резолвінг

Як домен я взяв `github.com`.

### Команда 1: nslookup

```bash
nslookup github.com
```

```text
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	github.com
Address: 140.82.121.4
```

### Команда 2: dig

```bash
dig github.com
```

```text
; <<>> DiG 9.18.39-0ubuntu0.24.04.8-Ubuntu <<>> github.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15846
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;github.com.			IN	A

;; ANSWER SECTION:
github.com.		59	IN	A	140.82.121.4

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Tue Oct 27 18:19:10 EET 2026
;; MSG SIZE  rcvd: 55
```

### Результат

- **Домен:** `github.com`
- **IP:** `140.82.121.4` (запис типу `A`, тобто IPv4-адреса)
- **DNS-сервер:** `127.0.0.53`, порт 53, протокол UDP

### Чому DNS-сервер має адресу 127.0.0.53

`127.0.0.53` — це не роутер і не сервер провайдера, а локальний DNS-резолвер `systemd-resolved` на моєму комп'ютері. Це той самий процес, що слухає порт 53 у завданнях 1 і 2. Він кешує відповіді і пересилає запити далі. Куди саме, видно в `resolvectl`:

```bash
resolvectl status wlp0s20f3
```

```text
Current DNS Server: 192.168.20.1
       DNS Servers: 192.168.20.1
```

Отже, запит проходить такий ланцюжок:

```text
nslookup / dig → 127.0.0.53 (systemd-resolved) → 192.168.20.1 (домашній роутер) → DNS-сервер провайдера → ... → авторитетний сервер github.com
```

Адресу DNS-сервера `192.168.20.1` комп'ютер отримав від роутера через DHCP разом з IP-адресою (див. домашнє завдання 1).

### Що ще видно у виводі

- **`Non-authoritative answer`** — відповідь дав не авторитетний сервер домену `github.com`, а проміжний резолвер, який узяв її з кешу.
- **`59`** у секції ANSWER — це TTL (time to live): скільки секунд запис ще можна зберігати в кеші. Потім його треба запитати знову.
- **`Query time: 0 msec`** — відповідь прийшла миттєво, бо вже була в локальному кеші `systemd-resolved`.
- **`status: NOERROR`** — домен існує, запит виконано успішно.
- **`(UDP)`** — DNS-запит пішов по UDP на порт 53. Це підтверджує висновок із завдання 4.
