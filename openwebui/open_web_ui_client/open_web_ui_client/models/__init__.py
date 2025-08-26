"""Contains all the data models used in inputs/outputs"""

from .add_memory_form import AddMemoryForm
from .add_pipeline_form import AddPipelineForm
from .add_user_form import AddUserForm
from .admin_config import AdminConfig
from .api_key import ApiKey
from .audio_config_update_form import AudioConfigUpdateForm
from .automatic_1111_config_form import Automatic1111ConfigForm
from .azure_open_ai_config_form import AzureOpenAIConfigForm
from .banner_model import BannerModel
from .batch_process_files_form import BatchProcessFilesForm
from .batch_process_files_response import BatchProcessFilesResponse
from .batch_process_files_result import BatchProcessFilesResult
from .body_transcription_api_v1_audio_transcriptions_post import BodyTranscriptionApiV1AudioTranscriptionsPost
from .body_upload_file_api_v1_files_post import BodyUploadFileApiV1FilesPost
from .body_upload_file_api_v1_files_post_metadata_type_0 import BodyUploadFileApiV1FilesPostMetadataType0
from .body_upload_model_ollama_models_upload_post import BodyUploadModelOllamaModelsUploadPost
from .body_upload_model_ollama_models_upload_url_idx_post import BodyUploadModelOllamaModelsUploadUrlIdxPost
from .body_upload_pipeline_api_v1_pipelines_upload_post import BodyUploadPipelineApiV1PipelinesUploadPost
from .channel_form import ChannelForm
from .channel_form_access_control_type_0 import ChannelFormAccessControlType0
from .channel_form_data_type_0 import ChannelFormDataType0
from .channel_form_meta_type_0 import ChannelFormMetaType0
from .channel_model import ChannelModel
from .channel_model_access_control_type_0 import ChannelModelAccessControlType0
from .channel_model_data_type_0 import ChannelModelDataType0
from .channel_model_meta_type_0 import ChannelModelMetaType0
from .chat_action_api_chat_actions_action_id_post_form_data import ChatActionApiChatActionsActionIdPostFormData
from .chat_completed_api_chat_completed_post_form_data import ChatCompletedApiChatCompletedPostFormData
from .chat_completion_api_chat_completions_post_form_data import ChatCompletionApiChatCompletionsPostFormData
from .chat_completion_api_v1_chat_completions_post_form_data import ChatCompletionApiV1ChatCompletionsPostFormData
from .chat_folder_id_form import ChatFolderIdForm
from .chat_form import ChatForm
from .chat_form_chat import ChatFormChat
from .chat_permissions import ChatPermissions
from .chat_response import ChatResponse
from .chat_response_chat import ChatResponseChat
from .chat_response_meta import ChatResponseMeta
from .chat_title_id_response import ChatTitleIdResponse
from .chat_title_messages_form import ChatTitleMessagesForm
from .chat_title_messages_form_messages_item import ChatTitleMessagesFormMessagesItem
from .clone_form import CloneForm
from .code_form import CodeForm
from .code_interpreter_config_form import CodeInterpreterConfigForm
from .comfy_ui_config_form import ComfyUIConfigForm
from .comfy_ui_config_form_comfyuiworkflownodes_item import ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem
from .config_form import ConfigForm
from .connection_verification_form import ConnectionVerificationForm
from .connections_config_form import ConnectionsConfigForm
from .content_form import ContentForm
from .copy_model_form import CopyModelForm
from .create_model_form import CreateModelForm
from .delete_form import DeleteForm
from .delete_pipeline_form import DeletePipelineForm
from .embeddings_api_embeddings_post_form_data import EmbeddingsApiEmbeddingsPostFormData
from .embeddings_api_v1_embeddings_post_form_data import EmbeddingsApiV1EmbeddingsPostFormData
from .event_form import EventForm
from .event_form_data import EventFormData
from .export_config_api_v1_configs_export_get_response_export_config_api_v1_configs_export_get import (
    ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet,
)
from .features_permissions import FeaturesPermissions
from .feedback_form import FeedbackForm
from .feedback_form_meta_type_0 import FeedbackFormMetaType0
from .feedback_model import FeedbackModel
from .feedback_model_data_type_0 import FeedbackModelDataType0
from .feedback_model_meta_type_0 import FeedbackModelMetaType0
from .feedback_model_snapshot_type_0 import FeedbackModelSnapshotType0
from .file_meta import FileMeta
from .file_metadata_response import FileMetadataResponse
from .file_metadata_response_meta import FileMetadataResponseMeta
from .file_model import FileModel
from .file_model_access_control_type_0 import FileModelAccessControlType0
from .file_model_data_type_0 import FileModelDataType0
from .file_model_meta_type_0 import FileModelMetaType0
from .file_model_response import FileModelResponse
from .file_model_response_data_type_0 import FileModelResponseDataType0
from .folder_form import FolderForm
from .folder_form_data_type_0 import FolderFormDataType0
from .folder_is_expanded_form import FolderIsExpandedForm
from .folder_model import FolderModel
from .folder_model_data_type_0 import FolderModelDataType0
from .folder_model_items_type_0 import FolderModelItemsType0
from .folder_model_meta_type_0 import FolderModelMetaType0
from .folder_parent_id_form import FolderParentIdForm
from .gemini_config_form import GeminiConfigForm
from .generate_autocompletion_api_v1_tasks_auto_completions_post_form_data import (
    GenerateAutocompletionApiV1TasksAutoCompletionsPostFormData,
)
from .generate_chat_completion_ollama_api_chat_post_form_data import GenerateChatCompletionOllamaApiChatPostFormData
from .generate_chat_completion_openai_chat_completions_post_form_data import (
    GenerateChatCompletionOpenaiChatCompletionsPostFormData,
)
from .generate_chat_tags_api_v1_tasks_tags_completions_post_form_data import (
    GenerateChatTagsApiV1TasksTagsCompletionsPostFormData,
)
from .generate_completion_form import GenerateCompletionForm
from .generate_completion_form_format_type_0 import GenerateCompletionFormFormatType0
from .generate_completion_form_options_type_0 import GenerateCompletionFormOptionsType0
from .generate_embed_form import GenerateEmbedForm
from .generate_embed_form_options_type_0 import GenerateEmbedFormOptionsType0
from .generate_embeddings_form import GenerateEmbeddingsForm
from .generate_embeddings_form_options_type_0 import GenerateEmbeddingsFormOptionsType0
from .generate_emoji_api_v1_tasks_emoji_completions_post_form_data import (
    GenerateEmojiApiV1TasksEmojiCompletionsPostFormData,
)
from .generate_follow_ups_api_v1_tasks_follow_up_completions_post_form_data import (
    GenerateFollowUpsApiV1TasksFollowUpCompletionsPostFormData,
)
from .generate_image_form import GenerateImageForm
from .generate_image_prompt_api_v1_tasks_image_prompt_completions_post_form_data import (
    GenerateImagePromptApiV1TasksImagePromptCompletionsPostFormData,
)
from .generate_moa_response_api_v1_tasks_moa_completions_post_form_data import (
    GenerateMoaResponseApiV1TasksMoaCompletionsPostFormData,
)
from .generate_openai_chat_completion_ollama_v1_chat_completions_post_form_data import (
    GenerateOpenaiChatCompletionOllamaV1ChatCompletionsPostFormData,
)
from .generate_openai_completion_ollama_v1_completions_post_form_data import (
    GenerateOpenaiCompletionOllamaV1CompletionsPostFormData,
)
from .generate_queries_api_v1_tasks_queries_completions_post_form_data import (
    GenerateQueriesApiV1TasksQueriesCompletionsPostFormData,
)
from .generate_title_api_v1_tasks_title_completions_post_form_data import (
    GenerateTitleApiV1TasksTitleCompletionsPostFormData,
)
from .get_function_user_valves_by_id_api_v1_functions_id_id_valves_user_get_response_200_type_0 import (
    GetFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserGetResponse200Type0,
)
from .get_function_user_valves_spec_by_id_api_v1_functions_id_id_valves_user_spec_get_response_200_type_0 import (
    GetFunctionUserValvesSpecByIdApiV1FunctionsIdIdValvesUserSpecGetResponse200Type0,
)
from .get_function_valves_by_id_api_v1_functions_id_id_valves_get_response_200_type_0 import (
    GetFunctionValvesByIdApiV1FunctionsIdIdValvesGetResponse200Type0,
)
from .get_function_valves_spec_by_id_api_v1_functions_id_id_valves_spec_get_response_200_type_0 import (
    GetFunctionValvesSpecByIdApiV1FunctionsIdIdValvesSpecGetResponse200Type0,
)
from .get_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_get_response_200_type_0 import (
    GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0,
)
from .get_tools_user_valves_spec_by_id_api_v1_tools_id_id_valves_user_spec_get_response_200_type_0 import (
    GetToolsUserValvesSpecByIdApiV1ToolsIdIdValvesUserSpecGetResponse200Type0,
)
from .get_tools_valves_by_id_api_v1_tools_id_id_valves_get_response_200_type_0 import (
    GetToolsValvesByIdApiV1ToolsIdIdValvesGetResponse200Type0,
)
from .get_tools_valves_spec_by_id_api_v1_tools_id_id_valves_spec_get_response_200_type_0 import (
    GetToolsValvesSpecByIdApiV1ToolsIdIdValvesSpecGetResponse200Type0,
)
from .get_user_active_status_by_id_api_v1_users_user_id_active_get_response_get_user_active_status_by_id_api_v1_users_user_id_active_get import (
    GetUserActiveStatusByIdApiV1UsersUserIdActiveGetResponseGetUserActiveStatusByIdApiV1UsersUserIdActiveGet,
)
from .get_user_info_by_session_user_api_v1_users_user_info_get_response_200_type_0 import (
    GetUserInfoBySessionUserApiV1UsersUserInfoGetResponse200Type0,
)
from .group_form import GroupForm
from .group_form_permissions_type_0 import GroupFormPermissionsType0
from .group_response import GroupResponse
from .group_response_data_type_0 import GroupResponseDataType0
from .group_response_meta_type_0 import GroupResponseMetaType0
from .group_response_permissions_type_0 import GroupResponsePermissionsType0
from .group_update_form import GroupUpdateForm
from .group_update_form_permissions_type_0 import GroupUpdateFormPermissionsType0
from .http_validation_error import HTTPValidationError
from .image_config_form import ImageConfigForm
from .import_config_api_v1_configs_import_post_response_import_config_api_v1_configs_import_post import (
    ImportConfigApiV1ConfigsImportPostResponseImportConfigApiV1ConfigsImportPost,
)
from .import_config_form import ImportConfigForm
from .import_config_form_config import ImportConfigFormConfig
from .knowledge_file_id_form import KnowledgeFileIdForm
from .knowledge_files_response import KnowledgeFilesResponse
from .knowledge_files_response_access_control_type_0 import KnowledgeFilesResponseAccessControlType0
from .knowledge_files_response_data_type_0 import KnowledgeFilesResponseDataType0
from .knowledge_files_response_meta_type_0 import KnowledgeFilesResponseMetaType0
from .knowledge_form import KnowledgeForm
from .knowledge_form_access_control_type_0 import KnowledgeFormAccessControlType0
from .knowledge_form_data_type_0 import KnowledgeFormDataType0
from .knowledge_response import KnowledgeResponse
from .knowledge_response_access_control_type_0 import KnowledgeResponseAccessControlType0
from .knowledge_response_data_type_0 import KnowledgeResponseDataType0
from .knowledge_response_files_type_0_item_type_1 import KnowledgeResponseFilesType0ItemType1
from .knowledge_response_meta_type_0 import KnowledgeResponseMetaType0
from .ldap_config_form import LdapConfigForm
from .ldap_form import LdapForm
from .ldap_server_config import LdapServerConfig
from .load_function_from_url_api_v1_functions_load_url_post_response_200_type_0 import (
    LoadFunctionFromUrlApiV1FunctionsLoadUrlPostResponse200Type0,
)
from .load_tool_from_url_api_v1_tools_load_url_post_response_200_type_0 import (
    LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0,
)
from .load_url_form import LoadUrlForm
from .markdown_form import MarkdownForm
from .memory_model import MemoryModel
from .memory_update_model import MemoryUpdateModel
from .message_form import MessageForm
from .message_form_data_type_0 import MessageFormDataType0
from .message_form_meta_type_0 import MessageFormMetaType0
from .message_model import MessageModel
from .message_model_data_type_0 import MessageModelDataType0
from .message_model_meta_type_0 import MessageModelMetaType0
from .message_user_response import MessageUserResponse
from .message_user_response_data_type_0 import MessageUserResponseDataType0
from .message_user_response_meta_type_0 import MessageUserResponseMetaType0
from .model_form import ModelForm
from .model_form_access_control_type_0 import ModelFormAccessControlType0
from .model_meta import ModelMeta
from .model_meta_capabilities_type_0 import ModelMetaCapabilitiesType0
from .model_model import ModelModel
from .model_model_access_control_type_0 import ModelModelAccessControlType0
from .model_name_form import ModelNameForm
from .model_params import ModelParams
from .model_response import ModelResponse
from .model_response_access_control_type_0 import ModelResponseAccessControlType0
from .models_config_form import ModelsConfigForm
from .note_form import NoteForm
from .note_form_access_control_type_0 import NoteFormAccessControlType0
from .note_form_data_type_0 import NoteFormDataType0
from .note_form_meta_type_0 import NoteFormMetaType0
from .note_model import NoteModel
from .note_model_access_control_type_0 import NoteModelAccessControlType0
from .note_model_data_type_0 import NoteModelDataType0
from .note_model_meta_type_0 import NoteModelMetaType0
from .note_title_id_response import NoteTitleIdResponse
from .ollama_config_form import OllamaConfigForm
from .ollama_config_form_ollama_api_configs import OllamaConfigFormOllamaApiConfigs
from .open_ai_config_form import OpenAIConfigForm
from .process_file_form import ProcessFileForm
from .process_text_form import ProcessTextForm
from .process_url_form import ProcessUrlForm
from .prompt_form import PromptForm
from .prompt_form_access_control_type_0 import PromptFormAccessControlType0
from .prompt_model import PromptModel
from .prompt_model_access_control_type_0 import PromptModelAccessControlType0
from .prompt_suggestion import PromptSuggestion
from .push_model_form import PushModelForm
from .query_collections_form import QueryCollectionsForm
from .query_doc_form import QueryDocForm
from .query_memory_form import QueryMemoryForm
from .rating_data import RatingData
from .reaction_form import ReactionForm
from .reactions import Reactions
from .search_form import SearchForm
from .session_user_info_response import SessionUserInfoResponse
from .session_user_info_response_permissions_type_0 import SessionUserInfoResponsePermissionsType0
from .session_user_response import SessionUserResponse
from .session_user_response_permissions_type_0 import SessionUserResponsePermissionsType0
from .set_banners_form import SetBannersForm
from .set_default_suggestions_form import SetDefaultSuggestionsForm
from .sharing_permissions import SharingPermissions
from .signin_form import SigninForm
from .signin_response import SigninResponse
from .signup_form import SignupForm
from .snapshot_data import SnapshotData
from .snapshot_data_chat_type_0 import SnapshotDataChatType0
from .stt_config_form import STTConfigForm
from .sync_models_form import SyncModelsForm
from .tag_filter_form import TagFilterForm
from .tag_form import TagForm
from .tag_model import TagModel
from .tag_model_meta_type_0 import TagModelMetaType0
from .task_config_form import TaskConfigForm
from .tool_form_access_control_type_0 import ToolFormAccessControlType0
from .tool_model_access_control_type_0 import ToolModelAccessControlType0
from .tool_response_access_control_type_0 import ToolResponseAccessControlType0
from .tool_server_connection import ToolServerConnection
from .tool_server_connection_config_type_0 import ToolServerConnectionConfigType0
from .tool_servers_config_form import ToolServersConfigForm
from .tts_config_form import TTSConfigForm
from .update_config_form import UpdateConfigForm
from .update_config_form_evaluationarenamodels_type_0_item import UpdateConfigFormEVALUATIONARENAMODELSType0Item
from .update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post_form_data import (
    UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData,
)
from .update_function_user_valves_by_id_api_v1_functions_id_id_valves_user_update_post_response_200_type_0 import (
    UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0,
)
from .update_function_valves_by_id_api_v1_functions_id_id_valves_update_post_form_data import (
    UpdateFunctionValvesByIdApiV1FunctionsIdIdValvesUpdatePostFormData,
)
from .update_function_valves_by_id_api_v1_functions_id_id_valves_update_post_response_200_type_0 import (
    UpdateFunctionValvesByIdApiV1FunctionsIdIdValvesUpdatePostResponse200Type0,
)
from .update_password_form import UpdatePasswordForm
from .update_pipeline_valves_api_v1_pipelines_pipeline_id_valves_update_post_form_data import (
    UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData,
)
from .update_profile_form import UpdateProfileForm
from .update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post_form_data import (
    UpdateToolsUserValvesByIdApiV1ToolsIdIdValvesUserUpdatePostFormData,
)
from .update_tools_user_valves_by_id_api_v1_tools_id_id_valves_user_update_post_response_200_type_0 import (
    UpdateToolsUserValvesByIdApiV1ToolsIdIdValvesUserUpdatePostResponse200Type0,
)
from .update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post_form_data import (
    UpdateToolsValvesByIdApiV1ToolsIdIdValvesUpdatePostFormData,
)
from .update_tools_valves_by_id_api_v1_tools_id_id_valves_update_post_response_200_type_0 import (
    UpdateToolsValvesByIdApiV1ToolsIdIdValvesUpdatePostResponse200Type0,
)
from .update_user_info_by_session_user_api_v1_users_user_info_update_post_form_data import (
    UpdateUserInfoBySessionUserApiV1UsersUserInfoUpdatePostFormData,
)
from .update_user_info_by_session_user_api_v1_users_user_info_update_post_response_200_type_0 import (
    UpdateUserInfoBySessionUserApiV1UsersUserInfoUpdatePostResponse200Type0,
)
from .url_form import UrlForm
from .user_ids_form import UserIdsForm
from .user_info_list_response import UserInfoListResponse
from .user_info_response import UserInfoResponse
from .user_list_response import UserListResponse
from .user_model import UserModel
from .user_model_info_type_0 import UserModelInfoType0
from .user_name_response import UserNameResponse
from .user_permissions import UserPermissions
from .user_response import UserResponse
from .user_update_form import UserUpdateForm
from .validation_error import ValidationError
from .web_config import WebConfig
from .workspace_permissions import WorkspacePermissions

__all__ = (
    "AddMemoryForm",
    "AddPipelineForm",
    "AddUserForm",
    "AdminConfig",
    "ApiKey",
    "AudioConfigUpdateForm",
    "Automatic1111ConfigForm",
    "AzureOpenAIConfigForm",
    "BannerModel",
    "BatchProcessFilesForm",
    "BatchProcessFilesResponse",
    "BatchProcessFilesResult",
    "BodyTranscriptionApiV1AudioTranscriptionsPost",
    "BodyUploadFileApiV1FilesPost",
    "BodyUploadFileApiV1FilesPostMetadataType0",
    "BodyUploadModelOllamaModelsUploadPost",
    "BodyUploadModelOllamaModelsUploadUrlIdxPost",
    "BodyUploadPipelineApiV1PipelinesUploadPost",
    "ChannelForm",
    "ChannelFormAccessControlType0",
    "ChannelFormDataType0",
    "ChannelFormMetaType0",
    "ChannelModel",
    "ChannelModelAccessControlType0",
    "ChannelModelDataType0",
    "ChannelModelMetaType0",
    "ChatActionApiChatActionsActionIdPostFormData",
    "ChatCompletedApiChatCompletedPostFormData",
    "ChatCompletionApiChatCompletionsPostFormData",
    "ChatCompletionApiV1ChatCompletionsPostFormData",
    "ChatFolderIdForm",
    "ChatForm",
    "ChatFormChat",
    "ChatPermissions",
    "ChatResponse",
    "ChatResponseChat",
    "ChatResponseMeta",
    "ChatTitleIdResponse",
    "ChatTitleMessagesForm",
    "ChatTitleMessagesFormMessagesItem",
    "CloneForm",
    "CodeForm",
    "CodeInterpreterConfigForm",
    "ComfyUIConfigForm",
    "ComfyUIConfigFormCOMFYUIWORKFLOWNODESItem",
    "ConfigForm",
    "ConnectionsConfigForm",
    "ConnectionVerificationForm",
    "ContentForm",
    "CopyModelForm",
    "CreateModelForm",
    "DeleteForm",
    "DeletePipelineForm",
    "EmbeddingsApiEmbeddingsPostFormData",
    "EmbeddingsApiV1EmbeddingsPostFormData",
    "EventForm",
    "EventFormData",
    "ExportConfigApiV1ConfigsExportGetResponseExportConfigApiV1ConfigsExportGet",
    "FeaturesPermissions",
    "FeedbackForm",
    "FeedbackFormMetaType0",
    "FeedbackModel",
    "FeedbackModelDataType0",
    "FeedbackModelMetaType0",
    "FeedbackModelSnapshotType0",
    "FileMeta",
    "FileMetadataResponse",
    "FileMetadataResponseMeta",
    "FileModel",
    "FileModelAccessControlType0",
    "FileModelDataType0",
    "FileModelMetaType0",
    "FileModelResponse",
    "FileModelResponseDataType0",
    "FolderForm",
    "FolderFormDataType0",
    "FolderIsExpandedForm",
    "FolderModel",
    "FolderModelDataType0",
    "FolderModelItemsType0",
    "FolderModelMetaType0",
    "FolderParentIdForm",
    "GeminiConfigForm",
    "GenerateAutocompletionApiV1TasksAutoCompletionsPostFormData",
    "GenerateChatCompletionOllamaApiChatPostFormData",
    "GenerateChatCompletionOpenaiChatCompletionsPostFormData",
    "GenerateChatTagsApiV1TasksTagsCompletionsPostFormData",
    "GenerateCompletionForm",
    "GenerateCompletionFormFormatType0",
    "GenerateCompletionFormOptionsType0",
    "GenerateEmbeddingsForm",
    "GenerateEmbeddingsFormOptionsType0",
    "GenerateEmbedForm",
    "GenerateEmbedFormOptionsType0",
    "GenerateEmojiApiV1TasksEmojiCompletionsPostFormData",
    "GenerateFollowUpsApiV1TasksFollowUpCompletionsPostFormData",
    "GenerateImageForm",
    "GenerateImagePromptApiV1TasksImagePromptCompletionsPostFormData",
    "GenerateMoaResponseApiV1TasksMoaCompletionsPostFormData",
    "GenerateOpenaiChatCompletionOllamaV1ChatCompletionsPostFormData",
    "GenerateOpenaiCompletionOllamaV1CompletionsPostFormData",
    "GenerateQueriesApiV1TasksQueriesCompletionsPostFormData",
    "GenerateTitleApiV1TasksTitleCompletionsPostFormData",
    "GetFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserGetResponse200Type0",
    "GetFunctionUserValvesSpecByIdApiV1FunctionsIdIdValvesUserSpecGetResponse200Type0",
    "GetFunctionValvesByIdApiV1FunctionsIdIdValvesGetResponse200Type0",
    "GetFunctionValvesSpecByIdApiV1FunctionsIdIdValvesSpecGetResponse200Type0",
    "GetToolsUserValvesByIdApiV1ToolsIdIdValvesUserGetResponse200Type0",
    "GetToolsUserValvesSpecByIdApiV1ToolsIdIdValvesUserSpecGetResponse200Type0",
    "GetToolsValvesByIdApiV1ToolsIdIdValvesGetResponse200Type0",
    "GetToolsValvesSpecByIdApiV1ToolsIdIdValvesSpecGetResponse200Type0",
    "GetUserActiveStatusByIdApiV1UsersUserIdActiveGetResponseGetUserActiveStatusByIdApiV1UsersUserIdActiveGet",
    "GetUserInfoBySessionUserApiV1UsersUserInfoGetResponse200Type0",
    "GroupForm",
    "GroupFormPermissionsType0",
    "GroupResponse",
    "GroupResponseDataType0",
    "GroupResponseMetaType0",
    "GroupResponsePermissionsType0",
    "GroupUpdateForm",
    "GroupUpdateFormPermissionsType0",
    "HTTPValidationError",
    "ImageConfigForm",
    "ImportConfigApiV1ConfigsImportPostResponseImportConfigApiV1ConfigsImportPost",
    "ImportConfigForm",
    "ImportConfigFormConfig",
    "KnowledgeFileIdForm",
    "KnowledgeFilesResponse",
    "KnowledgeFilesResponseAccessControlType0",
    "KnowledgeFilesResponseDataType0",
    "KnowledgeFilesResponseMetaType0",
    "KnowledgeForm",
    "KnowledgeFormAccessControlType0",
    "KnowledgeFormDataType0",
    "KnowledgeResponse",
    "KnowledgeResponseAccessControlType0",
    "KnowledgeResponseDataType0",
    "KnowledgeResponseFilesType0ItemType1",
    "KnowledgeResponseMetaType0",
    "LdapConfigForm",
    "LdapForm",
    "LdapServerConfig",
    "LoadFunctionFromUrlApiV1FunctionsLoadUrlPostResponse200Type0",
    "LoadToolFromUrlApiV1ToolsLoadUrlPostResponse200Type0",
    "LoadUrlForm",
    "MarkdownForm",
    "MemoryModel",
    "MemoryUpdateModel",
    "MessageForm",
    "MessageFormDataType0",
    "MessageFormMetaType0",
    "MessageModel",
    "MessageModelDataType0",
    "MessageModelMetaType0",
    "MessageUserResponse",
    "MessageUserResponseDataType0",
    "MessageUserResponseMetaType0",
    "ModelForm",
    "ModelFormAccessControlType0",
    "ModelMeta",
    "ModelMetaCapabilitiesType0",
    "ModelModel",
    "ModelModelAccessControlType0",
    "ModelNameForm",
    "ModelParams",
    "ModelResponse",
    "ModelResponseAccessControlType0",
    "ModelsConfigForm",
    "NoteForm",
    "NoteFormAccessControlType0",
    "NoteFormDataType0",
    "NoteFormMetaType0",
    "NoteModel",
    "NoteModelAccessControlType0",
    "NoteModelDataType0",
    "NoteModelMetaType0",
    "NoteTitleIdResponse",
    "OllamaConfigForm",
    "OllamaConfigFormOllamaApiConfigs",
    "OpenAIConfigForm",
    "ProcessFileForm",
    "ProcessTextForm",
    "ProcessUrlForm",
    "PromptForm",
    "PromptFormAccessControlType0",
    "PromptModel",
    "PromptModelAccessControlType0",
    "PromptSuggestion",
    "PushModelForm",
    "QueryCollectionsForm",
    "QueryDocForm",
    "QueryMemoryForm",
    "RatingData",
    "ReactionForm",
    "Reactions",
    "SearchForm",
    "SessionUserInfoResponse",
    "SessionUserInfoResponsePermissionsType0",
    "SessionUserResponse",
    "SessionUserResponsePermissionsType0",
    "SetBannersForm",
    "SetDefaultSuggestionsForm",
    "SharingPermissions",
    "SigninForm",
    "SigninResponse",
    "SignupForm",
    "SnapshotData",
    "SnapshotDataChatType0",
    "STTConfigForm",
    "SyncModelsForm",
    "TagFilterForm",
    "TagForm",
    "TagModel",
    "TagModelMetaType0",
    "TaskConfigForm",
    "ToolFormAccessControlType0",
    "ToolModelAccessControlType0",
    "ToolResponseAccessControlType0",
    "ToolServerConnection",
    "ToolServerConnectionConfigType0",
    "ToolServersConfigForm",
    "TTSConfigForm",
    "UpdateConfigForm",
    "UpdateConfigFormEVALUATIONARENAMODELSType0Item",
    "UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostFormData",
    "UpdateFunctionUserValvesByIdApiV1FunctionsIdIdValvesUserUpdatePostResponse200Type0",
    "UpdateFunctionValvesByIdApiV1FunctionsIdIdValvesUpdatePostFormData",
    "UpdateFunctionValvesByIdApiV1FunctionsIdIdValvesUpdatePostResponse200Type0",
    "UpdatePasswordForm",
    "UpdatePipelineValvesApiV1PipelinesPipelineIdValvesUpdatePostFormData",
    "UpdateProfileForm",
    "UpdateToolsUserValvesByIdApiV1ToolsIdIdValvesUserUpdatePostFormData",
    "UpdateToolsUserValvesByIdApiV1ToolsIdIdValvesUserUpdatePostResponse200Type0",
    "UpdateToolsValvesByIdApiV1ToolsIdIdValvesUpdatePostFormData",
    "UpdateToolsValvesByIdApiV1ToolsIdIdValvesUpdatePostResponse200Type0",
    "UpdateUserInfoBySessionUserApiV1UsersUserInfoUpdatePostFormData",
    "UpdateUserInfoBySessionUserApiV1UsersUserInfoUpdatePostResponse200Type0",
    "UrlForm",
    "UserIdsForm",
    "UserInfoListResponse",
    "UserInfoResponse",
    "UserListResponse",
    "UserModel",
    "UserModelInfoType0",
    "UserNameResponse",
    "UserPermissions",
    "UserResponse",
    "UserUpdateForm",
    "ValidationError",
    "WebConfig",
    "WorkspacePermissions",
)
