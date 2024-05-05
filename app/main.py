from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, Response
from utils import create_jira_table, get_jira_filter_issues, jira_api_check, create_handover_doc


app = FastAPI()


@app.get("/ping")
def ping():
    if jira_api_check() > 400:
        return Response("Jira API called failed",status_code=500)
    return {"pong"}

@app.get("/filter/{filter_id}",response_class=PlainTextResponse)
def get_filter_issues(filter_id):
    
    issues= get_jira_filter_issues(filter_id)
    jira_table=create_jira_table(issues)
    
    return jira_table


@app.get("/handover_doc",response_class=PlainTextResponse)
def get_handover_doc():
    return create_handover_doc()
