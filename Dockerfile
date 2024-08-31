# Lambda Python 3.11 기본 이미지 사용
FROM public.ecr.aws/lambda/python:3.11

# 작업 디렉토리 설정
WORKDIR ${LAMBDA_TASK_ROOT}

# 요구 사항 파일 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# 애플리케이션 코드 복사
COPY app ${LAMBDA_TASK_ROOT}/app

# 핸들러 설정 (기본 핸들러는 app.lambda_function.lambda_handler)
CMD [ "app.lambda_function.lambda_handler" ]
