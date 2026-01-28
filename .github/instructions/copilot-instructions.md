# GitHub Copilot 코딩 지침

## 프로젝트 개요

Python 기반 DataOps 프로젝트입니다. 데이터 파이프라인 구축, 자동화, 모니터링 및 데이터 품질 관리를 목표로 합니다.
모든 코드는 확장 가능하고 유지보수 가능하며 테스트 가능해야 합니다.

## 코딩 표준

### Python 코드 작성 규칙
- PEP 8 스타일 가이드 엄격히 준수
- Black 포맷터 사용 (line length: 100)
- 타입 힌트를 모든 함수 시그니처에 포함
- Docstring은 Google 스타일로 작성
- 변수명은 명확하고 설명적으로 작성 (약어 최소화)

### 코드 구조
```python
# 좋은 예시
def process_customer_data(
    df: pd.DataFrame,
    start_date: datetime,
    end_date: datetime
) -> pd.DataFrame:
    """고객 데이터를 처리하고 필터링합니다.
    
    Args:
        df: 원본 고객 데이터프레임
        start_date: 시작 날짜
        end_date: 종료 날짜
    
    Returns:
        처리된 데이터프레임
    
    Raises:
        ValueError: 날짜 범위가 유효하지 않을 때
    """
    # 구현...
```

## 아키텍처 가이드라인

### 프로젝트 구조
```
data-ops/
├── dags/               # Airflow DAG 파일
│   ├── etl_pipeline.py
│   └── data_quality_check.py
├── src/
│   ├── extractors/     # 데이터 추출
│   ├── transformers/   # 데이터 변환
│   ├── loaders/        # CSV 저장
│   ├── validators/     # 데이터 검증
│   └── utils/          # 유틸리티 함수
├── data/               # 데이터 저장소
│   ├── raw/           # 원본 데이터
│   ├── processed/     # 처리된 데이터
│   └── output/        # 최종 CSV 파일
├── tests/              # 테스트 코드
├── logs/               # Airflow 로그
├── plugins/            # Airflow 커스텀 플러그인
├── config/             # 설정 파일
│   ├── airflow.cfg
│   └── connections.yaml
├── docker/             # Docker 설정
│   └── docker-compose.yaml
└── docs/               # 문서
```

### 디자인 패턴
- **Factory Pattern**: 다양한 데이터 소스 커넥터 생성
- **Strategy Pattern**: 다양한 데이터 처리 전략
- **Pipeline Pattern**: ETL 프로세스 구성
- **Singleton Pattern**: 데이터베이스 연결 관리

## 모범 사례

### 데이터 처리
- 대용량 데이터는 청크(chunk) 단위로 처리
- Pandas보다 Polars 사용 권장 (성능 최적화)
- 메모리 사용량 모니터링 및 최적화
- 데이터 파이프라인은 멱등성(idempotency) 보장

### 에러 핸들링
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def fetch_data_from_api(url: str) -> dict:
    """API에서 데이터를 가져오며, 실패 시 재시도합니다."""
    # 구현...
```

### 로깅
```python
import logging
import structlog

logger = structlog.get_logger(__name__)

def process_data(data_id: str) -> None:
    logger.info("데이터 처리 시작", data_id=data_id)
    try:
        # 처리 로직
        logger.info("데이터 처리 완료", data_id=data_id)
    except Exception as e:
        logger.error("데이터 처리 실패", data_id=data_id, error=str(e))
        raise
```

## 공통 패턴

### Airflow DAG 기본 구조
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

def extract_data(**context):
    """데이터를 추출합니다."""
    # 추출 로직
    pass

def transform_data(**context):
    """데이터를 변환합니다."""
    # 변환 로직
    pass

def load_to_csv(**context):
    """CSV 파일로 저장합니다."""
    # CSV 저장 로직
    pass

with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL 파이프라인',
    schedule_interval='@daily',
    catchup=False,
    tags=['etl', 'csv'],
) as dag:
    
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )
    
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )
    
    load_task = PythonOperator(
        task_id='load_to_csv',
        python_callable=load_to_csv,
    )
    
    extract_task >> transform_task >> load_task
```

### CSV 저장 및 데이터 검증
```python
import pandas as pd
from pathlib import Path
from datetime import datetime

def save_to_csv(df: pd.DataFrame, filename: str, output_dir: str = "data/output") -> str:
    """데이터프레임을 CSV 파일로 저장합니다."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"{output_dir}/{filename}_{timestamp}.csv"
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    return filepath

def validate_data_quality(df: pd.DataFrame) -> bool:
    """데이터 품질을 검증합니다."""
    # 필수 컬럼 체크
    required_columns = ['id', 'name', 'date']
    if not all(col in df.columns for col in required_columns):
        return False
    
    # 결측치 체크
    if df[required_columns].isnull().any().any():
        return False
    
    # 중복 체크
    if df.duplicated(subset=['id']).any():
        return False
    
    return True
```

## 테스트 요구사항

### 테스트 커버리지
- 최소 80% 이상의 코드 커버리지 유지
- 모든 파이프라인 함수는 단위 테스트 필수
- 통합 테스트로 전체 워크플로우 검증

### 테스트 작성 규칙
```python
import pytest
from unittest.mock import Mock, patch

def test_process_data_success():
    """데이터 처리 성공 케이스를 테스트합니다."""
    # Given
    input_data = pd.DataFrame({"col1": [1, 2, 3]})
    
    # When
    result = process_data(input_data)
    
    # Then
    assert len(result) == 3
    assert "col1" in result.columns

def test_process_data_with_empty_dataframe():
    """빈 데이터프레임 처리를 테스트합니다."""
    # Given
    empty_df = pd.DataFrame()
    
    # When & Then
    with pytest.raises(ValueError):
        process_data(empty_df)
```

## 문서화 표준

### 함수 문서화
- 모든 public 함수는 상세한 docstring 필수
- 파라미터, 반환값, 예외사항 명시
- 사용 예시 포함

### README 작성
- 프로젝트 설명 및 목적
- 설치 방법 및 환경 설정
- 사용 예시 및 실행 방법
- 기여 가이드라인

## 보안 가이드라인

### 민감 정보 관리
- 절대 코드에 비밀번호, API 키 하드코딩 금지
- `.env` 파일 사용 및 `.gitignore`에 추가
- AWS Secrets Manager, HashiCorp Vault 사용 권장

### 데이터 보안
```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY = os.getenv("API_KEY")
```

## 성능 고려사항

### 최적화 전략
- 벡터화 연산 사용 (루프 최소화)
- 불필요한 데이터 복사 방지
- 인덱싱 및 쿼리 최적화
- 병렬 처리 활용 (multiprocessing, dask)
- 캐싱 전략 적용

### 모니터링
```python
import time
from functools import wraps

def measure_time(func):
    """함수 실행 시간을 측정합니다."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"{func.__name__} 실행 시간: {end - start:.2f}초")
        return result
    return wrapper
```

## 응답 언어

모든 코드 주석, 문서, 그리고 생성되는 텍스트는 **한국어**로 작성해주세요.

