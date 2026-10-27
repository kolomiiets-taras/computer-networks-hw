# Домашнє завдання 1. Основи комп'ютерних мереж

**Студент:** Коломієць Тарас
**Модуль:** 1 — Основи комп'ютерних мереж
**ОС:** Ubuntu 24.04.5 LTS, підключення через Wi-Fi

---

## Завдання 1. Дослідження мережі

### Команда

```bash
ip a
```

### Результат

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp122s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 74:d4:dd:c7:09:b9 brd ff:ff:ff:ff:ff:ff
3: wlp0s20f3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether d0:57:7e:7a:25:3d brd ff:ff:ff:ff:ff:ff
    inet 192.168.20.185/24 brd 192.168.20.255 scope global dynamic noprefixroute wlp0s20f3
       valid_lft 4790sec preferred_lft 4790sec
    inet6 fe80::ae86:5a6e:cba3:4190/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
4: br-22212bf45d60: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether f2:86:4b:57:52:42 brd ff:ff:ff:ff:ff:ff
    inet 172.22.0.1/16 brd 172.22.255.255 scope global br-22212bf45d60
       valid_lft forever preferred_lft forever
5: br-65a2c4fe4af2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether a6:f6:0d:ea:58:ad brd ff:ff:ff:ff:ff:ff
    inet 172.20.0.1/16 brd 172.20.255.255 scope global br-65a2c4fe4af2
       valid_lft forever preferred_lft forever
6: br-b51ec5038624: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 12:ce:09:0b:41:73 brd ff:ff:ff:ff:ff:ff
    inet 172.19.0.1/16 brd 172.19.255.255 scope global br-b51ec5038624
       valid_lft forever preferred_lft forever
7: br-d66961d6845d: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether e2:0f:e2:8b:16:40 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-d66961d6845d
       valid_lft forever preferred_lft forever
    inet6 fe80::e00f:e2ff:fe8b:1640/64 scope link
       valid_lft forever preferred_lft forever
8: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 42:6e:d7:f7:54:f3 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::406e:d7ff:fef7:54f3/64 scope link
       valid_lft forever preferred_lft forever
15: vethefaaa98@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-d66961d6845d state UP group default
    link/ether d6:27:83:ef:79:23 brd ff:ff:ff:ff:ff:ff link-netnsid 2
    inet6 fe80::d427:83ff:feef:7923/64 scope link
       valid_lft forever preferred_lft forever
16: vethee88b9b@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-d66961d6845d state UP group default
    link/ether 8e:85:a8:a2:6c:67 brd ff:ff:ff:ff:ff:ff link-netnsid 3
    inet6 fe80::8c85:a8ff:fea2:6c67/64 scope link
       valid_lft forever preferred_lft forever
17: veth41ccae8@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-d66961d6845d state UP group default
    link/ether 46:ed:f7:70:7c:c4 brd ff:ff:ff:ff:ff:ff link-netnsid 4
    inet6 fe80::44ed:f7ff:fe70:7cc4/64 scope link
       valid_lft forever preferred_lft forever
18: br-1c0f58942093: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 16:9c:1c:c7:e4:99 brd ff:ff:ff:ff:ff:ff
    inet 172.21.0.1/16 brd 172.21.255.255 scope global br-1c0f58942093
       valid_lft forever preferred_lft forever
    inet6 fe80::149c:1cff:fec7:e499/64 scope link
       valid_lft forever preferred_lft forever
23: veth92c6495@if2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-1c0f58942093 state UP group default
    link/ether 86:ce:c7:dd:11:11 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::84ce:c7ff:fedd:1111/64 scope link
       valid_lft forever preferred_lft forever
```

### Огляд інтерфейсів

| Інтерфейс | Що це | Стан |
|---|---|---|
| `lo` | Loopback — віртуальний інтерфейс для зв'язку комп'ютера із самим собою (`127.0.0.1`) | UP |
| `enp122s0` | Дротовий Ethernet-адаптер | DOWN (`NO-CARRIER` — кабель не підключено) |
| `wlp0s20f3` | Бездротовий Wi-Fi-адаптер | **UP — основне робоче підключення** |
| `docker0`, `br-*` | Віртуальні мости (bridge), які створює Docker для мереж контейнерів | частина UP, частина DOWN |
| `veth*` | Віртуальні пари Ethernet, що з'єднують Docker-контейнери з мостами `br-*` | UP |

Через інтернет працює лише `wlp0s20f3`, тому нижче розбираю саме його.

### Параметри основного підключення

| Параметр | Значення | Пояснення |
|---|---|---|
| **Інтерфейс** | `wlp0s20f3` | `wl` = wireless (бездротовий), `p0s20f3` = розташування адаптера на шині PCI (bus 0, slot 20, function 3) |
| **Тип підключення** | Wi-Fi (бездротове, IEEE 802.11) | Визначається за префіксом `wl` у назві; `nmcli device` показує тип `wifi` |
| **MAC-адреса** | `d0:57:7e:7a:25:3d` | Рядок `link/ether`. Фізична адреса мережевої карти, **канальний рівень (L2) моделі OSI** |
| **IP-адреса** | `192.168.20.185` | Рядок `inet`. Логічна адреса пристрою в мережі, **мережевий рівень (L3) моделі OSI**. Позначка `dynamic` означає, що адресу видав DHCP-сервер роутера (оренда ще `4790sec`) |
| **Маска** | `/24` = `255.255.255.0` | Визначає, яка частина IP-адреси позначає мережу (`192.168.20`), а яка — хост (`.185`). Належить до **мережевого рівня (L3) моделі OSI**, бо працює разом з IP-адресою |
| **Gateway (шлюз)** | `192.168.20.1` | У виводі `ip a` шлюзу немає, його видно в `ip r` (рядок `default via 192.168.20.1`). Це домашній роутер, через який пакети йдуть за межі локальної мережі |
| **Broadcast** | `192.168.20.255` | Рядок `brd`. Пакет на цю адресу отримують усі пристрої підмережі `192.168.20.0/24` |
| **Hosts** | 254 адреси: `192.168.20.1` – `192.168.20.254` | Під номер хоста маска `/24` залишає 8 біт: 2⁸ = 256 адрес. Мінус адреса мережі `192.168.20.0` і broadcast `192.168.20.255` = **254 хости** |

**Розрахунок підмережі:**

```text
IP-адреса:      192.168.20.185  = 11000000.10101000.00010100.10111001
Маска /24:      255.255.255.0   = 11111111.11111111.11111111.00000000
Адреса мережі:  192.168.20.0    (IP AND маска)
Broadcast:      192.168.20.255  (усі біти хоста = 1)
Перший хост:    192.168.20.1    (це і є шлюз — роутер)
Останній хост:  192.168.20.254
Кількість хостів: 2^(32-24) - 2 = 256 - 2 = 254
```

---

## Завдання 2. Дослідження маршрутизації

### Команда

```bash
ip r
```

### Результат

```text
default via 192.168.20.1 dev wlp0s20f3 proto dhcp src 192.168.20.185 metric 600
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown
172.18.0.0/16 dev br-d66961d6845d proto kernel scope link src 172.18.0.1
172.19.0.0/16 dev br-b51ec5038624 proto kernel scope link src 172.19.0.1 linkdown
172.20.0.0/16 dev br-65a2c4fe4af2 proto kernel scope link src 172.20.0.1 linkdown
172.21.0.0/16 dev br-1c0f58942093 proto kernel scope link src 172.21.0.1
172.22.0.0/16 dev br-22212bf45d60 proto kernel scope link src 172.22.0.1 linkdown
192.168.20.0/24 dev wlp0s20f3 proto kernel scope link src 192.168.20.185 metric 600
```

### Протокол, через який отримано IP

**Протокол — DHCP** (Dynamic Host Configuration Protocol).

Це видно в першому рядку: `default via 192.168.20.1 dev wlp0s20f3 proto dhcp`. Позначка `proto dhcp` означає, що IP-адресу `192.168.20.185`, маску та шлюз за замовчуванням комп'ютер отримав автоматично від DHCP-сервера, який працює на домашньому роутері. Це підтверджує й позначка `dynamic` у виводі `ip a`.

### Розбір маршрутів

| Маршрут | Пояснення |
|---|---|
| `default via 192.168.20.1 dev wlp0s20f3 proto dhcp` | Маршрут за замовчуванням: усі пакети до адрес, для яких немає окремого маршруту (тобто весь інтернет), йдуть на роутер `192.168.20.1` через Wi-Fi. Отриманий через DHCP. `metric 600` — пріоритет маршруту (менше число = вищий пріоритет) |
| `192.168.20.0/24 dev wlp0s20f3 proto kernel scope link` | Локальна мережа. Пристрої `192.168.20.x` доступні напряму, без шлюзу (`scope link`). `proto kernel` — ядро Linux додало маршрут автоматично, коли інтерфейсу призначили IP |
| `172.17.0.0/16` … `172.22.0.0/16` (`docker0`, `br-*`) | Внутрішні мережі Docker-контейнерів, також `proto kernel`. Позначка `linkdown` — у мережі зараз немає запущених контейнерів |

---

## Завдання 3. Знаходження публічної IP-адреси

### Команда

```bash
curl ifconfig.io
```

### Результат

```text
87.xxx.xxx.xxx
```

> Останні три октети публічної адреси замасковано з міркувань приватності: файл лежить у відкритому репозиторії. Перший октет `87` залишено, щоб було видно, що адреса не з приватного діапазону.

### Порівняння локальної та публічної адрес

| | Адреса | Звідки видно |
|---|---|---|
| Локальна (приватна) | `192.168.20.185` | `ip a`, інтерфейс `wlp0s20f3` |
| Публічна | `87.xxx.xxx.xxx` | `curl ifconfig.io` — так мене бачить сервер в інтернеті |

**Чи однакові адреси?** Ні, адреси різні.

**Чому різні?**

Адреса `192.168.20.185` належить до приватного діапазону `192.168.0.0/16` (RFC 1918). Такі адреси використовують лише всередині локальних мереж, і в інтернеті вони не маршрутизуються. Ту саму адресу `192.168.20.185` можуть мати тисячі комп'ютерів в інших домашніх мережах.

Між комп'ютером та інтернетом стоїть домашній роутер (`192.168.20.1`). Він має два боки: локальний з адресою `192.168.20.1` і зовнішній з публічною адресою від провайдера. Роутер виконує **NAT** (Network Address Translation): коли пакет виходить з локальної мережі, роутер замінює приватну адресу відправника `192.168.20.185` своєю публічною `87.xxx.xxx.xxx` і запам'ятовує це з'єднання в таблиці трансляцій. Коли приходить відповідь, роутер за цією таблицею повертає її потрібному пристрою в локальній мережі.

**Висновок:** сервер `ifconfig.io` бачить не мій комп'ютер, а роутер, тому показує адресу `87.xxx.xxx.xxx`. Усі пристрої в домашній мережі (ноутбук, телефон тощо) виходять в інтернет з цієї однієї публічної адреси. NAT економить дефіцитні адреси IPv4 і водночас приховує внутрішню структуру мережі: ззовні не можна напряму звернутися до `192.168.20.185`.
