from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    nome: str
    email: str

usuarios: List[User] = []

@app.post("/usuarios")
def criar_usuario(usuario: User):
    usuarios.append(usuario)
    return usuario

@app.get("/usuarios")
def listar_usuarios():
    return usuarios
