#search products
#signup
#login
#add to cart
#checkout
#suggest products
#wishlist
#review
#track the order
#customer support
#order history
#return order
#update profile
#update password
#filter products
#payment modes
#share a product link
#upload image and find similar products
 from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

  class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    category = Column(String)
    stock = Column(Integer)
    image = Column(String)
    size = Column(String)
    