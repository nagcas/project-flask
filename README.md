# 🚀 Fullstack Base App — React + Flask

Applicazione fullstack strutturata con:

- ⚛️ **Frontend:** React + Vite
- 🐍 **Backend:** Flask (API REST)
- 🏗️ Architettura modulare (routes, controllers, services, models)
- 🔐 Pronta per integrazione con autenticazione JWT e database

---

## 📁 Struttura del Progetto

```bash
project-flask/
│
├── backend/
│ │
│ ├── run.py # Entry point dell'app Flask
│ ├── config.py # Configurazioni (DB, JWT, SECRET_KEY)
│ ├── requirements.txt # Dipendenze Python
│ │
│ └── app/
│ │
│ ├── init.py # Application Factory
│ ├── extensions.py # Inizializzazione DB, JWT, Migrate
│ │
│ ├── controllers/ # Logica HTTP (request/response)
│ │ └── user_controller.py
│ │
│ ├── routes/ # Definizione endpoint (Blueprints)
│ │ └── user_routes.py
│ │
│ ├── services/ # Logica business
│ │ └── user_service.py
│ │
│ ├── models/ # Modelli database (SQLAlchemy)
│ │ └── user_model.py
│ │
│ ├── middlewares/ # Middleware personalizzati (auth, logging)
│ │ └── auth_middleware.py
│ │
│ └── utils/ # Funzioni helper (opzionale)
│
└── frontend/
│
├── package.json # Dipendenze Node
├── vite.config.js # Configurazione Vite + proxy API
│
├── public/ # Asset pubblici
│
└── src/
│
├── main.jsx # Entry point React
├── App.jsx # Componente principale
│
├── components/ # Componenti riutilizzabili
│
├── pages/ # Pagine applicazione
│
├── services/ # Gestione chiamate API
│ └── api.js
│
└── assets/ # Immagini / CSS
```

---

# 🏗️ Architettura Backend

Il backend segue una separazione chiara delle responsabilità:

- **Routes** → Definiscono gli endpoint API
- **Controllers** → Gestiscono request e response
- **Services** → Contengono la logica applicativa
- **Models** → Gestione database
- **Middlewares** → Autenticazione, validazioni, logging
- **Extensions** → Inizializzazione centralizzata delle estensioni Flask

Questa struttura garantisce:

- Scalabilità
- Manutenibilità
- Separazione delle responsabilità (SoC)
- Facilità di testing

---

# ⚙️ Avvio Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
python run.py
```

## Backend disponibile su:

```code
http://127.0.0.1:5000
```

# ⚛️ Avvio Frontend

```bash
cd frontend
npm install
npm run dev
```

## Frontend disponibile su:

```
http://localhost:5173
```

# 🔄 Comunicazione API

## Le API sono esposte con prefisso:

```
/api/

```

# 📦 Stack Tecnologico

### Frontend:

- React
- Vite
- JavaScript

### Backend:

- Flask
- Flask-CORS
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended

### 👨‍💻 Autore

Gianluca Chiaravalloti
Full Stack Developer

```

```
