from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebConfig")


@_attrs_define
class WebConfig:
    """
    Attributes:
        enable_web_search (Union[None, Unset, bool]):
        web_search_engine (Union[None, Unset, str]):
        web_search_trust_env (Union[None, Unset, bool]):
        web_search_result_count (Union[None, Unset, int]):
        web_search_concurrent_requests (Union[None, Unset, int]):
        web_loader_concurrent_requests (Union[None, Unset, int]):
        web_search_domain_filter_list (Union[None, Unset, list[str]]):
        bypass_web_search_embedding_and_retrieval (Union[None, Unset, bool]):
        bypass_web_search_web_loader (Union[None, Unset, bool]):
        searxng_query_url (Union[None, Unset, str]):
        yacy_query_url (Union[None, Unset, str]):
        yacy_username (Union[None, Unset, str]):
        yacy_password (Union[None, Unset, str]):
        google_pse_api_key (Union[None, Unset, str]):
        google_pse_engine_id (Union[None, Unset, str]):
        brave_search_api_key (Union[None, Unset, str]):
        kagi_search_api_key (Union[None, Unset, str]):
        mojeek_search_api_key (Union[None, Unset, str]):
        bocha_search_api_key (Union[None, Unset, str]):
        serpstack_api_key (Union[None, Unset, str]):
        serpstack_https (Union[None, Unset, bool]):
        serper_api_key (Union[None, Unset, str]):
        serply_api_key (Union[None, Unset, str]):
        tavily_api_key (Union[None, Unset, str]):
        searchapi_api_key (Union[None, Unset, str]):
        searchapi_engine (Union[None, Unset, str]):
        serpapi_api_key (Union[None, Unset, str]):
        serpapi_engine (Union[None, Unset, str]):
        jina_api_key (Union[None, Unset, str]):
        bing_search_v7_endpoint (Union[None, Unset, str]):
        bing_search_v7_subscription_key (Union[None, Unset, str]):
        exa_api_key (Union[None, Unset, str]):
        perplexity_api_key (Union[None, Unset, str]):
        perplexity_model (Union[None, Unset, str]):
        perplexity_search_context_usage (Union[None, Unset, str]):
        sougou_api_sid (Union[None, Unset, str]):
        sougou_api_sk (Union[None, Unset, str]):
        web_loader_engine (Union[None, Unset, str]):
        enable_web_loader_ssl_verification (Union[None, Unset, bool]):
        playwright_ws_url (Union[None, Unset, str]):
        playwright_timeout (Union[None, Unset, int]):
        firecrawl_api_key (Union[None, Unset, str]):
        firecrawl_api_base_url (Union[None, Unset, str]):
        tavily_extract_depth (Union[None, Unset, str]):
        external_web_search_url (Union[None, Unset, str]):
        external_web_search_api_key (Union[None, Unset, str]):
        external_web_loader_url (Union[None, Unset, str]):
        external_web_loader_api_key (Union[None, Unset, str]):
        youtube_loader_language (Union[None, Unset, list[str]]):
        youtube_loader_proxy_url (Union[None, Unset, str]):
        youtube_loader_translation (Union[None, Unset, str]):
    """

    enable_web_search: Union[None, Unset, bool] = UNSET
    web_search_engine: Union[None, Unset, str] = UNSET
    web_search_trust_env: Union[None, Unset, bool] = UNSET
    web_search_result_count: Union[None, Unset, int] = UNSET
    web_search_concurrent_requests: Union[None, Unset, int] = UNSET
    web_loader_concurrent_requests: Union[None, Unset, int] = UNSET
    web_search_domain_filter_list: Union[None, Unset, list[str]] = UNSET
    bypass_web_search_embedding_and_retrieval: Union[None, Unset, bool] = UNSET
    bypass_web_search_web_loader: Union[None, Unset, bool] = UNSET
    searxng_query_url: Union[None, Unset, str] = UNSET
    yacy_query_url: Union[None, Unset, str] = UNSET
    yacy_username: Union[None, Unset, str] = UNSET
    yacy_password: Union[None, Unset, str] = UNSET
    google_pse_api_key: Union[None, Unset, str] = UNSET
    google_pse_engine_id: Union[None, Unset, str] = UNSET
    brave_search_api_key: Union[None, Unset, str] = UNSET
    kagi_search_api_key: Union[None, Unset, str] = UNSET
    mojeek_search_api_key: Union[None, Unset, str] = UNSET
    bocha_search_api_key: Union[None, Unset, str] = UNSET
    serpstack_api_key: Union[None, Unset, str] = UNSET
    serpstack_https: Union[None, Unset, bool] = UNSET
    serper_api_key: Union[None, Unset, str] = UNSET
    serply_api_key: Union[None, Unset, str] = UNSET
    tavily_api_key: Union[None, Unset, str] = UNSET
    searchapi_api_key: Union[None, Unset, str] = UNSET
    searchapi_engine: Union[None, Unset, str] = UNSET
    serpapi_api_key: Union[None, Unset, str] = UNSET
    serpapi_engine: Union[None, Unset, str] = UNSET
    jina_api_key: Union[None, Unset, str] = UNSET
    bing_search_v7_endpoint: Union[None, Unset, str] = UNSET
    bing_search_v7_subscription_key: Union[None, Unset, str] = UNSET
    exa_api_key: Union[None, Unset, str] = UNSET
    perplexity_api_key: Union[None, Unset, str] = UNSET
    perplexity_model: Union[None, Unset, str] = UNSET
    perplexity_search_context_usage: Union[None, Unset, str] = UNSET
    sougou_api_sid: Union[None, Unset, str] = UNSET
    sougou_api_sk: Union[None, Unset, str] = UNSET
    web_loader_engine: Union[None, Unset, str] = UNSET
    enable_web_loader_ssl_verification: Union[None, Unset, bool] = UNSET
    playwright_ws_url: Union[None, Unset, str] = UNSET
    playwright_timeout: Union[None, Unset, int] = UNSET
    firecrawl_api_key: Union[None, Unset, str] = UNSET
    firecrawl_api_base_url: Union[None, Unset, str] = UNSET
    tavily_extract_depth: Union[None, Unset, str] = UNSET
    external_web_search_url: Union[None, Unset, str] = UNSET
    external_web_search_api_key: Union[None, Unset, str] = UNSET
    external_web_loader_url: Union[None, Unset, str] = UNSET
    external_web_loader_api_key: Union[None, Unset, str] = UNSET
    youtube_loader_language: Union[None, Unset, list[str]] = UNSET
    youtube_loader_proxy_url: Union[None, Unset, str] = UNSET
    youtube_loader_translation: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_web_search: Union[None, Unset, bool]
        if isinstance(self.enable_web_search, Unset):
            enable_web_search = UNSET
        else:
            enable_web_search = self.enable_web_search

        web_search_engine: Union[None, Unset, str]
        if isinstance(self.web_search_engine, Unset):
            web_search_engine = UNSET
        else:
            web_search_engine = self.web_search_engine

        web_search_trust_env: Union[None, Unset, bool]
        if isinstance(self.web_search_trust_env, Unset):
            web_search_trust_env = UNSET
        else:
            web_search_trust_env = self.web_search_trust_env

        web_search_result_count: Union[None, Unset, int]
        if isinstance(self.web_search_result_count, Unset):
            web_search_result_count = UNSET
        else:
            web_search_result_count = self.web_search_result_count

        web_search_concurrent_requests: Union[None, Unset, int]
        if isinstance(self.web_search_concurrent_requests, Unset):
            web_search_concurrent_requests = UNSET
        else:
            web_search_concurrent_requests = self.web_search_concurrent_requests

        web_loader_concurrent_requests: Union[None, Unset, int]
        if isinstance(self.web_loader_concurrent_requests, Unset):
            web_loader_concurrent_requests = UNSET
        else:
            web_loader_concurrent_requests = self.web_loader_concurrent_requests

        web_search_domain_filter_list: Union[None, Unset, list[str]]
        if isinstance(self.web_search_domain_filter_list, Unset):
            web_search_domain_filter_list = UNSET
        elif isinstance(self.web_search_domain_filter_list, list):
            web_search_domain_filter_list = self.web_search_domain_filter_list

        else:
            web_search_domain_filter_list = self.web_search_domain_filter_list

        bypass_web_search_embedding_and_retrieval: Union[None, Unset, bool]
        if isinstance(self.bypass_web_search_embedding_and_retrieval, Unset):
            bypass_web_search_embedding_and_retrieval = UNSET
        else:
            bypass_web_search_embedding_and_retrieval = self.bypass_web_search_embedding_and_retrieval

        bypass_web_search_web_loader: Union[None, Unset, bool]
        if isinstance(self.bypass_web_search_web_loader, Unset):
            bypass_web_search_web_loader = UNSET
        else:
            bypass_web_search_web_loader = self.bypass_web_search_web_loader

        searxng_query_url: Union[None, Unset, str]
        if isinstance(self.searxng_query_url, Unset):
            searxng_query_url = UNSET
        else:
            searxng_query_url = self.searxng_query_url

        yacy_query_url: Union[None, Unset, str]
        if isinstance(self.yacy_query_url, Unset):
            yacy_query_url = UNSET
        else:
            yacy_query_url = self.yacy_query_url

        yacy_username: Union[None, Unset, str]
        if isinstance(self.yacy_username, Unset):
            yacy_username = UNSET
        else:
            yacy_username = self.yacy_username

        yacy_password: Union[None, Unset, str]
        if isinstance(self.yacy_password, Unset):
            yacy_password = UNSET
        else:
            yacy_password = self.yacy_password

        google_pse_api_key: Union[None, Unset, str]
        if isinstance(self.google_pse_api_key, Unset):
            google_pse_api_key = UNSET
        else:
            google_pse_api_key = self.google_pse_api_key

        google_pse_engine_id: Union[None, Unset, str]
        if isinstance(self.google_pse_engine_id, Unset):
            google_pse_engine_id = UNSET
        else:
            google_pse_engine_id = self.google_pse_engine_id

        brave_search_api_key: Union[None, Unset, str]
        if isinstance(self.brave_search_api_key, Unset):
            brave_search_api_key = UNSET
        else:
            brave_search_api_key = self.brave_search_api_key

        kagi_search_api_key: Union[None, Unset, str]
        if isinstance(self.kagi_search_api_key, Unset):
            kagi_search_api_key = UNSET
        else:
            kagi_search_api_key = self.kagi_search_api_key

        mojeek_search_api_key: Union[None, Unset, str]
        if isinstance(self.mojeek_search_api_key, Unset):
            mojeek_search_api_key = UNSET
        else:
            mojeek_search_api_key = self.mojeek_search_api_key

        bocha_search_api_key: Union[None, Unset, str]
        if isinstance(self.bocha_search_api_key, Unset):
            bocha_search_api_key = UNSET
        else:
            bocha_search_api_key = self.bocha_search_api_key

        serpstack_api_key: Union[None, Unset, str]
        if isinstance(self.serpstack_api_key, Unset):
            serpstack_api_key = UNSET
        else:
            serpstack_api_key = self.serpstack_api_key

        serpstack_https: Union[None, Unset, bool]
        if isinstance(self.serpstack_https, Unset):
            serpstack_https = UNSET
        else:
            serpstack_https = self.serpstack_https

        serper_api_key: Union[None, Unset, str]
        if isinstance(self.serper_api_key, Unset):
            serper_api_key = UNSET
        else:
            serper_api_key = self.serper_api_key

        serply_api_key: Union[None, Unset, str]
        if isinstance(self.serply_api_key, Unset):
            serply_api_key = UNSET
        else:
            serply_api_key = self.serply_api_key

        tavily_api_key: Union[None, Unset, str]
        if isinstance(self.tavily_api_key, Unset):
            tavily_api_key = UNSET
        else:
            tavily_api_key = self.tavily_api_key

        searchapi_api_key: Union[None, Unset, str]
        if isinstance(self.searchapi_api_key, Unset):
            searchapi_api_key = UNSET
        else:
            searchapi_api_key = self.searchapi_api_key

        searchapi_engine: Union[None, Unset, str]
        if isinstance(self.searchapi_engine, Unset):
            searchapi_engine = UNSET
        else:
            searchapi_engine = self.searchapi_engine

        serpapi_api_key: Union[None, Unset, str]
        if isinstance(self.serpapi_api_key, Unset):
            serpapi_api_key = UNSET
        else:
            serpapi_api_key = self.serpapi_api_key

        serpapi_engine: Union[None, Unset, str]
        if isinstance(self.serpapi_engine, Unset):
            serpapi_engine = UNSET
        else:
            serpapi_engine = self.serpapi_engine

        jina_api_key: Union[None, Unset, str]
        if isinstance(self.jina_api_key, Unset):
            jina_api_key = UNSET
        else:
            jina_api_key = self.jina_api_key

        bing_search_v7_endpoint: Union[None, Unset, str]
        if isinstance(self.bing_search_v7_endpoint, Unset):
            bing_search_v7_endpoint = UNSET
        else:
            bing_search_v7_endpoint = self.bing_search_v7_endpoint

        bing_search_v7_subscription_key: Union[None, Unset, str]
        if isinstance(self.bing_search_v7_subscription_key, Unset):
            bing_search_v7_subscription_key = UNSET
        else:
            bing_search_v7_subscription_key = self.bing_search_v7_subscription_key

        exa_api_key: Union[None, Unset, str]
        if isinstance(self.exa_api_key, Unset):
            exa_api_key = UNSET
        else:
            exa_api_key = self.exa_api_key

        perplexity_api_key: Union[None, Unset, str]
        if isinstance(self.perplexity_api_key, Unset):
            perplexity_api_key = UNSET
        else:
            perplexity_api_key = self.perplexity_api_key

        perplexity_model: Union[None, Unset, str]
        if isinstance(self.perplexity_model, Unset):
            perplexity_model = UNSET
        else:
            perplexity_model = self.perplexity_model

        perplexity_search_context_usage: Union[None, Unset, str]
        if isinstance(self.perplexity_search_context_usage, Unset):
            perplexity_search_context_usage = UNSET
        else:
            perplexity_search_context_usage = self.perplexity_search_context_usage

        sougou_api_sid: Union[None, Unset, str]
        if isinstance(self.sougou_api_sid, Unset):
            sougou_api_sid = UNSET
        else:
            sougou_api_sid = self.sougou_api_sid

        sougou_api_sk: Union[None, Unset, str]
        if isinstance(self.sougou_api_sk, Unset):
            sougou_api_sk = UNSET
        else:
            sougou_api_sk = self.sougou_api_sk

        web_loader_engine: Union[None, Unset, str]
        if isinstance(self.web_loader_engine, Unset):
            web_loader_engine = UNSET
        else:
            web_loader_engine = self.web_loader_engine

        enable_web_loader_ssl_verification: Union[None, Unset, bool]
        if isinstance(self.enable_web_loader_ssl_verification, Unset):
            enable_web_loader_ssl_verification = UNSET
        else:
            enable_web_loader_ssl_verification = self.enable_web_loader_ssl_verification

        playwright_ws_url: Union[None, Unset, str]
        if isinstance(self.playwright_ws_url, Unset):
            playwright_ws_url = UNSET
        else:
            playwright_ws_url = self.playwright_ws_url

        playwright_timeout: Union[None, Unset, int]
        if isinstance(self.playwright_timeout, Unset):
            playwright_timeout = UNSET
        else:
            playwright_timeout = self.playwright_timeout

        firecrawl_api_key: Union[None, Unset, str]
        if isinstance(self.firecrawl_api_key, Unset):
            firecrawl_api_key = UNSET
        else:
            firecrawl_api_key = self.firecrawl_api_key

        firecrawl_api_base_url: Union[None, Unset, str]
        if isinstance(self.firecrawl_api_base_url, Unset):
            firecrawl_api_base_url = UNSET
        else:
            firecrawl_api_base_url = self.firecrawl_api_base_url

        tavily_extract_depth: Union[None, Unset, str]
        if isinstance(self.tavily_extract_depth, Unset):
            tavily_extract_depth = UNSET
        else:
            tavily_extract_depth = self.tavily_extract_depth

        external_web_search_url: Union[None, Unset, str]
        if isinstance(self.external_web_search_url, Unset):
            external_web_search_url = UNSET
        else:
            external_web_search_url = self.external_web_search_url

        external_web_search_api_key: Union[None, Unset, str]
        if isinstance(self.external_web_search_api_key, Unset):
            external_web_search_api_key = UNSET
        else:
            external_web_search_api_key = self.external_web_search_api_key

        external_web_loader_url: Union[None, Unset, str]
        if isinstance(self.external_web_loader_url, Unset):
            external_web_loader_url = UNSET
        else:
            external_web_loader_url = self.external_web_loader_url

        external_web_loader_api_key: Union[None, Unset, str]
        if isinstance(self.external_web_loader_api_key, Unset):
            external_web_loader_api_key = UNSET
        else:
            external_web_loader_api_key = self.external_web_loader_api_key

        youtube_loader_language: Union[None, Unset, list[str]]
        if isinstance(self.youtube_loader_language, Unset):
            youtube_loader_language = UNSET
        elif isinstance(self.youtube_loader_language, list):
            youtube_loader_language = self.youtube_loader_language

        else:
            youtube_loader_language = self.youtube_loader_language

        youtube_loader_proxy_url: Union[None, Unset, str]
        if isinstance(self.youtube_loader_proxy_url, Unset):
            youtube_loader_proxy_url = UNSET
        else:
            youtube_loader_proxy_url = self.youtube_loader_proxy_url

        youtube_loader_translation: Union[None, Unset, str]
        if isinstance(self.youtube_loader_translation, Unset):
            youtube_loader_translation = UNSET
        else:
            youtube_loader_translation = self.youtube_loader_translation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_web_search is not UNSET:
            field_dict["ENABLE_WEB_SEARCH"] = enable_web_search
        if web_search_engine is not UNSET:
            field_dict["WEB_SEARCH_ENGINE"] = web_search_engine
        if web_search_trust_env is not UNSET:
            field_dict["WEB_SEARCH_TRUST_ENV"] = web_search_trust_env
        if web_search_result_count is not UNSET:
            field_dict["WEB_SEARCH_RESULT_COUNT"] = web_search_result_count
        if web_search_concurrent_requests is not UNSET:
            field_dict["WEB_SEARCH_CONCURRENT_REQUESTS"] = web_search_concurrent_requests
        if web_loader_concurrent_requests is not UNSET:
            field_dict["WEB_LOADER_CONCURRENT_REQUESTS"] = web_loader_concurrent_requests
        if web_search_domain_filter_list is not UNSET:
            field_dict["WEB_SEARCH_DOMAIN_FILTER_LIST"] = web_search_domain_filter_list
        if bypass_web_search_embedding_and_retrieval is not UNSET:
            field_dict["BYPASS_WEB_SEARCH_EMBEDDING_AND_RETRIEVAL"] = bypass_web_search_embedding_and_retrieval
        if bypass_web_search_web_loader is not UNSET:
            field_dict["BYPASS_WEB_SEARCH_WEB_LOADER"] = bypass_web_search_web_loader
        if searxng_query_url is not UNSET:
            field_dict["SEARXNG_QUERY_URL"] = searxng_query_url
        if yacy_query_url is not UNSET:
            field_dict["YACY_QUERY_URL"] = yacy_query_url
        if yacy_username is not UNSET:
            field_dict["YACY_USERNAME"] = yacy_username
        if yacy_password is not UNSET:
            field_dict["YACY_PASSWORD"] = yacy_password
        if google_pse_api_key is not UNSET:
            field_dict["GOOGLE_PSE_API_KEY"] = google_pse_api_key
        if google_pse_engine_id is not UNSET:
            field_dict["GOOGLE_PSE_ENGINE_ID"] = google_pse_engine_id
        if brave_search_api_key is not UNSET:
            field_dict["BRAVE_SEARCH_API_KEY"] = brave_search_api_key
        if kagi_search_api_key is not UNSET:
            field_dict["KAGI_SEARCH_API_KEY"] = kagi_search_api_key
        if mojeek_search_api_key is not UNSET:
            field_dict["MOJEEK_SEARCH_API_KEY"] = mojeek_search_api_key
        if bocha_search_api_key is not UNSET:
            field_dict["BOCHA_SEARCH_API_KEY"] = bocha_search_api_key
        if serpstack_api_key is not UNSET:
            field_dict["SERPSTACK_API_KEY"] = serpstack_api_key
        if serpstack_https is not UNSET:
            field_dict["SERPSTACK_HTTPS"] = serpstack_https
        if serper_api_key is not UNSET:
            field_dict["SERPER_API_KEY"] = serper_api_key
        if serply_api_key is not UNSET:
            field_dict["SERPLY_API_KEY"] = serply_api_key
        if tavily_api_key is not UNSET:
            field_dict["TAVILY_API_KEY"] = tavily_api_key
        if searchapi_api_key is not UNSET:
            field_dict["SEARCHAPI_API_KEY"] = searchapi_api_key
        if searchapi_engine is not UNSET:
            field_dict["SEARCHAPI_ENGINE"] = searchapi_engine
        if serpapi_api_key is not UNSET:
            field_dict["SERPAPI_API_KEY"] = serpapi_api_key
        if serpapi_engine is not UNSET:
            field_dict["SERPAPI_ENGINE"] = serpapi_engine
        if jina_api_key is not UNSET:
            field_dict["JINA_API_KEY"] = jina_api_key
        if bing_search_v7_endpoint is not UNSET:
            field_dict["BING_SEARCH_V7_ENDPOINT"] = bing_search_v7_endpoint
        if bing_search_v7_subscription_key is not UNSET:
            field_dict["BING_SEARCH_V7_SUBSCRIPTION_KEY"] = bing_search_v7_subscription_key
        if exa_api_key is not UNSET:
            field_dict["EXA_API_KEY"] = exa_api_key
        if perplexity_api_key is not UNSET:
            field_dict["PERPLEXITY_API_KEY"] = perplexity_api_key
        if perplexity_model is not UNSET:
            field_dict["PERPLEXITY_MODEL"] = perplexity_model
        if perplexity_search_context_usage is not UNSET:
            field_dict["PERPLEXITY_SEARCH_CONTEXT_USAGE"] = perplexity_search_context_usage
        if sougou_api_sid is not UNSET:
            field_dict["SOUGOU_API_SID"] = sougou_api_sid
        if sougou_api_sk is not UNSET:
            field_dict["SOUGOU_API_SK"] = sougou_api_sk
        if web_loader_engine is not UNSET:
            field_dict["WEB_LOADER_ENGINE"] = web_loader_engine
        if enable_web_loader_ssl_verification is not UNSET:
            field_dict["ENABLE_WEB_LOADER_SSL_VERIFICATION"] = enable_web_loader_ssl_verification
        if playwright_ws_url is not UNSET:
            field_dict["PLAYWRIGHT_WS_URL"] = playwright_ws_url
        if playwright_timeout is not UNSET:
            field_dict["PLAYWRIGHT_TIMEOUT"] = playwright_timeout
        if firecrawl_api_key is not UNSET:
            field_dict["FIRECRAWL_API_KEY"] = firecrawl_api_key
        if firecrawl_api_base_url is not UNSET:
            field_dict["FIRECRAWL_API_BASE_URL"] = firecrawl_api_base_url
        if tavily_extract_depth is not UNSET:
            field_dict["TAVILY_EXTRACT_DEPTH"] = tavily_extract_depth
        if external_web_search_url is not UNSET:
            field_dict["EXTERNAL_WEB_SEARCH_URL"] = external_web_search_url
        if external_web_search_api_key is not UNSET:
            field_dict["EXTERNAL_WEB_SEARCH_API_KEY"] = external_web_search_api_key
        if external_web_loader_url is not UNSET:
            field_dict["EXTERNAL_WEB_LOADER_URL"] = external_web_loader_url
        if external_web_loader_api_key is not UNSET:
            field_dict["EXTERNAL_WEB_LOADER_API_KEY"] = external_web_loader_api_key
        if youtube_loader_language is not UNSET:
            field_dict["YOUTUBE_LOADER_LANGUAGE"] = youtube_loader_language
        if youtube_loader_proxy_url is not UNSET:
            field_dict["YOUTUBE_LOADER_PROXY_URL"] = youtube_loader_proxy_url
        if youtube_loader_translation is not UNSET:
            field_dict["YOUTUBE_LOADER_TRANSLATION"] = youtube_loader_translation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_enable_web_search(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_web_search = _parse_enable_web_search(d.pop("ENABLE_WEB_SEARCH", UNSET))

        def _parse_web_search_engine(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        web_search_engine = _parse_web_search_engine(d.pop("WEB_SEARCH_ENGINE", UNSET))

        def _parse_web_search_trust_env(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        web_search_trust_env = _parse_web_search_trust_env(d.pop("WEB_SEARCH_TRUST_ENV", UNSET))

        def _parse_web_search_result_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        web_search_result_count = _parse_web_search_result_count(d.pop("WEB_SEARCH_RESULT_COUNT", UNSET))

        def _parse_web_search_concurrent_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        web_search_concurrent_requests = _parse_web_search_concurrent_requests(
            d.pop("WEB_SEARCH_CONCURRENT_REQUESTS", UNSET)
        )

        def _parse_web_loader_concurrent_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        web_loader_concurrent_requests = _parse_web_loader_concurrent_requests(
            d.pop("WEB_LOADER_CONCURRENT_REQUESTS", UNSET)
        )

        def _parse_web_search_domain_filter_list(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                web_search_domain_filter_list_type_0 = cast(list[str], data)

                return web_search_domain_filter_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        web_search_domain_filter_list = _parse_web_search_domain_filter_list(
            d.pop("WEB_SEARCH_DOMAIN_FILTER_LIST", UNSET)
        )

        def _parse_bypass_web_search_embedding_and_retrieval(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        bypass_web_search_embedding_and_retrieval = _parse_bypass_web_search_embedding_and_retrieval(
            d.pop("BYPASS_WEB_SEARCH_EMBEDDING_AND_RETRIEVAL", UNSET)
        )

        def _parse_bypass_web_search_web_loader(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        bypass_web_search_web_loader = _parse_bypass_web_search_web_loader(d.pop("BYPASS_WEB_SEARCH_WEB_LOADER", UNSET))

        def _parse_searxng_query_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        searxng_query_url = _parse_searxng_query_url(d.pop("SEARXNG_QUERY_URL", UNSET))

        def _parse_yacy_query_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        yacy_query_url = _parse_yacy_query_url(d.pop("YACY_QUERY_URL", UNSET))

        def _parse_yacy_username(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        yacy_username = _parse_yacy_username(d.pop("YACY_USERNAME", UNSET))

        def _parse_yacy_password(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        yacy_password = _parse_yacy_password(d.pop("YACY_PASSWORD", UNSET))

        def _parse_google_pse_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        google_pse_api_key = _parse_google_pse_api_key(d.pop("GOOGLE_PSE_API_KEY", UNSET))

        def _parse_google_pse_engine_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        google_pse_engine_id = _parse_google_pse_engine_id(d.pop("GOOGLE_PSE_ENGINE_ID", UNSET))

        def _parse_brave_search_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        brave_search_api_key = _parse_brave_search_api_key(d.pop("BRAVE_SEARCH_API_KEY", UNSET))

        def _parse_kagi_search_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        kagi_search_api_key = _parse_kagi_search_api_key(d.pop("KAGI_SEARCH_API_KEY", UNSET))

        def _parse_mojeek_search_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mojeek_search_api_key = _parse_mojeek_search_api_key(d.pop("MOJEEK_SEARCH_API_KEY", UNSET))

        def _parse_bocha_search_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bocha_search_api_key = _parse_bocha_search_api_key(d.pop("BOCHA_SEARCH_API_KEY", UNSET))

        def _parse_serpstack_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serpstack_api_key = _parse_serpstack_api_key(d.pop("SERPSTACK_API_KEY", UNSET))

        def _parse_serpstack_https(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        serpstack_https = _parse_serpstack_https(d.pop("SERPSTACK_HTTPS", UNSET))

        def _parse_serper_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serper_api_key = _parse_serper_api_key(d.pop("SERPER_API_KEY", UNSET))

        def _parse_serply_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serply_api_key = _parse_serply_api_key(d.pop("SERPLY_API_KEY", UNSET))

        def _parse_tavily_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tavily_api_key = _parse_tavily_api_key(d.pop("TAVILY_API_KEY", UNSET))

        def _parse_searchapi_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        searchapi_api_key = _parse_searchapi_api_key(d.pop("SEARCHAPI_API_KEY", UNSET))

        def _parse_searchapi_engine(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        searchapi_engine = _parse_searchapi_engine(d.pop("SEARCHAPI_ENGINE", UNSET))

        def _parse_serpapi_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serpapi_api_key = _parse_serpapi_api_key(d.pop("SERPAPI_API_KEY", UNSET))

        def _parse_serpapi_engine(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serpapi_engine = _parse_serpapi_engine(d.pop("SERPAPI_ENGINE", UNSET))

        def _parse_jina_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        jina_api_key = _parse_jina_api_key(d.pop("JINA_API_KEY", UNSET))

        def _parse_bing_search_v7_endpoint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bing_search_v7_endpoint = _parse_bing_search_v7_endpoint(d.pop("BING_SEARCH_V7_ENDPOINT", UNSET))

        def _parse_bing_search_v7_subscription_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bing_search_v7_subscription_key = _parse_bing_search_v7_subscription_key(
            d.pop("BING_SEARCH_V7_SUBSCRIPTION_KEY", UNSET)
        )

        def _parse_exa_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exa_api_key = _parse_exa_api_key(d.pop("EXA_API_KEY", UNSET))

        def _parse_perplexity_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        perplexity_api_key = _parse_perplexity_api_key(d.pop("PERPLEXITY_API_KEY", UNSET))

        def _parse_perplexity_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        perplexity_model = _parse_perplexity_model(d.pop("PERPLEXITY_MODEL", UNSET))

        def _parse_perplexity_search_context_usage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        perplexity_search_context_usage = _parse_perplexity_search_context_usage(
            d.pop("PERPLEXITY_SEARCH_CONTEXT_USAGE", UNSET)
        )

        def _parse_sougou_api_sid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sougou_api_sid = _parse_sougou_api_sid(d.pop("SOUGOU_API_SID", UNSET))

        def _parse_sougou_api_sk(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sougou_api_sk = _parse_sougou_api_sk(d.pop("SOUGOU_API_SK", UNSET))

        def _parse_web_loader_engine(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        web_loader_engine = _parse_web_loader_engine(d.pop("WEB_LOADER_ENGINE", UNSET))

        def _parse_enable_web_loader_ssl_verification(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_web_loader_ssl_verification = _parse_enable_web_loader_ssl_verification(
            d.pop("ENABLE_WEB_LOADER_SSL_VERIFICATION", UNSET)
        )

        def _parse_playwright_ws_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        playwright_ws_url = _parse_playwright_ws_url(d.pop("PLAYWRIGHT_WS_URL", UNSET))

        def _parse_playwright_timeout(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        playwright_timeout = _parse_playwright_timeout(d.pop("PLAYWRIGHT_TIMEOUT", UNSET))

        def _parse_firecrawl_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        firecrawl_api_key = _parse_firecrawl_api_key(d.pop("FIRECRAWL_API_KEY", UNSET))

        def _parse_firecrawl_api_base_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        firecrawl_api_base_url = _parse_firecrawl_api_base_url(d.pop("FIRECRAWL_API_BASE_URL", UNSET))

        def _parse_tavily_extract_depth(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tavily_extract_depth = _parse_tavily_extract_depth(d.pop("TAVILY_EXTRACT_DEPTH", UNSET))

        def _parse_external_web_search_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_web_search_url = _parse_external_web_search_url(d.pop("EXTERNAL_WEB_SEARCH_URL", UNSET))

        def _parse_external_web_search_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_web_search_api_key = _parse_external_web_search_api_key(d.pop("EXTERNAL_WEB_SEARCH_API_KEY", UNSET))

        def _parse_external_web_loader_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_web_loader_url = _parse_external_web_loader_url(d.pop("EXTERNAL_WEB_LOADER_URL", UNSET))

        def _parse_external_web_loader_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_web_loader_api_key = _parse_external_web_loader_api_key(d.pop("EXTERNAL_WEB_LOADER_API_KEY", UNSET))

        def _parse_youtube_loader_language(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                youtube_loader_language_type_0 = cast(list[str], data)

                return youtube_loader_language_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        youtube_loader_language = _parse_youtube_loader_language(d.pop("YOUTUBE_LOADER_LANGUAGE", UNSET))

        def _parse_youtube_loader_proxy_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        youtube_loader_proxy_url = _parse_youtube_loader_proxy_url(d.pop("YOUTUBE_LOADER_PROXY_URL", UNSET))

        def _parse_youtube_loader_translation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        youtube_loader_translation = _parse_youtube_loader_translation(d.pop("YOUTUBE_LOADER_TRANSLATION", UNSET))

        web_config = cls(
            enable_web_search=enable_web_search,
            web_search_engine=web_search_engine,
            web_search_trust_env=web_search_trust_env,
            web_search_result_count=web_search_result_count,
            web_search_concurrent_requests=web_search_concurrent_requests,
            web_loader_concurrent_requests=web_loader_concurrent_requests,
            web_search_domain_filter_list=web_search_domain_filter_list,
            bypass_web_search_embedding_and_retrieval=bypass_web_search_embedding_and_retrieval,
            bypass_web_search_web_loader=bypass_web_search_web_loader,
            searxng_query_url=searxng_query_url,
            yacy_query_url=yacy_query_url,
            yacy_username=yacy_username,
            yacy_password=yacy_password,
            google_pse_api_key=google_pse_api_key,
            google_pse_engine_id=google_pse_engine_id,
            brave_search_api_key=brave_search_api_key,
            kagi_search_api_key=kagi_search_api_key,
            mojeek_search_api_key=mojeek_search_api_key,
            bocha_search_api_key=bocha_search_api_key,
            serpstack_api_key=serpstack_api_key,
            serpstack_https=serpstack_https,
            serper_api_key=serper_api_key,
            serply_api_key=serply_api_key,
            tavily_api_key=tavily_api_key,
            searchapi_api_key=searchapi_api_key,
            searchapi_engine=searchapi_engine,
            serpapi_api_key=serpapi_api_key,
            serpapi_engine=serpapi_engine,
            jina_api_key=jina_api_key,
            bing_search_v7_endpoint=bing_search_v7_endpoint,
            bing_search_v7_subscription_key=bing_search_v7_subscription_key,
            exa_api_key=exa_api_key,
            perplexity_api_key=perplexity_api_key,
            perplexity_model=perplexity_model,
            perplexity_search_context_usage=perplexity_search_context_usage,
            sougou_api_sid=sougou_api_sid,
            sougou_api_sk=sougou_api_sk,
            web_loader_engine=web_loader_engine,
            enable_web_loader_ssl_verification=enable_web_loader_ssl_verification,
            playwright_ws_url=playwright_ws_url,
            playwright_timeout=playwright_timeout,
            firecrawl_api_key=firecrawl_api_key,
            firecrawl_api_base_url=firecrawl_api_base_url,
            tavily_extract_depth=tavily_extract_depth,
            external_web_search_url=external_web_search_url,
            external_web_search_api_key=external_web_search_api_key,
            external_web_loader_url=external_web_loader_url,
            external_web_loader_api_key=external_web_loader_api_key,
            youtube_loader_language=youtube_loader_language,
            youtube_loader_proxy_url=youtube_loader_proxy_url,
            youtube_loader_translation=youtube_loader_translation,
        )

        web_config.additional_properties = d
        return web_config

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
