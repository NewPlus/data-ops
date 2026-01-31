from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from typing import Any, Iterable, Mapping


@dataclass(frozen=True)
class CollectorResult:
	"""수집 결과 정보를 담는 데이터 클래스입니다.

	Attributes:
		collected_at: 수집 일자와 시간
		collector: 수집자 이름
		collector_name: 수집기 클래스 이름
		data_type: 수집 데이터의 종류
		record_count: 수집된 데이터 행 수
	"""

	collected_at: datetime
	collector: str
	collector_name: str
	data_type: str
	record_count: int


class BaseCollector(ABC):
	"""Collector 공통 기능을 제공하는 추상 클래스입니다.

	모든 Collector는 이 클래스를 상속해야 하며, `collect` 메서드를 구현해야 합니다.
	공통 기능(Parquet 저장, 경로 생성, 실행 플로우)을 이 클래스에서 처리합니다.
	"""

	def __init__(
		self,
		source_name: str,
		source_type: str,
		user_name: str,
		config_collector: Mapping[str, Any],
	) -> None:
		"""BaseCollector를 초기화합니다.

		Args:
			source_name: 데이터 소스 이름
			source_type: 데이터 소스 종류
			user_name: 수집자 이름
			config_collector: 수집기 설정 맵
		"""

		self._source_name = source_name
		self._source_type = source_type
		self._user_name = user_name
		self._config_collector = dict(config_collector)

	@property
	def source_name(self) -> str:
		"""데이터 소스 이름을 반환합니다."""

		return self._source_name

	def get_source_name(self) -> str:
		"""데이터 소스 이름을 반환합니다."""

		return self._source_name

	def get_source_type(self) -> str:
		"""데이터 소스 종류를 반환합니다."""

		return self._source_type

	def get_user_name(self) -> str:
		"""수집자 이름을 반환합니다."""

		return self._user_name

	def get_config_collector(self) -> Mapping[str, Any]:
		"""수집기 설정 맵을 반환합니다."""

		return self._config_collector

	@abstractmethod
	def collect(self) -> Iterable[Mapping[str, Any]]:
		"""데이터를 수집하여 JSON 직렬화 가능한 레코드 목록을 반환합니다."""

	def run(self) -> CollectorResult:
		"""수집 → 저장까지의 표준 실행 플로우를 수행합니다.

		Returns:
			수집 결과 정보
		"""

		records = list(self.collect())
		self._validate_json_serializable(records)
		self._validate_records(records)
		return CollectorResult(
			collected_at=datetime.now(timezone.utc),
			collector=self._user_name,
			collector_name=self.__class__.__name__,
			data_type=str(self._config_collector.get("data_type", "unknown")),
			record_count=len(records),
		)

	def _validate_json_serializable(self, records: Iterable[Mapping[str, Any]]) -> None:
		"""수집 결과가 JSON으로 직렬화 가능한지 검증합니다.

		Args:
			records: 수집된 레코드 목록
		"""

		json.dumps(list(records), ensure_ascii=False)

	@abstractmethod
	def _validate_records(self, records: Iterable[Mapping[str, Any]]) -> None:
		"""수집 결과 레코드를 검증합니다.

		Args:
			records: 수집된 레코드 목록
		"""
