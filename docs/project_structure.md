# 프로젝트 구조 문서

## 폴더 구조 설명

### `/dags`
Airflow DAG 파일을 저장하는 폴더입니다.
- 데이터 파이프라인 정의
- 스케줄링 설정
- Task 의존성 관리

### `/src`
프로젝트의 핵심 소스 코드를 포함합니다.

#### `/src/collector`
다양한 데이터 소스에서 데이터를 수집하는 모듈입니다.
- `BaseCollector` 추상 클래스
- 각 데이터 소스별 Collector 구현

#### `/src/cleaners`
LLM을 활용하여 데이터를 정제하는 모듈입니다.
- LLM API 클라이언트
- 데이터 구조화 로직
- Task 파일 파서

#### `/src/loaders`
정제된 데이터를 CSV로 저장하는 모듈입니다.
- Parquet → CSV 변환
- 메타 컬럼 추가
- 파일명 관리

#### `/src/validators`
데이터 품질을 검증하는 모듈입니다.
- 필수 컬럼 체크
- 데이터 타입 검증
- 중복 데이터 감지

#### `/src/utils`
프로젝트 전반에서 사용되는 유틸리티 함수입니다.
- Parquet 유틸리티
- 로깅 헬퍼
- 공통 함수

### `/resources`
LLM Task 정의 파일(YAML)을 저장합니다.
- 출력 스키마 정의
- 추출 규칙 명시
- 검증 규칙 설정

### `/data`
데이터 파일을 저장하는 폴더입니다.

#### `/data/raw`
수집된 원본 데이터 (Parquet 형식)

#### `/data/processed`
LLM으로 정제된 데이터 (Parquet 형식)

#### `/data/output`
최종 결과물 (CSV 형식)

### `/config`
프로젝트 설정 파일 및 예시 파일을 저장합니다.
- LLM 설정
- Airflow 설정
- Task 파일 예시

### `/docker`
Docker 관련 파일을 저장합니다.
- `docker-compose.yaml`: 컨테이너 오케스트레이션 정의

### `/tests`
테스트 코드를 저장합니다.
- 단위 테스트
- 통합 테스트
- 픽스처

### `/logs`
Airflow 실행 로그를 저장합니다.

### `/plugins`
Airflow 커스텀 플러그인을 저장합니다.

### `/docs`
프로젝트 문서를 저장합니다.
- 사용 가이드
- API 문서
- 아키텍처 다이어그램
