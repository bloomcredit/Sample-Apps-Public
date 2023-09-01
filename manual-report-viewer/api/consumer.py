from requests import post

from models.request import (
    CreateConsumerRequest,
    ConsumerFields,
    ConsumerAttributes,
    ConsumerName,
    ConsumerAddress,
)

from models.response import ErrorResponse, ConsumerSuccessResponse


def createConsumerRequest(app, formFields):
    headers = {
        "Authorization": f'Bearer {app.config["ACCESS_TOKEN"]}',
        "accept": "application/json",
        "content-type": "application/json",
    }

    # Create request dict
    request = CreateConsumerRequest(
        data=ConsumerFields(
            type="consumers",
            attributes=ConsumerAttributes(
                ssn=formFields["ssn"].replace("-", ""),
                date_of_birth=formFields["birthdate"],
                name=ConsumerName(
                    first_name=formFields["Fname"], last_name=formFields["Lname"]
                ),
                addresses=[
                    ConsumerAddress(
                        line1=formFields["address"].upper(),
                        city=formFields["city"].upper(),
                        state_code=formFields["state"].upper(),
                        zipcode=formFields["zipcode"],
                        primary=True,
                    )
                ],
            ),
        )
    ).json()

    # Make post request to /core/consumers
    r = post(app.config["CREATE_CONSUMER_URL"],
             headers=headers, data=request)

    response_body = r.json()
    if not r.ok:
        app.logger.error(
            "Error register test consumer. Response Body: %s", response_body)
        return ErrorResponse(status="FAILED", errors=response_body.get("errors", []))

    consumer_success_id = response_body["data"]["id"]
    app.logger.info(
        "Success register test consumer. Response Body: %s", response_body)
    return ConsumerSuccessResponse(status="SUCCESS", id=consumer_success_id)
