# AWS Student Innovation Program

**Project Portfolio - Wayne State University SEAL Lab Partnership**

## Program Overview

The following four projects represent **recommended architectures** designed specifically for student completion within a **4-5 week timeframe**. Each project includes multiple implementation tracks to accommodate different skill levels and interests.

### About AWS Services

Amazon Web Services (AWS) provides cloud computing services that allow organizations to build applications without managing physical servers. Each project uses different AWS services that work together like building blocks - some handle data storage, others provide artificial intelligence capabilities, and others manage user interfaces.

### Project Flexibility

These architectures are starting points, not rigid requirements. Student teams can choose different implementation paths based on their technical background, interests, and progress. Optional components allow teams to expand their projects if they complete core requirements ahead of schedule.

---

## EMU Starfish Inspired System

**Difficulty Level:** TECHNICAL

### Project Goal

Create a digital system that allows faculty, advisors, and staff to easily flag students who need support or recognition. Think of it as a collaborative early warning system that helps the SEAL Lab identify students who could benefit from additional resources or celebrate those doing well.

### AWS Services & Technologies

- **DynamoDB** - Database for storing student records and flags
- **API Gateway** - Handles data input from web forms
- **Lambda** - Backend logic for processing flag submissions
- **S3** - Hosts static website and stores documents
- **SNS** - Sends notifications when flag thresholds are exceeded

### What Students Will Build

- Web interface where faculty and staff can submit student flags or kudos
- **Choose Implementation:** Dashboard showing recent flags OR notification system for high-priority alerts

### Student Requirements & Fit

- **Technical Level:** This project requires basic programming skills and familiarity with web design
- **Best For:** Students interested in full-stack development and building complete web applications
- **Team Requirements:** 3-4 students recommended; 1-2 students familiar with scripting languages (Python, Node.js, etc.), 1 student familiar with web design (HTML/CSS/JavaScript), 1 student familiar with database concepts

### 5-Week Development Timeline

**Week 1: Foundation Setup**
- Database Developer: Design DynamoDB schema and create tables with sample data
- Frontend Developer: Create basic HTML forms and page structure
- Backend Developer: Set up AWS services (API Gateway, Lambda functions skeleton)

**Weeks 2-3: Parallel Development**
- Frontend Developer: Complete web interface styling and form validation
- Backend Developer: Develop Lambda functions and API Gateway integration
- Database Developer: Refine data models and create database utilities
- *Integration checkpoints: Test API connections with mock data*

**Weeks 4-5: Integration & Implementation Choice**
- All team members: Connect frontend to backend services
- Week 5 focus: Choose and implement either Dashboard OR Notifications system
- Final testing and deployment

### AI Support & Acceleration

Q Developer will be used to help with the following:

- **CloudFormation templates:** Pre-configured AWS infrastructure setup
- **Code templates:** Starting HTML/JavaScript and Python Lambda code
- **Sample data:** Realistic test data for development and testing
- **AI prompt library:** Sample prompts for DynamoDB schema, API Gateway setup, and Lambda functions

### Optional/Production Enhancements

**Stretch Goals (if time permits):**

- **User authentication:** Cognito integration for role-based access
- **Audit logging:** Track who submitted which flags and when

---

## Academic Success Predictor

**Difficulty Level:** LOW CODE / NO CODE

### Project Goal

Build a comprehensive academic risk assessment package that analyzes student data to predict which students might need extra support. The system provides both visual dashboards and conversational AI interfaces, delivered as a cohesive user experience through automated reporting and seamless navigation between tools.

### AWS Services & Technologies

- **Amazon S3** - Stores synthetic student data files and analysis results
- **SageMaker Canvas** - No-code tool for building predictive AI models
- **QuickSight** - Creates visual dashboards and automated email reports
- **Amazon Q Business** - AI-powered conversational interface for exploring student risk factors

### What Students Will Build

- Academic Risk Assessment Package with weekly automated email reports
- QuickSight dashboard for visual analytics with embedded link to Q Business app
- Q Business conversational interface for deeper data exploration

### Student Requirements & Fit

- **Technical Level:** Low-code project requiring basic understanding of data concepts and AI/ML workflows
- **Best For:** Business-focused students interested in data analytics and AI applications
- **Team Requirements:** 3-4 students recommended; 1-2 students familiar with data analysis concepts, 1 student familiar with business intelligence tools, 1 student interested in AI/ML applications

### 5-Week Development Timeline

**Week 1: Data Foundation**
- Data Analyst: Generate comprehensive synthetic student datasets
- BI Developer: Explore QuickSight capabilities and plan dashboard structure
- AI/ML Student: Research Q Business capabilities

**Weeks 2-3: Parallel Development**
- Data Analyst: Upload data to S3 and train SageMaker Canvas model
- BI Developer: Build QuickSight dashboard with key visualizations
- AI/ML Student: Set up Q Business app with data sources
- *Integration checkpoints: Ensure data consistency across platforms*

**Weeks 4-5: Integration & Automation**
- All team members: Connect systems and test data flow
- Week 5 focus: Set up automated email reporting and final integration
- Polish user experience across all components

### AI Support & Acceleration

Q Developer will be used to help with the following:

- **Sample scripts for creating realistic synthetic student datasets**

### Optional/Production Enhancements

**Stretch Goals (if time permits):**

- **Role-based dashboards:** Different QuickSight views for faculty, advisors, and administrators
- **Custom webpage integration:** Embed QuickSight dashboard and/or Q Business app into a unified web interface

---

## SEAL Lab Campus Chatbot

**Difficulty Level:** TECHNICAL

### Project Goal

Create an AI-powered chatbot that can answer student questions about SEAL Lab services, tutoring information, and campus resources. The chatbot will be available 24/7 to help students get information even when staff aren't available.

### AWS Services & Technologies

- **Bedrock** - Amazon's AI service for conversational chatbots
- **Bedrock Knowledge Base** - Stores and organizes SEAL Lab information for the chatbot to reference
- **Lambda & API Gateway** - Handles the chatbot logic and web interface connections
- **S3** - Hosts the chat interface and stores knowledge base documents

### What Students Will Build

- Web-based chatbot that students can access
- Knowledge base containing comprehensive SEAL Lab information
- Integrated system connecting frontend chat interface with backend AI services

### Student Requirements & Fit

- **Technical Level:** This project requires basic programming skills and familiarity with web design
- **Best For:** Students interested in conversational interfaces and training AI models with custom data
- **Team Requirements:** 3-4 students recommended; 1-2 students familiar with scripting languages (Python, Node.js, etc.), 1 student familiar with web development (HTML/CSS/JavaScript), 1 student interested in AI/ML applications

### 5-Week Development Timeline

**Week 1: Content & Infrastructure Setup**
- AI Content Developer: Gather and organize SEAL Lab information
- Backend Developer: Setup Lambda skeleton for LLM and basic chat functionality
- Frontend Developer: Design chat interface mockups and basic HTML structure

**Weeks 2-3: Parallel Development**
- AI Content Developer: Setup Knowledge Base and populate with comprehensive content
- Backend Developer: Develop API logic and Bedrock integration
- Frontend Developer: Build complete chat interface (HTML, CSS, JavaScript)
- *Integration checkpoints: Test Knowledge Base responses and API connectivity*

**Weeks 4-5: Integration & Enhancement**
- All team members: Connect frontend chat interface with backend services
- Week 5 focus: Fine-tune chatbot responses and user experience
- Final testing and deployment

### AI Support & Acceleration

All of these aids will be created with Q Developer:

- **CloudFormation templates:** Complete AWS infrastructure deployment
- **Frontend chat interface:** Generate chat UI components and styling
- **Code templates:** Sample code for connecting frontend to backend services
- **AI prompt library:** Sample prompts for Bedrock Knowledge Base setup and Lambda integration

### Optional/Production Enhancements

**Stretch Goals (if time permits):**

- **User authentication:** Cognito integration for personalized chat experiences
- **Tutoring session scheduling:** Amazon Bedrock Agent that schedules tutoring sessions (or simulates this functionality)

---

## Campus Opportunity Calendar

**Difficulty Level:** TECHNICAL

### Project Goal

Build an automated system that discovers educational opportunities (free courses, certifications, scholarships, workshops) from multiple websites and presents them in an organized format. This helps SEAL Lab staff discover and promote relevant opportunities to students without manual searching.

### AWS Services & Technologies

- **DynamoDB** - Stores discovered educational opportunities and event data
- **Bedrock Knowledge Base** - Web crawler that automatically discovers content from educational websites
- **Bedrock Agent** - AI agent that extracts event information and populates the database
- **EventBridge** - Schedules automatic weekly knowledge base refresh and data sync
- **SNS OR S3** - Either sends email notifications OR hosts static calendar website

### What Students Will Build

- Automated system that discovers educational opportunities from multiple websites
- **Choose Implementation:** Email notification system OR web-based calendar interface
- Weekly automated refresh system that keeps opportunities current

### Student Requirements & Fit

- **Technical Level:** This project requires basic understanding of systems integration and automation
- **Best For:** Students interested in automation, AI agents, and system integration
- **Team Requirements:** 4 students recommended; 1 student familiar with scripting languages (Python, Node.js, etc.), 1 student familiar with database concepts, 2 students interested in AI/ML applications

### 5-Week Development Timeline

**Week 1: Architecture Setup**
- Database Developer: Create DynamoDB table structure for event data
- Backend Developer: Setup Lambda skeleton for populating DynamoDB table
- AI/ML Student 1: Research target educational websites for Knowledge Base
- AI/ML Student 2: Explore Bedrock Agent capabilities

**Weeks 2-3: Parallel Development**
- Database Developer: Refine data models and create database utilities
- Backend Developer: Setup EventBridge automation for weekly refresh
- AI/ML Student 1: Setup Knowledge Base and populate with comprehensive content
- AI/ML Student 2: Create and configure Bedrock Agent (that uses Lambda function for populating the DynamoDB table)
- *Integration checkpoints: Test data extraction and database population*

**Weeks 4-5: Automation & Implementation Choice**
- All team members: Set up EventBridge automation for weekly refresh
- Week 5 focus: Choose and implement either Email notifications (SNS) OR Calendar website (S3)
- Final testing and deployment

### AI Support & Acceleration

Q Developer will help create:

- **CloudFormation templates:** Complete AWS infrastructure deployment
- **Bedrock Agent configuration:** Agent setup and action group configuration
- **AI prompt library:** DynamoDB table design, EventBridge automation, and static calendar development

### Optional/Production Enhancements

**Stretch Goals (if time permits):**

- **User preferences:** Personalized filtering based on student interests and academic focus
- **Calendar integration:** Export events as iCal format for Google Calendar and Outlook import

---

## Program Information

**AWS Student Innovation Program** | Wayne State University SEAL Lab Partnership  
4-5 Week Project Timeline | Pilot Program | Flexible Implementation Tracks
