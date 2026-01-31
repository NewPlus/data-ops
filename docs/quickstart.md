# 빠른 시작 가이드

## 1. 프로젝트 설정

### 환경 변수 설정
```bash
cp .env.example .env
# .env 파일을 열어 API 키 설정
```

### 의존성 설치
```bash
make install
# 또는
pip install -r requirements.txt
```

## 2. 개발 환경 시작

### 방법 A: Airflow Standalone (권장 - 개발용)
```bash
make airflow-start
# 또는
airflow standalone
```

브라우저에서 `http://localhost:8080` 접속

### 방법 B: Docker Compose
```bash
make docker-up
# 또는
cd docker && docker-compose up -d
```

## 3. 첫 번째 파이프라인 만들기

### Step 1: Collector 작성
```bash
# src/collector/sample_collector.py 생성
```

### Step 2: Task 파일 작성
```bash
# resources/sample_task.yaml 생성
# config/example_review_task.yaml 참고
```

### Step 3: DAG 확인
Airflow UI에서 DAG 확인 및 실행

## 4. 테스트

```bash
make test
# 또는
pytest tests/ -v
```

## 5. 코드 품질 확인

```bash
# 포맷팅
make format

# 린팅
make lint
```

## 6. 정리

```bash
# 임시 파일 정리
make clean

# Docker 종료
make docker-down
```

## 다음 단계

- [docs/architecture.md](architecture.md) - 아키텍처 이해
- [docs/project_structure.md](project_structure.md) - 프로젝트 구조
- [PRD.md](../PRD.md) - 전체 요구사항
- [.github/copilot-instructions.md](../.github/copilot-instructions.md) - 코딩 규칙
