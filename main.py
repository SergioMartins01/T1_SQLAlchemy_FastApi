from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./banco.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class PerfilDB(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    perfil_nome = Column(String)
   
    usuario = relationship("UsuarioDB", back_populates="perfil")

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    id_perfil = Column(Integer, ForeignKey("perfis.id"))
    
    perfil = relationship("PerfilDB", back_populates="usuario")

Base.metadata.create_all(bind=engine)

class PerfilCreate(BaseModel):
    perfil_nome: str

class PerfilResponse(BaseModel):
    id: int
    perfil_nome: str
    model_config = ConfigDict(from_attributes=True)

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: PerfilCreate

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: PerfilResponse
    model_config = ConfigDict(from_attributes=True)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios", response_model=UsuarioResponse, status_code=201)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(UsuarioDB).filter(UsuarioDB.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo_perfil = PerfilDB(perfil_nome=usuario.perfil.perfil_nome)
    db.add(novo_perfil)
    db.commit()
    db.refresh(novo_perfil)
    novo_usuario = UsuarioDB(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        id_perfil=novo_perfil.id
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@app.get("/usuarios", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()