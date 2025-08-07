# Week 2: Core AWS Services Deep Dive (Part 1)

## Learning Objectives
By the end of this week, students will be able to:
- Configure IAM users, roles, and policies for secure access
- Create and manage S3 buckets and objects
- Build and deploy basic Lambda functions
- Understand how these services work together in applications

## Instructor-Led Session (2 hours)

### Part 1: Identity and Access Management (IAM) (40 minutes)
- **Why IAM Matters**
  - Security best practices and least privilege principle
  - Root account vs. IAM users
- **Core IAM Concepts**
  - Users, groups, roles, and policies
  - Authentication vs. authorization
- **Hands-on Demo**
  - Create IAM user with console access
  - Attach policies and test permissions
  - Create service role for Lambda

### Part 2: Simple Storage Service (S3) (40 minutes)
- **S3 Fundamentals**
  - Buckets, objects, and keys
  - Storage classes and pricing
  - Security and access control
- **Common Use Cases**
  - Static website hosting
  - Data backup and archival
  - Application data storage
- **Hands-on Demo**
  - Create S3 bucket
  - Upload files and set permissions
  - Enable static website hosting

### Part 3: AWS Lambda (40 minutes)
- **Serverless Computing Concepts**
  - Event-driven architecture
  - Pay-per-execution model
  - Automatic scaling
- **Lambda Fundamentals**
  - Function structure and runtime
  - Triggers and event sources
  - Environment variables and configuration
- **Hands-on Demo**
  - Create simple "Hello World" Lambda function
  - Test function in console
  - View logs in CloudWatch

## Self-Paced Learning (2-3 hours)

### Required Labs
1. **IAM Security Lab** (45 minutes)
   - Create IAM user for yourself
   - Set up MFA
   - Create custom policy for S3 access
   - Test permissions

2. **S3 Storage Lab** (60 minutes)
   - Create bucket with versioning enabled
   - Upload different file types
   - Configure bucket for static website
   - Set up bucket policies

3. **Lambda Function Lab** (75 minutes)
   - Build Lambda function that processes S3 events
   - Configure S3 trigger
   - Test end-to-end workflow
   - Review CloudWatch logs

### Reading/Videos
- AWS IAM Best Practices documentation
- S3 User Guide (Getting Started section)
- Lambda Developer Guide (Getting Started)

## Integration Example
**Simple File Processing Pipeline:**
1. User uploads file to S3 bucket
2. S3 triggers Lambda function
3. Lambda processes file and saves result
4. IAM roles ensure secure access throughout

## Key Takeaways
- IAM is the foundation of AWS security - always follow least privilege
- S3 is more than storage - it's a platform for web hosting and data processing
- Lambda enables serverless applications that scale automatically
- These services work together to create powerful, secure applications
