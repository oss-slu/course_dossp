---
title: Threat Model
points_possible: 1.0
due_at: '2025-11-20T05:59:59Z'
submission_types:
- online_upload
allowed_extensions:
- pdf
published: true
assignment_group_id: 149308
grading_type: points
canvas_id: 657141
---
## Due: November 19, 2025

## Overview

Security is a critical concern for any software product, and open source projects face unique security challenges. A threat model helps you systematically identify potential security risks, understand their impact, and plan appropriate mitigations. This checkpoint asks you to create a threat model for your product that considers both general software security principles and threats specific to open source development.

## Learning Objectives

By completing this checkpoint, you will:
- Understand fundamental threat modeling principles and practices
- Identify potential security threats relevant to your specific product
- Analyze attack surfaces and threat actors in your product's context
- Prioritize security risks based on likelihood and impact
- Consider security challenges unique to open source projects
- Develop practical mitigation strategies

## Background: Security in Open Source

Open source projects face distinctive security considerations:
- **Transparency**: Your code is publicly visible, making vulnerabilities discoverable by both good and bad actors
- **Supply chain risks**: Dependencies on other open source projects can introduce vulnerabilities
- **Contribution model**: Accepting external contributions requires trust and verification mechanisms
- **Resource constraints**: Many OSS projects have limited security expertise and resources
- **Downstream impact**: Your project may be a dependency for others, amplifying security impacts
A threat model helps you understand these risks and make informed decisions about where to invest your security efforts.

## Assignment

Create a threat model for your product that:
- **Identifies your product's attack surface**
- What are the entry points to your system?
- What data does your product handle?
- What external systems or services does it interact with?
- Who are the different types of users/actors?
- **Catalogs potential threats**
- What could go wrong?
- Who might want to attack your system and why?
- What vulnerabilities exist in your current design?
- Consider both technical threats (e.g., SQL injection, XSS) and open source-specific threats (e.g., malicious contributions, compromised dependencies)
- **Assesses and prioritizes risks**
- What is the potential impact of each threat?
- How likely is each threat to be realized?
- Which risks require immediate attention vs. long-term planning?
- **Proposes mitigations**
- What can you do to prevent, detect, or reduce each threat?
- What security controls are appropriate for your context?
- What trade-offs exist between security and other product goals?

## Suggested Approaches

There are many valid approaches to threat modeling. Choose methods that make sense for your product:
- **STRIDE**: Categorize threats as Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, or Elevation of Privilege
- *Best for: Products with user authentication, data storage, or multiple trust levels. Provides comprehensive coverage across threat categories. Good starting point if you're unsure where to begin.*
- **Attack Trees**: Map out how an attacker might achieve specific goals
- *Best for: Products with high-value targets (e.g., sensitive data, critical infrastructure, financial transactions). Helps you think like an attacker and understand attack paths. Useful when you have specific security concerns to explore in depth.*
- **Data Flow Diagrams**: Identify threats at trust boundaries in your system
- *Best for: Products with multiple components, external integrations, or data moving between different security contexts (e.g., client-server, microservices, third-party APIs). Visualizes where data crosses trust boundaries.*
- **PASTA** (Process for Attack Simulation and Threat Analysis): Risk-centric methodology
- *Best for: Products where business risk and compliance matter significantly. More comprehensive but time-intensive. Consider if your product handles regulated data, has clear business objectives tied to security, or needs to align with organizational risk frameworks.*
- **Simple lists**: If your product is straightforward, a structured list of threats and mitigations may suffice
- *Best for: Products with limited attack surface (e.g., command-line tools, libraries with no network access, single-purpose utilities). Also appropriate for early-stage products where a lightweight approach helps you get started.*
**You can combine approaches**: For example, use Data Flow Diagrams to visualize your architecture, then apply STRIDE at each trust boundary. Or start with a simple list and deepen your analysis with Attack Trees for your highest-priority threats.
Consider tools that fit your workflow:
- Diagramming tools for visualizing attack surfaces
- Threat modeling frameworks
- Spreadsheets or tables for tracking threats and mitigations
- Your existing documentation tools

## The goal is understanding and addressing your security risks, not following a specific methodology.

## Resources

### OSS-Cybersecurity Team Support

The OSS-Cybersecurity team is available to help all teams with threat modeling:
- **Consultation**: Reach out for advice on approach, methodology, or specific concerns
- **Document Review**: Submit your draft threat model for feedback
- Reviews are prioritized on a ranked first-come-first-served basis (ranked by the Cybersecurity team's internal risk assessment)
- Response time depends on team availability

### Additional Resources

- **OWASP Threat Modeling**: https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Open source-specific guidance**:
- OpenSSF Best Practices: https://bestpractices.coreinfrastructure.org/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- **Threat modeling guides**: Search for threat modeling tutorials specific to your technology stack

### For Internal Services Teams

If your team supports other OSS teams (infra/ops, CI/CD & automation, dev analytics, cybersecuirty), you're protecting not just external users but the entire OSS program. The OSS-Cybersecurity team will work with you to create a threat model for OSS program infrastructure. Please coordinate with them early.

## Deliverable

Submit a **threat model document** that (probably) includes:
- **Executive Summary**: Brief overview of your product's key security risks and priorities
- **Product Context**: What your product does, who uses it, and what it protects
- **Attack Surface Analysis**: Entry points, data flows, trust boundaries
- **Threat Catalog**: Identified threats with:
- Description of the threat
- Potential impact
- Likelihood assessment
- Affected components/users
- **Risk Prioritization**: Which threats require immediate vs. long-term attention
- **Mitigation Strategy**: Planned or implemented controls for high-priority threats
- **Open Questions**: Security concerns you're unsure how to address

### Format Requirements

- **Primary deliverable**: PDF document uploaded to the checkpoint submission
- **Living document**: Include a link to a living version (Google Doc, Sharepoint Word Doc, GitHub markdown, wiki page, etc.) that future teams can update as the product evolves
- **Length**: As long as necessary to cover your threats meaningfully (minimum 3 pages, up to about 15 pages, but this varies by product complexity)

### What Makes a Strong Submission

- Demonstrates understanding of your product's specific security context
- Shows realistic thinking about threats relevant to your users and use cases
- Prioritizes risks appropriately (not everything is critical; not everything is low-priority)
- Proposes practical mitigations aligned with your resources and timeline
- Considers open source-specific security challenges
- Reflects genuine analysis rather than generic security checklists

## Notes

- **This is a learning exercise**: You're not expected to be security experts. The goal is to think systematically about security and develop good practices.
- **Document your thinking**: Even if you're uncertain about something, document your reasoning and questions.
- **Real impact**: This threat model will help future teams understand security considerations for your product.
- **Iterate later**: This is a point-in-time assessment. Security is ongoing, and your threat model will evolve.
