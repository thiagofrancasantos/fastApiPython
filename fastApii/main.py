from fastapi import FastAPI

app = FastAPI()

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
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({"id": curso_id})

    return curso



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)