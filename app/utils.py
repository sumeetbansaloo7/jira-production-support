import json
import os
from dotenv import load_dotenv
import requests
import base64
from requests.auth import HTTPBasicAuth

load_dotenv()

JIRA_TOKEN=os.getenv('JIRA_TOKEN')
JIRA_FILTERS=os.getenv('JIRA_FILTERS')
JIRA_API_URL=os.getenv('JIRA_API_URL')
JIRA_EMAIL=os.getenv('JIRA_EMAIL')
SEARCH_PATH="/search?jql=filter="
SEARCH_QUERY_PARAMS="&fields=key,fields&fields=summary"
BASE_BROWSW_URL="https://go-jek.atlassian.net/browse/"

config={
    "JIRA_TOKEN":JIRA_TOKEN,
    "JIRA_FILTERS":JIRA_FILTERS,
    "JIRA_API_URL":JIRA_API_URL,
    "JIRA_EMAIL":JIRA_EMAIL
    }

headers = {
    "Accept": "application/json",
}

auth = HTTPBasicAuth(JIRA_EMAIL,JIRA_TOKEN)

def jira_api_check():
    response = requests.request(
        method="GET",
        url=JIRA_API_URL+"/myself",
        headers=headers,
        auth=auth
        )
    return response.status_code

def get_jira_filter_issues(filter_id):
    response = requests.request(
        method="GET",
        url=JIRA_API_URL+SEARCH_PATH+filter_id+SEARCH_QUERY_PARAMS,
        headers=headers,
        auth=auth
        )
    issues=parse_issues(json.loads(response.text)["issues"])

    return issues

def get_jira_filter_name(filter_id):
    response = requests.request(
        method="GET",
        url=JIRA_API_URL+"/filter/"+filter_id,
        headers=headers,
        auth=auth
        )
    name=json.loads(response.text)["name"]

    return name

def parse_issues(issues):
    new_issues={}
    for issue in issues:
        new_issues[issue["key"]]=issue["fields"]["summary"]
    return new_issues

def create_jira_table(issues: dict):
    table="|Key|Issue|\n|---|-----|\n"
    for issue in issues:
        table+=f"|**[{issue}]({BASE_BROWSW_URL+issue})**|{issues[issue]}|\n"
    print(table)
    return table

def create_handover_doc():
    filters= JIRA_FILTERS.split(',')
    handover_doc=""
    
    for filter in filters:
        handover_doc+=f"**{get_jira_filter_name(filter)}**\n\n"
        issues= get_jira_filter_issues(filter)
        jira_table=create_jira_table(issues)
        handover_doc+=jira_table+"\n\n"
        
    return handover_doc
