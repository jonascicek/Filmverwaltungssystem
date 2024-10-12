# Projekt - Filmverwaltung



Zuerst haben wir die versteckte Zip - Datei gesucht 



Diese konnten wir nur mit Passwort mit unzip entpacken:



http://marcolindner.io/assets/db_installation.zip



Entcripted haben wir das Passwort mit dem echo - Befehl, der in der Zip-Datei gespeichert war, allerdings musste am Ende das große D in ein kleines umformatiert werden.



Dann konnten wir uns mit vim oder less die Installationsanleitung aufrufen:



**Anleitung zur Installation einer MySQL Datenbank unter Ubuntu innerhalb von Multipass VMs**



Wir haben zwei Multipass VMs installiert –eine für den Python-Code und eine für die Datenbank. Es ist wichtig, die Verbindung zwischen diesen VMs korrekt einzurichten. Außerdem sollte beachtet werden, dass die Aktivierung von UFW (Uncomplicated Firewall) innerhalb der VMs zu Verbindungsproblemen führen kann, da Multipass die Netzwerkverbindungen verwaltet. Daher haben wir UFW **nicht** aktiviert.



### **Schritt 1: Erstellen der Multipass VMs**



- Wir benötigen zwei VMs innerhalb von Multipass:

  - **python-vm**: Für die Ausführung des Python-Codes.

  - **DB-VM**: Für die Installation von MySQL.



#### **1.1 Python-VM erstellen**



---



    multipass launch --name python-vm



---



#### **1.2 Datenbank-VM erstellen**



---



    multipass launch --name DB-VM



---



### **Schritt 2: IP-Adressen der VMs herausfinden**



Um die VMs miteinander kommunizieren zu lassen, benötigen wir ihre IP-Adressen.



#### **2.1 IP-Adresse der Datenbank-VM**



---



    multipass list



---



Dies zeigt eine Liste aller VMs mit ihren IP-Adressen. Die IP-Adresse der DB-VM haben wir uns dann notiert. 



### **Schritt 3: Installation der Datenbank auf der DB-VM**



Wir installieren nun **MySQL** auf der DB-VM.



#### **3.1 Verbindung zur Datenbank-VM herstellen**



---



    multipass shell db-vm



---



#### **3.2 Systemaktualisierung**



---



    sudo apt update && sudo apt upgrade -y



---



#### **3.3 MYSQL Installation**



---



    sudo apt install mysql-server -y



---



##### **3.4 MySQL sichern**



---



    sudo mysql_secure_installation



---



Während dieses Prozesses wurden wir aufgefordert:



- Ein Root-Passwort festzulegen.

- Anonyme Benutzer zu entfernen.

- Root-Login remote zu deaktivieren.

- Testdatenbanken zu entfernen.

- Tabellenrechte neu zu laden.



Wir haben sichere Einstellungen gewählt und uns das Passwort gemerkt.



##### **3.5 Remote-Zugriff für MySQL einrichten**



- **MySQL-Konfiguration bearbeiten:**



---



    sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf



---



- **Bind-Adresse anpassen:**



Wir haben uns die bind-address gesucht und diese mit 0.0.0.0 ersetzt. Die Änderung haben wir gespeichert.



- **MySQL neu starten:**



---



    sudo systemctl restart mysql



---



##### **3.6 Benutzer für Remote-Zugriff erstellen**



Mit



---

    sudo mysql



---



haben wir uns an der MySQL-Konsole angemeldet



Dann haben wir einen neuen Benutzer angelegt:



---



    CREATE USER 'dein_benutzername'@'%' IDENTIFIED BY 'dein_passwort';  #<- erstellt den Nutzer

    GRANT ALL PRIVILEGES ON *.* TO 'dein_benutzername'@'%';             #<- vergibt die Rechte

    FLUSH PRIVILEGES;                                                   #<- Startet die Rechte

    EXIT;



---



### **Schritt 4: Verbindung von der Python-VM zur Datenbank herstellen**



#### **4.1 Verbindung zur Python-VM herstellen**



---



    multipass shell python-vm



---



#### **4.2 Systemaktualisierung**



    sudo apt update && sudo apt upgrade -y



#### **4.3 Python-Umgebung einrichten**



Wir haben pip und  eine virtuelle Umgebungen installiert:



---



    sudo apt install python3-pip python3-venv -y



---



Dann haben wir eine virtuelle Umgebung erstellt:



---



    python3 -m venv venv



---

source venv/bin/activate



---



#### **4.4 Notwendige Python-Pakete installieren**



---



    pip install mysql-connector-python

  

---



#### **4.5 Testskript erstellen**



Erstelle ein Python-Skript, um die Verbindung zur Datenbank zu testen.



---



    vim test_mysql_connection.py



---



Im Editor haben wir folgenden Code eingegeben:



---



    import mysql.connector



---



---



    def create_connection():

        connection = mysql.connector.connect(

        host='IP_ADRESSE_DB_VM', 

        user='dein_benutzername', 

        password='dein_passwort', 

        database='Filmverwaltungssystem'  

        )

                                                        #Werte werden entsprechend individuell angepasst



    return connection



    try:

        conn = create_connection()

        print("Verbindung zur MySQL-Datenbank erfolgreich")

        conn.close()

        except mysql.connector.Error as err:

        print(f"Fehler: {err}")



---

  

#### **4.6 Skript ausführen**



Wir haben geprüft, dass wir noch in unserer virtuellen Umgebung sind und haben dann das Skript ausgeführt:



---



    python test_mysql_connection.py



---



### **5 Datenbank in der DB-VM erstellen**



In der DB-VM haben wir eine filmverwaltung.sql DB erstellt:



***# Create Database Filmverwaltungssystem***



    CREATE DATABASE IF NOT EXISTS



        Filmverwaltungssystem;



        USE Filmverwaltungssystem;



    CREATE TABLE IF NOT EXISTS Filme(

        id int PRIMARY KEY AUTO_INCREMENT,

        title varchar(128) NOT NULL,

        director varchar(32) NOT NULL,

        genre varchar(32) NOT NULL,

        releaseyear int NOT NULL,

        rating float NOT NULL

        );



### **6 Datenbank einrichten in der python-vm** 



Der Code ist inklusive der Beschreibung in der Filmverwaltungsystem.py hinterlegt.
