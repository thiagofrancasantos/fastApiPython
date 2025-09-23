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

print('teste funcionando')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True)