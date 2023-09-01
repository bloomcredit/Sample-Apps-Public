from requests import post
from models.response import ErrorResponse, GetOrderSuccessResponse


def getOrder(app, order_id):
    headers = {
        "Authorization": f'Bearer {app.config["ACCESS_TOKEN"]}',
        "accept": "application/json",
        "content-type": "application/json",
    }

    query = """query ($id: uuid!) {
    credit_data_order_by_pk(order_id: $id) {
        consumer_id
        credit_scores {
            model
            value
        },
        order_id,
    }
}
    """

    variables = {
        "id": order_id
    }

    r = post(app.config["QUERY_DATA_GQL_URL"], headers=headers, json={
        'query': query, 'variables': variables})

    response_body = r.json()
    if not r.ok:
        app.logger.error(
            "Error getting the order %s. Response Body: %s", order_id, response_body)
        return ErrorResponse(status="FAILED", errors=response_body.get("errors", []))

    app.logger.info(
        "Success getting the order %s. Response Body: %s", order_id, response_body)
    return GetOrderSuccessResponse(
        status="SUCCESS", data=response_body.get("data", {})
    )
