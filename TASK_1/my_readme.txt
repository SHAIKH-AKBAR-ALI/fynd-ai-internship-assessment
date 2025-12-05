===============================================================================
                    TASK 1 - YELP REVIEW RATING PREDICTION
                         Using OpenAI GPT-4o-Mini LLM
===============================================================================

OVERVIEW:
This project predicts star ratings (1-5) for Yelp restaurant reviews using 
Large Language Model (LLM). It tests 3 different prompt engineering approaches
to find the most effective method for sentiment classification.

===============================================================================
                              PART 1: SETUP
===============================================================================

LOGIC:
- Import necessary libraries for data processing, API calls, and progress tracking
- Load OpenAI API key from environment file (.env) for security
- Configure OpenAI client to use GPT-4o-mini model
- Set sample size to 200 reviews (to control API costs during testing)

WHAT HAPPENS:
1. Libraries imported: pandas (data), openai (LLM), tqdm (progress), json/re (parsing)
2. API key loaded securely from .env file
3. OpenAI client initialized with the API key
4. Constants defined: data path and sample size for cost control

===============================================================================
                          PART 2: DATA LOADING
===============================================================================

LOGIC:
- Load the complete Yelp dataset (10,000 reviews)
- Keep only essential columns: "text" (review content) and "stars" (rating)
- Remove any rows with missing data
- Take a random sample of 200 reviews to reduce API costs
- Display basic statistics and preview the data

WHAT HAPPENS:
1. Full dataset loaded from yelp.csv (10,000 rows)
2. Filtered to keep only text and stars columns
3. Null values removed to ensure clean data
4. Random sample of 200 reviews selected (with fixed seed for reproducibility)
5. Data preview shown to verify structure

===============================================================================
                      PART 3: JSON RESPONSE PARSER
===============================================================================

LOGIC:
- LLM responses can come in various formats (with/without code blocks)
- Need robust parsing to extract JSON from different response styles
- Handle cases where JSON might be wrapped in ```json blocks
- Extract JSON even if it's embedded within other text
- Return None if no valid JSON found

WHAT HAPPENS:
1. Function checks if response text exists
2. Removes markdown code fences (```json) if present
3. Tries to parse direct JSON format first
4. If that fails, searches for JSON pattern within text
5. Returns parsed JSON object or None if parsing fails

===============================================================================
                        PART 4: LLM API WRAPPER
===============================================================================

LOGIC:
- Create a simple wrapper function for OpenAI API calls
- Use GPT-4o-mini model (cost-effective choice)
- Set temperature to 0.0 for consistent, deterministic responses
- Handle the API request/response cycle cleanly

WHAT HAPPENS:
1. Function takes a prompt string as input
2. Sends request to OpenAI with specified model and parameters
3. Extracts and returns the text content from the response
4. Provides clean interface for making LLM predictions

===============================================================================
                    PART 5: PROMPT VERSION 1 (SIMPLE)
===============================================================================

LOGIC:
- Basic, straightforward approach to classification
- Clear instructions asking for 1-5 star rating
- Specify exact JSON format expected in response
- Minimal context, letting the model use its training

WHAT HAPPENS:
1. Tells model it's analyzing a Yelp restaurant review
2. Requests rating in specific JSON format
3. Provides the review text for analysis
4. Expects: {"predicted_stars": <number>, "explanation": "<reason>"}

===============================================================================
                  PART 6: PROMPT VERSION 2 (FEW-SHOT)
===============================================================================

LOGIC:
- Provide examples to guide the model's behavior
- Show 3 examples covering different sentiment levels (negative, neutral, positive)
- Help model understand the rating scale through concrete examples
- Demonstrate the exact output format expected

WHAT HAPPENS:
1. Shows example: "Terrible food" → 1 star (very negative)
2. Shows example: "The food was okay" → 3 stars (neutral/mixed)
3. Shows example: "Amazing staff and tasty food" → 5 stars (very positive)
4. Then asks model to classify the actual review using same pattern

===============================================================================
                   PART 7: PROMPT VERSION 3 (CHAIN)
===============================================================================

LOGIC:
- Encourage internal reasoning before final output
- Ask model to analyze internally first, then provide clean JSON
- Minimize explanation length to focus on accuracy
- Streamlined approach with emphasis on final result

WHAT HAPPENS:
1. Instructs model to analyze the review internally first
2. Requests only the final JSON output (no intermediate steps shown)
3. Emphasizes very short explanations to reduce noise
4. Focuses on getting clean, parseable responses

===============================================================================
                      PART 8: EVALUATION SYSTEM
===============================================================================

LOGIC:
- Test each prompt version on the same dataset for fair comparison
- Track multiple metrics: accuracy, JSON parsing success rate, sample size
- Handle API errors gracefully during batch processing
- Calculate accuracy only on successfully parsed responses

WHAT HAPPENS:
1. For each review in sample:
   - Generate prompt using specified version
   - Call LLM API and get response
   - Parse JSON from response
   - Extract predicted rating and explanation
   - Compare with true rating
2. Calculate metrics:
   - Total samples processed
   - Percentage of valid JSON responses
   - Accuracy (correct predictions / valid predictions)

===============================================================================
                        PART 9: RESULTS & COMPARISON
===============================================================================

LOGIC:
- Run all three prompt versions on the same 200 review sample
- Compare their performance across key metrics
- Save detailed results and summary comparison
- Identify which prompt engineering approach works best

WHAT HAPPENS:
1. Execute evaluation for all 3 prompt versions (takes ~15 minutes total)
2. Results show:
   - V1 (Simple): 68.5% accuracy, 100% JSON success rate
   - V2 (Few-shot): 66.0% accuracy, 100% JSON success rate  
   - V3 (Chain): 66.5% accuracy, 100% JSON success rate
3. Save results to CSV files for further analysis
4. V1 (Simple approach) performed best with 68.5% accuracy

===============================================================================
                              KEY FINDINGS
===============================================================================

BEST APPROACH: Version 1 (Simple Classification)
- Achieved highest accuracy at 68.5%
- All prompt versions had 100% JSON parsing success
- Simple, direct instructions worked better than complex prompting
- Few-shot examples didn't improve performance significantly
- Chain-of-thought approach didn't provide advantage for this task

TECHNICAL SUCCESS:
- Robust JSON parsing handled all LLM response variations
- API wrapper provided reliable interface to OpenAI
- Evaluation framework enabled fair comparison of approaches
- Cost-controlled sampling made experimentation feasible

===============================================================================
                               FILES CREATED
===============================================================================

1. task1_prompt_comparison.csv - Summary metrics for all 3 approaches
2. task1_results_v1.csv - Detailed results for Simple approach
3. task1_results_v2.csv - Detailed results for Few-shot approach  
4. task1_results_v3.csv - Detailed results for Chain approach

Each results file contains: true ratings, predicted ratings, explanations, 
and raw LLM outputs for analysis and debugging.

===============================================================================