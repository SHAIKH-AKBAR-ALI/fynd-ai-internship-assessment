# Fynd Assessment - LLM-Powered Applications

## 🎯 Project Overview

This repository contains two comprehensive tasks demonstrating advanced Large Language Model (LLM) integration for real-world applications. The project showcases prompt engineering, sentiment analysis, and AI-powered feedback systems using OpenAI's GPT-4o-mini.

## 🏗️ Project Architecture

```
Fynd Assessment
│
├── TASK_1/                    # Rating Prediction System
│   ├── Task_1.ipynb          # Jupyter notebook implementation
│   ├── yelp.csv              # Dataset (10K Yelp reviews)
│   ├── task1_*.csv           # Generated results and comparisons
│   └── README.md             # Task 1 documentation
│
├── TASK_2/                    # Feedback Management System  
│   ├── app.py                # Streamlit web application
│   ├── requirements.txt      # Python dependencies
│   ├── feedback.csv          # Generated feedback data
│   └── README.md             # Task 2 documentation
│
├── .env                      # API keys (not in repo)
└── README.md                 # This main documentation
```

## 📋 Task Summaries

### Task 1: Yelp Review Rating Prediction
**Objective**: Develop and compare prompt engineering strategies for sentiment classification

**Key Features**:
- 🔬 **3 Prompt Engineering Approaches**: Simple, Few-shot, Chain-of-thought
- 📊 **Comprehensive Evaluation**: Accuracy, JSON validity, consistency metrics
- 🎯 **Best Performance**: 68.5% accuracy with simple classification approach
- 📈 **Robust Analysis**: 200-sample evaluation with statistical comparison

**Technical Stack**: Python, OpenAI API, Pandas, Jupyter Notebook

### Task 2: AI-Powered Feedback Management System
**Objective**: Build a dual-dashboard system for feedback collection and analytics

**Key Features**:
- 👥 **User Dashboard**: Feedback submission with AI-generated responses
- 🛠️ **Admin Dashboard**: Analytics, visualizations, and AI insights
- 📊 **Real-time Analytics**: Live metrics, charts, and trend analysis
- 🤖 **AI Integration**: Automated summaries and improvement suggestions

**Technical Stack**: Streamlit, OpenAI API, Plotly, Pandas, CSV Storage

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.8+
pip install pandas openai python-dotenv streamlit plotly tqdm jupyter
```

### Environment Setup
```bash
# Clone repository
git clone <repository-url>
cd fynd-assessment-llm-tasks

# Configure API key
echo "OPENAI_API_KEY=your_openai_api_key" > .env
```

### Running Task 1
```bash
cd TASK_1
jupyter notebook Task_1.ipynb
# Execute all cells to run evaluation
```

### Running Task 2
```bash
cd TASK_2
streamlit run app.py
# Access web interface at http://localhost:8501
```

## 🔧 Technical Architecture

### System Design Philosophy

**Modular Architecture**
- Each task is self-contained with its own dependencies
- Shared LLM integration patterns across both tasks
- Consistent error handling and data validation

**LLM Integration Strategy**
```python
# Standardized LLM wrapper
def call_llm(prompt, model="gpt-4o-mini", temperature=0.0):
    # Consistent API interface
    # Error handling and retry logic
    # Response parsing and validation
```

**Data Flow Patterns**
```
Input → Validation → LLM Processing → Response Parsing → Storage/Display
```

### Core Components

#### 1. LLM Integration Layer
- **Model**: OpenAI GPT-4o-mini (cost-effective, high-performance)
- **Configuration**: Deterministic responses (temperature=0.0) for Task 1, creative responses (temperature=0.7) for Task 2
- **Error Handling**: Graceful API failure management with fallback responses

#### 2. Data Processing Pipeline
- **Input Validation**: Robust checking for required fields and data types
- **Response Parsing**: JSON extraction from various LLM response formats
- **Storage Management**: CSV-based persistence with proper error handling

#### 3. Evaluation Framework (Task 1)
- **Multi-metric Analysis**: Accuracy, JSON validity, response consistency
- **Comparative Testing**: Side-by-side evaluation of prompt strategies
- **Statistical Rigor**: Fixed random seeds for reproducible results

#### 4. Web Interface (Task 2)
- **Responsive Design**: Clean, intuitive user interface
- **Real-time Updates**: Dynamic dashboard with live data refresh
- **Interactive Analytics**: Plotly-powered visualizations

## 📊 Results & Performance

### Task 1: Prompt Engineering Analysis

| Approach | Accuracy | JSON Validity | Key Insight |
|----------|----------|---------------|-------------|
| **Simple Classification** | **68.5%** | 100% | Direct instructions outperform complex prompting |
| Few-Shot Learning | 66.0% | 100% | Examples don't significantly improve performance |
| Chain-of-Thought | 66.5% | 100% | Reasoning steps add complexity without benefit |

**Key Findings**:
- Simple, direct prompts achieve highest accuracy
- 100% JSON parsing success across all approaches
- Cost-effective evaluation with 200-sample testing

### Task 2: System Performance

**User Experience Metrics**:
- ⚡ **Response Time**: <3 seconds for LLM-generated replies
- ✅ **Success Rate**: 100% form submission success
- 🎯 **User Satisfaction**: Personalized, contextual responses

**Admin Analytics Capabilities**:
- 📈 **Real-time Metrics**: Live dashboard updates
- 📊 **Visual Analytics**: Interactive charts and trends
- 🤖 **AI Insights**: Automated pattern recognition and suggestions

## 🛠️ Development Insights

### Prompt Engineering Lessons
1. **Simplicity Wins**: Direct instructions often outperform complex prompting strategies
2. **JSON Consistency**: Robust parsing is crucial for reliable LLM integration
3. **Cost Management**: Strategic sampling enables thorough evaluation within budget constraints

### System Design Principles
1. **User-Centric Design**: Intuitive interfaces for both end-users and administrators
2. **Modular Architecture**: Separate concerns for maintainability and scalability
3. **Error Resilience**: Comprehensive error handling for production reliability

### LLM Integration Best Practices
1. **Deterministic vs Creative**: Choose temperature based on use case requirements
2. **Response Validation**: Always validate and parse LLM outputs
3. **Fallback Strategies**: Implement graceful degradation for API failures

## 🔮 Future Enhancements

### Task 1 Extensions
- **Advanced Prompting**: Test GPT-4, Claude, or other models
- **Larger Datasets**: Scale evaluation to full 10K dataset
- **Multi-class Metrics**: Precision, recall, F1-score analysis
- **Cross-validation**: K-fold validation for robust performance assessment

### Task 2 Improvements
- **Database Integration**: Replace CSV with PostgreSQL/MongoDB
- **User Authentication**: Multi-user support with role-based access
- **Advanced Analytics**: Sentiment trends, keyword analysis, predictive insights
- **API Development**: RESTful API for external integrations

### System-wide Upgrades
- **Containerization**: Docker deployment for consistent environments
- **CI/CD Pipeline**: Automated testing and deployment
- **Monitoring**: Application performance and LLM usage tracking
- **Security**: Enhanced data protection and API security

## 📚 Documentation Structure

Each task includes comprehensive documentation:

- **README.md**: Technical architecture and implementation details
- **Code Comments**: Inline documentation for complex logic
- **Results Analysis**: Detailed performance metrics and insights
- **Usage Examples**: Step-by-step execution instructions

## 🤝 Contributing

This project demonstrates production-ready LLM integration patterns suitable for:
- **Educational Reference**: Learning prompt engineering and LLM integration
- **Business Applications**: Customer feedback systems and sentiment analysis
- **Research Projects**: Comparative analysis of LLM approaches
- **Portfolio Demonstrations**: Showcasing AI/ML engineering capabilities

## 📄 License

This project is developed as part of the Fynd assessment and demonstrates practical LLM application development skills.

---

**Built with ❤️ by SHAIKH AKBAR ALI using OpenAI GPT-4o-mini, Streamlit, and modern Python ecosystem**