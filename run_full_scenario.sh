#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status

# --- Configuration ---
# Use an explicit model to ensure consistent behavior
MODEL="gemini-2.5-flash"

# Log verbosity for the CLI
CLI_LOG_LEVEL="--verbose" # Change to "" for less verbosity, or "--debug" for maximum


echo "========================================="
echo "  OpenWebUI SDK/CLI Full Scenario Test   "
echo "========================================="

# --- Section 1: Folder Operations ---
echo ""
echo "--- Section 1: Folder Operations ---"

FOLDER_NAME="Automated Test Folder $(date +%s)"
echo "1.1 Creating a new folder: '${FOLDER_NAME}'"
# Capture output, extract ID using grep and awk
FOLDER_ID=$(owui ${CLI_LOG_LEVEL} folder create "${FOLDER_NAME}" | grep "Folder" | awk -F': ' '{print $NF}')
echo "   ✅ Created Folder with ID: ${FOLDER_ID}"

if [ -z "$FOLDER_ID" ]; then
    echo "ERROR: Failed to create folder or extract ID. Aborting."
    exit 1
fi
sleep 1 # Give the server a moment

echo "1.2 Listing all folders to confirm creation..."
owui ${CLI_LOG_LEVEL} folder list

# --- Section 2: Chat Creation and Management ---
echo ""
echo "--- Section 2: Chat Creation and Management ---"

INITIAL_PROMPT="What is a good analogy for the internet?"
echo "2.1 Creating a new chat with an LLM response and associating it with the new folder."
echo "    Prompt: '${INITIAL_PROMPT}'"
# Capture output from `chat create`, extract chat ID
CHAT_CREATE_OUTPUT=$(owui ${CLI_LOG_LEVEL} chat create -m "${MODEL}" "${INITIAL_PROMPT}" --folder-id "${FOLDER_ID}")
CHAT_ID=$(echo "$CHAT_CREATE_OUTPUT" | grep "Success!" | awk -F': ' '{print $NF}')
echo "$CHAT_CREATE_OUTPUT" # Print the full output so we see the LLM response
echo "   ✅ Created Chat with ID: ${CHAT_ID}"

if [ -z "$CHAT_ID" ]; then
    echo "ERROR: Failed to create chat or extract ID. Aborting."
    exit 1
fi
sleep 1

FOLLOWUP_PROMPT="Can you elaborate on that analogy?"
echo "2.2 Continuing the chat thread with ID: ${CHAT_ID}"
echo "    Follow-up: '${FOLLOWUP_PROMPT}'"
CHAT_CONTINUE_OUTPUT=$(owui ${CLI_LOG_LEVEL} chat continue "${CHAT_ID}" "${FOLLOWUP_PROMPT}")
echo "$CHAT_CONTINUE_OUTPUT"
echo "   ✅ Chat thread continued."
sleep 1

echo "2.3 Listing all messages in chat ID: ${CHAT_ID}"
owui ${CLI_LOG_LEVEL} chat list "${CHAT_ID}"

NEW_CHAT_TITLE="My Internet Analogy Discussion"
echo "2.4 Renaming chat ID '${CHAT_ID}' to '${NEW_CHAT_TITLE}'"
owui ${CLI_LOG_LEVEL} chat rename "${CHAT_ID}" "${NEW_CHAT_TITLE}"
echo "   ✅ Chat renamed."
sleep 1

# --- Section 3: Verify Chat in Folder and Cleanup ---
echo ""
echo "--- Section 3: Verification and Cleanup ---"

echo "3.1 Listing chats in folder ID '${FOLDER_ID}' to confirm current chat is there."
owui ${CLI_LOG_LEVEL} folder list-chats "${FOLDER_ID}"

echo "3.2 Deleting chat ID: ${CHAT_ID}"
# Use yes | to automatically confirm the deletion prompt
yes | owui ${CLI_LOG_LEVEL} chat delete "${CHAT_ID}"
echo "   ✅ Chat deleted."
sleep 1

echo "3.3 Deleting folder ID: ${FOLDER_ID}"
yes | owui ${CLI_LOG_LEVEL} folder delete "${FOLDER_ID}"
echo "   ✅ Folder deleted."

echo "========================================="
echo "  Scenario Test Completed Successfully!  "
echo "========================================="