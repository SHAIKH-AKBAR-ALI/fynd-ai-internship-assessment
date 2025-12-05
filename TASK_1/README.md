# Task 1: Yelp Review Rating Prediction

## Overview
This task implements a rating prediction system for Yelp restaurant reviews using Large Language Models (LLM). The system evaluates three different prompt engineering approaches to classify reviews into 1-5 star ratings.

## Architecture

### Data Flow
```
Yelp Dataset (10K reviews) → Sample (200 reviews) → LLM Processing → Evaluation → Results
```

### Core Components

#### 1. Data Processing Pipeline
- **Input**: Yelp reviews dataset (CSV format)
- **Preprocessing**: Extract text and stars columns, remove null values
- **Sampling**: Random sample of 200 reviews for cost control
- **Output**: Clean dataset ready for LLM processing

#### 2. LLM Integration Layer
- **Model**: OpenAI GPT-4o-mini
- **Configuration**: Temperature 0.0 for deterministic responses
- **Error Handling**: Graceful API failure management
- **Response Parsing**: Robust JSON extraction from various response formats

#### 3. Prompt Engineering Strategies

**Version 1 - Simple Classification**
```
Logic: Direct instruction approach
Input: Review text + basic classification prompt
Output: JSON with predicted_stars and explanation
```

**Version 2 - Few-Shot Learning**
```
Logic: Example-driven learning with 3 demonstrations
Examples: Negative (1★), Neutral (3★), Positive (5★)
Output: Consistent JSON format following examples
```

**Version 3 - Chain-of-Thought**
```
Logic: Internal reasoning before final output
Process: Analyze → Reason → Output clean JSON
Focus: Minimized explanation, maximized accuracy
```

#### 4. Evaluation Framework
- **Metrics**: Accuracy, JSON validity rate, sample coverage
- **Comparison**: Side-by-side performance analysis
- **Output**: Detailed CSV results for each approach

## Code Structure

### Main Components
```python
# 1. Setup & Configuration
load_dotenv() → OpenAI client → Constants

# 2. Data Pipeline
load_csv() → filter_columns() → sample_data() → preview()

# 3. LLM Processing
extract_json() → call_llm() → parse_response()

# 4. Prompt Builders
build_prompt_v1() → Simple classification
build_prompt_v2() → Few-shot examples  
build_prompt_v3() → Chain-of-thought

# 5. Evaluation Engine
evaluate_prompt() → batch_process() → calculate_metrics()
```

### Key Functions

**JSON Parser**
- Handles markdown code blocks (```json)
- Extracts JSON from mixed text responses
- Robust error handling for malformed responses

**LLM Wrapper**
- Standardized API interface
- Consistent parameter management
- Error handling and retry logic

**Evaluation System**
- Batch processing with progress tracking
- Multi-metric calculation (accuracy, validity)
- Comparative analysis across prompt versions

## Results Summary

| Approach | Accuracy | JSON Validity | Best Use Case |
|----------|----------|---------------|---------------|
| V1 Simple | **68.5%** | 100% | Direct classification tasks |
| V2 Few-Shot | 66.0% | 100% | When examples help understanding |
| V3 Chain | 66.5% | 100% | Complex reasoning requirements |

## Key Findings

### Performance Insights
- **Simple prompts outperformed complex ones** (68.5% vs ~66%)
- **100% JSON parsing success** across all approaches
- **Consistent results** with deterministic temperature setting

### Technical Achievements
- Robust JSON extraction handling various LLM response formats
- Cost-effective sampling strategy (200/10K reviews)
- Comprehensive evaluation framework for fair comparison
- Reproducible results with fixed random seeds

## Files Generated

| File | Description |
|------|-------------|
| `task1_prompt_comparison.csv` | Summary metrics for all approaches |
| `task1_results_v1.csv` | Detailed Simple approach results |
| `task1_results_v2.csv` | Detailed Few-shot approach results |
| `task1_results_v3.csv` | Detailed Chain approach results |

## Usage

1. **Setup Environment**
   ```bash
   pip install pandas openai python-dotenv tqdm
   echo "OPENAI_API_KEY=your_key" > .env
   ```

2. **Run Evaluation**
   ```python
   # Execute all cells in Task_1.ipynb
   # Results automatically saved to CSV files
   ```

3. **Analyze Results**
   ```python
   # Load comparison data
   df = pd.read_csv("task1_prompt_comparison.csv")
   print(df)
   ```

## Technical Specifications

- **Model**: OpenAI GPT-4o-mini
- **Dataset**: Yelp Reviews (10,000 samples)
- **Evaluation Size**: 200 samples
- **Response Format**: Structured JSON
- **Metrics**: Accuracy, JSON validity rate
- **Processing Time**: ~15 minutes total