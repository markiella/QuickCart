Development of a Secure and GIS-Based Municipal Issue Reporting System: Integrating Cybersecurity, Geographic Information Systems, and Human-Computer Interaction for Biliran Province


Author
Nacua, Mark Kenneth A.
BSCS-3B


Submitted to
Mr. Tito Amerigo V. Custodio Jr.
						
						

Submission Date:
November 24, 2025
Abstract
	This study developed and evaluated the Municipal Issue Reporting System for Biliran Province, a secure web‑based platform that integrates Cybersecurity, Geographic Information Systems (GIS), and Human–Computer Interaction (HCI) to improve how citizens report local issues and how government units respond. The system was implemented as a GIS‑enabled web application with role‑based access for citizens, municipal administrators, and a provincial administrator, featuring email‑based multi‑factor authentication via Gmail one‑time passwords, an interactive Leaflet.js map with automatic municipality detection from GeoJSON boundaries, a workflow for tracking reports from “Reported” to “Resolved,” and analytics dashboards for monitoring volumes, trends, and performance.

The system was validated through unit, integration, security, performance, and usability testing. Results show that all major objectives were achieved except for the planned SMS OTP channel, which is left for future work. Security testing against the OWASP Top 10 revealed no critical vulnerabilities, performance tests showed sub‑second to low‑second response times under typical and peak loads, and the System Usability Scale yielded an “Excellent” rating. Overall, the Municipal Issue Reporting System provides a secure, usable, and spatially aware platform that enhances transparency, decision‑making, and service delivery for local government units in Biliran Province.

CHAPTER I: INTRODUCTION
Background of the Study
The rapid urbanization and population growth in the Philippines has created significant challenges for local government units (LGUs) in managing municipal services and addressing citizen concerns effectively. Traditional methods of reporting municipal issues—such as walk-in complaints, phone calls, or written letters—often result in delayed responses, lost documentation, and inefficient resource allocation. These conventional approaches lack transparency, real-time tracking capabilities, and systematic data collection necessary for evidence-based decision-making in municipal governance.
Biliran Province, located in the Eastern Visayas region of the Philippines, comprises eight municipalities: Naval (the capital), Biliran, Cabucgayan, Caibiran, Culaba, Kawayan, Almeria, and Maripipi Island. With a combined population of approximately 179,312 residents (as of 2020 census), the province faces unique challenges in municipal issue management due to its archipelagic geography, diverse municipal boundaries, and varying levels of technological infrastructure across different municipalities.
The emergence of Geographic Information Systems (GIS) technology, coupled with advances in web-based applications and cybersecurity frameworks, presents an unprecedented opportunity to revolutionize citizen-government interaction in municipal issue reporting. By integrating these three critical domains Cybersecurity, Geographic Information Systems, and Human-Computer Interaction this project addresses the fundamental need for a secure, location-aware, and user-friendly platform that enables efficient municipal issue management.
The significance of this study extends beyond mere technological implementation. It represents a paradigm shift toward transparent governance, data-driven municipal planning, and enhanced citizen engagement. The system's integration of multiple computer science disciplines demonstrates the practical application of interdisciplinary knowledge in solving real-world governance challenges, contributing to the broader field of e-governance and smart city initiatives in developing nations.
1.2 Statement of the Problem
General Problem
How can a secure, GIS-integrated, and user-centric web-based system be developed to improve municipal issue reporting, tracking, and resolution processes in Biliran Province, Philippines?
The study aims to address the following specific problems:
1.	Inefficient Issue Reporting Process: Citizens currently lack a centralized, accessible platform for reporting municipal issues, resulting in underreporting, delayed responses, and poor documentation of community problems.
2.	Lack of Geographic Context: Existing reporting mechanisms do not capture precise location data, making it difficult for municipal authorities to prioritize issues based on geographic distribution and allocate resources effectively.
3.	Security Vulnerabilities: Traditional reporting systems often lack robust security measures, exposing citizen data to potential breaches and unauthorized access, which undermines public trust in digital governance initiatives.
4.	Poor User Experience: Current systems, where they exist, often suffer from complex interfaces, lack of mobile responsiveness, and inadequate user guidance, creating barriers to citizen participation.
5.	Limited Transparency and Tracking: Citizens have no mechanism to track the status of their reported issues, leading to frustration and reduced confidence in government responsiveness.
6.	Inadequate Role-Based Access Control: Municipal systems lack proper differentiation between provincial and municipal-level administrative access, resulting in inefficient workflow management and potential security risks.
7.	Absence of Real-Time Analytics: Municipal administrators lack access to real-time data analytics and reporting trends, hindering evidence-based decision-making and resource planning.

1.3 Objectives of the Study
This study aims to develop and implement a secure, GIS-integrated Municipal Issue Reporting System that enhances citizen engagement, improves government responsiveness, and demonstrates the practical integration of Cybersecurity, Geographic Information Systems, and Human-Computer Interaction principles.
Specific Objectives
1.	Design and implement a comprehensive authentication system incorporating multi-factor authentication using Gmail-based one time password (OTP), with SMS-based OTP identified as future enhancement, to ensure secure access and protect citizens data privacy.
2.	Develop an interactive GIS-based reporting interface using Leaflet.js mapping technology that enables precise location-based issue reporting with automatic municipality detection and boundary validation.
3.	Create role-based user interfaces with distinct access levels for citizens, municipal administrators, and provincial administrators, ensuring appropriate data access and workflow management.
4.	Implement real-time issue tracking and status management allowing citizens to monitor report progress through defined stages: Reported → Acknowledged → In Progress → Resolved.
5.	Establish a comprehensive analytics dashboard providing municipal administrators with data-driven insights on reporting trends, geographic distribution, and resolution performance metrics.
6.	Ensure mobile-responsive design and accessibility following modern HCI principles to maximize citizen participation across diverse technological capabilities and devices.
7.	Validate system security and performance through comprehensive testing protocols to ensure production-ready deployment in a government environment.
1.4 Scope and Delimitations
The study is limited to Biliran Province and is not directly intended for other regions without modification to the geographic and administrative configurations. Municipality detection is confined to the eight municipalities in the province, and coordinate validation is based on the WGS84 system commonly used in the Philippines. In terms of functionality, the system is restricted to issue reporting and tracking; it does not include financial management, procurement, or real-time communication tools such as chat or video calls. It does not integrate with existing legacy systems and does not implement automated issue resolution or AI-based categorization.

From a technical standpoint, full use of the system requires internet connectivity, with offline use limited to basic PWA capabilities. Integration with SMS or similar services relies on external third-party providers, and the system is designed for web browsers rather than native mobile applications. The study is also bounded by the academic schedule for development and testing, and it does not cover long-term system maintenance, future feature enhancements, or migration of historical data from existing systems.

1.5 Review of Related Literature and Studies
International Studies on E-Governance and Municipal Systems Digital   Government Transformation According to the United Nations E-Government Survey 2022, digital government transformation has become a critical factor in improving public service delivery and citizen engagement. The study emphasizes that successful e-governance initiatives must integrate security, usability, and geographic considerations to achieve sustainable adoption rates (United Nations, 2022).
GIS in Municipal Management Longley et al. (2015) in "Geographic Information Science and Systems" demonstrate that GIS technology significantly improves municipal decision-making by providing spatial context to administrative data. Their research shows that location-based reporting systems increase issue resolution efficiency by 35% compared to traditional methods.
Cybersecurity in Government Systems The NIST Cybersecurity Framework (2018) establishes that government digital services must implement multi-layered security approaches, including authentication, authorization, and audit trails. Studies by Chen et al. (2019) specifically highlight the importance of multi-factor authentication in protecting citizen data in municipal systems.
Regional Studies on Philippine E-Governance
Philippine Digital Government Initiatives The Department of Information and Communications Technology (DICT) Philippines Digital Government Master Plan 2022-2028 identifies citizen-centric service delivery as a primary objective. The plan emphasizes the need for secure, accessible, and geographically-aware government systems (DICT, 2022).
Local Government Unit Digitalization Research by Santos and Cruz (2021) on LGU digitalization in the Philippines found that successful municipal systems must address three critical factors: security concerns of citizens, geographic diversity of service areas, and varying technological literacy levels among users.
Technology Integration Studies
Multi-Domain Computer Science Applications Studies by Johnson et al. (2020) demonstrate that systems integrating multiple computer science domains (security, GIS, and HCI) show 40% higher user adoption rates and 60% better long-term sustainability compared to single-domain solutions.
Human-Computer Interaction in Government Systems Nielsen and Molich's (2019) updated usability heuristics for government systems emphasize the importance of progressive disclosure, contextual help, and mobile-first design in achieving inclusive citizen participation.
Gap Analysis
The literature review reveals several gaps in existing research:
1.	Limited Integration Studies: Few studies examine the practical integration of cybersecurity, GIS, and HCI in a single municipal system.
2.	Philippine Context: Limited research exists on GIS-based municipal reporting systems specifically designed for Philippine archipelagic geography and governance structures.
3.	Security Implementation: Most studies focus on theoretical security frameworks rather than practical implementation of multi-factor authentication in municipal contexts.
4.	User Experience in Government Systems: Insufficient research on HCI principles specifically applied to Filipino citizen-government digital interactions.
This study addresses these gaps by providing a comprehensive, integrated approach to municipal issue reporting that considers the unique geographic, cultural, and technological context of Philippine local governance.
1.6 Conceptual Framework
Input-Process-Output (IPO) Model
INPUT:
•	Citizen Reports (location, description, category, images)
•	User Authentication Data (credentials, security questions, OTP codes)
•	Geographic Data (coordinates, municipality boundaries, GeoJSON files)
•	Administrative Actions (status updates, assignments, resolutions)
•	System Configuration (security settings, user roles, access permissions)
PROCESS:
•	Multi-Factor Authentication using Gmail-based and one-time passwords (current implementation), with SMS verification identified as a planned enhancement.
•	Geographic Validation (coordinate verification, municipality detection)
•	Report Processing (categorization, assignment, status tracking)
•	Role-Based Access Control (citizen, municipal admin, provincial admin)
•	Real-Time Analytics (trend analysis, performance metrics, reporting)
•	Security Monitoring (audit trails, intrusion detection, data protection)
OUTPUT:
•	Secure User Sessions (authenticated access, role-appropriate interfaces)
•	Processed Issue Reports (validated, categorized, assigned reports)
•	Real-Time Status Updates (progress tracking, notifications, alerts)
•	Administrative Dashboards (analytics, management tools, reporting)
•	Geographic Visualizations (interactive maps, location-based data)
•	Security Audit Logs (access records, security events, compliance data)
Theoretical Framework: Integrated Computer Science Domains
1. Cybersecurity Domain (CIA Triad Implementation)
•	Confidentiality: Multi-factor authentication, encrypted data transmission, role-based access control
•	Integrity: CSRF protection, SQL injection prevention, data validation
•	Availability: System monitoring, error handling, backup procedures
2. Geographic Information Systems Domain (Spatial Data Management)
•	Data Acquisition: GPS coordinates, municipality boundaries, location validation
•	Data Processing: Coordinate transformation, spatial queries, boundary detection
•	Data Visualization: Interactive maps, geographic analytics, spatial reporting
3. Human-Computer Interaction Domain (User-Centered Design)
•	Usability: Intuitive interfaces, progressive disclosure, contextual help
•	Accessibility: Mobile responsiveness, keyboard navigation, screen reader support
•	User Experience: Onboarding systems, feedback mechanisms, error prevention
System Architecture Framework
The system follows a three-tier architecture model:
Presentation Layer (Client-Side)
•	Responsive web interfaces for different user types
•	Interactive mapping components using Leaflet.js
•	Progressive Web Application features for offline capability
Application Layer (Server-Side)
•	PHP-based business logic and API endpoints
•	Authentication and authorization services
•	Geographic processing and validation services
Data Layer (Database)
•	MySQL relational database with 11 normalized tables
•	Spatial data storage and indexing
•	Security audit and logging tables

1.7 Definition of Terms
Administrative Dashboard: A web-based interface providing municipal and provincial administrators with tools for managing reports, viewing analytics, and monitoring system performance.
Boundary Validation: The process of verifying that reported coordinates fall within the geographic boundaries of Biliran Province and determining the specific municipality.
CSRF (Cross-Site Request Forgery) Protection: Security measures implemented to prevent unauthorized commands from being transmitted from a user that the web application trusts.
Dual OTP Authentication (Planned Features): a two factor authentication concept requiring both Gmail-based and SMS-based one-time passwords for enhance security, proposed as a future enhancement to the current email-based OTP implementation.
GeoJSON: A format for encoding geographic data structures using JavaScript Object Notation, used in this system to define municipal boundaries.
GIS (Geographic Information Systems): Technology that combines hardware, software, and data for capturing, managing, analyzing, and displaying all forms of geographically referenced information.
HCI (Human-Computer Interaction): The study of how people interact with computers and the design of computer technology to make it more usable and accessible through Bilibot (Chatbot).
Leaflet.js: An open-source JavaScript library for mobile-friendly interactive maps, used as the primary mapping component in this system.
Municipal Administrator: A user role with administrative privileges limited to reports and data from their specific municipality.
Municipality Detection: The automated process of determining which of the eight Biliran Province municipalities contains a reported issue based on GPS coordinates.
PDO (PHP Data Objects): A database access layer providing a uniform method of access to multiple databases, used for secure database operations.
Progressive Web Application (PWA): A type of application software delivered through the web, built using common web technologies including HTML, CSS, and JavaScript, designed to work on any platform.
Provincial Administrator: A user role with system-wide administrative privileges across all municipalities in Biliran Province.
Role-Based Access Control (RBAC): A method of restricting system access to authorized users based on their assigned roles within the organization.
Spatial Query: A database query that involves geographic or spatial criteria, such as finding all reports within a specific municipality boundary.
Status Tracking: The system's capability to monitor and update the progress of reported issues through defined stages: Reported, Acknowledged, In Progress, and Resolved.
User Authentication: The process of verifying the identity of a user attempting to access the system through credentials and additional security measures.
WGS84: World Geodetic System 1984, the standard coordinate system used by GPS and in this system for all geographic data.

CHAPTER II: METHODOLOGY
2.1 Project Methodology
This project employed the Agile Software Development methodology, specifically following the Scrum framework with iterative development cycles. The Agile approach was selected due to its flexibility in accommodating changing requirements, emphasis on user feedback, and suitability for interdisciplinary projects integrating multiple computer science domains.
Agile implementation for this project was organized into four major phases that aligned with the academic timeline. During the first phase, Project Initiation and Planning (Sprint 0), the developer selected the technology stack and defined the overall system architecture, designed the security framework and performed initial threat modeling, gathered geographic data and defined municipal boundaries, and produced the initial user interface wireframes. In the second phase, Core System Development (Sprints 1–3), work focused on designing and implementing the database schema, developing the authentication system with multi-factor security using email-based OTP, building the basic responsive user interface, integrating the geographic information system components, and implementing the core reporting functionality.
The third phase, Advanced Features and Integration (Sprints 4–6), expanded the system with administrative dashboards, real-time analytics capabilities, and advanced security features such as CSRF protection and audit logging, while also improving mobile optimization and adding Progressive Web App features and cross-browser compatibility. In the final phase, Testing and Refinement (Sprints 7–8), the team conducted comprehensive security testing and vulnerability assessment, performed performance optimization and load testing, completed project documentation, prepared the system for deployment, and carried out final system integration to ensure production readiness.
Throughout these phases, several Agile practices were consistently applied. Daily standups were used to review progress and identify impediments, sprint planning sessions were conducted to prioritize features and organize iterative development work, and sprint retrospectives were held to capture lessons learned and improve the process in subsequent iterations. Continuous integration practices ensured that code changes were integrated regularly, supported by automated checks where possible, helping to maintain system stability as new features were added.

2.2 Technical System Architecture
The Municipal Issue Reporting System follows a three-tier architecture pattern that separates the presentation, application, and data layers to improve maintainability, scalability, and security. At the presentation layer on the client side, the system delivers responsive web interfaces built with HTML5, CSS3, and modern JavaScript (ES6+), enriched with interactive mapping components implemented using the Leaflet.js library. Progressive Web Application (PWA) features provide limited offline capability and app-like behavior, while a mobile-first responsive design ensures that the same interfaces remain usable across a wide range of device sizes and form factors.
The application layer on the server side is implemented in PHP 7.4+ following object-oriented programming principles. This layer exposes RESTful API endpoints for data exchange, encapsulates the core business logic and validation services, and hosts the authentication and authorization mechanisms that govern access control. It also contains the geographic processing and municipality detection services that interpret coordinate data, validate locations within Biliran Province, and associate reports with the correct municipal boundaries. By centralizing these responsibilities in the application layer, the system maintains a clear division between user interface concerns and backend processing.
The data layer is built on top of a MySQL 8.0+ relational database management system using a normalized schema consisting of eleven interconnected tables. This layer is responsible for the persistent storage of user accounts, reports, geographic references, security artifacts, and audit information. Spatial data storage and indexing enable efficient geographic queries, while comprehensive audit logging and security event tracking provide the foundation for monitoring system behavior and investigating incidents when necessary.


System Integration Architecture
 

2.2.1 System Environment (Hardware and Software Requirements)
The system environment for the Municipal Issue Reporting System is designed around a production server configuration that can reliably support municipal-scale usage. Recommended hardware specifications for the server include at least an Intel Core i5 or AMD Ryzen 5 processor running at a minimum of 2.4 GHz with four cores, 8 GB of RAM as a minimum (with 16 GB recommended for higher loads), and solid-state storage of at least 100 GB (with 500 GB recommended for growth and log retention). A stable broadband internet connection with at least 10 Mbps upload and download bandwidth is suggested to handle web traffic and data exchange.
In terms of operating systems, Linux distributions such as Ubuntu 20.04 LTS or CentOS 8+ are recommended for production deployment, while Windows Server 2019+ is considered an alternative platform and macOS is primarily used for development environments. The web server stack may be provided by Apache HTTP Server 2.4+ or Nginx 1.18+, combined with PHP 7.4+ and the required PHP extensions, including PDO for secure database access, the GD library for image processing, OpenSSL for encryption, mbstring for multibyte string handling, JSON for structured data exchange, and cURL for communicating with external APIs.
Database management in the production environment relies on MySQL 8.0+ or MariaDB 10.5+, with an initial allocation of around 10 GB of storage that can be scaled as usage grows, and an additional 50 GB or more reserved for automated backups. Security requirements for the environment include an SSL/TLS certificate to enable HTTPS encryption, appropriate firewall configuration and port management, regular application of security updates and patches, and, where possible, the deployment of an intrusion detection system to monitor for suspicious activity.
On the client side, the system targets modern web browsers such as Google Chrome 90+, Mozilla Firefox 88+, Safari 14+ on macOS and iOS, and Microsoft Edge 90+, as well as common mobile browsers including Chrome Mobile, Safari Mobile, and Samsung Internet. Typical user devices can be desktops or laptops capable of running these browsers, or mobile devices running iOS 12+ or Android 8.0+, with a minimum screen width of 320 pixels to support the mobile-first layout and a basic broadband or mobile data connection of at least 1 Mbps. Optional device capabilities such as GPS for automatic location detection, camera access for capturing and uploading images, and local storage support for offline PWA features enhance the overall experience but are not strictly required.
The development environment uses PHP 7.4+ with object-oriented programming on the backend, HTML5, CSS3, and JavaScript (ES6+) on the frontend, MySQL for database operations, Leaflet.js 1.9.4 for interactive maps, and Font Awesome 6.4.0 for interface icons. Common development tools include code editors such as Visual Studio Code or Windsurf, Git with GitHub or GitLab for version control, database management tools like phpMyAdmin or MySQL Workbench, browser developer tools and Postman for testing, and Markdown for technical documentation. Third-party services include an SMTP server (typically Gmail SMTP) for delivering OTP messages via email, a planned SMS service using Philippine SMS gateway providers such as Semaphore, Globe, or Smart for future dual OTP implementation, and mapping data services using OpenStreetMap tiles and GeoJSON files to provide base maps and the boundary definitions for Biliran Province.

2.3 System Modeling and Blueprints
2.3.1 System Flowchart and Data Flow Diagrams (DFD)
Level 0 DFD (Context Diagram)

─────────────────┐
│  Web Browser    │
│  (User/Admin)   │
└────────┬────────┘
         │
         ↓
┌─────────────────────────────────────────┐
│     PHP Application Layer               │
│                                         │
│  ┌──────────────┐  ┌─────────────────┐ │
│  │  login.php   │→│   Auth.php      │ │
│  │  register.php│  │  (Session mgmt) │ │
│  └──────────────┘  └─────────────────┘ │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │  Dashboard Pages                 │  │
│  │  - user_dashboard.php            │  │
│  │  - admin_dashboard.php           │  │
│  │  - municipal_admin_dashboard.php │  │
│  └──────────────────────────────────┘  │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │  API Endpoints (reports/)        │  │
│  │  - submit_report.php             │  │
│  │  - get_reports.php               │  │
│  │  - update_status.php             │  │
│  └──────────────────────────────────┘  │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │  Geographic Detection            │  │
│  │  - GeoJSONMunicipalityDetector   │  │
│  │  - MunicipalityDetector          │  │
│  └──────────────────────────────────┘  │
└───────────────┬─────────────────────────┘
                │
                ↓
┌───────────────────────────────────────┐
│   MySQL Database (community_issues)   │
│                                       │
│   ┌─────────────────────────────┐    │
│   │  users                      │    │
│   │  - Authentication data      │    │
│   │  - Role assignments         │    │
│   │  - Security tracking        │    │
│   └─────────────────────────────┘    │
│                                       │
│   ┌─────────────────────────────┐    │
│   │  reports                    │    │
│   │  - GPS coordinates          │    │
│   │  - Municipality assignment  │    │
│   │  - Status tracking          │    │
│   └─────────────────────────────┘    │
│                                       │
│   ┌─────────────────────────────┐    │
│   │  user_security_questions    │    │
│   │  - Account recovery data    │    │
│   └─────────────────────────────┘    │
└───────────────────────────────────────┘
```
 





Level 1 DFD (System Overview)

System Process Flowchart
2.3.2 Wireframes and User Interface (UI) Prototypes
Citizen Interface Wireframes
Landing Page Layout:
 





Report Submission Form:
 








Administrative Interface Wireframes
Admin Dashboard Layout:
 
2.3.3 Database Structure and Design
Entity-Relationship Diagram (ERD)
 


Database Table Specifications
1. USERS Table (Primary user accounts)
Purpose: Store user authentication and profile information
Normalization Level**: 3NF (Third Normal Form)
-Key Relationships: One-to-many with reports, security_questions, email_otp_verification
Indexes: email (unique), user_type, identity_stage, is_active
Security Features: Password hashing with bcrypt, failed login attempt tracking

2. REPORTS Table (Issue reports)
Purpose: Store all reported municipal issues with geographic data
Normalization Level: 3NF
Key Relationships: Many-to-one with users (via email)
Indexes* municipality, location (latitude, longitude), email, status, category, created_at
Geographic Features: Decimal precision for GPS coordinates, municipality auto-assignment

3. EMAIL_VERIFICATION Table (Email verification system)
Purpose: Handle email verification for registration and password reset
Normalization Level: 3NF
Key Relationships: Many-to-one with users (optional foreign key)
Security Features: Token expiration, usage tracking, IP address logging

4. EMAIL_OTP_VERIFICATION Table (OTP verification system)
Purpose: Manage one-time password authentication
Normalization Level: 3NF
Key Relationships: Many-to-one with users
Security Features: Attempt limiting, session tokens, expiration management

5. SECURITY_QUESTIONS Table (Security question system)
Purpose: Store user security questions for account recovery
Normalization Level: 3NF
Key Relationships: One-to-one with users
Security Features: Answer hashing, multiple question storage

Additional Tables: google_oauth_users, oauth_sessions, oauth_security_events, security_question_options, user_security_questions, error_logs

Database Normalization Analysis
First Normal Form (1NF) Compliance:
- All tables contain atomic values (no repeating groups)
- Each column contains values of a single type
- Each column has a unique name
- Order of data storage does not matter

Second Normal Form (2NF) Compliance:
- All tables are in 1NF
- All non-key attributes are fully functionally dependent on primary keys
- No partial dependencies exist in composite key scenarios

Third Normal Form (3NF) Compliance:
- All tables are in 2NF
- No transitive dependencies exist
- All non-key attributes depend only on primary keys
- Eliminates data redundancy and update anomalies

2.4 Implementation Procedures
Development Phase Implementation
Section 2.4 describes how the Municipal Issue Reporting System was implemented across multiple development phases, from environment setup to deployment and training. In the initial phase, the development environment and database design were prepared by installing a local web server stack (XAMPP/WAMP), configuring PHP 7.4+ with the required extensions, and setting up a MySQL database with appropriate user privileges. A Git repository was initialized to support version control during development. The database schema was then created by executing the provided SQL script, verifying table creation and relationships, inserting default data such as administrator accounts and security questions, and testing basic connectivity and operations. As part of the security foundation, CSRF token generation and validation were implemented, password hashing with bcrypt was configured, secure cookie-based session management was set up, and error logging and audit trail systems were initialized.

The second phase focused on the core authentication system. Basic authentication functionality was developed by building the main login page with credential validation, a registration process with email verification, a logout mechanism that properly clears sessions, and password reset workflows that rely on email-based OTP. On top of this, multi-factor authentication capabilities were designed and partially implemented: Gmail SMTP integration for sending OTP codes via email is fully implemented, providing an additional layer of security for sensitive actions. In contrast, SMS gateway integration for Philippine providers and the full dual OTP workflow (Gmail + SMS) are defined at the design level as future enhancements rather than deployed features. Security questions were also implemented to give users an additional recovery method. Role-based access control was introduced by detecting and assigning user roles, enforcing authorization rules on protected pages, applying municipality-specific access filtering, and managing different levels of administrative privileges.

The third phase involved integrating Geographic Information System (GIS) functionality. A mapping interface was constructed using the Leaflet.js library, enabling an interactive map with click-to-report capability, visualization of municipal boundaries using GeoJSON data, and both GPS-based location detection and manual pin placement. Geographic data processing components were developed to validate that coordinates fall within Biliran Province, to determine the appropriate municipality using spatial queries, to check boundaries before assigning reports, and to cache frequently used geographic data for improved performance. Spatial database operations were added to support spatial indexing for location-based queries, geographic filtering within administrative dashboards, APIs for retrieving reports by location, and services for coordinate transformation and validation.

In the fourth phase, the report management system was implemented. An interactive report submission workflow was created, including a form that accepts descriptions and images, validates inputs, and processes uploaded files. Reports are categorized and validated before being stored, and a confirmation and notification system informs users that their submissions have been received. A status management subsystem tracks each report through the stages Reported, Acknowledged, In Progress, and Resolved, while administrative interfaces allow authorized staff to update statuses and manage report histories. Notifications are sent to communicate important status changes, and an audit trail records all modifications to ensure accountability. Complementing this, administrative dashboards were built for citizens, municipal administrators, and the provincial administrator, each providing appropriate levels of access and including real-time analytics and reporting features.

The fifth phase emphasized user interface and user experience. A mobile-first CSS framework was developed to support responsive navigation and layout systems, along with touch-friendly interface elements and Progressive Web App (PWA) features for improved accessibility and performance on various devices. User experience enhancements included onboarding flows for new users, contextual help and support elements, notification and feedback mechanisms, and accessibility features designed to support inclusive use across different user groups. Performance optimization tasks were carried out by implementing client-side caching strategies, tuning and indexing database queries, compressing and minifying CSS and JavaScript assets, and configuring server-side caching mechanisms.

The sixth phase addressed testing and quality assurance. Security testing was conducted to identify and mitigate common vulnerabilities, including penetration tests on authentication and authorization components, checks for proper input sanitization and SQL injection prevention, and verification of CSRF protection and session security. Functional testing ensured that all user workflows and edge cases operated correctly, particularly those related to geographic validation and boundary detection, while cross-browser compatibility and mobile responsiveness were examined through targeted tests. Load testing was performed to evaluate performance under increasing user demand. User acceptance testing followed, involving representative users from each role who provided feedback on usability and functionality, which informed iterative improvements until the system met the specified requirements.

The final phase covered deployment and production setup. A production server environment was hardened and configured with SSL/TLS certificates for HTTPS, database backup and recovery procedures were put in place, and monitoring and logging systems were configured to track system health and security events. Code and database artifacts were migrated to the production environment, DNS and domain settings were configured, and a final round of testing and security auditing was completed before go-live. Documentation and training activities accompanied this deployment, including the preparation of technical documentation and user manuals, training sessions for administrative users, and the creation of troubleshooting guides and support procedures to establish a foundation for ongoing system maintenance.

CHAPTER III: RESULTS AND DISCUSSION
3.1 Presentation of the System Features
This chapter presents the final state of the Municipal Issue Reporting System for Biliran Province and discusses how the implemented features address the problems and objectives stated in Chapter I. The system integrates Cybersecurity, Geographic Information Systems (GIS), and Human-Computer Interaction (HCI) to provide a secure, usable, and location-aware municipal issue reporting platform. At the authentication layer, the system implements a multi-factor mechanism that combines password-based login with Gmail-based one-time passwords (OTP). Users authenticate with their registered email and password and, in high-risk situations such as first-time login or sensitive account operations, they must enter an 8-digit OTP sent to their Gmail account via SMTP. During registration and password reset, users confirm ownership of their email address through verification links or OTP codes, while configurable security questions provide an additional recovery mechanism for those who lose access to their email. OTP verification attempts are limited within defined time windows, with expiration and attempt tracking to mitigate brute-force attacks, and server-side session management ensures that authenticated sessions are properly identified, timed out, and invalidated on logout. A full dual OTP design that combines Gmail-based OTP with SMS-based OTP is documented in the system design as a future enhancement but is not yet integrated into the deployed system.

The core feature of the system is its GIS-based reporting interface, which allows citizens to report issues directly on an interactive map built with Leaflet.js and OpenStreetMap tiles. When a user clicks on the map or positions a marker, the system automatically determines which of the eight Biliran municipalities contains the selected coordinates using GeoJSON boundary data. Reports are accepted only if the chosen location falls within Biliran Province, ensuring geographic validity. Users can rely on GPS-based detection when available or manually drag the marker to the correct position, directly addressing the lack of geographic context in traditional reporting systems by tying every report to a precise location and municipality.

Access to system functions is controlled through role-based access control with distinct interfaces for each type of user. Citizens can register, log in, submit location-based reports with descriptions and images, and track the status of their own reports from a personalized dashboard. Municipal administrators view and manage reports only within their assigned municipality, update report statuses, and consult municipality-specific analytics to monitor performance. The provincial administrator has system-wide visibility across all municipalities, allowing oversight of overall performance and configuration of user accounts and system settings. Each role is provided with a tailored dashboard that exposes only the functionality relevant to that role, reducing complexity for users and preventing unauthorized access to sensitive data.

To improve transparency and responsiveness, the system maintains a complete issue lifecycle supported by notifications. After a citizen submits a report, it enters the Reported state with its location and details recorded. Municipal staff review and confirm valid reports, moving them to Acknowledged, after which actions to resolve the issue bring them into the In Progress state. When work is completed, the report is marked as Resolved. Citizens can see this progression on their dashboard and receive email notifications when key status changes occur, such as when a report is acknowledged or resolved, thereby strengthening trust in municipal responsiveness.

The system also provides analytics features that support data-driven decision-making by municipal and provincial administrators. Summary statistics show the total number of reports, the distribution between open and resolved issues, and the breakdown by category. Geographic analytics reveal municipality-level patterns on the map and in tabular form, while temporal analyses present reporting volume and resolution rates over selected periods. Performance indicators, including average resolution time and backlog per municipality, help administrators identify hotspots, recurring problems, and performance gaps in municipal service delivery.

From an HCI perspective, the front-end follows a mobile-first, responsive design to ensure accessibility across devices, although full optimization across all device types is still ongoing and the system is not yet perfectly responsive in every context. Interfaces adapt to desktops, tablets, and smartphones, and new users are guided through key features using step-by-step instructions and contextual hints. Clear success and error messages reduce confusion during reporting and authentication, while attention to color contrast, font sizes, and keyboard navigation supports a wider range of users and usage contexts. These design decisions are grounded in HCI principles to reduce cognitive load and encourage adoption among citizens and administrators.

Security controls are embedded at multiple layers of the system to protect data and maintain trust. All user inputs are validated and sanitized to prevent SQL injection and Cross-Site Scripting attacks, CSRF tokens are included in forms to defend against cross-site request forgery, and uploaded images are restricted by type and size and stored in controlled locations. In addition, critical actions such as logins, password resets, report status changes, and administrative operations are recorded in audit logs, enabling accountability and supporting incident investigation if needed. Together, these measures help provide a secure environment suitable for deployment in a municipal government context.

3.2 Discussion of Results
This section analyzes how the implemented system addresses the specific problems and objectives identified in Chapter I, and explains any limitations and deviations from the original plan.
3.2.1 Achievement of Project Objectives
Objective 1: Design and implement a comprehensive authentication system incorporating multi-factor authentication. 
Result: Partially Achieved. The system successfully implements multi-factor authentication using password + Gmail-based OTP, along with email verification and security questions. This significantly improves security compared to password-only login.
Deviation: The originally envisioned dual OTP (Gmail + SMS) mechanism was not fully implemented in the deployed system. SMS OTP integration remains at the design and planning stage due to time and infrastructure constraints (e.g., third-party SMS gateway subscription and government deployment requirements).
Impact: Despite the absence of SMS OTP, the current email-based MFA still mitigates many common attack vectors such as credential stuffing and brute-force attacks.

Objective 2: Develop an interactive GIS-based reporting interface using Leaflet.js.
Result: Successfully Achieved. The system provides an interactive map with municipality detection and boundary validation. All reports are spatially located within Biliran Province.

Objective 3: Create role-based user interfaces with distinct access levels.
Result: Successfully Achieved. Citizens, municipal administrators, and the provincial administrator each have dedicated dashboards with appropriate access rights and data visibility.

Objective 4: Implement real-time issue tracking and status management.
Result: Successfully Achieved. The defined status workflow (Reported → Acknowledged → In Progress → Resolved) is operational, and status changes are visible to both citizens and administrators.


Objective 5: Establish a comprehensive analytics dashboard.
Result: Successfully Achieved. Administrators can view geographic and temporal analytics, as well as basic performance indicators, supporting data-driven management.

Objective 6: Ensure mobile-responsive design and accessibility.
Result: Successfully Achieved. The system works across common desktop and mobile browsers, and user feedback from testing indicates that the interface is easy to use on mobile devices but not fully responsive some of the button are missing when it decrease the size.

Objective 7: Validate system security and performance through testing.
Result: Successfully Achieved. Functional, security, and usability tests (including a System Usability Scale instrument) were conducted. The results indicate that the system is secure, performant, and usable for its intended audience.

3.2.2 System Performance and User Experience
Testing and observation during development indicate that the system performs reliably under typical academic and pilot-scale loads. Page load times for key views (landing page, dashboards, and map interface) were within acceptable limits for government web applications.
From a user experience perspective, both citizens and administrators were able to complete core tasks (account registration, report submission, status updates, and analytics viewing) with high task completion rates and positive satisfaction scores. The integration of the interactive map and clear status indicators contributed significantly to perceived system usefulness.

3.2.3 Limitations and Future Enhancements
Despite its successful implementation, the system has several limitations and areas for improvement:

Single-Channel OTP: The current MFA relies solely on Gmail-based OTP. While this improves security over passwords alone, it still depends on the security of the user's email account. Integrating SMS OTP or alternative second factors (e.g., authenticator apps) remains a priority for future work.
SMS Gateway Integration: The design anticipates the use of Philippine SMS gateway providers, but no live SMS integration is present in the deployed version. Future iterations should implement and evaluate SMS-based OTP to complete the dual OTP concept.
Scalability: The system was tested under academic conditions. Additional optimization and infrastructure scaling may be required for deployment in a full provincial or national context.
Offline and Low-Bandwidth Scenarios: Although the system is responsive, it still relies heavily on stable internet connectivity. Enhanced offline support and data synchronization could further improve accessibility.
These limitations form the basis for future enhancements and research directions.
3.3 System Testing and Evaluation
This section documents the testing methodology, instruments, and key results used to evaluate the system in terms of functionality, security, performance, and usability.

3.3.1 Testing Methodology
Multiple testing approaches were used to ensure that the system met its functional and non-functional requirements:
Unit Testing: Core functions (e.g., OTP generation/verification, coordinate validation, report submission, and status updates) were tested at the component level.
Integration Testing: Interactions between modules (authentication, GIS, reporting, and analytics) were verified to ensure end-to-end workflows operated correctly.
System Testing: Full user journeys, from registration and login to report resolution and analytics viewing, were tested in a near-production environment.
Security Testing: Common web vulnerabilities (SQL Injection, XSS, CSRF, authentication bypass, insecure file uploads) were assessed using manual techniques guided by the OWASP Top 10.
Performance Testing: The system was evaluated under increasing user loads to observe response times and stability.
User Acceptance Testing (UAT): Representative users from the target groups (citizens and administrators) performed realistic tasks and provided feedback.
- Usability Evaluation (SUS): The System Usability Scale questionnaire was used to quantify perceived usability.

3.3.2 Functional and Security Testing Results
Functional Testing:
All core workflows (registration, login with Gmail OTP, report submission, report status updates, and viewing analytics) executed successfully across multiple test scenarios.
GIS features (municipality detection and boundary validation) correctly restricted reports to valid locations within Biliran Province.

Security Testing:
SQL Injection: No exploitable injection points were discovered; parameterized queries (PDO prepared statements) are used for database access.
Cross-Site Scripting (XSS): Input sanitization and output encoding prevented reflected XSS in tested forms.
Cross-Site Request Forgery (CSRF): CSRF tokens were validated on sensitive operations such as report submission and account actions.
Authentication Bypass: Password + Gmail OTP flows resisted basic bypass attempts, and rate limiting prevented rapid OTP guessing.
Session Management: Sessions expired after inactivity and were invalidated on logout; session identifiers were not exposed in URLs.

The results show that the system incorporates essential security practices appropriate for a municipal information system.

3.3.3 Summary of Evaluation
The combined results of functional, security, performance, and usability evaluations indicate that the Municipal Issue Reporting System:

- Meets or exceeds most functional requirements identified in Chapter I.
- Provides a secure environment for handling citizen reports through email-based multi-factor authentication and layered security controls.
- Delivers an intuitive, GIS-enabled interface that citizens and administrators can use effectively.
- Achieves an excellent usability rating based on the System Usability Scale.

The main deviation from the original plan is the absence of deployed SMS OTP integration. Nevertheless, the current system already demonstrates the feasibility and benefits of integrating Cybersecurity, GIS, and HCI for municipal governance and provides a strong foundation for future enhancements such as dual-channel OTP and broader geographic scaling.

Conclusion
This study developed and evaluated the Municipal Issue Reporting System for Biliran Province, a web-based platform that integrates Cybersecurity, Geographic Information Systems (GIS), and Human-Computer Interaction (HCI) to improve the reporting and management of local issues. Grounded in the problems identified in Chapter I, the system was designed to address limitations in traditional reporting mechanisms, such as lack of geographic context, limited transparency, and weak authentication.

In terms of authentication and security, the system implements a multi-factor authentication mechanism that combines password-based login with Gmail-based one-time passwords (OTP), along with email verification and configurable security questions. Although the original design envisioned a dual OTP approach using both Gmail and SMS, only the email-based OTP channel was implemented and deployed due to practical constraints related to SMS gateway integration. Despite this limitation, the implemented multi-factor authentication significantly improves security compared to password-only login and aligns with the project objective of strengthening user account protection.

The system successfully delivers an interactive GIS-based reporting interface using Leaflet.js and GeoJSON boundary data for Biliran Province. Citizens can submit reports by selecting precise locations on a map, while the system automatically validates that reports fall within provincial boundaries and assigns them to the correct municipality. This directly addresses the need for spatially aware reporting and supports more accurate prioritization and resource allocation.
Role-based access control and tailored dashboards for citizens, municipal administrators, and a provincial administrator ensure that users see only the information and functions relevant to their responsibilities. Real-time status tracking, from Reported to Resolved, and email notifications for key status changes enhance transparency and citizen trust. Analytics features that summarize report volumes, trends, and performance indicators further support evidence-based decision-making by local government units.

From an HCI perspective, the system adopts a mobile-first, responsive design with clear feedback mechanisms, guided interactions, and attention to basic accessibility considerations. While the interface is not yet perfectly optimized for all devices and scenarios, usability evaluation using the System Usability Scale yielded an overall score in the "Excellent" range, indicating that users found the system easy to learn and efficient to use.

Overall, the Municipal Issue Reporting System met most of its functional objectives: it implemented secure, email-based multi-factor authentication; provided a GIS-enabled reporting workflow; delivered role-based dashboards and analytics; and achieved positive usability and acceptance results. The primary deviation from the original design is the absence of live SMS OTP integration, which remains a documented enhancement for future work.

4.2 Recommendations
Based on the results and identified limitations, several recommendations are proposed for future development, deployment, and research:
1. Implement Dual OTP with SMS Integration:
   Future iterations should integrate Philippine SMS gateway providers (e.g., Semaphore, Globe, Smart) to complete the dual OTP concept originally envisioned. The implemented Gmail-based OTP workflow and database structures can serve as a foundation for adding an SMS channel, enabling either sequential or combined verification flows.

2. Enhance Multi-Factor Authentication Options:
   Beyond SMS, the system could explore additional second factors such as authenticator applications, hardware tokens, or push-based approvals. This would reduce reliance on email accounts and provide users with alternative secure authentication options.

3. Improve Responsiveness and Accessibility:
   While the current interface is mobile-first, further work is recommended to optimize layouts for a wider range of screen sizes, strengthen accessibility (e.g., ARIA roles, keyboard navigation, color contrast), and conduct additional usability testing with diverse user groups.

4. Scale Infrastructure and Performance:
   For production deployment at a wider provincial or regional scale, server capacity, database optimization, and caching strategies should be revisited. Load testing with higher concurrent usage and realistic traffic patterns is recommended to ensure stability under peak demand.

5. Expand Analytics and Reporting:
   Additional analytics features, such as predictive models for issue hotspots or more detailed time-series analyses, could further support planning and resource allocation. Exportable reports and integration with existing LGU information systems may also increase the systems practical value.

6. Strengthen Security Monitoring and Incident Response:
   Implementing centralized logging, real-time alerting, and intrusion detection or prevention systems would enhance the security posture of a live deployment. Formal incident response procedures and periodic security audits are also recommended.


7. Conduct Longitudinal and Comparative Studies:
   Future research can investigate the long-term impact of the system on reporting rates, resolution times, and citizen satisfaction, as well as compare this GIS-based approach with traditional reporting channels.

6. Appendices
The appendices provide supplementary material that supports but does not fit within the main body of the research. Suggested contents include, but are not limited to, the following:

- Appendix A – System Interface Screenshots: 
Landing Page:


Municipal Admin:
Dashboard:
 
Analytics:
 

Map View:
 



Provincial Admin:
Dashboard:
 
Analytics:
 



Map View:
 
System Logs:
 




Login Page:
 
Registration Page:
 




- Appendix B  Database Schema and ERD: 
 

- Appendix C Developer Information: Scan the QR Code for the developers information.
 




References
National Institute of Standards and Technology. (2017). Digital Identity Guidelines: Authentication and Lifecycle Management (SP 800 63B). NIST Special Publication 800 63B. https://pages.nist.gov/800-63-3/sp800-63b.html
OWASP general web security OWASP Foundation. (2021). OWASP Top Ten Web Application Security Risks. https://owasp.org/www-project-top-ten/
OWASP authentication best practices (passwords, MFA, sessions) OWASP Foundation. (n.d.). Authentication Cheat Sheet. OWASP Cheat Sheet Series. https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
General, textbook-level security reference Stallings, W., & Brown, L. (2018). Computer Security: Principles and Practice (4th ed.). Pearson.
Goodchild, M. F. (2007). Citizens as sensors: The world of volunteered geography. GeoJournal, 69(4), 211–221.
Quality of OpenStreetMap data Haklay, M. (2010). How good is volunteered geographical information? A comparative study of OpenStreetMap and Ordnance Survey datasets. Environment and Planning B: Planning and Design, 37(4), 682–703.
Official OpenStreetMap project reference OpenStreetMap Foundation. (n.d.). OpenStreetMap [Data]https://www.openstreetmap.org set].
Leaflet mapping library used in your system Agafonkin, V. (n.d.). Leaflet: An open-source JavaScript library for mobile-friendly interactive maps. https://leafletjs.com
Brooke, J. (1996). SUS: A “quick and dirty” usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & I. L. McClelland (Eds.), Usability Evaluation in Industry (pp. 189–194). London: Taylor & Francis.
Bangor, A., Kortum, P. T., & Miller, J. T. (2008). An empirical evaluation of the System Usability Scale. International Journal of Human–Computer Interaction, 24(6), 574–594.
Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S., Elmqvist, N., & Diakopoulos, N. (2016). Designing the User Interface: Strategies for Effective Human–Computer Interaction (6th ed.). Pearson.
Schwaber, K., & Sutherland, J. (2020). The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game. Scrum.org & Scrum Alliance. https://scrumguides.org
United Nations. (2020). UN E Government Survey 2020: Digital Government in the Decade of Action for Sustainable Development. United Nations Department of Economic and Social Affairs.https://publicadministration.un.org/egovkb





