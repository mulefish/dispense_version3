# dispense_version3
https://github.com/mulefish/dispense_version3


# Flow

```mermaid
flowchart TB
    c1-->a2
    
    subgraph one
    a1-->a2
    end
    
    subgraph two
    b1-->b2
    end
    
    
    subgraph three
    c1-->c2
    end
    one --> two
    three --> two
    two --> c2

```



```mermaid
    flowchart TB
    A[Splash page]
    B[Login]
    C[DB]
    D[Pick stores]
    E[Pick products]
    F[Money]
    G[Tag]



    A-->B
    subgraph one
    B-->C
    end
    
    A-->D
    subgraph two
        D-->E
        E-->F
        F-->G
    end


```
