## About the connector
Logz.io delivers unified, full stack observability and security as a fully-managed SaaS based on best-of-breed open source. The Open 360 platform brings together logs, metrics, traces, and security data, applying powerful AI/ML features to improve troubleshooting, reduce response times, and help manage costs.
<p>This document provides information about the Logz.io Connector, which facilitates automated interactions, with a Logz.io server using FortiSOAR&trade; playbooks. Add the Logz.io Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Logz.io.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-logz-io</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Logz.io server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Logz.io server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Logz.io</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the logz.io server to connect and perform automated operations.
</td>
</tr><tr><td>API key</td><td>Specify the API key to access the endpoint to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Alerts List</td><td>Returns the complete list of all alerts configured for the account.</td><td>retrieve_all_alerts <br/>Investigation</td></tr>
<tr><td>Get Alert By ID</td><td>Retrieves the alert details based on the alert ID that you have specified.</td><td>retrieve_alert_by_id <br/>Investigation</td></tr>
<tr><td>Enable Alert By ID</td><td>Enables an alert by its alert ID. This is reversible. The alert can be disabled again at any time.</td><td>enable_alert_by_id <br/>Investigation</td></tr>
<tr><td>Disable Alert By ID</td><td>Disables an alert by its alert ID. This is reversible. The alert can be enabled again at any time.</td><td>disable_alert_by_id <br/>Investigation</td></tr>
<tr><td>Search Logs</td><td>Searches your account data using the Elasticsearch Search API DSL query language. total: This call returns up to 1,000 results per query for aggregated results, or 10,000 results for non-aggregated results.</td><td>search_logs <br/>Investigation</td></tr>
<tr><td>Get Insights List</td><td>Retrieves the detailed list of insights based on the parameters that you have specified.</td><td>get_list_of_insights <br/>Investigation</td></tr>
<tr><td>Get Security Events List</td><td>Runs a search query in your Logz.io Cloud SIEM account to fetch the security events that match the query parameters.</td><td>fetch_security_events <br/>Investigation</td></tr>
<tr><td>Delete Alert By ID</td><td>Delete alert based on the alert ID that you have specified.</td><td>delete_an_alert <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Alerts List
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>[
    [
        {
            "id": "",
            "updatedAt": "",
            "updatedBy": "",
            "createdAt": "",
            "createdBy": "",
            "enabled": "",
            "title": "",
            "description": "",
            "tags": [],
            "output": {
                "recipients": {
                    "emails": [],
                    "notificationEndpointIds": []
                },
                "suppressNotificationsMinutes": "",
                "type": ""
            },
            "searchTimeFrameMinutes": "",
            "subComponents": [
                {
                    "queryDefinition": {
                        "query": "",
                        "filters": {
                            "bool": {
                                "must": [
                                    {
                                        "match_phrase": {
                                            "Field": {
                                                "query": ""
                                            }
                                        }
                                    }
                                ],
                                "must_not": [
                                    {
                                        "match_phrase": {
                                            "Field": {
                                                "query": ""
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        "groupBy": [],
                        "aggregation": {
                            "aggregationType": "",
                            "fieldToAggregateOn": "",
                            "valueToAggregateOn": ""
                        },
                        "shouldQueryOnAllAccounts": "",
                        "accountIdsToQueryOn": []
                    },
                    "trigger": {
                        "operator": "",
                        "severityThresholdTiers": {
                            "MEDIUM": "",
                            "HIGH": "",
                            "SEVERE": ""
                        }
                    },
                    "output": {
                        "shouldUseAllFields": ""
                    }
                }
            ],
            "correlations": {
                "correlationOperators": [
                    ""
                ],
                "joins": [
                    {
                        "0": "",
                        "1": ""
                    }
                ]
            },
            "schedule": {
                "cronExpression": "",
                "timezone": ""
            }
        }
    ]
]</pre>
### operation: Get Alert By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify Unique identifier of the alert in Logz.io.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    [
        {
            "id": "",
            "updatedAt": "",
            "updatedBy": "",
            "createdAt": "",
            "createdBy": "",
            "enabled": "",
            "title": "",
            "description": "",
            "tags": [],
            "output": {
                "recipients": {
                    "emails": [],
                    "notificationEndpointIds": []
                },
                "suppressNotificationsMinutes": "",
                "type": ""
            },
            "searchTimeFrameMinutes": "",
            "subComponents": [
                {
                    "queryDefinition": {
                        "query": "",
                        "filters": {
                            "bool": {
                                "must": [
                                    {
                                        "match_phrase": {
                                            "Field": {
                                                "query": ""
                                            }
                                        }
                                    }
                                ],
                                "must_not": [
                                    {
                                        "match_phrase": {
                                            "Field": {
                                                "query": ""
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        "groupBy": [],
                        "aggregation": {
                            "aggregationType": "",
                            "fieldToAggregateOn": "",
                            "valueToAggregateOn": ""
                        },
                        "shouldQueryOnAllAccounts": "",
                        "accountIdsToQueryOn": []
                    },
                    "trigger": {
                        "operator": "",
                        "severityThresholdTiers": {
                            "MEDIUM": "",
                            "HIGH": "",
                            "SEVERE": ""
                        }
                    },
                    "output": {
                        "shouldUseAllFields": ""
                    }
                }
            ],
            "correlations": {
                "correlationOperators": [
                    ""
                ],
                "joins": [
                    {
                        "0": "",
                        "1": ""
                    }
                ]
            },
            "schedule": {
                "cronExpression": "",
                "timezone": ""
            }
        }
    ]
]</pre>
### operation: Enable Alert By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify Unique identifier of the alert in Logz.io.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Disable Alert By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Specify Unique identifier of the alert in Logz.io.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Search Logs
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Query</td><td>The query can take any of the parameters described in the Elasticsearch Search API DSL documentation
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Get Insights List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Start Date</td><td>UNIX timestamp in milliseconds specifying the start date for the query time frame.
</td></tr><tr><td>End Date</td><td>UNIX timestamp in milliseconds specifying the end date for the query time frame.
</td></tr><tr><td>Offset</td><td>Specify the offset that is starting index from where the records should be fetched.
</td></tr><tr><td>Size</td><td>Specify the maximum number of records to return. Must be a positive integer between 1-100.
</td></tr><tr><td>Insight Types</td><td>Filters results by Insight type. LOGCEPTION filters for application insights. PUBLIC_CI filters for Cognitive Insights.
</td></tr><tr><td>Tag Names</td><td>Filters results by the tag values used to categorize Insights.
</td></tr><tr><td>Log Types</td><td>Filters results by log type.
</td></tr><tr><td>Only New</td><td>Filters for Insights that first occurred in the selected time frame. In other words, excludes Insights that were first identified before or after the selected time range.
</td></tr><tr><td>Sort By</td><td>Sorts Insights by the selected parameters.
</td></tr><tr><td>Sort Order</td><td>Select the checkbox to sort in ascending order. The sorting of records is done on the field specified in Sort By parameter.
</td></tr><tr><td>Search</td><td>Searches for an Insight by its title.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "pageSize": "",
        "from": "",
        "total": "",
        "results": [
            {
                "insightId": "",
                "insightType": "",
                "tagName": "",
                "description": "",
                "links": "",
                "additionalData": "",
                "firstOccurrence": "",
                "lastOccurrence": "",
                "count": "",
                "logTypes": [
                    ""
                ],
                "kibanaLink": "",
                "insightTitle": ""
            }
        ]
    }
]</pre>
### operation: Get Security Events List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Search Term</td><td>Filter for a matching string in the security rule name.
</td></tr><tr><td>Severities</td><td>Filter by the severities of the security rules.
</td></tr><tr><td>From Date</td><td>Absolute UNIX timestamp in seconds (not milliseconds). Your security account's retention policy determines the earliest events you'll be able to retrieve.
</td></tr><tr><td>To Date</td><td>Absolute UNIX timestamp in seconds (not milliseconds).
</td></tr><tr><td>Include Muted Events</td><td>Defines if muted events need to be passed. The endpoint will return both non-muted and muted events if this is set to true.
</td></tr><tr><td>Sort By</td><td>Specify the sort by value to sort the records.
</td></tr><tr><td>Sort Order</td><td>Select the checkbox to sort in descending order. The sorting of records is done on the field specified in Sort By parameter.
</td></tr><tr><td>Page Number</td><td>If you overshoot the page number, it will return empty with no results, but it won't fail the request.
</td></tr><tr><td>Page Size</td><td>Controls the number of results per page. Valid inputs are 1 to 1000.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
### operation: Delete Alert By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Alert ID</td><td>Unique identifier of the alert in Logz.io.
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - logz-io - 1.0.0` playbook collection comes bundled with the Logz.io connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Logz.io connector.

- Get Alerts List
- Get Alert By ID
- Enable Alert By ID
- Disable Alert By ID
- Search Logs
- Get Insights List
- Get Security Events List
- Delete Alert By ID

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
