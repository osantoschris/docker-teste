from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:postgres@192.168.3.41:5432/postgres")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome="Christian Oliveira", email="christianoliveira8@gmail.com")
session.add(novo_usuario)
session.commit()
print("Usuario adicionado com sucesso!")

novo_usuario = Usuario(nome="Joyce Pereira", email="joyceps@live.com")
session.add(novo_usuario)
session.commit()
print("Usuario adicionado com sucesso!")

usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(usuario.id, usuario.nome, usuario.email)

usuario_atualizar = session.query(Usuario).filter(Usuario.id == 1).first()
usuario_atualizar.nome = "Christian dos Santos Oliveira"
session.commit()
print("Usuario alterado com sucesso!")

usuario_deletar = session.query(Usuario).filter(Usuario.id == 2).first()
session.delete(usuario_deletar)
session.commit()
print("Usuario deletado com sucesso!")

session.close()