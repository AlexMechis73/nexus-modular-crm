graph TD
    A(Inizio: Cliente Chiama) --> B[Crea Record 'Order'];
    B --> C{Ordine necessita Approvazione?};
    C -- Sì --> D[Ciclo di Approvazione];
    C -- No --> E[Ordine Approvato];
    D --> E;
    E --> F[Processa e Spedisci];
    F --> Z(Fine);