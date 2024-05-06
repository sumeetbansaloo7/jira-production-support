# Jira Production Support

Service to get multiple JIRA filters details and get list of issues in it via JIRA API.

## Environment Variables
> JIRA_TOKEN=<br>
> JIRA_FILTERS=<br>
> JIRA_API_URL=<br>
> JIRA_EMAIL=<br>

To apply in your k8s cluster: 
`kubectl apply -f k8s-deploy.yaml`

## Routes
> GET /ping
 - Health check for the service

> GET /filter/{filter_id}
 - Returns Markdown table of all issues in given filter.

> GET /Handover_doc
 - Returns Markdown table of all issues in all filters that are in env variable.
