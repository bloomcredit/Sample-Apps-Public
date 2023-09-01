from requests import post
from models.response import ErrorResponse, PlaceOrderSuccessResponse
from models.request import OrderAttributes, OrderFields, CreateOrderRequest


def createOrderRequest(app, consumer_id, name):
    headers = {
        'Authorization': f'Bearer {app.config["ACCESS_TOKEN"]}',
        "accept": "application/json",
        "content-type": "application/json",
    }

    payload = CreateOrderRequest(
        data=OrderFields(
            type="order",
            attributes=OrderAttributes(
                consumer_id=f'{consumer_id}',
                portfolio_id=app.config["PORTFOLIO_ID"],
                sku=app.config["SKU"]
            )
        )
    ).json()

    # Make request to /data-access/orders/
    r = post(app.config["ORDER_DATA_URL"],
             headers=headers, data=payload)

    # Make response json format
    response_body = r.json()

    if not r.ok:
        app.logger.error(
            "Error making order. Response Body: %s", response_body)
        return ErrorResponse(
            status="FAILED",
            errors=[
                {
                    "status": response_body["status_code"],
                    "title": response_body["status_message"],
                    "detail": response_body["status_details"]
                }
            ])

    data = response_body['data']
    attributes = response_body['data']['attributes']
    app.logger.info(
        "Success making order. Response Body: %s", response_body)
    return PlaceOrderSuccessResponse(
        consumer_id=consumer_id,
        order_id=data["id"],
        name=name,
        sku=app.config["SKU"],
        status=attributes["status"]
    )
