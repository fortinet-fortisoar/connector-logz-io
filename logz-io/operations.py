import json
import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('logz-io')


class LogzIO(object):
    def __init__(self, config):
        self.server_url = config.get('server_url').strip()
        self.api_key = config.get('api_key').strip()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-API-TOKEN': self.api_key
        }
        if self.server_url.startswith("http://"):
            self.server_url = self.server_url.replace("http://", "https://", 1)
        elif not self.server_url.startswith("https://"):
            self.server_url = f"https://{self.server_url}"

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False, data=None):
        url = self.server_url + endpoint
        logger.debug(f'Final URL to make REST call is: {url}')
        if headers:
            self.headers.update(headers)
        try:
            logger.debug(f'Making request with {method} and headers {self.headers}.')
            response = requests.request(method, url, headers=self.headers, data=json.dumps(data), timeout=10)
            if response.status_code in [200]:  # Successful responses
                if health_check:
                    return response
                response_data = response.json()
                return {'status': 'Success', 'data': response_data}
            elif response.status_code == 204:
                logger.info(f'No Content not found: {response.content}')
                return {'status': 'Success', 'status_code': response.status_code, 'response': "No Content"}
            elif response.status_code == 404:
                logger.info(f'Alert not found: {response.content}')
                return response.json()
            else:
                logger.error(f'Failed with response: {response.content}')
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': response.status_code, 'response': response.content})
        except requests.exceptions.RequestException as e:
            logger.error(f'Request failed: {e}')
            raise ConnectorError(str(e))


def _check_health(config):
    """
    Checks the health of the LogzIO service by making an API call to the '/v2/whoami' endpoint.

    Args:
        config (dict): A configuration dictionary containing necessary parameters to connect to LogzIO.

    Returns:
        bool: True if the health check is successful, raises ConnectorError otherwise.

    Raises:
        ConnectorError: If the health check fails, an error is logged and a ConnectorError is raised.
    """
    try:
        obj = LogzIO(config)
        obj.make_api_call(endpoint='/v2/whoami', health_check=True)
        return True
    except Exception as err:
        logger.exception(f'Health check failed: {err}')
        raise ConnectorError(f'Health check failed: {err}')


def build_payload(params):
    """
    Builds a dictionary payload by filtering out parameters that are None or empty strings.

    Args:
        params (dict): A dictionary of parameters where keys are strings and values can be of any type.

    Returns:
        dict: A dictionary containing only the key-value pairs from `params` where the value is not None and not an empty string.
    """
    result = {k: v for k, v in params.items() if v is not None and v != ''}
    return result


def retrieve_all_alerts(config, params):
    """
    Retrieves all alerts from the LogzIO service.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): Additional parameters for the API call (currently not used).

    Returns:
        list: A list of alerts retrieved from the LogzIO service.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
    """
    try:
        obj = LogzIO(config)
        return obj.make_api_call(endpoint='/v2/alerts')
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


def retrieve_alert_by_id(config, params):
    """
    Retrieves a specific alert from the LogzIO service using its alert ID.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing the alert ID under the key 'alert_id'.

    Returns:
        dict: The alert details retrieved from the LogzIO service.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
    """
    try:
        obj = LogzIO(config)
        alert_id = params.get('alert_id')
        return obj.make_api_call(endpoint=f'/v2/alerts/{alert_id}')
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


def enable_alert_by_id(config, params):
    """
    Enables a specific alert in the LogzIO service using its alert ID.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing the alert ID under the key 'alert_id'.

    Returns:
        dict: The response from the LogzIO service indicating the result of the enable operation.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
    """
    try:
        obj = LogzIO(config)
        alert_id = params.get('alert_id')
        return obj.make_api_call(endpoint=f'/v2/alerts/{alert_id}/enable', method='POST')
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


def disable_alert_by_id(config, params):
    """
    Disables a specific alert in the LogzIO service using its alert ID.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing the alert ID under the key 'alert_id'.

    Returns:
        dict: The response from the LogzIO service indicating the result of the disable operation.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
    """
    try:
        obj = LogzIO(config)
        alert_id = params.get('alert_id')
        return obj.make_api_call(endpoint=f'/v2/alerts/{alert_id}/disable', method='POST')
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


def search_logs(config, params):
    """
    Searches logs in the LogzIO service based on the provided query string.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing the search query under the key 'query'.

    Returns:
        dict: The response from the LogzIO service containing the search results.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
        Exception: Any other unexpected errors are logged with traceback.
    """
    try:
        obj = LogzIO(config)
        query_string = params.get('query')
        response = obj.make_api_call(endpoint='/v1/search', method='POST', data=query_string)
        logger.debug(f'Response from API: {response}')
        return response
    except ConnectorError as e:
        logger.error(f'ConnectorError: {e}')
    except Exception as e:
        logger.error(f'An unexpected error occurred: {e}', exc_info=True)


def get_list_of_insights(config, params):
    """
    Retrieves a list of insights from the LogzIO service based on the provided parameters.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing various parameters for filtering insights, including:
            - startDate (str): The start date for the insights query.
            - endDate (str): The end date for the insights query.
            - from (int, optional): The starting index for pagination (default is 0).
            - size (int, optional): The number of insights to return (default is 10).
            - insightTypes (str): Comma-separated insight types to filter results.
            - tagNames (str, optional): Comma-separated tag names to filter results.
            - logTypes (list, optional): A list of log types to filter results.
            - onlyNew (bool, optional): If True, only new insights are returned (default is False).
            - sortBy (str, optional): The field by which to sort the results (default is 'timestamp').
            - asc (bool, optional): If True, results are sorted in ascending order (default is True).
            - search (str, optional): A search string to filter insights.

    Returns:
        dict: The response from the LogzIO service containing the list of insights.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
    """
    try:
        obj = LogzIO(config)
        params = build_payload(params)
        payload = {
            "startDate": params.get('startDate'),
            "endDate": params.get('endDate'),
            "from": params.get('from', 0),
            "size": params.get('size', 10),
            "insightTypes": params.get('insightTypes').split(','),
            "tagNames": params.get('tagNames', '').split(',') if params.get('tagNames') else None,
            "logTypes": params.get('logTypes', []),
            "onlyNew": params.get('onlyNew', False),
            "sortBy": params.get('sortBy', 'timestamp'),
            "asc": params.get('asc', True),
            "search": params.get('search', "")
        }
        logger.debug(f'Payload: {payload}')
        return obj.make_api_call(endpoint='/v1/insights/list', method='POST', data=payload)
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


def fetch_security_events(config, params):
    """
    Fetches security events from the LogzIO service based on the provided parameters.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing parameters for the security events search, including:
            - searchTerm (str, optional): The term to search for (default is 'Falco').
            - severities (list or str): A list of severities to filter events. Can be a single string or a list of strings.
            - fromDate (str): The start date for the search range.
            - toDate (str): The end date for the search range.
            - includeMutedEvents (bool): If True, muted events are included in the results.
            - field (str): The field by which to sort the results.
            - descending (bool): If True, results are sorted in descending order.
            - pageNumber (int): The page number for pagination.
            - pageSize (int): The number of events to return per page.

    Returns:
        dict: The response from the LogzIO service containing the fetched security events.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged, and a failure message is returned.
    """
    try:
        obj = LogzIO(config)
        searchTerm = params.get('searchTerm', 'Falco')
        severities = params.get('severities')
        if isinstance(severities, str):
            severities = [severities]
        fromDate = params.get('fromDate')
        toDate = params.get('toDate')
        includeMutedEvents = params.get('includeMutedEvents')
        field = params.get('field')
        descending = params.get('descending')
        pageNumber = params.get('pageNumber')
        pageSize = params.get('pageSize')
        payload = {
            "filter": {
                "searchTerm": searchTerm,
                "severities": severities,
                "timeRange": {
                    "fromDate": fromDate,
                    "toDate": toDate
                },
                "includeMutedEvents": includeMutedEvents
            },
            "sort": [
                {
                    "field": field,
                    "descending": descending
                }
            ],
            "pagination": {
                "pageNumber": pageNumber,
                "pageSize": pageSize
            }
        }
        cleaned_payload = build_payload(payload)
        if not cleaned_payload.get('filter'):
            cleaned_payload.pop('filter', None)
        if not cleaned_payload.get('sort'):
            cleaned_payload.pop('sort', None)
        if not cleaned_payload.get('pagination'):
            cleaned_payload.pop('pagination', None)
        logger.debug(f'Payload: {cleaned_payload}')
        return obj.make_api_call(endpoint='/v2/security/rules/events/search', method='POST', data=cleaned_payload)
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')
        return {'status': 'Failure', 'message': str(e)}


def delete_an_alert(config, params):
    """
    Deletes a specific alert from the LogzIO service using its alert ID.

    Args:
        config (dict): A configuration dictionary for connecting to LogzIO.
        params (dict): A dictionary containing the alert ID under the key 'alert_id'.

    Returns:
        dict: The response from the LogzIO service indicating the result of the delete operation.

    Raises:
        ConnectorError: If there is an error during the API call, it is logged.
    """
    try:
        obj = LogzIO(config)
        alertId = params.get('alert_id')
        return obj.make_api_call(endpoint=f'/v2/alerts/{alertId}', method='DELETE')
    except ConnectorError as e:
        logger.error(f'Failed with error: {e}')


operations = {
    'retrieve_all_alerts': retrieve_all_alerts,
    'retrieve_alert_by_id': retrieve_alert_by_id,
    'enable_alert_by_id': enable_alert_by_id,
    'disable_alert_by_id': disable_alert_by_id,
    'search_logs': search_logs,
    'get_list_of_insights': get_list_of_insights,
    'fetch_security_events': fetch_security_events,
    'delete_an_alert': delete_an_alert
}
