from typing import List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Header

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from time import sleep

from models import Curso

def fake_db():
    try:
        print('Abrindo conexao com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexao com banco de dados...')
        sleep(1)
    

app = FastAPI(
    title='Api de Cursos',
    version='0.0.1',
    description='Api para visualizar cursos'   
)

cursos = {
    1: {
        "titulo": "Hoje o ceu abriu",
        "aulas": 122,
        "horas": 79
    },
    2: {
        "titulo": "Teste de Uso",
        "aulas": 12,
        "horas": 7
    },
    3: {
        "titulo": "Caso de teste",
        "aulas": 15,
        "horas": 10
    }
}

@app.get('/cursos')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser entre 1 e 3', gt=0, lt=4), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.'
        )

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nao existe um curso com id {curso_id}")
    
@app.delete('/cursos{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nao existe um curso com id {curso_id}") 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)