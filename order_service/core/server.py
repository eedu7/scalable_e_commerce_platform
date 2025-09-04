from fastapi import FastAPI


def my_app() -> FastAPI:
    app_ = FastAPI(title="Order Service")

    return app_


app: FastAPI = my_app()
