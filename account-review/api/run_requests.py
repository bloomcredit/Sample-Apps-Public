from db.db_utils import get_consumer_byid
from api import order, get_order


def getData(app, selected_items):
    successful = []
    failed = []

    for consumer_id in selected_items:
        consumer_request = get_consumer_byid(consumer_id)

        # Skip if consumer was not found in DB
        if not consumer_request:
            continue

        order_request = order.createOrderRequest(
            app, consumer_id, consumer_request.get("name"))

        if order_request.status == 'SUCCESS':
            gql_order = get_order.getOrder(
                app, order_request.order_id)

            # Safety checks for the gql_order structure
            if gql_order.status == 'SUCCESS':
                credit_data = gql_order.data["credit_data_order_by_pk"]
                # If credit data was not found, we assume it failed and asign ??? to credit score
                if credit_data:
                    credit_scores = credit_data["credit_scores"]
                    if credit_scores:
                        vantage = credit_scores[0]["value"]
                        if vantage:
                            successful.append({
                                "id": consumer_request.get("id"),
                                "name": consumer_request.get("name"),
                                "vantage": vantage
                            })
                else:
                    failed.append({
                        "id": consumer_request.get("id"),
                        "name": consumer_request.get("name"),
                        "vantage": "???"
                    })

    return {"successful_scores": successful, "failed_scores": failed}
