# Week 4: AI-Assisted Development with Q Developer

## Learning Objectives
By the end of this week, students will be able to:
- Set up and configure Amazon Q Developer
- Write effective prompts for code generation
- Use Q Developer for AWS-specific development tasks
- Build a complete mini-application using AI assistance
- Troubleshoot and debug AI-generated code

## Instructor-Led Session (2 hours)

### Part 1: Introduction to Q Developer (30 minutes)
- **What is Amazon Q Developer?**
  - AI coding assistant vs. general AI chatbot
  - Integration with IDEs and AWS Console
  - Capabilities: code generation, explanation, debugging
- **Setup and Configuration**
  - Installing Q Developer extension
  - Authentication and permissions
  - Console vs. IDE usage

### Part 2: Prompt Engineering for Code (45 minutes)
- **Effective Prompt Structure**
  - Be specific about context and requirements
  - Include programming language and frameworks
  - Specify input/output formats
- **AWS-Specific Prompting**
  - Mention AWS services by name
  - Include IAM and security considerations
  - Request error handling and logging
- **Live Demo: Prompt Refinement**
  - Start with basic prompt
  - Iteratively improve for better results
  - Handle common issues and errors

### Part 3: Q Developer Setup and Exploration (30 minutes)
- **Setup and Configuration**
  - Install Q Developer in preferred environment
  - Complete authentication setup
  - Test basic code generation capabilities
  - Explore different prompt styles

## Self-Paced Learning (2-3 hours)

### Required Labs
1. **Prompt Engineering Practice** (60 minutes)
   - Use prompts from the AI prompts package
   - Generate code for each core AWS service
   - Practice refining prompts for better results
   - Document what works and what doesn't

2. **Mini-Project: Student Directory** (2 hours)
   - **Goal**: Build complete student lookup system
   - **Components**:
     - DynamoDB table for student data
     - Lambda function for search API
     - Simple HTML interface
     - CloudFormation for deployment
   - **Process**: Use Q Developer for all code generation
   - **Deliverable**: Working application deployed in AWS

### Reading/Videos
- Q Developer User Guide
- Prompt Engineering Best Practices
- Review AI prompts package from project materials

## Mini-Project Specifications

### Student Directory System
**Functionality:**
- Store student information (ID, name, major, year)
- Search students by name or major
- Display results in web interface

**Technical Requirements:**
- DynamoDB table with appropriate schema
- Lambda function with proper error handling
- HTML/CSS/JavaScript frontend
- All code generated using Q Developer prompts

**Success Criteria:**
- Application deploys without errors
- Search functionality works correctly
- Code is well-commented and understandable
- Student can explain how each component works

## Troubleshooting Common Issues

### When Q Developer Code Doesn't Work:
1. **Check the error message** - paste it back to Q Developer
2. **Simplify the request** - break complex tasks into smaller parts
3. **Add more context** - specify AWS region, service versions, etc.
4. **Ask for explanations** - "Explain what this code does step by step"

### When Code is Too Complex:
1. **Request simpler version** - "Make this easier for a beginner"
2. **Ask for alternatives** - "Show me a different way to do this"
3. **Break it down** - "Split this into separate functions"

## Key Takeaways
- Q Developer is a powerful tool, but you need to understand the generated code
- Good prompts lead to better code - be specific and iterative
- Always test generated code incrementally
- AI assistance accelerates development but doesn't replace understanding
- The combination of AWS knowledge + AI assistance is extremely powerful

## Preparation for Project Phase
Students should now be ready to:
- Choose their project team and preferred project
- Use the AI prompts package effectively
- Build AWS applications with confidence
- Troubleshoot issues independently
