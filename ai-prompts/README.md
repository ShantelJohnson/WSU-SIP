# AI Prompts Package for WSU Student Innovation Program

This directory contains sample AI prompts to accelerate student development across all four projects. These prompts are designed to be used with Amazon Q Developer or other AI coding assistants.

## 📁 Directory Structure

```
ai-prompts/
├── README.md (this file)
├── success-predictor/
│   └── data-generation-prompts.md
├── starfish-system/
│   ├── cloudformation-prompts.md
│   ├── dynamodb-prompts.md
│   ├── lambda-api-prompts.md
│   ├── frontend-prompts.md
│   └── sample-data-prompts.md
├── campus-chatbot/
│   ├── cloudformation-prompts.md
│   ├── bedrock-prompts.md
│   ├── frontend-chat-prompts.md
│   └── integration-prompts.md
└── opportunity-calendar/
    ├── cloudformation-prompts.md
    ├── dynamodb-prompts.md
    ├── bedrock-agent-prompts.md
    └── eventbridge-prompts.md
```

## 🚀 Quick Start Guide

1. **Copy and paste prompts** into Amazon Q Developer or your preferred AI assistant
2. **Customize the prompts** with your specific requirements (table names, regions, etc.)
3. **Review generated code** before implementation - understand what it does
4. **Test incrementally** - don't implement everything at once
5. **Ask follow-up questions** to refine the generated code

---

## 💡 Prompt Engineering Tips for AWS Student Projects

### Writing Effective Prompts

#### 1. Be Specific About Context
- Mention you're building for AWS services
- Specify the programming language (Python, JavaScript, etc.)
- Include the AWS service names (DynamoDB, Lambda, S3, etc.)

#### 2. Ask for Complete, Working Examples
- Request "complete working code" rather than snippets
- Ask for error handling and logging
- Specify output format (JSON, CSV, HTML, etc.)

#### 3. Include Constraints
- Mention any limitations (free tier, specific regions)
- Specify data sizes or performance requirements
- Include security considerations

### Sample Effective Prompt Structure
```
Create a [complete/working] [language] [function/script/application] that:
1. [Primary objective]
2. [Secondary requirements]
3. [Output format/behavior]

Requirements:
- Uses AWS [service names]
- Includes error handling
- [Any specific constraints]

Please include comments explaining each section.
```

## 🔧 Troubleshooting Common Issues

### When Q Developer Code Doesn't Work:
1. **Check the error message** - paste it back to Q Developer
2. **Request step-by-step** - "Break this down into smaller functions I can test individually"
3. **Simplify the request** - "Give me just the basic version first"
4. **Ask for debugging help** - "This code gave me error [paste error]. How do I fix it?"

### When Code is Too Complex:
1. **Ask for simplification** - "Make this simpler for a beginner to understand"
2. **Request explanations** - "Explain what each part of this code does"
3. **Ask for alternatives** - "Show me a different way to accomplish this"
4. **Break it down** - "Split this into separate functions"

### When You Need Modifications:
1. **Be specific about changes** - "Modify this to also include [specific feature]"
2. **Ask for variations** - "Show me 2-3 different ways to implement this"
3. **Request optimization** - "How can I make this more efficient?"

## ✅ Best Practices

- **Start simple** - Get basic functionality working first
- **Test incrementally** - Don't implement everything at once
- **Ask follow-up questions** - AI assistants can clarify and improve code
- **Understand before implementing** - Make sure you know what the code does
- **Save working versions** - Keep copies of code that works before making changes

## ⚠️ Important Notes

- These prompts generate starting code, not production-ready solutions
- Students should understand and modify the generated code
- Always test generated code in a development environment first
- Use these as learning aids to understand AWS service patterns
- AI assistance accelerates development but doesn't replace understanding
