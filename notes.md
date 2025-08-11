ecommerce_api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py         # Login and token generation
│   │       │   ├── users.py        # User registration
│   │       │   ├── products.py     # Product listing and management
│   │       │   ├── carts.py        # Shopping cart operations
│   │       │   └── orders.py       # Checkout and order history
│   │       └── api.py          # Main router for v1
│   ├── core/
│   │   ├── config.py       # Pydantic settings management (reads .env)
│   │   └── security.py     # Password hashing and JWT logic
│   ├── crud/
│   │   ├── base.py         # Base class with common CRUD methods
│   │   ├── crud_user.py
│   │   ├── crud_product.py
│   │   └── crud_order.py
│   ├── db/
│   │   ├── base.py         # SQLAlchemy models base class
│   │   └── session.py      # Database session setup
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── order_item.py   # Association table for products in an order
│   ├── schemas/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   └── token.py
│   └── main.py             # Main FastAPI app instance and router inclusion
│
├── tests/                  # All application tests
│   └── ...
│
├── .env                    # Environment variables (DB connection, secrets)
├── .gitignore              # Files to ignore in Git
├── Dockerfile              # Instructions to build the app container
├── docker-compose.yml      # Defines local dev services (app, db)
├── pyproject.toml          # Project dependencies (using Poetry or PDM)
└── README.md               # Project documentation