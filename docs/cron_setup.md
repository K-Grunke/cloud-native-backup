# 🕒 Konfiguracja automatyzacji (Cron)

Ten dokument opisuje, jak skonfigurować system Linux (w tym środowisko WSL 2), aby codziennie automatycznie wykonywał zrzut bazy danych i wysyłał go do chmury.

## 1. Uruchomienie usługi cron (Ważne dla WSL 2)
W tradycyjnych systemach serwerowych Linux usługa `cron` działa domyślnie. Jeśli jednak używasz Windows Subsystem for Linux (WSL), musisz ją uruchomić ręcznie po każdym restarcie komputera (lub dodać do autostartu).

Aby uruchomić usługę, wpisz w terminalu:
```bash
    sudo service cron start
```

## 2. Edycja harmonogramu
Aby dodać nowe zautomatyzowane zadanie, otwórz edytor harmonogramu przypisany do Twojego użytkownika:
```bash
crontab -e
```

## 3. Dodanie reguły backupu
Dodaj poniższą linię na samym dole pliku. Upewnij się, że ścieżka do projektu (po poleceniu cd) odpowiada Twojej rzeczywistej ścieżce w systemie.
```bash
0 2 * * * cd /twoja_ścieżka_do_projektu/cloud-native-backup && /usr/bin/python3 src/backup_manager.py
```

### 💡 Wyjaśnienie składni:
- 0 2 * * * - Parametr czasu: uruchom punktualnie o 2:00 w nocy, każdego dnia, każdego miesiąca.
- cd /mnt/c/Projekty/cloud_backup - Przed wykonaniem skryptu, system musi wejść do głównego folderu projektu. Dzięki temu logi poprawnie zapiszą się w folderze logs/.
- && - Znak warunku. Oznacza: Uruchom następną komendę TYLKO wtedy, gdy poprzednia (przejście do folderu) zakończyła się sukcesem.
- /usr/bin/python3 src/backup_manager.py - Ścieżka bezwzględna do pythona i wywołanie naszego skryptu.

## 4. Zapisz plik i wyjdź (`Ctrl + O`, `Enter`, `Ctrl + X`).

## 5. Weryfikacja działania
Po dodaniu wpisu i zapisaniu pliku. System powinien wyświetlić komunikat:
```bash
crontab: installing new crontab.
```
Aby sprawdzić, czy backupy wykonują się poprawnie, rano sprawdź plik **logs/backup_manager.log**.

---

# English version

# 🕒 Automation Setup (Cron)

This document describes how to configure a Linux system (including WSL 2 environments) to automatically execute daily database dumps and upload them to the cloud.

## 1. Starting the cron service (Important for WSL 2)
In traditional Linux server environments, the `cron` daemon runs by default. However, if you are using Windows Subsystem for Linux (WSL), you must start it manually after every system reboot (or configure it to run on startup).

To start the service, run the following command in your terminal:
```bash
sudo service cron start
```
## 2. Editing the schedule
To add a new automated task, open the crontab editor assigned to your user:

```bash
crontab -e
```

## 3. Adding the backup rule
Add the following line at the very bottom of the file. Ensure that the project path (after the cd command) matches your actual directory path.

```bash
0 2 * * * cd /your_path_to_this_project/cloud-native-backup && /usr/bin/python3 src/backup_manager.py
```

### 💡 Syntax Explanation:

- 0 2 * * * - Time parameter: execute exactly at 2:00 AM, every day, every month.
- cd /mnt/c/Projekty/cloud_backup - Navigates to the project root directory before executing the script. This ensures that log files are correctly saved in the logs/ folder.
- && - Conditional operator. It means: Execute the next command ONLY if the previous one (directory change) succeeded.
- /usr/bin/python3 src/backup_manager.py - Absolute path to the Python runtime and the script execution.

## 4. Save and exit file (`Ctrl + O`, `Enter`, `Ctrl + X`).

## 5. Verifying execution
After adding the entry, save and exit the file. The system should display the following message:
```bash
crontab: installing new crontab.
```
To verify that the backups are running correctly, check the **logs/backup_manager.log** file the following morning.
