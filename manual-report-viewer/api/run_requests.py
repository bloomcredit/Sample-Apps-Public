from api import consumer, order, get_order


def getData(app, formFields):
    # Get Full Name
    name = formFields['Fname'] + " " + formFields['Lname']
    consumer_request = consumer.createConsumerRequest(
        app, formFields)
    if consumer_request.status == "FAILED":
        return consumer_request
    order_request = order.createOrderRequest(
        app, consumer_request.id, name)
    if order_request.status == "FAILED":
        return order_request
    gql_order = get_order.getOrder(app, order_request.order_id)
    return gql_order
