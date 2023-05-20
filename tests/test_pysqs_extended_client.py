import base64

import pytest

# from string import ascii_letters, digits
# from random import choice
from pysqs_extended_client.config import (
    AWS_ACCESS_KEY_ID,
    AWS_DEFAULT_REGION,
    AWS_SECRET_ACCESS_KEY,
    AWS_SQS_QUEUE_URL,
)
from pysqs_extended_client.SQSClientExtended import SQSClientExtended

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

def test_send_message_with_invalid_credentials():
	with pytest.raises(FileNotFoundError):
		message = None
		with open("C:\\DjangoCourse\\Courses\\celery\\introduction-promo.mp4", "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
			message = encoded_string.decode("utf-8")

		sqs = SQSClientExtended(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, 
		'tiptapcode-sqs-data')

		# _100mb_large_string = ''.join([choice(ascii_letters + digits) for i in range(104857600)])

		# message = "_100mb_large_string"

		sqs.send_message(AWS_SQS_QUEUE_URL, message)

		res = sqs.receive_message(AWS_SQS_QUEUE_URL)

		for message in res:
			sqs.delete_message(AWS_SQS_QUEUE_URL, message.get('ReceiptHandle'))


