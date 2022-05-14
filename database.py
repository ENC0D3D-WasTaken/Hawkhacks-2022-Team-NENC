from sqlalchemy import Float, Boolean, Column, DateTime, ForeignKey,String ,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from settings import settings

def engine_init(settings):
    url = f'postgresql+psycopg2://{settings["username"]}:{settings["password"]}@{settings["host"]}:{settings["port"]}/{settings["db"]}'
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url,pool_size=50,echo=False)
    return engine

engine = engine_init(settings)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

Base = declarative_base()

class User(Base):
    __tablename__ = 'userlist'
    id = Column(Integer, primary_key=True)
    memberId = Column(Integer,unique=True)
    name = Column(String(),unique=True)
    timestamp = Column(DateTime)
    balance = Column(Float)

class NFTCollections(Base):
    __tablename__ = 'nftcollections'
    id = Column(Integer, primary_key=True)
    name = Column(String(),unique=True)
    description = Column(String())
    mintPrice = Column(Integer())
    timestamp = Column(DateTime())

class NFTCollectionItems(Base):
    __tablename__ = 'nftcollectionitems'
    id = Column(Integer, primary_key=True)
    collectionId = Column(Integer, ForeignKey('nftcollections.id'))
    name = Column(String(),unique=True)
    timestamp = Column(DateTime())

class CryptoCurrencies(Base):
    __tablename__ = 'cryptocurrencylist'
    id = Column(Integer, primary_key=True)
    name = Column(String(),unique=True)
    price = Column(Integer())
    abr = Column(String())
    quantity = Column(Integer())
    timestamp = Column(DateTime())
    
class CryptoCurrencyTransactions(Base):
    __tablename__ = 'cryptocurrencytransactions'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('userlist.id'))
    cryptoId = Column(Integer, ForeignKey('cryptocurrencylist.id'))
    quantity = Column(Integer())
    boughtFor = Column(Integer())
    timestamp = Column(DateTime())

class NFTMint(Base):
    __tablename__ = 'nfttransactions'
    id = Column(Integer, primary_key=True)
    boughtFor = Column(Integer())
    timestamp = Column(DateTime())

class CryptoforNFTTrade(Base):
    __tablename__ = 'cryptofornfttrade'
    id = Column(Integer, primary_key=True)
    buyer = Column(String, ForeignKey('userlist.name'))
    seller = Column(String, ForeignKey('userlist.name'))
    CryptoAmount = Column(Integer())
    CryptoType = Column(String, ForeignKey('cryptocurrencylist.name'))
    NFTType = Column(String, ForeignKey('nftcollections.name'))
    NFTname = Column(String(),ForeignKey('nftcollectionitems.name'))
    timestamp = Column(DateTime())

class NFTforCryptoTrade(Base):
    __tablename__ = 'nftforcryptotrade'
    id = Column(Integer, primary_key=True)
    buyer = Column(String, ForeignKey('userlist.name'))
    seller = Column(String, ForeignKey('userlist.name'))
    CryptoAmount = Column(Integer())
    CryptoType = Column(String, ForeignKey('cryptocurrencylist.name'))
    NFTType = Column(String, ForeignKey('nftcollections.name'))
    NFTname = Column(String,ForeignKey('nftcollectionitems.name'))
    timestamp = Column(DateTime())
    

Base.metadata.create_all(bind=engine)