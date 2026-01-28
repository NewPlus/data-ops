# GitHub Copilot 워크스페이스 설정

## 프로젝트 컨텍스트

이 프로젝트는 DataOps를 주제로 하는 Python 기반 프로젝트입니다.
데이터 파이프라인 구축, 데이터 품질 관리, 데이터 모니터링, 그리고 데이터 워크플로우 자동화에 중점을 둡니다.

## 기술 스택

- **언어**: Python 3.9+
- **데이터 처리**: pandas, numpy
- **오케스트레이션**: Apache Airflow
- **데이터 저장**: CSV 파일 (로컬)
- **컨테이너**: Docker, Docker Compose
- **버전 관리**: Git

## 개발 워크플로우

1. 기능 개발 시 feature 브랜치 생성
2. 데이터 파이프라인 코드 작성
3. 단위 테스트 및 통합 테스트 작성
4. 데이터 품질 검증 추가
5. Pull Request 생성 및 코드 리뷰
6. CI/CD 파이프라인 통과 확인
7. main 브랜치로 병합

## 코드 스타일

- **Python 스타일 가이드**: PEP 8 준수
- **Formatter**: Black (line length: 100)
- **Linter**: Ruff 또는 Flake8
- **Type Hints**: 모든 함수에 타입 힌트 사용
- **Docstring**: Google 스타일 또는 NumPy 스타일
- **변수명**: snake_case 사용
- **클래스명**: PascalCase 사용
- **상수**: UPPER_CASE 사용

## 의존성 관리

- `requirements.txt`: 프로덕션 의존성
- `requirements-dev.txt`: 개발 의존성
- `poetry` 또는 `pipenv` 사용 권장
- 가상환경 사용 필수 (venv, conda)

## 환경 설정

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 환경 변수 설정
cp .env.example .env
```

## 자주 사용하는 명령어

```bash
# 코드 포맷팅
black .
isort .

# 린트 체크
ruff check .
mypy .

# 테스트 실행
pytest tests/
pytest --cov=src tests/

# Airflow 초기화
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

# Airflow 실행 (개발 모드)
airflow standalone

# 또는 Docker Compose로 실행
docker-compose up -d

# DAG 리스트 확인
airflow dags list

# 특정 DAG 실행
airflow dags trigger <dag_id>

# DAG 테스트
airflow dags test <dag_id> <execution_date>
```

## 코드 작성 시 주의사항

- 모든 데이터 처리 함수는 멱등성(idempotency)을 보장해야 함
- Airflow DAG는 `dags/` 폴더에 저장
- CSV 파일은 `data/` 폴더에 저장 (raw, processed, output 구분)
- 대용량 데이터 처리 시 메모리 효율성 고려 (chunking 사용)
- 민감한 정보는 환경 변수로 관리 (.env 파일 사용)
- Airflow Connection과 Variable을 활용한 설정 관리
- 로깅은 structured logging 방식 사용 (JSON 형식)
- 에러 핸들링 및 재시도 로직 구현 (Airflow의 retry 기능 활용)
- 데이터 품질 검증 로직 포함 (BranchPythonOperator 활용)
- CSV 파일명에 타임스탬프 포함 권장 (덮어쓰기 방지)

