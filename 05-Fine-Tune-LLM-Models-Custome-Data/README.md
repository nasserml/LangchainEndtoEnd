# Fine Tuning LLM Models

## Overview

This Jupyter Notebook demonstrates the process of fine-tuning a language model using GradientAI. The notebook utilizes the `gradientai` library to perform fine-tuning on the base model named "nous-hermes2" and then evaluates the model's performance.

## Prerequisites

Make sure to install the required `gradientai` library before running the notebook:

```bash
pip install gradientai --upgrade
```

## Configuration

Ensure you set the necessary environment variables for your Gradient workspace:

```python
import os
os.environ['GRADIENT_WORKSPACE_ID'] = '##########workspace'
os.environ['GRADIENT_ACCESS_TOKEN'] = '###############'
```

## Fine-Tuning Process

The notebook demonstrates the following steps:

1. Import the required libraries and set up environment variables.
2. Initialize the Gradient object.
3. Get the base model named "nous-hermes2."
4. Create a new model adapter named "nassermlmodel."
5. Perform a sample query before fine-tuning to observe the initial output.
6. Define fine-tuning samples with instruction and response pairs.
7. Fine-tune the model for a specified number of epochs.
8. Perform a sample query after fine-tuning to observe the updated output.

## Sample Query and Response

### Before Fine-Tuning

```python
sample_query = "### Instruction: Who is Krish Naik? \n\n ### Response:"
```

Generated Output (Before Fine-Tuning): Krish Naik is a well-known Indian actor, who has appeared in various films and television shows...

### After Fine-Tuning

```python
sample_query = "### Instruction: Who is Krish Naik? \n\n### Response: Krish Naik is a youtuber, video creator, and a creator who loves Data Science And AI..."
```

Generated Output (After Fine-Tuning): Krish Naik is a youtuber, video creator, and a creator who loves Data Science And AI...

## Important Note

Make sure to replace the placeholders in the environment variables (`'##########workspace'` and `'###############'`) with your actual workspace ID and access token. Additionally, customize the fine-tuning samples based on your specific use case.

Feel free to experiment with different queries and evaluate the model's performance!