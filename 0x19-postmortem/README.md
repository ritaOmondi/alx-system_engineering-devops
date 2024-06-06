                                           #Postmoterm
Postmortem: EVENT

On June 6th, 2024, between 9:00 AM and 11:30 AM EAT, our e-commerce website experienced a significant outage, affecting approximately 40% of our users. The root cause of the incident was a memory leak in the backend API server.

Timeline

9:00 AM EAT : The issue was first detected by our monitoring system, which triggered an alert indicating high CPU utilization and slow response times from the backend API server.

9:05 AM EAT - The on-call engineer was notified and began investigating the issue. Initial checks revealed that the API server was consuming an abnormally high amount of memory, causing the server to become unresponsive.

9:15 AM EAT - The engineering team was mobilized, and they started analyzing the application logs and server metrics to identify the root cause of the memory leak.
9:30 AM EAT - Suspecting a bug in the latest code deployment, the team started rolling back the deployment, but this did not resolve the issue.
10:00 AM EAT - The incident was escalated to the engineering manager, and the team decided to scale out the API server by provisioning additional instances.
10:15 AM EAT - The new API server instances were deployed, but the memory leak persisted, causing the overall system to remain unstable.
10:45 AM EAT - The engineering team, along with the site reliability engineering (SRE) team, began a deeper investigation, analyzing the application code and the server configurations.
11:00 AM EAT - The root cause was identified as a memory leak in the third-party library used in the API server's codebase.
11:15 AM EAT - A temporary fix was implemented by restarting the affected API server instances, which provided a short-term solution.
11:30 AM EAT - The website was restored to normal operation, and the team continued to work on a permanent solution.

Root Cause and Resolution

The root cause of the incident was a memory leak in the third-party library used in the backend API server. This library, which was responsible for handling user authentication, had a bug that caused it to continuously allocate memory without properly releasing it. As a result, the API server's memory consumption grew exponentially, leading to severe performance degradation and eventual unresponsiveness.

To resolve the issue, the engineering team first attempted to roll back the latest deployment, but this did not address the underlying problem. The team then scaled out the API server by provisioning additional instances, but the memory leak persisted, causing the overall system to remain unstable.

After a deeper investigation, the team identified the root cause as the memory leak in the third-party library. A temporary fix was implemented by restarting the affected API server instances, which provided a short-term solution. The team then worked on a permanent fix by upgrading the third-party library to a version that addressed the memory leak issue.

Corrective and Preventative Measures

To address this incident and prevent similar issues in the future, the following corrective and preventative measures will be implemented:

Upgrade the third-party library responsible for the memory leak to the latest stable version.
Implement more robust monitoring and alerting mechanisms to quickly detect and respond to memory-related issues in the API server.
Conduct a comprehensive review of the application's use of third-party libraries and dependencies to identify and address any potential vulnerabilities or performance issues.
Implement a more rigorous testing and deployment process, including load testing and canary deployments, to identify and mitigate issues before they reach production.
Provide additional training and knowledge sharing sessions for the engineering team on best practices for debugging and resolving memory-related issues in distributed systems.
By taking these corrective and preventative measures, the team aims to improve the overall reliability and stability of the e-commerce website, ensuring a seamless experience for our users.



Sense of Humor on Postmoterm

Issue Summary

On June 6th, 2024, between 9:00 AM and 11:30 AM EAT, our e-commerce website experienced a significant outage, affecting approximately 40% of our users. The root cause of the incident was a memory leak in the backend API server, which we affectionately dubbed the "Memory Vampire." 🧛‍♂️

Timeline

9:00 AM EAT - The issue was first detected by our monitoring system, which triggered an alert indicating high CPU utilization and slow response times from the backend API server. Our on-call engineer, let's call him "Captain Caffeine," sprang into action.
9:05 AM EAT - Captain Caffeine began investigating the issue, only to find that the API server was consuming an abnormally high amount of memory, causing it to become unresponsive. He let out a loud groan, "Not again!"
9:15 AM EAT - The engineering team was mobilized, and they started analyzing the application logs and server metrics to identify the root cause of the memory leak. It was starting to feel like a game of "Where's Waldo?" but with lines of code instead of a striped shirt.
9:30 AM EAT - Suspecting a bug in the latest code deployment, the team started rolling back the deployment, but this did not resolve the issue. They stared at the screen, scratching their heads, wondering, "Did we accidentally summon the Memory Vampire?"
10:00 AM EAT - The incident was escalated to the engineering manager, and the team decided to scale out the API server by provisioning additional instances. It was like playing a high-stakes game of "Whack-a-Mole," trying to keep up with the memory-hungry server.

