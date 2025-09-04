from fastapi import FastAPI


def my_app() -> FastAPI:
    app_ = FastAPI(title="Payment Service")

    return app_


app: FastAPI = my_app()
