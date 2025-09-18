# Week 2: Core AWS Services Deep Dive (Part 1)

## Learning Objectives
By the end of this week, students will be able to:
- Configure IAM users, roles, and policies for secure access
- Create and manage S3 buckets and objects
- Build and deploy basic Lambda functions
- Understand how these services work together in applications

## Instructor-Led Session (2 hours)

### Part 1: IAM (20 minutes)
- **Identity and Access Management fundamentals**
- **Users, roles, and policies**
- **AWS Security Best Practices**
  - Shared Responsibility Model
  - Principal of least privilege

### Part 2: S3 (30 minutes)
- **Simple Storage Service fundamentals**
- **Buckets, objects, and security**
- **Common use cases**

### Break (10 minutes)

### Part 3: Lambda (20 minutes)
- **Serverless computing concepts**
- **Function structure and triggers**
- **Event-driven architecture**

### Part 4: Workshop Studio (20 minutes)
- **Setup Workshop Studio accounts**
- **Environment configuration**

### Part 5: Assignment Review (20 minutes)
- **Review self-paced learning assignment**
- **The labs will use the Workshop studio accounts we setup in Part 4**

## Self-Paced Learning

### Required Labs
**Temporary Account Access:** https://catalog.us-east-1.prod.workshops.aws/join?access-code=7990-045c17-0c
- **S3 Hands-On Lab:** https://catalog.workshops.aws/general-immersionday/en-US/basic-modules/60-s3/s3 
- **IAM Roles:** https://catalog.workshops.aws/iam-immersionday/en-US/basic-modules/20-identities-and-access-management/3-roles 
  - **Including 'Optional IAM Service Roles':** https://catalog.workshops.aws/iam-immersionday/en-US/basic-modules/20-identities-and-access-management/3-roles/2-sr-lab 
- **Skillbuilder - AWS Lambda Getting Started:** https://skillbuilder.aws/learn/S6YE1Z74TX/aws-lambda-getting-started/D5XQ4GCZXR
- **Optional Content:**
  - Serverless 101 - AWS Lambda (video): https://youtu.be/GEABePyhFPA
  - Getting Started with Amazon S3 (video): https://youtu.be/FZCZbPEMlXk 


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
