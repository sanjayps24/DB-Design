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

Base = declarative_base()

 class Cart(Base):
        __tablename__ = 'cart'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer)
        product_id = Column(Integer)
        quantity = Column(Integer)
        price = Column(Integer)
        total = Column(Integer)
        status = Column(String)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
 
 class Wishlist(Base):
        __tablename__ = 'wishlist'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer)
        product_id = Column(Integer)
        status = Column(String)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

 class Product(Base):
        __tablename__ = 'product'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        price = Column(Integer)
        description = Column(String)
        category = Column(String)
        stock = Column(Integer)
        image = Column(String)
        size = Column(String) #7 sizes
        color = Column(String) #20 colors
        brand = Column(String) #10 brands
        rating = Column(Integer)
        reviews = Column(Integer)
        isprime = Column(Boolean)
        taxpercent = Column(Integer)

 class ProductReview(Base):
        __tablename__ = 'product_review'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        product_id = Column(Integer, ForeignKey('product.id'))
        rating = Column(Integer)
        review = Column(String)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

 class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)
        password = Column(String)
        address = Column(String)
        phone = Column(String)
        alt_phone = Column(String)
        isprime = Column(Boolean)

    class Order(Base):
        __tablename__ = 'order'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer)
        product_id = Column(Integer)
        quantity = Column(Integer)
        price = Column(Integer)
        total = Column(Integer)
        status = Column(String)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
        payment_type = Column(String)
        payment_status = Column(String)

    class OrderDetails(Base):
        __tablename__ = 'order_details'
        id = Column(Integer, primary_key=True)
        order_id = Column(Integer, ForeignKey('order.id'))
        product_id = Column(Integer, ForeignKey('product.id'))
        quantity = Column(Integer)
        price = Column(Integer)
        total = Column(Integer)
        status = Column(String)
        created_at = Column(DateTime, default=datetime.now())
        updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
 