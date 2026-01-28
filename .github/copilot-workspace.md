# GitHub Copilot 워크스페이스 설정

## 프로젝트 컨텍스트

이 프로젝트는 DataOps를 주제로 하는 Python 기반 프로젝트입니다.
데이터 파이프라인 구축, 데이터 품질 관리, 데이터 모니터링, 그리고 데이터 워크플로우 자동화에 중점을 둡니다.

### 데이터 파이프라인 플로우

1. **데이터 수집**: `src/collector/`의 데이터 수집 코드 실행 → DataFrame → Parquet 저장
2. **데이터 정제**: Parquet 파일 읽기 → LLM 기반 정제 → Parquet 저장
3. **데이터 저장**: Parquet 파일 읽기 → CSV 파일로 최종 저장
4. **오케스트레이션**: 전체 과정을 Apache Airflow로 관리

## 기술 스택

- **언어**: Python 3.13+
- **데이터 처리**: pandas, numpy, pyarrow (Parquet 처리)
- **LLM**: OpenAI API, Anthropic API, 또는 로컬 LLM
- **오케스트레이션**: Apache Airflow
- **데이터 저장**: Parquet (중간), CSV (최종)
- **컨테이너**: Docker, Docker Compose
- **버전 관리**: Git

## 개발 워크플로우

1. 기능 개발 시 feature 브랜치 생성
2. 데이터 수집 코드 작성 (`src/collector/` - 향후 구현 예정)
3. LLM 정제 task 정의 (`resources/` - task 파일 작성)
4. Airflow DAG 구성 (수집 → 정제 → 저장)
5. 단위 테스트 및 통합 테스트 작성
6. Pull Request 생성 및 코드 리뷰
7. CI/CD 파이프라인 통과 확인
8. main 브랜치로 병합

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

# Parquet 파일 확인 (pandas 사용)
python -c "import pandas as pd; df = pd.read_parquet('data/raw/sample.parquet'); print(df.head())"

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

# Task 단위 테스트
airflow tasks test <dag_id> <task_id> <execution_date>
```

## 코드 작성 시 주의사항

### 데이터 수집 (`src/collector/`)
- 각 데이터 소스별로 독립적인 수집 모듈 작성 (향후 구현 예정)
- 수집된 데이터는 반드시 pandas DataFrame으로 변환
- DataFrame은 즉시 Parquet 형식으로 `data/raw/` 폴더에 저장
- Parquet 저장 시 압축 옵션 사용 (`compression='snappy'`)

### 데이터 정제 (LLM 기반)
- `resources/` 폴더의 task 파일에서 LLM 정제 작업 정의
- Parquet 파일에서 데이터 읽기 → LLM 처리 → Parquet 저장 (`data/processed/`)
- LLM API 호출 시 rate limit 및 에러 핸들링 필수
- 정제 결과는 원본과 함께 보관 (추적 가능성)

### 데이터 저장
- 최종 데이터는 `data/output/` 폴더에 CSV 형식으로 저장
- CSV 파일명에 타임스탬프 포함 (`YYYYMMDD_HHMMSS` 형식)

### Airflow DAG 작성
- 모든 데이터 처리 함수는 멱등성(idempotency)을 보장해야 함
- Airflow DAG는 `dags/` 폴더에 저장
- Task 간 데이터 전달은 XCom 또는 파일 경로 사용
- 에러 핸들링 및 재시도 로직 구현 (Airflow의 retry 기능 활용)
- 대용량 데이터 처리 시 메모리 효율성 고려 (chunking 사용)

### 보안 및 설정
- LLM API 키는 환경 변수로 관리 (.env 파일 사용)
- Airflow Connection과 Variable을 활용한 설정 관리
- 민감한 정보는 절대 코드에 하드코딩 금지

### 로깅
- 로깅은 structured logging 방식 사용 (JSON 형식)
- 각 단계별 처리 시간 및 데이터 건수 로깅

