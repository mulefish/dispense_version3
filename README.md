# dispense_version3
https://github.com/mulefish/dispense_version3


# Flow

```mermaid
  graph TD; 
 A[Splash Page ]
A[style DB fill:#00758f]

 B[jwt_iss]
 C[GCP service account];
 D[Google Workspace Admin Console]
 E[Enable Domain Wide Deligation Access for ads]
 F[Create Developer Token]
 G[Test Manager Account ]
 H[approve dev token]   
 I[Test call]
 J[Ready to go]
 A-- gives us --> B;
 A -- Enable --> C;
 C --> D;
 D --> E;
 E --> F;
 F -- create --> G --> I;
 F -- create --> H;
 I --> J;
 H --> J;
```
