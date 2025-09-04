from fastapi import FastAPI


def my_app() -> FastAPI:
    app_ = FastAPI(title="Cart Serivce")

    return app_


app: FastAPI = my_app()
