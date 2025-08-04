# Dockerfile

FROM public.ecr.aws/lambda/python:3.11

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# (Optional) Install dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (filename.handler_function)
CMD ["lambda_function.lambda_handler"]
