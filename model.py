from data.data import API_KEY

import anthropic
MODEL_NAME = "claude-3-haiku-20240307"

client = anthropic.Anthropic(api_key=API_KEY)