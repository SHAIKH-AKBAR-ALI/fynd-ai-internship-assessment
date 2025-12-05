# Task 2: AI-Powered Feedback Management System

## Overview
A dual-dashboard Streamlit application that collects customer feedback and provides AI-powered analytics. The system features separate interfaces for users (feedback submission) and administrators (analytics and insights).

## Architecture

### System Design
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Streamlit App   │───▶│   Admin Panel   │
│   (Feedback)    │    │                  │    │   (Analytics)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   CSV Storage    │
                       │   + LLM API      │
                       └──────────────────┘
```

### Data Flow Architecture

#### User Journey
```
Form Input → Validation → LLM Response Generation → CSV Storage → Success Message
```

#### Admin Journey  
```
CSV Load → Statistics Calculation → Chart Generation → LLM Analysis → Insights Display
```

## Core Components

### 1. User Dashboard
**Purpose**: Collect and respond to customer feedback

**Components**:
- **Feedback Form**: Name, rating (1-5), review text
- **Input Validation**: Required field checking
- **LLM Response Generator**: Personalized replies using GPT-4o-mini
- **Data Persistence**: Automatic CSV storage with timestamps

**Code Flow**:
```python
# Form submission handling
if submitted:
    validate_input() → generate_llm_response() → save_to_csv() → display_response()
```

### 2. Admin Dashboard  
**Purpose**: Analyze feedback patterns and generate insights

**Components**:
- **Statistics Panel**: Total feedback, average rating, latest submission
- **Visualization Engine**: Rating distribution charts, time-series analysis
- **AI Analytics**: LLM-powered summaries and improvement suggestions
- **Data Explorer**: Raw feedback data viewer

**Code Flow**:
```python
# Dashboard rendering
load_csv() → calculate_metrics() → generate_charts() → ai_analysis() → display_results()
```

### 3. Data Management Layer

**Storage Schema**:
```python
FEEDBACK_COLUMNS = [
    "timestamp",      # ISO format datetime
    "user_name",      # Optional user identifier  
    "rating",         # Integer 1-5
    "review_text",    # Feedback content
    "user_llm_response"  # AI-generated response
]
```

**File Operations**:
- **Load**: Robust CSV reading with error handling
- **Append**: Thread-safe record addition
- **Validation**: Column consistency checking

### 4. LLM Integration

**Response Generation**:
```python
def generate_user_response(name, rating, text):
    # Personalized response based on sentiment
    # Acknowledges rating level (positive/negative)
    # Professional, empathetic tone
```

**Admin Analytics**:
```python
def generate_admin_summary(df):
    # Identifies common themes and patterns
    # Sentiment analysis across feedback
    # Overall satisfaction assessment

def generate_admin_actions(df):
    # Actionable improvement recommendations
    # Prioritized by impact and feasibility
    # Based on actual feedback content
```

## Technical Implementation

### Streamlit Architecture
```python
# App Structure
st.set_page_config() → Main Layout → Tab Navigation → Component Rendering

# User Tab
with tab_user:
    form_component() → llm_processing() → data_storage()

# Admin Tab  
with tab_admin:
    metrics_display() → charts_generation() → ai_insights()
```

### Error Handling Strategy
```python
# CSV Operations
try:
    pd.read_csv() → validate_columns() → return_dataframe()
except EmptyDataError:
    return_empty_dataframe()

# LLM API Calls
try:
    openai_request() → parse_response() → return_content()
except Exception:
    return_error_message()
```

### State Management
- **Session Independence**: Each user interaction is stateless
- **Data Persistence**: CSV-based storage for simplicity
- **Real-time Updates**: Dynamic dashboard refresh on new data

## Key Features

### User Experience
- **Intuitive Form**: Simple, clean feedback submission
- **Instant Response**: AI-generated personalized replies
- **Validation**: Real-time input checking
- **Confirmation**: Success feedback with response display

### Admin Analytics
- **Live Metrics**: Real-time statistics calculation
- **Visual Analytics**: Interactive Plotly charts
- **AI Insights**: Automated pattern recognition
- **Data Export**: Full dataset access for further analysis

### AI Capabilities
- **Sentiment Analysis**: Rating-aware response generation
- **Pattern Recognition**: Theme identification across feedback
- **Actionable Insights**: Specific improvement recommendations
- **Personalization**: Name-aware, context-sensitive responses

## File Structure
```
TASK_2/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── feedback.csv          # Generated data storage
└── .env                  # API keys (not in repo)
```

## Configuration

### Environment Setup
```bash
# Dependencies
pip install streamlit pandas openai python-dotenv plotly

# API Configuration
echo "OPENAI_API_KEY=your_key_here" > .env
```

### Application Launch
```bash
streamlit run app.py
```

## Data Schema

### CSV Structure
| Column | Type | Description |
|--------|------|-------------|
| timestamp | ISO String | Submission datetime (UTC) |
| user_name | String | Optional user identifier |
| rating | Integer | 1-5 star rating |
| review_text | Text | Feedback content |
| user_llm_response | Text | AI-generated response |

### Sample Data Flow
```
Input: {"name": "John", "rating": 5, "text": "Great service!"}
↓
Processing: LLM generates personalized response
↓  
Storage: CSV append with timestamp
↓
Output: Success message + AI response display
```

## Performance Considerations

### Scalability
- **CSV Limitations**: Suitable for moderate data volumes (<10K records)
- **LLM Rate Limits**: OpenAI API quotas apply
- **Memory Usage**: Efficient pandas operations for data processing

### Optimization
- **Lazy Loading**: Charts generated only when tab is active  
- **Batch Processing**: Efficient bulk operations for large datasets
- **Caching**: Streamlit native caching for repeated operations

## Security & Privacy

### Data Protection
- **Local Storage**: CSV files stored locally, not in cloud
- **API Security**: Environment variable for API keys
- **Input Sanitization**: Basic validation on user inputs

### Privacy Considerations
- **Optional Names**: User identification is optional
- **Data Retention**: Manual CSV management (no auto-deletion)
- **Access Control**: Single-user application (no authentication)