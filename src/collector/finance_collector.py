from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable, Mapping, Sequence

import yfinance as yf

from src.collector.base_collector import BaseCollector


class FinanceDataCollector(BaseCollector):
    """Yahoo Finance API를 통해 주가 데이터를 수집하는 Collector입니다."""

    def __init__(
        self,
        tickers: Sequence[str],
        source_name: str,
        source_type: str,
        user_name: str,
        config_collector: Mapping[str, Any],
    ) -> None:
        """FinanceDataCollector를 초기화합니다.

        Args:
            tickers: 수집할 티커 목록
            source_name: 데이터 소스 이름
            source_type: 데이터 소스 종류
            user_name: 수집자 이름
            config_collector: 수집기 설정 맵
        """

        super().__init__(
            source_name=source_name,
            source_type=source_type,
            user_name=user_name,
            config_collector=config_collector,
        )
        self._tickers = list(tickers)

    def collect(self) -> Iterable[Mapping[str, Any]]:
        """티커별 주가 데이터를 JSON 직렬화 가능한 형태로 수집합니다."""

        records: list[Mapping[str, Any]] = []
        collected_at = datetime.now(timezone.utc).isoformat()

        for ticker in self._tickers:
            info = yf.Ticker(ticker).fast_info
            records.append(
                {
                    "ticker": ticker,
                    "currency": info.get("currency"),
                    "timezone": info.get("timezone"),
                    "exchange": info.get("exchange"),
                    "market_price": info.get("last_price"),
                    "previous_close": info.get("previous_close"),
                    "open_price": info.get("open"),
                    "day_high": info.get("day_high"),
                    "day_low": info.get("day_low"),
                    "market_cap": info.get("market_cap"),
                    "collected_at": collected_at,
                }
            )

        return records

    def _validate_records(self, records: Iterable[Mapping[str, Any]]) -> None:
        """수집 결과 레코드의 기본 구조를 검증합니다.

        Args:
            records: 수집된 레코드 목록
        """

        required_keys = {"ticker", "market_price", "previous_close", "open_price"}
        for record in records:
            missing_keys = required_keys - set(record.keys())
            if missing_keys:
                raise ValueError(f"필수 키가 누락되었습니다: {sorted(missing_keys)}")
