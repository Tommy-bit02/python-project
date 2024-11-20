```mermaid
flowchart TD
    A[Start Adventure] --> B{Living Situation?}
    B -->|Apartment| C[Awake to screams and explosion outside apartment]
    B -->|House| D[Awake to smoke and horrific bark like a dog]
    
    C --> E[Choose action]
    D --> E[Choose action]

    E --> F[Stay Inside and Barricade Doors] --> G[You didn't survive] --> H[End Adventure]
    E --> H[Police Station] --> I[You didn't survive] --> H[End Adventure]
    E --> J[Head to Countryside] --> K[You survived!] --> H[End Adventure]
    E --> L[Find Family/Friends] --> M[You didn't survive] --> H[End Adventure]
    E --> N[Military Base] --> O[You survived!] --> H[End Adventure]
    E --> P[Escape by Sea] --> Q[You didn't survive] --> H[End Adventure]
    E --> R[Find Survivors] --> S[Heroic Sacrifice] --> T[You didn't survive] --> H[End Adventure]
    E --> U[Hide in Basement] --> V[You didn't survive] --> H[End Adventure]
    E --> W[Drive to Safety] --> X[You survived!] --> H[End Adventure]
    E --> Y[Signal for Help] --> Z[You survived!] --> H[End Adventure]

    subgraph End Adventure
        H[End Adventure]
    end
