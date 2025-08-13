from sqlalchemy.orm import Relationship
from app.schemas.address_schema import Address
from app.schemas.user_schema import User
from app.schemas.order_schema import Order
from app.schemas.cart_schema import Cart
from app.schemas.cart_item_schema import CartItem
from app.schemas.order_item_schema import OrderItem
from app.schemas.payments_schema import Payment
from app.schemas.product_schema import Product
from app.schemas.categories_schema import Category

# Define relationships
Address.user = Relationship(back_populates="addresses")
User.addresses = Relationship(back_populates="user")
User.orders = Relationship(back_populates="user")
User.carts = Relationship(back_populates="user")
Order.user = Relationship(back_populates="orders")
Cart.user = Relationship(back_populates="carts")
Cart.items = Relationship(back_populates="cart")
CartItem.cart = Relationship(back_populates="items")
CartItem.product = Relationship(back_populates="cart_items")
OrderItem.order = Relationship(back_populates="items")
OrderItem.product = Relationship(back_populates="order_items")
Payment.order = Relationship(back_populates="payment")
Product.order_items = Relationship(back_populates="product")
Product.cart_items = Relationship(back_populates="product")
Product.category = Relationship(back_populates="products")
Category.products = Relationship(back_populates="category")
