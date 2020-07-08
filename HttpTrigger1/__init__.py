import logging
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
   # params = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:qing-sql-servver.database.windows.net,1433;Database=qin-db;Uid=qingr;Pwd={##!1979};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    params2 = "mssql+pyodbc://qing-sql-servver/qin-db?driver=ODBC+Driver+17+for+SQL+Server"
    engine_azure_pro = create_engine(params2, fast_executemany=True, echo_pool=True)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
