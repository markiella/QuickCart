# Preliminaries and Chapter I

## Title Page

**Quick Cart: A Web-Based Local Grocery Ordering and Delivery Platform with Suki Discount System**

A Capstone Project Presented to  
the Faculty of the **[Department/College]**  
**[Name of School / University]**  

In Partial Fulfillment of the Requirements  
for the Degree **[Name of Degree Program]**  

by  

**[Student Name 1]**  
**[Student Name 2]**  
**[Student Name 3]**  

**[Month Year]**

---

## Abstract

This study presents **Quick Cart**, a web-based local grocery ordering and delivery platform designed for community-based grocery and sari-sari stores. Many neighborhood stores still rely on manual processes for order taking, inventory monitoring, discount application, and delivery coordination. These practices often lead to inaccurate orders, delayed fulfillment, and a lack of formal loyalty programs such as the traditional Filipino *“suki”* system. The project aims to address these issues by developing an integrated system that digitizes ordering, discounts, and delivery workflows.

Quick Cart was developed using the Agile software development life cycle. Requirements were gathered from local store owners, riders, and customers, followed by iterative design, implementation, and testing cycles. The system is implemented using Django 5, a custom user model for role-based access (Admin, Staff, Rider, and Customer), and a session-based cart. It features an online product catalog, checkout with discount computation, an automated *suki* loyalty mechanism, promo code management, staff and rider dashboards, and in-app notifications. A database seeding tool populates sample products, categories, and discount rules, while an image generation command integrates with the Pexels API to generate product images.

Evaluation was conducted through functional testing and user acceptance testing (UAT) with representative users. Results indicated that the system streamlined order processing, enhanced transparency of order statuses, and improved customer experience through automated discounts and clear delivery tracking. Based on the findings, the researchers conclude that Quick Cart effectively addresses the identified problems and can serve as a practical solution for small local groceries transitioning to digital operations, with potential for further enhancements such as online payments and mobile applications.

**Keywords:** Quick Cart, online grocery, suki discount, web-based system, Django, local delivery

---

## Table of Contents (Skeleton)

- **Preliminaries**  
  - Title Page  
  - Abstract  
  - Table of Contents  
  - List of Figures  
  - List of Tables  

- **Chapter I – The Problem and Its Background**  
  - 1.1 Project Context and Introduction  
  - 1.2 Statement of the Problem  
  - 1.3 Objectives of the Study  
  - 1.4 Scope and Delimitations  
  - 1.5 Review of Related Literature and Studies  
  - 1.6 Conceptual / Theoretical Framework  
  - 1.7 Definition of Terms  

- **Chapter II – Methodology and System Design**  
  - 2.1 Project Methodology  
  - 2.2 Technical System Architecture  
  - 2.2.1 System Environment (Hardware and Software Requirements)  
  - 2.3 System Modeling and Blueprints  
  - 2.4 Implementation Procedures  

- **Chapter III – Results and Discussion**  
  - 3.1 Presentation of the System Features  
  - 3.2 Discussion of Results  
  - 3.3 System Testing and Evaluation  

- **Final Sections**  
  - Conclusion  
  - Recommendations  
  - Bibliography / References  
  - Appendices  

---

## List of Figures (Sample Placeholders)

- Figure 1. Conceptual Framework (Input–Process–Output Model)  
- Figure 2. Context Diagram of Quick Cart  
- Figure 3. Level 0 Data Flow Diagram  
- Figure 4. Sample Wireframe of Customer Home Page  
- Figure 5. Sample Wireframe of Admin Dashboard  
- Figure 6. Entity–Relationship Diagram of Quick Cart Database  

## List of Tables (Sample Placeholders)

- Table 1. Summary of System Requirements  
- Table 2. Description of Main Database Tables  
- Table 3. User Acceptance Testing Results (Mean Scores per Criterion)  
- Table 4. Summary of System Usability Scale Scores  

---

# CHAPTER I: THE PROBLEM AND ITS BACKGROUND  

### 1.1 Project Context and Introduction  

Local grocery and sari-sari stores play a critical role in Filipino communities by providing daily necessities within walking distance. However, many of these stores still operate using manual processes: customers order in person or through informal chat messages, staff record orders in notebooks, and deliveries are coordinated by phone without systematic tracking. These practices can result in lost orders, inaccurate computations, and difficulties in monitoring regular customers who deserve *suki* discounts.

The rapid growth of e-commerce and on-demand delivery services has set new expectations for convenience, transparency, and speed. Yet, small local stores often lack the technical capacity and resources to adopt complex commercial platforms. There is a need for a lightweight, community-focused solution that digitizes ordering, inventory, and loyalty management while remaining simple enough for non-technical store owners and riders to use.

Quick Cart addresses this gap by providing a **web-based local grocery ordering and delivery system** with integrated *suki* discounts and promo codes. The system allows customers to browse products, manage a shopping cart, apply eligible discounts, and track orders, while admins, staff, and riders manage inventory, orders, and deliveries through role-specific dashboards. By automating these processes, Quick Cart aims to improve service quality for customers and operational efficiency for local stores.

### 1.2 Statement of the Problem  

#### General Problem  

How can a web-based system be designed and implemented to streamline grocery ordering, delivery, and loyalty discount management for local community stores in order to improve accuracy, transparency, and customer satisfaction?

#### Specific Problems  

The study seeks to address several specific problems that arise in the current ordering and delivery workflow of local groceries. First, customers lack a unified, web-based platform where they can conveniently browse products, add items to a cart, and place orders at their preferred time. Second, there is no automated and consistent way to compute and apply *suki* discounts, first-time customer promos, and promo codes during checkout, which can lead to errors and inconsistencies. Third, admins and staff do not have a centralized tool for efficiently managing products, inventory levels, and discount configurations, making day-to-day operations more difficult to monitor and control.

Fourth, there is no structured mechanism for admins to assign orders to specific riders and for riders to update delivery statuses in real time, resulting in fragmented coordination and possible delivery delays. Fifth, customers cannot easily track the status of their orders from placement to delivery and therefore have limited visibility into the fulfillment process. Sixth, store owners lack consolidated reports and dashboards that summarize orders, stock levels, and customer activity, limiting their ability to make informed, data-driven decisions about their business.

### 1.3 Objectives of the Study  

#### General Objective  

To develop and evaluate **Quick Cart**, a web-based local grocery ordering and delivery platform with integrated *suki* discount and promo management for community-based stores.

#### Specific Objectives  

The study specifically aims to achieve several concrete objectives in the development and evaluation of Quick Cart. First, it seeks to design and implement a web-based customer interface for browsing products, managing a cart, and placing orders. Second, it aims to develop a rule-based discount engine that automatically applies *suki* discounts, first-time customer promos, and promo codes at checkout so that discount application becomes consistent and transparent.

Third, the study intends to provide admin and staff modules for managing products, categories, inventory, and discount configurations in a centralized environment. Fourth, it strives to implement an order assignment and tracking module where admins assign orders to riders and riders update delivery statuses in real time. Fifth, it aims to enable customers to monitor their order status and receive notifications regarding key order updates. Sixth, it aims to evaluate the system through functional testing and user acceptance testing to determine its usability and effectiveness in addressing the identified problems.

### 1.4 Scope and Delimitations  

#### Scope  

The scope of this study covers four primary user groups within a local community grocery context: admins, staff, riders, and customers. Admins are responsible for managing users, products, discounts, and overall order oversight. Staff members assist in processing orders and updating inventory records, ensuring that product availability is accurately reflected in the system. Riders receive assigned orders and are accountable for updating delivery statuses as orders move from preparation to completion. Customers use the system to browse products, place orders, and track the progress of their deliveries.

In terms of functionality, the Quick Cart system includes an online product catalog with categories and featured items, a session-based shopping cart that supports both guest and logged-in users, and a checkout process that captures delivery details and automatically computes applicable discounts. The scope also encompasses *suki* loyalty discounts based on customer order history, first-time customer promos and configurable promo codes, as well as an admin and staff dashboard for managing products, orders, and discount configurations. In addition, a rider module is provided for viewing and updating assigned orders, while in-app notifications inform users about important events such as order updates and assignments. Supporting tools, such as database seeding and product image generation via management commands, are also included within the scope of the system.

#### Delimitations  

The study is delimited to operations within a local community service area and does not include complex route optimization or multi-city logistics. The current implementation focuses on cash-on-delivery or comparable offline payment methods; integration with online payment gateways such as e-wallets and credit card processors is beyond the scope of this project. Likewise, the system is implemented purely as a web-based application, and the design and development of native mobile applications are not covered in this study.

Furthermore, the analytics provided by Quick Cart are limited to basic dashboard summaries rather than advanced predictive forecasting or business intelligence. The evaluation of the system is based on controlled testing and a limited set of user participants, and therefore does not yet reflect large-scale, long-term deployment across multiple stores or communities.

### 1.5 Review of Related Literature and Studies  

The review of related literature focuses on four main areas relevant to Quick Cart: online grocery and e‑commerce systems, last‑mile delivery and order management, loyalty programs and the Filipino *suki* concept, and the digitalization of small retailers using web-based platforms. Together, these strands of research provide the theoretical and empirical foundation for the design of a local grocery ordering and delivery system.

#### Online Grocery and E‑Commerce Systems  

Early work on online grocery shopping emphasized the role of convenience and time savings in motivating consumers to shift away from purely in‑store purchasing. Morganosky and Cude (2000) found that online grocery services are particularly attractive to households constrained by time, mobility, or caregiving responsibilities. Verhoef and Langerak (2001) identified perceived usefulness, ease of use, and trust in the online retailer as important determinants of adoption in the Netherlands, highlighting that reliability of delivery and transparency of pricing are critical. Hand et al. (2009) further showed that situational factors, such as having young children or irregular work schedules, increase the likelihood that customers will adopt online grocery shopping.

More recent perspectives situate online grocery within a broader e‑commerce landscape. Laudon and Traver (2022) describe how successful e‑commerce platforms integrate secure authentication, clear product information, and mobile‑friendly interfaces to support customer trust and satisfaction. However, many of the commercial systems discussed in the literature are designed for large supermarket chains with extensive resources and standardized logistics. There is comparatively limited attention to lightweight solutions tailored for small, community-based groceries, particularly in developing countries such as the Philippines. Quick Cart responds to this gap by offering a focused set of features—product browsing, cart management, checkout, and order tracking—built on open-source technologies.

#### Delivery Management and Order Tracking  

The “last mile” between the store and the customer is one of the most challenging components of e‑commerce operations. Hübner, Kuhn, and Wollenburg (2016) noted that omni-channel grocery retailers must balance delivery reliability with cost efficiency, especially for perishable goods that require timely fulfillment. Boysen, Fedtke, and Schwerdfeger (2019) surveyed last‑mile delivery concepts and observed that many proposed optimization approaches assume sophisticated logistics infrastructures and specialized fleets which may not be realistic for small local stores. In community contexts, deliveries are often handled by a small number of riders using motorcycles or bicycles, with assignments coordinated manually.

These studies underscore the importance of clear order statuses and simple coordination mechanisms between store personnel and riders. Instead of complex routing algorithms, systems like Quick Cart prioritize practical features such as assigning orders to specific riders, updating delivery status in real time, and providing customers with transparent status indicators (e.g., Pending, Preparing, Out for Delivery, Delivered). This aligns with the literature’s recommendation to adapt last‑mile solutions to the scale and capabilities of the organization rather than attempting to replicate large‑scale logistics platforms.

#### Loyalty Programs and the *Suki* Concept  

Formal loyalty programs have been widely analyzed as tools for increasing customer retention and purchase frequency. Dowling and Uncles (1997) highlighted that not all loyalty schemes are effective; poorly designed programs can increase costs without producing meaningful behavior change. Sharp and Sharp (1997), however, showed that well-structured loyalty programs can modestly strengthen repeat‑purchase patterns when rewards are simple, visible, and consistently applied. Berman (2006) stressed that loyalty initiatives must align with customer expectations and the financial realities of the business, while Kumar and Reinartz (2012) situate loyalty programs within broader customer relationship management strategies that use transaction histories to tailor incentives.

In the Philippine setting, the traditional *“suki”* relationship between store owners and regular customers functions as an informal, culturally embedded loyalty system. Regular patrons often receive small discounts, better credit terms, or priority service based on personal familiarity rather than formal rules. This informality can make it difficult to track who qualifies for benefits, particularly when staff members change or multiple branches are involved. By codifying *suki* tiers and first-time customer promotions in software, Quick Cart translates this cultural practice into a rule‑based discount engine. This allows loyalty benefits to be applied automatically based on order history while preserving the spirit of the *suki* relationship discussed in the literature on loyalty programs.

#### Web-Based Systems for Small and Medium Enterprises  

Several studies and policy documents emphasize that small and medium enterprises (SMEs) face distinct challenges in adopting digital systems compared to large corporations. Issues such as limited capital, lack of in‑house IT expertise, and difficulty integrating point‑of‑sale, inventory, and online channels are commonly reported. The Philippine Department of Trade and Industry, through the *Philippine E‑Commerce Roadmap 2016–2020*, advocates for the digitalization of micro, small, and medium enterprises (MSMEs) to expand market reach and improve efficiency. Yet, many recommended approaches rely on joining general‑purpose marketplaces rather than deploying store‑owned platforms.

Academic texts on systems analysis and design, such as Kendall and Kendall (2019), as well as Pressman and Maxim (2020), underscore that solutions for SMEs must be aligned with their specific processes and resource constraints to ensure adoption. In this regard, Quick Cart’s use of Django, a relational database, and a role‑based modular design represents a practical application of these principles: the system is scoped to the needs of local groceries, supports clear workflows for admins, staff, riders, and customers, and can be hosted on modest infrastructure. This positions Quick Cart as a feasible digitalization pathway for small community stores that cannot afford enterprise‑level platforms.

### 1.6 Conceptual / Theoretical Framework  

This study is anchored on the **Input–Process–Output (IPO) model** and the **Agile Software Development Life Cycle**.

- **Inputs**  
  - Customer data (profiles, order history)  
  - Product and category information  
  - Discount configurations (*suki* tiers, first-time promos, promo codes)  
  - Order details (items, quantities, delivery address)  

- **Process**  
  - User authentication and role-based access control  
  - Product browsing, searching, and cart management  
  - Discount computation using predefined business rules  
  - Order creation, assignment to riders, and status updates  
  - Notification generation for order and delivery events  
  - Data storage and retrieval for reporting and dashboards  

- **Outputs**  
  - Confirmed and trackable customer orders  
  - Updated inventory and discount application records  
  - Order and delivery status updates visible to stakeholders  
  - Summary reports and dashboard views for admins and staff  

The Agile SDLC underlies the development approach, emphasizing iterative requirements gathering, prototyping, development, and testing. Feedback from prospective users (store owners, staff, and customers) informs successive iterations to refine functionality and user experience.

*(Figure 1 may illustrate the IPO model showing the relationships among inputs, processes, and outputs.)*

### 1.7 Definition of Terms  

- **Quick Cart** – The proposed web-based local grocery ordering and delivery system developed in this study.  
- **Suki** – A Filipino term referring to a regular customer who receives preferential treatment or discounts due to loyalty.  
- **Suki Discount** – A loyalty-based discount automatically applied to customers who meet predefined order history thresholds.  
- **First-Time Customer Promo** – A promotional discount given to customers placing their first order in the system.  
- **Promo Code** – A code that customers enter during checkout to receive special discounts subject to defined conditions.  
- **Session-Based Cart** – A mechanism that stores cart contents in the user’s session, supporting both guest and authenticated customers.  
- **Admin** – A user role with full access to manage products, discounts, users, and overall system settings.  
- **Staff** – A user role responsible for assisting with order processing and inventory management.  
- **Rider** – A user role responsible for delivering orders and updating delivery statuses.  
- **User Acceptance Testing (UAT)** – A testing activity where actual or representative users evaluate the system based on defined criteria and tasks.  
- **Entity–Relationship Diagram (ERD)** – A diagram that visually represents the entities in the database and their relationships.  
