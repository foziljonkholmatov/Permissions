import traceback
from rest_framework.views import exception_handler
from response import custom_response
from telegram_logger import send_telegram_error

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        return custom_response(
            success=False,
            message=str(exc),
            data=None,
            status_code=response.status_code
        )
    error_message = f"""
<b>UNEXPECTED ERROR</b>
View: {context.get('view')}
Exception: {str(exc)}
Traceback:
{''.join(traceback.format_tb(exc.__traceback__))}
    """
    send_telegram_error(error_message)

    return custom_response(
        success=False,
        message="Internal server error. Admin notified!",
        data=None,
        status_code=500
    )
