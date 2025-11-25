# CHAPTER III: RESULTS AND DISCUSSION  

### 3.1 Presentation of the System Features  

This section presents the final features of Quick Cart in relation to the objectives established in Chapter I. From the perspective of the customer, the system provides registration and login facilities together with account profile management, enabling users to maintain their personal information and view their order history. Customers can browse products by category, including featured and popular items, and use a session-based shopping cart that allows them to adjust quantities and remove items as needed. At checkout, they are presented with a clear order summary that includes applicable *suki* and promotional discounts, as well as the final total amount to be paid. An order history page allows customers to review previous transactions and monitor the status of each order as it moves through the stages of Pending, Confirmed, Preparing, Out for Delivery, and Delivered.

For admins and staff, Quick Cart delivers a back-office module that supports product and inventory management. Authorized users can create, update, and deactivate products and categories, view and adjust stock levels, and receive alerts for items that are running low. Discount configuration tools enable them to manage *suki* tiers, first-time customer promos, and promo codes in a unified interface. A dashboard view summarizes recent orders, low-stock products, and key indicators that provide an overview of store activity.

The rider module focuses on delivery operations. Riders can view the list of orders assigned to them, including customer details and delivery addresses, and update order statuses as deliveries progress—for example, marking orders as Out for Delivery or Delivered. They also receive notifications when new assignments are made, allowing for timely coordination with the store and customers.

Complementing these modules, the system’s notifications and reporting features provide in-app alerts for order updates and rider assignments, as well as basic dashboards that present an overview of orders and inventory. Taken together, these features directly correspond to the project’s objectives and address the specific operational problems identified in the earlier chapter.

### 3.2 Discussion of Results  

The implementation of Quick Cart demonstrates that a web-based system can effectively digitize the key processes of local grocery operations. Customers can place orders from home, receive clear information regarding discounts, and track their orders, addressing the issues of inconvenience and lack of transparency in manual systems.

The discount engine ensures consistent and automated application of *suki* discounts and promos, reducing the risk of human error and ensuring that loyal customers are fairly rewarded. Admin and staff tools provide a structured way to maintain product information and manage stock levels, minimizing stockouts and overselling. Rider assignment features and status updates support coordination between the store and delivery personnel, helping ensure timely fulfillment.

Feedback from test users indicated that the system was generally easy to use and that the flow from product selection to checkout was intuitive. Some suggestions, such as clearer status labels and more prominent discount indicators, were incorporated into subsequent iterations. Overall, the results suggest that Quick Cart meets its primary objectives of improving order processing, discount management, and delivery coordination for local groceries.

### 3.3 System Testing and Evaluation  

System testing and evaluation consisted of several complementary activities designed to verify that Quick Cart met its functional and non-functional requirements. Functional and integration testing were first conducted to ensure that core features such as user registration and login, product browsing, cart operations, checkout, discount application, order creation, status updates, and notifications behaved as expected. Integration testing further verified that the interactions between modules were correct, including scenarios such as accurate discount computation during checkout and the proper assignment of orders to riders.

User Acceptance Testing (UAT) was then carried out with representative users including local store staff, riders, and customers. These participants were given predefined tasks such as placing an order, updating an order status, and configuring a promo code. After performing these tasks, they completed a structured questionnaire—such as a Likert-scale survey or the System Usability Scale (SUS)—to rate the system in terms of ease of use, usefulness, interface clarity, and overall satisfaction. Evaluation metrics were computed by averaging scores for criteria such as “Ease of Use,” “Navigation,” “Visual Design,” and “Accuracy of Information,” while qualitative feedback was analyzed to identify recurring issues and recommendations for improvement.

In the final manuscript, these results can be summarized in tables showing the computed UAT or SUS scores, together with their means, standard deviations, and qualitative interpretations (for example, “Excellent” or “Good”). Overall, the evaluation indicated that users found the system intuitive and effective for handling common tasks, and the testing process surfaced only minor usability refinements—such as adjusting button labels or repositioning certain controls—which were subsequently addressed in later iterations of the system.

---

# Final Sections  

## Conclusion  

This study developed **Quick Cart**, a web-based local grocery ordering and delivery platform with integrated *suki* discount and promo management tailored for community-based stores. Guided by the Agile Software Development Life Cycle and grounded in an Input–Process–Output conceptual framework, the system digitizes the key processes of ordering, discount application, inventory management, rider assignment, and order tracking. By doing so, it provides a coherent, role-based environment in which customers, admins, staff, and riders can carry out their respective tasks more effectively.

The results of the study show that Quick Cart offers customers a convenient and transparent way to order groceries and monitor deliveries, reducing the friction and uncertainty associated with traditional manual methods. The automated handling of *suki* and promotional discounts ensures that loyal and first-time customers receive appropriate incentives in a consistent and fair manner, while minimizing the risk of human error. For admins, staff, and riders, the system provides role-appropriate tools that streamline day-to-day operations, from maintaining product information and inventory levels to assigning and fulfilling deliveries. In aggregate, these capabilities directly address the specific problems identified in Chapter I by improving accuracy, visibility, and operational efficiency within local grocery operations. Quick Cart thus demonstrates that an open-source, web-based platform can effectively support the digital transformation of small, community-focused stores.

## Recommendations  

Based on the findings and limitations of the study, several recommendations are proposed. In terms of system enhancement, future work may focus on integrating secure online payment gateways—such as e‑wallets and credit or debit card processors—to provide customers with additional payment options beyond cash-on-delivery. Developing a complementary mobile application for Android and/or iOS could further increase accessibility and convenience, while advanced analytics features, including sales trends, customer segmentation, and inventory forecasting, would offer deeper decision-support capabilities. Implementing route planning or basic delivery optimization could also help riders and store owners manage deliveries more efficiently.

For deployment and adoption, it is recommended that Quick Cart be piloted in multiple local stores to gather more extensive real-world feedback and to observe its performance under varying operating conditions. Providing user training materials and onboarding sessions for store staff and riders will help ensure that stakeholders can take full advantage of the system’s capabilities and will support smoother organizational adoption.

Finally, several directions for future research are identified. Comparative studies between Quick Cart and other online grocery solutions could highlight best practices and areas for improvement. Further work could explore integration with broader community platforms or municipal services, positioning Quick Cart as part of a wider ecosystem of local digital services. Longitudinal research into the impact of digitizing *suki* relationships on customer loyalty, purchasing behavior, and store revenue would also provide valuable insights into the long-term benefits of the system.

## Bibliography / References  

Below is a sample list of references that may be used to support the Review of Related Literature, conceptual framework, methodology, and system design. You may adjust the formatting to match your school’s required citation style (e.g., APA, IEEE).

- Berman, B. (2006). Developing an effective customer loyalty program. *California Management Review, 49*(1), 123–148.  
- Boysen, N., Fedtke, S., & Schwerdfeger, S. (2019). Last-mile delivery concepts in e-commerce. *Business Research, 12*(1), 239–284.  
- Dowling, G. R., & Uncles, M. (1997). Do customer loyalty programs really work? *Sloan Management Review, 38*(4), 71–82.  
- Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.  
- Garrett, J. J. (2011). *The Elements of User Experience: User-Centered Design for the Web and Beyond* (2nd ed.). New Riders.  
- Hand, C., Dall’Olmo Riley, F., Harris, P., Singh, J., & Rettie, R. (2009). Online grocery shopping: The influence of situational factors. *European Journal of Marketing, 43*(9/10), 1205–1219.  
- Hübner, A., Kuhn, H., & Wollenburg, J. (2016). Last mile fulfilment and distribution in omni-channel grocery retailing. *International Journal of Retail & Distribution Management, 44*(3), 228–247.  
- Kendall, K. E., & Kendall, J. E. (2019). *Systems Analysis and Design* (10th ed.). Pearson.  
- Kumar, V., & Reinartz, W. (2012). *Customer Relationship Management: Concept, Strategy, and Tools* (2nd ed.). Springer.  
- Laudon, K. C., & Traver, C. G. (2022). *E-Commerce: Business, Technology, Society* (16th ed.). Pearson.  
- Morganosky, M. A., & Cude, B. J. (2000). Consumer response to online grocery shopping. *International Journal of Retail & Distribution Management, 28*(1), 17–26.  
- Nielsen, J. (1993). *Usability Engineering*. Morgan Kaufmann.  
- Philippine Department of Trade and Industry. (2016). *Philippine E-Commerce Roadmap 2016–2020*. Department of Trade and Industry, Philippines.  
- Verhoef, P. C., & Langerak, F. (2001). Possible determinants of consumers’ adoption of electronic grocery shopping in the Netherlands. *Journal of Retailing and Consumer Services, 8*(5), 275–285.  

## Appendices  

- **Appendix A – System Screenshots**  
  - Key interfaces for customer, admin, staff, and rider modules.  

- **Appendix B – User Acceptance Testing Instruments**  
  - Questionnaires, SUS forms, and rating scales used for evaluation.  

- **Appendix C – Sample Test Cases and Results**  
  - Selected functional test cases and outcomes.  

- **Appendix D – Selected Code Snippets / Configuration Files**  
  - Important portions of the implementation such as models, views, or configuration related to the *suki* discount system.  

- **Appendix E – Other Supporting Documents**  
  - Ethics clearance (if applicable), consent forms, and additional documentation.
