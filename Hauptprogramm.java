public class Hauptprogramm {
    public static void main(String[] args) {
        // 1. Variablen definieren (Wirtschaftsinformatik-Beispiel)
        String produktName = "Fachbuch Wirtschaftsinformatik";
        double nettopreis = 49.99;
        double mwstSatz = 0.19; // 19% Mehrwertsteuer
        
        // 2. Berechnung durchführen
        double mwstBetrag = nettopreis * mwstSatz;
        double bruttopreis = nettopreis + mwstBetrag;
        
        // 3. Ergebnisse in der Konsole ausgeben
        System.out.println("=== RECHNUNGS-SIMULATOR ===");
        System.out.println("Produkt: " + produktName);
        System.out.println("Nettopreis: " + nettopreis + " €");
        System.out.printf("MwSt. (19%%): %.2f €%n", mwstBetrag);
        System.out.println("---------------------------");
        System.out.printf("Gesamtbetrag (Brutto): %.2f €%n", bruttopreis);
    }
}
