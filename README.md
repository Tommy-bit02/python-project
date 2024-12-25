graph TD
    A[Start Game] --> B[Intro Narration]
    B --> C[Moral Choices]
    C -->|Choice 1: Help Survivors| D[Reputation +10, Morale +10]
    C -->|Choice 2: Take Supplies| E[Reputation -20, Morale -10]
    C -->|Choice 3: Ignore Survivors| F[No Change in Reputation]
    D --> G[Exploration Choices]
    E --> G
    F --> G

    G[Exploration Choices] -->|Choice 1: Hospital| H[Visit Hospital]
    G -->|Choice 2: Forest| I[Visit Forest]
    G -->|Choice 3: Fortify Position| J[Stay in Position]
    H --> K[Scavenging Choices]
    I --> L[Combat Choices]
    J --> M[Wait for Next Move]

    K[Scavenging Choices] -->|Choice 1: Break Lock| N[Attract Zombies]
    K -->|Choice 2: Leave Container| O[No Zombies]
    K -->|Choice 3: Pick Lock Quietly| P[No Zombies, Gain Supplies]
    N --> Q[Combat Choices]
    O --> Q
    P --> Q

    L[Combat Choices] -->|Choice 1: Fight Zombies| R[Health -10]
    L -->|Choice 2: Use Flare| S[Stamina -10]
    L -->|Choice 3: Hide| T[Stamina -5]
    R --> U[NPC Interaction]
    S --> U
    T --> U

    U[NPC Interaction] -->|Choice 1: Reassure Chris| V[Trust +10]
    U -->|Choice 2: Tell Chris to Focus| W[Trust -5]
    U -->|Choice 3: Ignore Chris| X[Trust -10]
    V --> Y[Critical Decision]
    W --> Y
    X --> Y

    Y[Critical Decision] -->|Choice 1: Save Survivor| Z[Health -10, Morale +10]
    Y -->|Choice 2: Leave Survivor| AA[Morale -20]
    Y -->|Choice 3: Negotiate with Survivor| AB[Health -5]
    Z --> AC[Scavenging Choices]
    AA --> AC
    AB --> AC

    AC[Scavenging Choices] -->|Choice 1: Break Lock| N
    AC -->|Choice 2: Leave Container| O
    AC -->|Choice 3: Pick Lock Quietly| P

    N --> Q[Combat Choices]
    O --> Q
    P --> Q

    Q[Combat Choices] -->|Choice 1: Fight Zombies| R
    Q -->|Choice 2: Use Flare| S
    Q -->|Choice 3: Hide| T

    R --> U[NPC Interaction]
    S --> U
    T --> U

    U --> V[Critical Decision]

    V --> Z[Check Ending]
    W --> Z
    X --> Z

    Z -->|Good Ending| AE[Good Ending: United We Stand]
    Z -->|Bad Ending| AF[Bad Ending: Alone and Betrayed]
    Z -->|Neutral Ending| AG[Neutral Ending: Survival is a Struggle]

