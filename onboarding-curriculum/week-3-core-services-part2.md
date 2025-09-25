# Week 3: Core AWS Services Deep Dive (Part 2)

## Learning Objectives
By the end of this week, students will be able to:
- Design and create DynamoDB tables with appropriate schemas
- Use Amazon Bedrock to integrate AI models into applications
- Set up Amazon Q Business for organizational knowledge management
- Understand how these services integrate with Week 2 services

## Instructor-Led Session (2 hours)

### Part 1: DynamoDB (30 minutes)
- **NoSQL database fundamentals**
- **Tables, items, and attributes**
- **Primary keys and indexing**

### Part 2: Q Business (30 minutes)
- **Enterprise AI assistant overview**
- **Integration with organizational data**
- **Natural language queries**

### Break (10 minutes)

### Part 3: Bedrock (30 minutes)
- **Foundation models overview**
- **Available models and use cases**
- **Knowledge bases and agents**

### Part 4: Assignment Review (20 minutes)
- **Review self-paced learning assignment**
- **Q&A**

## Self-Paced Learning

### Required Labs
- **To-Do List Chatbot (Hands-on Workshop):** https://catalog.us-east-1.prod.workshops.aws/workshops/5a2df4d7-5702-46a1-b11d-1bb7318086a5/en-US/introduction
  - Access Link: https://catalog.us-east-1.prod.workshops.aws/join?access-code=a8e0-0f1dad-d5 
- **Skillbuilder - Q Business Getting Started:** https://skillbuilder.aws/learn/XDC51QHE4W/amazon-q-business-getting-started/GTNUVSWBJ2
- **Optional Content:**
  - **DynamoDB Core Concepts (video):** https://www.youtube.com/watch?v=Mw8wCj0gkRc
  - **Amazon Bedrock Agents (video):** https://www.youtube.com/watch?v=JkDzZFTXeSw
  - **Responsible AI:** https://aws.amazon.com/ai/responsible-ai/

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
