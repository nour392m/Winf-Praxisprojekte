import sqlite3

def init_database():
    # Verbindung zur Datenbank herstellen (Datei wird automatisch erstellt)
    conn = sqlite3.connect("unternehmen.db")
    cursor = conn.cursor()
    
    # 1. Tabelle erstellen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kunden (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stadt TEXT,
            umsatz REAL
        )
    """)
    
    # 2. Testdaten einfügen (falls Tabelle noch leer ist)
    cursor.execute("SELECT COUNT(*) FROM kunden")
    if cursor.fetchone()[0] == 0:
        kunden_liste = [
            ("Müller GmbH", "Düsseldorf", 15000.50),
            ("TechStart AG", "Köln", 8500.00),
            ("Schmidt Logistik", "Düsseldorf", 22000.00),
            ("Becker & Co", "Essen", 4300.20)
        ]
        cursor.executemany("INSERT INTO kunden (name, stadt, umsatz) VALUES (?, ?, ?)", kunden_liste)
        conn.commit()
        print("Testdaten erfolgreich eingefügt.")

    # 3. SQL-Abfrage: Alle Kunden aus Düsseldorf mit Umsatz > 5000
    print("\n--- SQL-Abfrage: Kunden aus Düsseldorf ---")
    cursor.execute("SELECT name, umsatz FROM kunden WHERE stadt = 'Düsseldorf'")
    
    for row in cursor.fetchall():
        print(f"Kunde: {row[0]} | Umsatz: {row[1]} €")
        
    conn.close()

if __name__ == "__main__":
    init_database()
