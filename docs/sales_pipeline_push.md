graph TD
    A(Inizio: Nuovo Lead) --> B[Contatto Iniziale];
    B --> C{Qualificato?};
    C -- No --> D[Archivia Lead (Lost)];
    C -- Sì --> E[Invio Proposta];
    E --> F{Negoziazione};
    F -- Accettata --> G[Lead Vinto];
    F -- Rifiutata --> D;
    G --> H((Crea Record 'Order'));
    D --> Z(Fine);
    H --> Z;