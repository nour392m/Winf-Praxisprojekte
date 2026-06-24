import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_report():
    # 1. Beispiel-Daten erstellen (simuliert eine echte Excel-Datei)
    data = {
        "Produkt": ["Laptop", "Maus", "Tastatur", "Monitor", "Kabel"],
        "Verkäufe": [45, 120, 85, 30, 250],
        "Umsatz": [45000, 3600, 5100, 12000, 2500]
    }
    df = pd.DataFrame(data)
    
    # 2. Daten filtern (z.B. nur Produkte mit Umsatz > 4000 €)
    high_revenue = df[df["Umsatz"] > 4000]
    
    print("Folgende Produkte haben das Umsatzziel erreicht:")
    print(high_revenue)
    
    # 3. Diagramm erstellen und als Bild speichern
    plt.figure(figsize=(8, 4))
    plt.bar(df["Produkt"], df["Umsatz"], color='skyblue')
    plt.title("Umsatz nach Produktkategorie")
    plt.xlabel("Produkt")
    plt.ylabel("Umsatz in €")
    
    # Ordner erstellen falls nicht vorhanden und Grafik speichern
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/umsatz_report.png")
    print("\nGrafik wurde erfolgreich im Ordner 'output' gespeichert!")

if __name__ == "__main__":
    generate_report()
