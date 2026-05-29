import subprocess
import datetime
import logging
import os
import gzip

#Konfiguracja logowania
logging.basicConfig(
    filename='backup_manager.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_backup():
    #generowanie nazwy z datą
    recent_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    sql_file_name = f"backup_{recent_date}.sql"
    gz_file_name = f"{sql_file_name}.gz"

    logging.info("--- Rozpoczynam proces backupu ---")

    try:
        #wykonywanie zrzutu bazy (DUBP) z Dockera
        logging.info(f"Tworzenie zrzutu: {sql_file_name}")
        dump_comm = "docker exec moja_baza_testowa pg_dump -U admin firma_db"
        
        with open(sql_file_name, 'w', encoding='utf-8') as output_file:
            subprocess.run(dump_comm, stdout= output_file, check = True, shell=True)

        #kompresja pliku do formatu .gz
        logging.info(f"Kompresja pliku do: {gz_file_name}")
        with open(sql_file_name, 'rb') as f_in:
            with gzip.open(gz_file_name, 'wb') as f_out:
                f_out.writelines(f_in)

        #wysłanie do chmury przez rclone (konfiguracja przez plik lokalny rclone.conf - należy wpisać swoją ścieżkę do tego pliku)
        logging.info("Transfer skompresowanego pliku do chmury MinIO...")
        rclone_comm = f"rclone --config /---wprowadz_swoja_sciezke_do_rclone.conf--- copy {gz_file_name} minio_local:moje-backupy/"
        subprocess.run(rclone_comm, shell = True, check = True)

        #usunięcie starych plików lokalnych
        os.remove(sql_file_name)
        os.remove(gz_file_name)
        logging.info("Sukces! Pliki pomyslnie wyslano i posprzatano lokalnie.\n")

    except Exception as e:
        logging.error(f"Wystapil blad krytyczny podczas backupu: {e}\n")

if __name__ == "__main__":
    create_backup()
