# ANTRIX - Automated Email Pipeline

## 📧 Simple Overview

ANTRIX is an intelligent email automation system that takes the hassle out of reaching out to businesses. Here's what it does in plain English:

1. **Finds Companies** - You provide a company name, and ANTRIX automatically searches for and gathers information about them
2. **Collects Details** - It pulls together company information, addresses, and contact details
3. **Creates Custom Emails** - Instead of sending generic emails, ANTRIX generates personalized emails tailored to each company
4. **Designs Brochures** - It automatically creates professional brochures to accompany your emails
5. **Quality Control** - The system reviews everything to ensure quality before sending
6. **Sends Automatically** - Using secure API keys, ANTRIX sends all emails without any manual intervention

Perfect for sales teams, B2B outreach, and marketing campaigns that need to scale!

![32a88e4d-ed68-4970-8e3f-74570c93b86f](https://github.com/user-attachments/assets/43673cc4-4e6f-4ae6-a5b3-7a2b8432b488)

---

## 🔧 Technical Architecture

ANTRIX is built with a sophisticated multi-stage pipeline that combines web scraping, natural language processing, content generation, and automated email delivery:

### Core Components:

**1. Data Acquisition Layer**
- Web scraping module for company information retrieval
- Integration with business databases and public APIs
- Address geocoding and verification services

**2. NLP & Personalization Engine**
- Advanced language models for email content generation
- Context-aware customization based on company industry, size, and profile
- Template-based email generation with dynamic variable insertion

**3. Content Generation Pipeline**
- Automated brochure generation using local machine learning models
- PDF/Image rendering engine for professional document creation
- Brand-aware design templates

**4. Supervision & Quality Assurance**
- Locally-run ML models for content validation
- Spam score checking and deliverability analysis
- Email template verification and compliance checks

**5. Delivery System**
- SMTP integration with multiple email service providers
- API-key authenticated secure delivery
- Batch processing capabilities with rate limiting
- Delivery status tracking and bounce handling

### Technology Stack:
- **Backend**: Python (core orchestration)
- **LLMs**: Local models for privacy-first operations
- **APIs**: Third-party integrations for enhanced data accuracy
- **Database**: Data persistence for campaigns and tracking
- **Security**: Encrypted API key management and secure credential storage

### Workflow:
```
Company Input → Data Scraping → Email Generation → Brochure Creation → Quality Check → Automated Delivery
```
## File Structure

- **main.py**: This is the main entry point of the application, responsible for initializing and executing the core functionalities.
- **db.py**: Contains all database-related operations including connections, queries, and data manipulation.
- **prompts/**: This directory includes various prompt templates used throughout the application for generating email content.
- **supervisor/**: This folder contains supervisor scripts that manage the overall email workflow and ensure tasks are executed in the correct sequence.
- **regenerate/**: Holds scripts for regenerating certain components of the email pipeline based on new inputs or configurations.
- **configuration/**: Includes configuration files necessary for setting up and customizing the application according to user preferences and system requirements.

This architecture ensures scalable, personalized outreach while maintaining security and quality standards.
