# Week 3: Core AWS Services Deep Dive (Part 2)

## Learning Objectives
By the end of this week, students will be able to:
- Design and create DynamoDB tables with appropriate schemas
- Use Amazon Bedrock to integrate AI models into applications
- Set up Amazon Q Business for organizational knowledge management
- Understand how these services integrate with Week 2 services

## Instructor-Led Session (2 hours)

### Part 1: Amazon DynamoDB (45 minutes)
- **NoSQL Database Concepts**
  - Relational vs. NoSQL databases
  - When to use DynamoDB vs. traditional databases
- **DynamoDB Fundamentals**
  - Tables, items, and attributes
  - Primary keys (partition key and sort key)
  - Global Secondary Indexes (GSI)
- **Hands-on Demo**
  - Create student records table
  - Insert and query data
  - Set up GSI for different query patterns

### Part 2: Amazon Bedrock (45 minutes)
- **Foundation Models Overview**
  - What are Large Language Models (LLMs)?
  - Available models in Bedrock (Claude, Llama, etc.)
  - Use cases: text generation, summarization, Q&A
- **Bedrock Components**
  - Model access and pricing
  - Knowledge Bases for custom data
  - Agents for complex workflows
- **Hands-on Demo**
  - Access Bedrock in console
  - Test text generation with different models
  - Create simple Knowledge Base

### Part 3: Amazon Q Business (30 minutes)
- **Enterprise AI Assistant**
  - Q Business vs. Q Developer
  - Integration with organizational data
  - Security and access controls
- **Key Features**
  - Document upload and indexing
  - Natural language queries
  - Conversation history and context
- **Hands-on Demo**
  - Set up Q Business application
  - Upload sample documents
  - Test conversational queries

## Self-Paced Learning (2-3 hours)

### Required Labs
1. **DynamoDB Data Modeling Lab** (60 minutes)
   - Design table for student flag system
   - Create table with appropriate keys
   - Insert sample data and test queries
   - Practice different query patterns

2. **Bedrock AI Integration Lab** (75 minutes)
   - Create Lambda function that calls Bedrock
   - Test different prompts and models
   - Build simple Q&A system
   - Handle API responses and errors

3. **Q Business Setup Lab** (45 minutes)
   - Create Q Business application
   - Upload SEAL Lab documentation
   - Test knowledge retrieval
   - Explore conversation features

### Reading/Videos
- DynamoDB Developer Guide (Core Components)
- Bedrock User Guide (Getting Started)
- Q Business Administrator Guide (Setup)

## Integration Examples

### Example 1: Student Support System
1. **DynamoDB** stores student records and flags
2. **Lambda** processes flag submissions
3. **Bedrock** analyzes flag patterns for insights
4. **S3** hosts the web interface
5. **IAM** secures all interactions

### Example 2: Knowledge Management
1. **Q Business** provides conversational interface
2. **S3** stores source documents
3. **Lambda** processes document updates
4. **DynamoDB** tracks usage analytics

## Key Takeaways
- DynamoDB excels at high-performance, scalable applications with predictable access patterns
- Bedrock democratizes AI by providing easy access to powerful foundation models
- Q Business transforms static documents into interactive knowledge systems
- All AWS services work together - design with integration in mind
