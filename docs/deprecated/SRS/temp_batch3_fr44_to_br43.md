## 7.12 Notifications

#### FR-44: In-app Notifications (P0)
**Requirement**: The system SHALL provide real-time in-app notifications for all critical user events and interactions.

**Notification Categories**:
| Category | Trigger Events | Delivery Method |
|----------|---------------|-----------------|
| **Offers & Transactions** | Offer received, counter-offer, acceptance, rejection, transaction step completion | Real-time push + in-app inbox |
| **Communication** | New message, appointment request, appointment confirmation/cancellation | Real-time push + badge count |
| **Verification** | Verification approved/rejected, documents requested, badge issued | In-app inbox + email |
| **Payments** | Payment successful, payment failed, refund processed, milestone payment due | Real-time push + in-app + email |
| **Listings** | Listing published, listing requires changes, price alert (saved searches) | In-app inbox |
| **Reviews** | Review received, response posted, dispute opened | In-app inbox + email |

**Notification Features**:
- Real-time push notifications (WebSocket or similar)
- In-app notification center with unread count
- Notification grouping (e.g., "3 new messages from Agent Rakib")
- Mark as read/unread
- Notification history (30 days retention minimum)
- Action buttons (e.g., "View Offer", "Respond Now")

**Details**:
- The system SHALL deliver notifications within 5 seconds of event trigger
- The system SHALL allow users to configure notification preferences per category
- The system SHALL respect "Do Not Disturb" hours (user-configurable)
- The system SHALL provide notification sound/vibration options

**Business Value**: Real-time notifications keep users engaged and reduce response delays, directly improving transaction completion rates.

**Acceptance Criteria**:
- Notifications delivered within 5 seconds
- Unread badge count displayed accurately
- Users can configure preferences for each category
- Notification history accessible for 30+ days
- Action buttons work correctly (deep linking)

---

#### FR-45: SMS/Email Notifications (P1)
**Requirement**: The system SHOULD send SMS and email notifications for critical events requiring immediate attention.

**Critical Events Requiring SMS/Email**:
| Priority | Event | Channels |
|----------|-------|----------|
| **High** | Payment confirmation, Verification approved, Appointment reminder (2 hours before) | SMS + Email |
| **Medium** | Offer received, Transaction milestone complete, Dispute opened | Email |
| **Low** | Weekly digest (saved search matches), New features announcement | Email only |

**SMS Notification Rules**:
- Maximum 3 SMS per day per user (except security alerts)
- SMS sent only for events marked "urgent" by user preferences
- SMS must include short message + link to app/web
- Opt-out option provided in all SMS

**Email Notification Rules**:
- Professional email templates with brand styling
- Clear subject lines (e.g., "Your offer for Banani Apartment was accepted")
- Email includes full event details + action buttons
- Unsubscribe link in footer (except mandatory security emails)

**Details**:
- The system SHALL use SMS gateway with 95%+ delivery rate
- The system SHALL track delivery status (sent, delivered, failed)
- The system SHALL retry failed SMS/emails with exponential backoff
- The system SHALL maintain opt-out preferences across all channels

**Business Value**: Multi-channel notifications ensure critical information reaches users even when not actively using the app.

**Acceptance Criteria**:
- SMS delivered within 30 seconds for high-priority events
- Email delivered within 5 minutes
- Delivery status tracked and visible to operations
- Opt-out preferences honored immediately
- Failed deliveries logged and retried

---

## 7.13 Contacts, Community & Content (P2)

> **Note**: This section covers P2 (future enhancement) features. Data models and permissions defined now to avoid rework in future releases.

#### FR-46: Search (P2)
**Requirement**: The system SHOULD provide comprehensive search across social features including groups, pages, posts, people, and professional services.

**Search Scope**:
- Groups/Communities (e.g., "Gulshan Residents", "Property Investors BD")
- Pages (Business pages, Real estate company pages)
- Posts (Community discussions, market insights)
- People (Connect with buyers, sellers, agents in your area)
- Professional Services (Advanced filtering beyond FR-36, FR-39)

**Business Value**: Social search creates network effects and community engagement, increasing platform stickiness.

---

#### FR-47: Groups/Pages/Posts (P2)
**Requirement**: The system SHOULD support social community features including group creation, page following, and content posting with moderation.

**Key Features**:
- Create/join groups (public, private, verified-only)
- Follow business pages
- Like, comment, share posts
- Moderation queue for reported content
- Admin controls for group owners

**Business Value**: Community features transform platform from transactional marketplace to engaged community, increasing retention.

---

#### FR-48: View Blogs & Videos (P2)
**Requirement**: The system SHOULD provide curated content hub with educational blogs and videos.

**Content Categories**:
- Property buying guides
- Legal process explanations
- Financing options
- Market trends and insights
- Success stories

---

#### FR-49: Post Blogs & Videos (P2)
**Requirement**: The system SHOULD allow verified professionals to contribute moderated content.

**Contributor Requirements**:
- Professional verified status
- Platform approval for content contributor role
- All content moderated before publication

---

#### 7.13.1 Contacts & Networking

**Connection Model**:
- **Follow** (one-way): For agents, companies, pages
- **Connect** (two-way): Person-to-person networking (optional)

**Privacy Controls**:
- Profile visibility levels (public/registered/contacts-only)
- Contact request approvals
- Block/unblock functionality

**Discovery**:
- "People you may know" based on shared area, shared groups
- No heavy ML required for MVP

---

## 7.14 Admin & Moderation

#### FR-50: Admin Console (P0)
**Requirement**: The system SHALL provide comprehensive admin console for platform management and operations.

**Admin Console Modules**:

| Module | Key Functions | Access Level |
|--------|--------------|--------------|
| **User Management** | View users, suspend/ban accounts, reset passwords, merge duplicates | Super Admin |
| **Verification Queue** | Review verification requests, approve/reject with reasons | Verifier |
| **Listing Management** | Review listings, publish/reject, handle reported listings | Moderator |
| **Transaction Monitoring** | View all transactions, dispute resolution, refund approvals | Finance Team |
| **Payment Reconciliation** | Daily reconciliation reports, mismatch resolution | Finance Team |
| **Content Moderation** | Review reported posts, messages, reviews | Moderator |
| **Analytics Dashboard** | Platform metrics, user growth, revenue, conversion rates | Super Admin, Analysts |
| **System Configuration** | Platform settings, feature flags, business rules | Super Admin |

**Key Features**:
- Role-based access control (RBAC) with granular permissions
- Audit logging for all admin actions
- Bulk operations (e.g., bulk verify, bulk approve)
- Advanced search and filtering
- Export capabilities (CSV, Excel, PDF)
- Real-time dashboard with KPIs

**Details**:
- The system SHALL log every admin action with user ID, timestamp, and action details
- The system SHALL enforce multi-factor authentication for admin accounts
- The system SHALL provide admin activity reports for compliance
- The system SHALL restrict sensitive operations (ban user, refund) to Super Admins

**Business Value**: Comprehensive admin tools enable efficient platform operations and ensure quality control. Audit trails support compliance and dispute resolution.

**Acceptance Criteria**:
- All modules accessible based on user role
- Every action logged with full audit trail
- Search and filter work across all modules
- Export functions generate accurate reports
- Dashboard loads within 3 seconds

---

#### FR-51: Audit Logs (P0)
**Requirement**: The system SHALL maintain comprehensive, tamper-proof audit logs for all verification and payment events.

**Audit Log Categories**:

**Verification Events**:
- Verification request submitted (user, type, documents)
- Verification reviewed (verifier, decision, reason)
- Badge issued/revoked (admin, user affected, badge type)
- Document access granted/denied (requester, owner, documents)

**Payment Events**:
- Payment initiated (user, amount, method, order ID)
- Payment completed/failed (gateway response, transaction ID)
- Refund initiated/completed (admin, user, amount, reason)
- Payment hold placed/released (reason, admin, amount)

**Transaction Events**:
- Offer submitted/countered/accepted
- Transaction step completed
- Proof document uploaded
- Transaction disputed/resolved

**Audit Log Requirements**:
- **Immutability**: Logs cannot be edited or deleted
- **Retention**: Minimum 7 years (compliance requirement)
- **Access Control**: View-only access with strict permissions
- **Search**: Full-text search with advanced filters
- **Export**: Audit reports exportable for compliance

**Log Entry Format**:
```json
{
  "id": "uuid",
  "timestamp": "ISO 8601",
  "actor": "user_id or system",
  "action": "verification_approved",
  "resource_type": "verification_request",
  "resource_id": "VER-12345",
  "details": {
    "decision": "approved",
    "verification_type": "identity",
    "documents_reviewed": ["NID", "Selfie"]
  },
  "ip_address": "masked",
  "user_agent": "browser info"
}
```

**Business Value**: Comprehensive audit logs are essential for dispute resolution, fraud investigation, and regulatory compliance. Immutability ensures trust in platform records.

**Acceptance Criteria**:
- All critical events logged automatically
- Logs immutable and tamper-proof
- Search and filter work efficiently (< 3 seconds for 1M+ records)
- Audit reports exportable in multiple formats
- Retention policy enforced automatically

---

## 7.15 Transparency, Guides & FAQs

#### FR-52: Ownership Verification Guide UI (P0)
**Requirement**: The system SHALL provide step-by-step interactive guides for sellers on ownership verification process.

**Guide Features**:
- **Interactive Checklist**: Step-by-step workflow with progress tracking
- **Document Requirements**: Clear list of required documents per property type
- **Upload Guidance**: File format, size, quality requirements
- **Common Issues**: FAQ addressing typical verification problems
- **Verification Timeline**: Expected review time with status updates
- **Support Contact**: Quick access to verification support team

**Guide Integration**:
- Accessible from listing creation page
- Contextual help tooltips during document upload
- Email reminders with guide link for pending verifications

**Business Value**: Clear guidance reduces verification submission errors and speeds up the verification process, improving user satisfaction.

---

#### FR-53: Legal & Loan Guides (P1)
**Requirement**: The system SHOULD provide educational content explaining legal and financial processes.

**Legal Guides**:
- **Bayna Process**: What is Bayna, when to sign, what to include
- **Dalil Registration**: Sub-Registrar process, required documents, stamp duty calculation
- **Namjari/Mutation**: Application process, required forms, timeline expectations
- **Land Tax Payment**: Where to pay, how to calculate, payment proof

**Loan Guides**:
- **Home Loan Basics**: Eligibility, required documents, typical interest rates
- **Loan Application Process**: Step-by-step from application to disbursement
- **EMI Calculator Guide**: How to use, understanding affordability
- **Loan Comparison**: How to compare offers from multiple banks

**Implementation**:
- CMS-backed content for easy updates
- PDF download option
- Video tutorials for complex processes
- Contextual links from transaction steps

**Business Value**: Educational content reduces user anxiety and support burden while building platform authority as trusted advisor.

---

#### FR-54: FAQ Templates (P1)
**Requirement**: The system SHOULD allow sellers/agents to attach frequently asked questions to listings.

**Common FAQ Categories**:
- **Financial**: Service charge, maintenance fees, utility costs, booking money/deposit
- **Property Details**: Facing direction, parking availability, generator backup
- **Handover**: Possession date, handover process, utility transfer
- **Building Amenities**: Gym, pool, community hall, security features
- **Legal**: Ownership status, NOC status, building approval

**Features**:
- Pre-defined FAQ templates by property type
- Custom Q&A addition
- FAQ displayed prominently on listing page
- FAQ searchable from listing search

**Business Value**: FAQ reduces repetitive inquiries, saves time for agents, and provides buyers with quick answers.

---

#### FR-55: Cost Transparency Fields (P1)
**Requirement**: The system SHOULD capture and display all known property-related costs with clear labeling of unknown fields.

**Cost Categories**:

| Cost Type | Frequency | Example | Label if Not Provided |
|-----------|-----------|---------|----------------------|
| **Service Charge** | Monthly | BDT 8,000/month | "Not disclosed by seller" |
| **Maintenance Fee** | Monthly/Yearly | BDT 50,000/year | "Not disclosed by seller" |
| **Booking Money** | One-time | BDT 3,00,000 | "To be negotiated" |
| **Utility Deposit** | One-time | BDT 20,000 | "Not disclosed by seller" |
| **Registration Fee** | One-time | BDT 1,50,000 (estimated) | "Estimated, verify with Sub-Registrar" |
| **Property Tax** | Yearly | BDT 15,000/year | "Not disclosed by seller" |

**Display Rules**:
- All cost fields visible on listing detail page
- Unknown costs clearly labeled (never hidden)
- Estimated costs shown with disclaimer
- Total ownership cost calculator (optional P1 feature)

**Business Value**: Cost transparency builds trust and reduces disputes. Clear labeling of unknown costs sets proper expectations.

---

## 7.16 Safety, Abuse Reporting & Disputes

#### FR-56: Report Listing/User (P0)
**Requirement**: The system SHALL provide comprehensive reporting mechanism for fraudulent or inappropriate content.

**Report Categories**:

| Category | Applies To | Examples |
|----------|------------|----------|
| **Fraud** | Listings, Users | Fake ownership, non-existent property, impersonation |
| **Spam** | Listings, Messages, Users | Duplicate listings, spam messages, bot accounts |
| **Harassment** | Messages, Reviews, Users | Abusive language, threats, stalking |
| **Inappropriate Content** | Posts, Photos, Reviews | Offensive images, hate speech, adult content |
| **Misrepresentation** | Listings | Wrong photos, incorrect price, misleading description |
| **Scam/Phishing** | Messages, External Links | Fake payment requests, phishing links |

**Report Submission Features**:
- Category selection (dropdown)
- Free-text explanation (required, 50-500 characters)
- Screenshot/evidence upload (optional, max 5 files)
- Anonymous reporting option (identity hidden from reported party)
- Reporter contact option (for follow-up questions)

**Report Workflow**:
1. User submits report with evidence
2. System creates moderation case
3. Moderator reviews within 24-48 hours
4. Action taken (content removed, user warned/suspended, report dismissed)
5. Reporter notified of outcome (if contact provided)

**Details**:
- The system SHALL prevent report spam (max 5 reports per user per day)
- The system SHALL prioritize reports based on category severity
- The system SHALL automatically flag users with multiple reports
- The system SHALL provide appeals process for wrongly actioned reports

**Business Value**: Robust reporting system maintains platform quality and user safety. Quick response to reports builds trust.

**Acceptance Criteria**:
- Report button accessible on all listing/user/content pages
- Report submitted successfully with confirmation
- Moderator reviews reports within 48 hours
- Reporter notified of outcome within 72 hours
- False reports tracked and may result in reporter warnings

---

#### FR-57: Dispute Case Management (P1)
**Requirement**: The system SHOULD provide comprehensive dispute management workflow for order-related conflicts.

**Dispute Types**:
- Property not as described
- Service not delivered
- Payment issues (amount, refund)
- Document fraud
- Contractual disagreements

**Dispute Workflow** (see Section 7.16.1 for lifecycle details):
1. **Open**: User initiates dispute from order page
2. **Evidence Collection**: Both parties upload evidence (7 days)
3. **Review**: Admin reviews case with evidence
4. **Resolution**: Refund, partial refund, mediation, dismissal
5. **Closed**: Final outcome recorded, appeals window (7 days)

**Evidence Types**:
- Chat/message screenshots
- Proof documents from transaction timeline
- Payment receipts
- Photos/videos
- Third-party documents (lawyer opinion, police report)

**Resolution Actions**:
- Full refund (fraud proven)
- Partial refund (partial service delivered)
- Account warning/suspension (policy violation)
- Dismissal (insufficient evidence)
- Mediation (both parties agree to third-party arbitration)

**Business Value**: Formal dispute process protects both buyers and sellers while providing platform with clear resolution framework.

**Acceptance Criteria**:
- User can open dispute from any paid order
- Evidence upload supports multiple file types
- Admin can view all evidence and communication
- Resolution decision clearly communicated to both parties
- Refunds processed within 7-14 days when approved

---

#### 7.16.1 Dispute Lifecycle

**Recommended Workflow**:
**Open → Evidence Collection → Review → Resolution → Closed**

**SLA Targets** (configurable):
- Acknowledge dispute: Within 24 hours
- First review decision: Within 3 business days
- Evidence upload window: 7 days
- Appeals window: 7 days after resolution

**Resolution Types**:
1. **Refund (Full/Partial)**: Payment returned to buyer
2. **Cancel & Archive**: Transaction cancelled, no refund
3. **Continue with Corrective Steps**: Issues resolved, transaction continues
4. **Account Penalties**: Warning, suspension, or ban for policy violations

---

#### 7.16.2 Buyer Protection Alignment

**Integration with Payment Modes**:
- **Mode B (Platform Hold)**: Disputes can trigger hold release or refund decisions directly
- **Mode A (Direct Pay)**: Platform records dispute decision and initiates refund request via gateway API

**Dispute Impact on Transactions**:
- Active disputes freeze transaction step progress
- Step proofs cannot be marked verified during dispute
- Payments on hold until resolution

---

#### 7.16.3 Abuse Controls

**Minimum Controls**:
- **Block User**: Restricts all chat/call communication
- **Rate Limiting**: Server-side enforcement of message frequency limits
- **Automated Flagging**: Repeated reports trigger automatic review
- **Content Filtering**: Profanity filter, link detection, phone number sharing limits

**Spam Detection Rules**:
- More than 10 messages per minute: Auto-flagged
- Identical message sent to 5+ users: Auto-flagged
- External payment links shared: Warning + manual review
- Phone numbers shared before appointment: Warning message

---

## 7.17 Real Estate Company & Project Listings

#### FR-58: Project Listing Type (P1)
**Requirement**: The system SHOULD support real estate development project listings with unit inventory and construction progress tracking.

**Project-Specific Fields**:
- Developer/Company name (verified)
- Project name and location
- Total units and available units by type
- Construction status (% complete)
- Handover timeline
- Amenities and facilities
- Approval documents (RAJUK, building permission)

**Unit Management**:
- Multiple unit types (2-bed, 3-bed, penthouses)
- Per-unit pricing
- Floor plans per unit type
- Booking status per unit

**Business Value**: Project listings support real estate developers, a key professional user segment, and address the "slow project completion" concern from research.

---

#### FR-59: Project Progress Updates (P1)
**Requirement**: The system SHOULD allow verified developers to post construction progress updates with moderation.

**Progress Update Features**:
- Monthly progress percentage
- Construction milestone photos
- Timeline updates
- Challenges and resolution notes

**Moderation**:
- All updates reviewed by admin before publishing
- Misleading updates result in warnings
- Verified developers get priority approval

**Business Value**: Transparent progress updates build buyer confidence and reduce concerns about delayed projects.

---

## 7.18 Monetization & Billing

#### FR-60: Subscription Plans (P1)
**Requirement**: The system SHOULD offer tiered subscription plans for agents and developers with feature access and analytics.

**Plan Tiers**:

| Tier | Target User | Monthly Fee | Features |
|------|------------|-------------|----------|
| **Free** | Social users | BDT 0 | Basic search, 1 active listing, standard support |
| **Agent Basic** | Individual agents | BDT 1,500 | 10 active listings, analytics, priority support |
| **Agent Pro** | URA-certified agents | BDT 3,500 | 50 listings, advanced analytics, featured placement (5/month) |
| **Developer** | Real estate companies | BDT 10,000+ | Unlimited listings, project listings, brand page, dedicated support |

**Subscription Benefits**:
- Listing limits
- Analytics dashboard access
- Featured listing credits
- Priority customer support
- Profile badges ("Pro Agent")

---

#### FR-61: Featured Listings (P1)
**Requirement**: The system SHOULD allow paid promotion of listings with clear "Featured" labeling.

**Featured Listing Features**:
- Displayed at top of search results
- Highlighted border/badge
- Shown in homepage carousel
- Duration: 7 days, 15 days, 30 days
- Pricing: BDT 500 (7 days), BDT 1,200 (15 days), BDT 2,000 (30 days)

**Transparency**:
- Clear "Featured" label on all promoted listings
- No impact on organic search ranking after promotion expires

---

## 7.19 Service Provider Marketplace

#### FR-62: Service Listings (P1)
**Requirement**: The system SHOULD allow service providers to create listings for property-related services.

**Service Categories**:
- Interior design
- Renovation/construction
- Property management
- Cleaning services
- Home inspection
- Movers and packers

**Service Listing Fields**:
- Service category and subcategory
- Service area (districts covered)
- Pricing model (per sqft, per hour, fixed price, custom quote)
- Availability schedule
- Portfolio (photos of past work)
- Credentials and certifications

---

#### FR-63: Book/Order Services (P1)
**Requirement**: The system SHOULD enable users to book services with schedule, location, and scope details.

**Booking Fields**:
- Service type selection
- Schedule (date, time, duration estimate)
- Service location (property address)
- Scope description (free text)
- Budget range

---

#### FR-64: Provider Payout Hooks (P1)
**Requirement**: The system SHOULD store provider payout information with manual payout processing support.

**Payout Information**:
- Bank account details (verified)
- Payout schedule (per service, monthly)
- Commission/fee structure
- Tax withholding information

**Implementation**: Manual payout processing in MVP with future automation planned.

---

#### FR-65: Service Reviews (P1)
**Requirement**: The system SHOULD allow users to review service providers after service completion.

**Review Components**:
- Overall rating (1-5 stars)
- Quality of work
- Timeliness
- Communication
- Value for money
- Free-text review
- Photos of completed work (optional)

---

## 7.20 Government Land Portals (Bangladesh Context)

> **Critical Context**: MSC Home treats government portals as **external systems only**. No scraping, automation, or captcha solving. Link-out + user manual entry approach.

#### FR-66: Official Portal Deep Links (P0)
**Requirement**: The system SHALL provide contextual deep links to official Bangladesh government land portals.

**Supported Portals**:

| Portal | Purpose | Link Context |
|--------|---------|--------------|
| **DLRMS** | Digital Land Records Management System - view land records, maps | Property listing detail page (for land), Transaction step 2 (document collection) |
| **e-Namjari** | Online mutation application and tracking | Transaction step 8 (mutation application), Land ownership verification |
| **LDTax** | Land development tax payment and holding registration | Transaction step 10 (tax payment), Property ownership verification |

**Link Features**:
- Deep links to specific portal sections (e.g., DLRMS record search, LDTax payment page)
- Help text explaining portal purpose
- "How to use" guide with screenshots
- Portal contact information

**Business Value**: Guided portal access empowers users to complete government processes while maintaining platform compliance (no unauthorized integration).

**Acceptance Criteria**:
- Links open correct portal sections in new tab
- Help guides accessible from link buttons
- Portal availability status monitored (alert if portal down)

---

#### FR-67: Portal Reference Capture (P0)
**Requirement**: The system SHALL allow users to store portal reference numbers and evidence as part of transaction timeline without direct portal integration.

**Capturable Portal References**:

**DLRMS**:
- Application number
- Mobile number used for tracking
- Mouza, Dag, Khatian numbers
- Screenshot/PDF of search results

**e-Namjari (Mutation)**:
- Application reference number
- Mobile number
- Application date
- Screenshot of application receipt

**LDTax**:
- Holding number
- Assessment year
- Payment receipt number
- Screenshot of payment confirmation

**Reference Storage**:
- Portal type (dropdown)
- Reference identifiers (text fields)
- Mobile number used (for SMS updates from portal)
- Notes (free text)
- Attachments (screenshots, PDFs) - max 5 files per reference
- Timestamp and capturing user

**Details**:
- The system SHALL validate reference number formats (basic pattern matching)
- The system SHALL NOT attempt to verify references against portal APIs
- The system SHALL display portal references in transaction timeline
- Users SHALL be able to edit references if errors detected

**Business Value**: Reference tracking keeps transaction organized and provides verification evidence without requiring illegal portal access.

**Acceptance Criteria**:
- User can capture references from all 3 portals
- Screenshots/PDFs uploadable and previewable
- References displayed in transaction timeline
- Both parties can view captured references

---

#### FR-68: Status Tracking Assistance (Manual) (P1)
**Requirement**: The system SHOULD provide guided "check status" interface that mirrors portal requirements, storing user-entered status snapshots.

**Status Checking Workflow**:
1. User selects portal and reference type
2. System displays required fields (mirrors portal inputs)
3. User manually checks status on portal (system opens portal link)
4. User returns and enters status information
5. System stores status snapshot with timestamp
6. Optional: User uploads screenshot as proof

**Example - DLRMS Status Check**:
- Required inputs: Application number, mobile number, captcha math sum (user enters manually)
- User action: Opens DLRMS portal → enters details → views status → returns to MSC Home
- User captures: Status text (dropdown: Pending/Approved/Rejected), date checked, optional screenshot

**Status Snapshot Storage**:
- Portal type
- Reference identifiers
- Status value (user-entered or dropdown-selected)
- Status check date
- Optional evidence (screenshot)
- Timestamp and user

**Critical Limitation**:
- Platform MUST NOT attempt automated portal submissions
- Platform MUST NOT attempt to scrape pages or solve captchas
- Workflow is strictly **link-out + user manual entry + optional screenshot**

**Business Value**: Guided status checking reduces user confusion while maintaining full compliance with government portal terms.

---

#### FR-69: Proof Attachments from Portals (P1)
**Requirement**: The system SHOULD support uploading QR-coded documents from portals as transaction step proofs.

**Supported Documents**:
- Khatian copy with QR code (from DLRMS)
- DCR (Digital Cadastral Record)
- Mutation approval letter
- Land tax payment receipt

**Upload Features**:
- QR code detection (visual indicator)
- Document type tagging
- Link to transaction step
- Verification status tracking

---

## 7.21 Payment Gateway Integration (SSLCOMMERZ Hardening)

#### FR-70: Hosted Checkout Support (P0)
**Requirement**: The system SHALL support redirect-based hosted checkout as primary payment flow for MVP reliability.

**Hosted Checkout Flow**:
1. User selects payment method and confirms order
2. System creates payment session with gateway
3. User redirected to gateway hosted page
4. User completes payment with OTP/3DS on gateway page
5. Gateway redirects back to MSC Home with payment result
6. System validates result via IPN/validation call

**Benefits of Hosted Checkout**:
- PCI DSS compliance simplified (no card data on MSC servers)
- Gateway handles 3DS authentication
- Reduced fraud liability
- Mobile-optimized payment pages by gateway

**Business Value**: Hosted checkout reduces technical complexity and compliance burden while providing secure, reliable payment flow.

---

#### FR-71: IPN/Webhook Listener (P0)
**Requirement**: The system SHALL implement server-to-server notification endpoint (IPN) to receive payment status updates independent of user browser.

**IPN Functionality**:
- Endpoint: https://mschome.com/api/payments/ipn
- Gateway sends POST request with payment status
- System validates signature (gateway-specific)
- System updates order status based on IPN data
- System responds with 200 OK to acknowledge

**Why IPN is Critical**:
- User may close browser before redirect completes
- Network issues may prevent redirect
- IPN ensures payment status captured even if user doesn't return to site

**Security**:
- Verify gateway signature/hash before trusting IPN data
- Implement idempotency (handle duplicate IPNs)
- Validate transaction ID, amount, currency match order
- Log all IPN attempts for audit

**Business Value**: IPN prevents lost payment confirmations due to user browser issues, ensuring accurate order fulfillment.

---

#### FR-72: Post-Payment Validation Call (P0)
**Requirement**: The system SHALL validate all payment success notifications by calling gateway validation endpoint before marking orders as PAID.

**Validation Workflow**:
1. System receives payment success (IPN or redirect)
2. System calls gateway validation API with transaction ID
3. Gateway returns authoritative payment status
4. System reconciles: transaction ID, amount, currency, status
5. If all match: Mark order PAID, proceed with fulfillment
6. If mismatch: Mark order HOLD, alert operations

**Validation API Call**:
```
POST https://gateway.com/api/validate
{
  "merchant_id": "MSC123",
  "transaction_id": "GW-TXN-456",
  "signature": "hashed_signature"
}

Response:
{
  "status": "VALID",
  "amount": "350000.00",
  "currency": "BDT",
  "payment_status": "SUCCESS"
}
```

**Why Validation is Critical**:
- IPN alone can be spoofed
- Prevents fraud (fake payment confirmations)
- Ensures amount paid matches order amount

**Business Value**: Validation call prevents payment fraud and ensures only genuine payments result in order fulfillment.

---

#### FR-73: Refund Operations (P1)
**Requirement**: The system SHOULD support refund initiation and tracking via gateway refund API.

**Refund Features**:
- Full refund or partial refund support
- Refund reason capture (admin-entered)
- Gateway refund API integration
- Refund status tracking (initiated, processing, completed, failed)
- Refund reference ID storage

**Refund Timeline**:
- Refund initiated within 24 hours of approval
- Gateway processing: 7-14 business days (bank-dependent)
- User notified at each status change

---

#### FR-74: Risk Holds (P1)
**Requirement**: The system SHOULD place risky payments in HOLD state for manual verification.

**Risk Indicators**:
- Gateway flags transaction as "risky" or "under review"
- High-value first-time transaction (> BDT 5 Lakh)
- Multiple failed payment attempts before success
- Mismatched billing information
- VPN/proxy usage detected by gateway

**Hold Process**:
1. Payment technically successful but flagged
2. Order placed in HOLD state (not CONFIRMED)
3. Operations team notified for manual review
4. Team verifies: user identity, payment legitimacy, order details
5. After verification: Release hold → Order confirmed OR Initiate refund → Order cancelled

**Business Value**: Risk holds prevent fraud losses while balancing user experience (legitimate users verified quickly).

---

## 7.22 Operational & Safety Requirements

### 7.22.1 Listing Lifecycle & Moderation

#### FR-75: Listing Lifecycle State Machine (P0)
**Requirement**: The system SHALL implement defined listing status workflow with allowed state transitions.

**Listing States & Transitions**:
```
DRAFT → SUBMITTED → UNDER_REVIEW → [PUBLISHED | CHANGES_REQUESTED | REJECTED]
         ↓                                ↓            ↓
    [ARCHIVED]                        [PAUSED]    [SUBMITTED]
                                         ↓
                                    [ARCHIVED]
```

**State Definitions**:
- **DRAFT**: Incomplete listing, saved by seller
- **SUBMITTED**: Submitted for review, awaiting verification
- **UNDER_REVIEW**: Being reviewed by verifier
- **CHANGES_REQUESTED**: Verifier needs additional info/corrections
- **REJECTED**: Does not meet platform standards
- **PUBLISHED**: Live on platform, visible in search
- **PAUSED**: Temporarily hidden by seller (off-market)
- **ARCHIVED**: Permanently removed, retained for record (retention policy: 1 year)

**Transition Rules**:
- DRAFT can only → SUBMITTED (when requirements met)
- SUBMITTED can only → UNDER_REVIEW (auto or manual assignment)
- UNDER_REVIEW can → PUBLISHED (approved) OR CHANGES_REQUESTED (issues found) OR REJECTED (serious issues)
- CHANGES_REQUESTED can → SUBMITTED (after corrections)
- PUBLISHED can → PAUSED (seller action) OR ARCHIVED (seller action)
- Any non-terminal state can → ARCHIVED (user request + admin approval)

**Business Value**: Clear state machine prevents confusion and ensures all listings go through proper verification.

---

#### FR-76: Listing Moderation Queue (P0)
**Requirement**: The system SHALL provide verifier queue for efficient listing review with decision workflow.

**Queue Features**:
- All UNDER_REVIEW listings displayed
- Sortable by: submission date, property type, listing value, accuracy score
- Filterable by: location, property type, verified seller
- Assignable to specific verifiers
- SLA tracking (pending > 48 hours highlighted)

**Review Decision Options**:
1. **Approve**: Listing → PUBLISHED
2. **Reject**: Listing → REJECTED (reason required from predefined list + free text)
3. **Request Changes**: Listing → CHANGES_REQUESTED (specific issues noted)

**Reason Codes**:
- Incomplete information
- Poor quality photos
- Documents missing or illegible
- Price unrealistic
- Duplicate listing
- Suspected fraud

**Audit Trail**:
- All decisions logged with verifier ID, timestamp, reason
- Verifier performance metrics (avg review time, approval rate)

**Business Value**: Structured moderation queue ensures consistent review quality and fast turnaround.

---

#### FR-77: Re-Verification Triggers (P1)
**Requirement**: The system SHOULD automatically trigger re-review when significant listing changes occur or fraud reports received.

**Re-Verification Triggers**:
| Trigger | Threshold | Action |
|---------|-----------|--------|
| **Price Change** | > 15% change | Auto re-review |
| **Location Change** | Different area/district | Auto re-review |
| **Ownership Documents Updated** | New documents uploaded | Auto re-review |
| **Fraud Reports** | 3+ reports in 30 days | Auto pause + urgent review |
| **Inactive Re-publish** | Archived > 90 days, now re-submitted | Auto re-review |

**Re-Review Process**:
- Listing status changes to UNDER_REVIEW
- If currently PUBLISHED, may be paused during review (configurable)
- Seller notified of re-review reason
- Expedited review (24 hours vs. standard 48 hours)

**Business Value**: Re-verification maintains listing quality over time and catches fraudulent updates.

---

#### FR-78: Status History & Auditability (P0)
**Requirement**: The system SHALL store complete listing status history with full audit trail.

**History Entry Format**:
- Previous status
- New status
- Timestamp
- Actor (user ID or system)
- Reason (if status change requires reason)
- Related documents (if applicable)

**Admin View**:
- Timeline visualization of all status changes
- Filterable and exportable history
- Drill-down into specific changes

**Business Value**: Complete history supports dispute resolution and fraud investigation.

---

### 7.22.2 Document Vault Access Controls

#### FR-79: Document Access Requests (P0)
**Requirement**: The system SHALL allow controlled access to sensitive documents via explicit request workflow.

**Access Request Fields**:
- Requested documents (checklist: Dalil, Mutation, Tax Receipt, etc.)
- Purpose (dropdown: Due diligence, Loan application, Legal review, etc.)
- Additional notes (free text)
- Requested expiry (default: 7 days, max: 30 days)

**Requestable Documents**:
- Deed/Dalil
- Mutation/Namjari certificate
- Land tax receipts
- NOC (if applicable)
- Allotment letter
- Building approval

**Request Submission**:
- Accessible from listing detail page
- Requires user to be logged in and identity verified (minimum)
- Request logged with timestamp and requester details

---

#### FR-80: Document Access Grants (P0)
**Requirement**: The system SHALL allow document owners to approve/deny access requests with time-bound grants.

**Grant Approval Workflow**:
1. Owner receives access request notification
2. Owner reviews requester profile and purpose
3. Owner approves/denies with optional message
4. If approved: System generates time-bound access grant

**Grant Details**:
- Scope: Specific documents approved
- Expiry: Date/time when access expires (default: 7 days from approval)
- Permissions: View-only or Download (default: view-only)
- Revocable: Owner can revoke anytime

**Access Grant Record**:
- Grant ID
- Requester user ID
- Approved documents list
- Grant date and expiry
- Revocation status
- Access count (how many times viewed/downloaded)

**Business Value**: Explicit grant workflow gives owners control while enabling legitimate due diligence.

---

#### FR-81: Document Watermarking / View-Only (P1)
**Requirement**: The system SHOULD render watermarked previews for shared documents to discourage unauthorized distribution.

**Watermark Features**:
- Requester user ID
- Access date/time
- "MSC Home - Authorized Access Only" text
- Diagonal watermark across pages

**View-Only Implementation**:
- Documents rendered as images or secure PDF viewer
- Right-click disabled, print disabled (client-side)
- Download button only if permissions allow

---

#### FR-82: Document Access Audit Log (P0)
**Requirement**: The system SHALL log every document access attempt with outcome for audit and fraud investigation.

**Log Entry**:
- Document ID and type
- Requester user ID
- Access attempt timestamp
- Outcome: Allowed (viewed/downloaded) or Denied (expired/no grant/revoked)
- IP address (masked for privacy compliance)
- Browser/device info

**Audit Uses**:
- Investigate unauthorized access claims
- Track document leak sources
- Monitor suspicious access patterns
- Compliance reporting

---

### 7.22.3 Messaging Safety & Abuse Prevention

#### FR-83: Block & Report (P0)
**Requirement**: The system SHALL allow users to block other users, preventing all communication.

**Block Features**:
- Mutual block: Both users cannot message/call each other
- Blocked user list management
- Unblock option available
- Block reason optional (for user's reference)

---

#### FR-84: Anti-Spam Controls (P0)
**Requirement**: The system SHALL enforce server-side rate limits and abuse detection for messages and contacts.

**Rate Limits**:
- **Message Frequency**: Max 10 messages per minute per conversation
- **Repeated Content**: Same message sent to 5+ users flagged
- **Link Sharing**: Max 3 external links per conversation per day
- **Phone Number Sharing**: Warning after 1st occurrence, flagged after 2nd

**Server-Side Enforcement**:
- Limits enforced on server (client cannot bypass)
- Violations logged with severity score
- Automated temporary restrictions (e.g., 30-min message ban)

---

#### FR-85: Moderation Cases (P1)
**Requirement**: The system SHOULD create moderation cases for reported content with triage and action workflow.

**Moderation Actions**:
- **Warn**: Send warning message to user
- **Mute**: Temporarily disable messaging (24 hours, 7 days, 30 days)
- **Suspend**: Temporarily disable account
- **Ban**: Permanently disable account
- **Dismiss**: No action, report unfounded

**Case Management**:
- Priority queue (high-priority: fraud, threats; low-priority: spam)
- Assign to moderators
- Evidence snapshots (messages, screenshots)
- Action history and appeals

---

### 7.22.4 Notifications: Preferences & Delivery

#### FR-86: Notification Preferences (P0)
**Requirement**: The system SHALL allow users to configure per-category notification preferences and quiet hours.

**Preference Categories**:
- Offers & Transactions (High priority)
- Messages & Appointments (High priority)
- Verifications (Medium priority)
- Listings & Alerts (Medium priority)
- Marketing & Updates (Low priority)

**Per-Category Settings**:
- In-app: On/Off
- Email: On/Off
- SMS: On/Off
- Quiet Hours: Start time - End time (e.g., 10 PM - 7 AM)

**Exceptions**:
- Security alerts (login from new device, password change) always sent via all channels

---

#### FR-87: Reliable Notification Delivery (P1)
**Requirement**: The system SHOULD implement retry logic and dead-letter queue for failed notifications.

**Retry Logic**:
- Failed SMS/Email retried with exponential backoff (1 min, 5 min, 15 min)
- Max 3 retry attempts
- After 3 failures, moved to dead-letter queue

**Dead-Letter Queue Monitoring**:
- Operations team alerted of persistent failures
- Weekly reports on delivery rates
- Investigation of systematic issues (provider outage, etc.)

---

### 7.22.5 Disputes, Cancellations, Refunds

#### FR-88: Dispute Lifecycle (P1)
**Requirement**: The system SHOULD implement complete dispute workflow (see Section 7.16.1 for detailed lifecycle).

**Lifecycle States**:
- Open → Evidence Collection → Review → Resolution → Closed

**Outcomes**:
- Refund (full/partial)
- Cancel order
- Continue with corrective steps
- Dismiss claim

---

#### FR-89: Cancellation Policy Engine (P1)
**Requirement**: The system SHOULD define and enforce cancellation rules based on order state and timeline.

**Cancellation Policy** (see Section 7.8 for detailed policy):
- Within 24 hours: 90% refund
- After 24 hours, before Bayna: 70% refund
- After Bayna: Mutual consent required

---

#### FR-90: Refund Tracking (P1)
**Requirement**: The system SHOULD store and track refund attempts with status updates.

**Refund Statuses**:
- Requested → Approved → Initiated → Processing → Completed/Failed

**Tracking**:
- Link refunds to disputes
- Gateway refund reference IDs
- Timeline tracking (request to completion)

---

### 7.22.6 Payments: Idempotency & Signature Verification

#### FR-91: Idempotent Payment Processing (P0)
**Requirement**: The system SHALL process payment notifications idempotently to prevent duplicate charges.

**Idempotency Implementation**:
- Generate unique idempotency key per payment attempt
- Store key with payment record
- Reject duplicate requests with same key (return original response)
- Use provider transaction ID + local key for deduplication

---

#### FR-92: Verify Gateway Signatures (P0)
**Requirement**: The system SHALL verify gateway callback/IPN signatures before trusting payload data.

**Signature Verification**:
- Gateway includes signature/hash field in callbacks
- System recomputes signature using shared secret
- If signatures match: Trust payload
- If mismatch: Reject and log security event

---

#### FR-93: Reconciliation Report (P1)
**Requirement**: The system SHOULD provide daily reconciliation export comparing orders vs. payments vs. gateway status.

**Reconciliation Report Includes**:
- All orders placed (count, total value)
- All payments received (count, total value)
- Matched orders (order + payment confirmed)
- Mismatches (payment without order, order without payment)
- Pending verifications

**Output**: CSV/Excel export for finance team review

---

## 8. Business Rules (BR)

> **Purpose**: Business rules define the policies, calculations, and logical constraints that govern system behavior. These rules ensure consistency, enforce platform standards, and implement domain-specific logic.

---

### 8.1 Verification Rules

#### BR-1: Verified Badge Issuance
**Rule**: The system SHALL issue verified badges only after successful verification approval by authorized verifier.
**Rationale**: Prevents fake verified badges and maintains badge credibility.

#### BR-2: Role-Based Document Requirements
**Rule**: The system SHALL require different documents based on professional role (e.g., lawyer requires BAR certificate, agent requires URA certificate).
**Rationale**: Ensures appropriate credentials for each profession type.

#### BR-3: Listing Verification Dependency
**Rule**: A listing SHALL receive "Listing Verified" badge only after ownership verification is completed.
**Rationale**: Listing verification builds on ownership verification, cannot skip prerequisite.

#### BR-4: e-KYC Fallback (P1)
**Rule**: If e-KYC provider check fails or is unavailable, the system SHALL proceed with manual verification. The system SHALL store all e-KYC provider attempts for audit.
**Rationale**: Ensures verification process continues even if automated provider unavailable.

---

### 8.2 Accuracy Score Rules

#### BR-5: Score Calculation Basis
**Rule**: Accuracy Score SHALL be computed from field completeness with weighted values for required and optional fields.
**Rationale**: Incentivizes complete listings while recognizing that some fields are more critical than others.

#### BR-6: Accuracy Score Formula
**Rule**: The system SHALL calculate Accuracy Score using the formula:

$$\text{AccuracyScore} = \left(\frac{\sum w_i \cdot \mathbb{1}[\text{field}_i \text{ present}]}{\sum w_i}\right) \times 100$$

Where:
- $w_i$ = weight assigned to field $i$ (configurable by Admin)
- $\mathbb{1}[\text{field}_i \text{ present}]$ = indicator function (1 if field filled, 0 if empty)
- $\sum w_i$ = sum of all field weights

**Example**:
- Required field weight: 10
- Recommended field weight: 5
- Optional field weight: 1
- Listing with 5/5 required, 3/5 recommended, 2/10 optional:
  - Numerator: (5×10) + (3×5) + (2×1) = 67
  - Denominator: (5×10) + (5×5) + (10×1) = 85
  - Score: (67/85) × 100 = 78.82% (rounded to 79%)

**Rationale**: Mathematical formula ensures consistent, objective scoring. Configurable weights allow platform to adjust scoring based on field importance.

#### BR-7: Score Impact on Ranking (Optional)
**Rule**: The system MAY boost search ranking for listings with higher accuracy scores (all else being equal).
**Rationale**: Incentivizes sellers to complete listings, improving overall marketplace quality.

---

### 8.3 Cost Transparency Rules

#### BR-8: No Hidden Costs Declaration
**Rule**: A listing MUST NOT claim "no extra costs" or "all costs included" unless the seller has explicitly confirmed all cost fields.
**Rationale**: Prevents misleading "no hidden costs" claims when seller hasn't disclosed all costs.

#### BR-9: Unknown Cost Labeling
**Rule**: If a seller does not provide a cost field value, the UI MUST label it as "Not provided by seller" or similar clear language (never hide the field).
**Rationale**: Transparency about what is unknown prevents buyer surprises and sets proper expectations.

---

### 8.4 Offers & Transactions Rules

#### BR-10: Offer Submission Requirement
**Rule**: Only logged-in, authenticated buyers SHALL be allowed to submit offers.
**Rationale**: Prevents spam offers and ensures accountability.

#### BR-11: Offer State Transitions
**Rule**: Offer states MUST follow the workflow: SUBMITTED → COUNTERED → ACCEPTED/REJECTED/WITHDRAWN. No other transitions are allowed.
**Rationale**: Clear state machine prevents ambiguous offer status.

#### BR-12: Transaction Creation Trigger
**Rule**: An accepted offer MUST automatically create a transaction record with unique transaction ID.
**Rationale**: Formal transaction record begins audit trail and step tracking.

#### BR-13: Transaction Step Immutability
**Rule**: Transaction steps SHALL be append-only and timestamped. Completed steps cannot be deleted (only marked as disputed if issues arise).
**Rationale**: Immutable timeline provides reliable audit trail for dispute resolution.

#### BR-14: Step Proof Requirements (MVP)
**Rule**: A transaction step SHALL be marked complete only if the required proof type is attached (document upload OR counterparty confirmation).
**Rationale**: Proof requirement ensures steps are verifiable, not just claimed.

---

### 8.5 Payment Rules

#### BR-15: Payment-Order-Transaction Linking
**Rule**: A payment MUST reference exactly one order. A property order MUST reference exactly one transaction.
**Rationale**: Clear linking enables traceability and prevents payment ambiguity.

#### BR-16: Payment Confirmation Requirement
**Rule**: OTP or 3D Secure authentication SHALL be required for payment confirmation (gateway-dependent, enforced by gateway).
**Rationale**: Additional authentication reduces payment fraud.

#### BR-17: Cancellation Refund Rule
**Rule**: If an order cancellation is approved and payment has already succeeded, the system SHALL initiate refund workflow.
**Rationale**: Ensures buyers receive refunds for cancelled paid orders.

---

### 8.6 Buyer Protection & Disputes Rules

#### BR-18: Dispute Eligibility (P1)
**Rule**: A dispute SHALL only be opened for orders in PAID status within a configurable claim window (default: 7 days after payment OR during active transaction).
**Rationale**: Time limits prevent old disputes while protecting recent transactions.

#### BR-19: Dispute Audit Requirement (P1)
**Rule**: All dispute status changes MUST be logged with admin user ID, timestamp, and reason. These logs are admin-audited.
**Rationale**: Accountability for dispute resolutions prevents bias and supports appeals.

---

### 8.7 Review Rules

#### BR-20: Review Timing
**Rule**: Reviews SHALL only be allowed after transaction completion status is reached.
**Rationale**: Premature reviews may be inaccurate; completion ensures full experience.

#### BR-21: One Review Per Transaction
**Rule**: Each party SHALL submit exactly one review per transaction. No duplicate reviews allowed.
**Rationale**: Prevents review spam and gaming.

---

### 8.8 Service Provider Marketplace Rules

#### BR-22: Service Review Timing
**Rule**: Service reviews SHALL only be allowed after a service order status is marked COMPLETED.
**Rationale**: Ensures reviewer has received full service before rating.

#### BR-23: Payout Auditability
**Rule**: Provider payout status MUST be auditable, including who approved, when, and reference details.
**Rationale**: Financial audit trail for compliance and dispute resolution.

---

### 8.9 Payment Gateway Validation & Risk Rules

#### BR-24: Payment Validation Requirement
**Rule**: An order MUST be marked PAID only after back-end validation succeeds. IPN notification alone is NOT sufficient.
**Rationale**: Prevents fraud via fake IPN notifications.

#### BR-25: Validation Reconciliation
**Rule**: Back-end validation MUST reconcile at minimum: transaction ID, amount, currency type, and final status against order details.
**Rationale**: Ensures payment matches order (no amount mismatch or currency fraud).

#### BR-26: Risky Payment Holds
**Rule**: If the payment gateway returns a "risky" flag for an otherwise successful payment, the platform MUST place the order into HOLD state and require additional verification before delivering buyer protection or confirming service.
**Rationale**: Protects platform from fraud losses while preserving legitimate transaction ability.

#### BR-27: TLS and API Security
**Rule**: The payment integration MUST require TLS 1.2+ on the merchant server and use server-to-server calls for sensitive API operations (validation, refunds).
**Rationale**: Protects payment data in transit and prevents man-in-the-middle attacks.

---

### 8.10 Listing Lifecycle & Moderation Rules

#### BR-28: Publication Visibility Rule
**Rule**: Listings MUST NOT be publicly visible (in search results or direct link access) unless their status is PUBLISHED.
**Rationale**: Prevents incomplete or rejected listings from appearing to buyers.

#### BR-29: Changes Requested Re-submission
**Rule**: Listings with CHANGES_REQUESTED status CANNOT return to PUBLISHED without re-submission and a new review decision.
**Rationale**: Ensures corrected listings are re-verified before going live.

#### BR-30: Auto-Pause on Fraud Reports (P1)
**Rule**: A listing SHOULD be automatically paused if it receives a configurable number of credible fraud reports (default: 3) pending admin review.
**Rationale**: Quick response to potential fraud protects buyers while preserving seller rights (review process).

#### BR-31: Re-Verification Action Requirement
**Rule**: Re-verification triggers (FR-77) MUST result in either (a) requiring review before republishing, OR (b) status downgrade to UNDER_REVIEW/PAUSED until resolved.
**Rationale**: Ensures significant listing changes are verified before buyers see updated information.

---

### 8.11 Document Vault Access Policy Rules

#### BR-32: Private by Default
**Rule**: Vault documents MUST be private by default. Access requires explicit grant (FR-80) or verifier/admin role.
**Rationale**: Protects sensitive ownership and identity documents from unauthorized access.

#### BR-33: Time-Bound Grant Expiry
**Rule**: Access grants MUST be time-bound and revocable. The system MUST deny access after expiry.
**Rationale**: Limits exposure window and gives owners control to revoke if circumstances change.

#### BR-34: Watermarked Sharing (P1)
**Rule**: When document sharing is enabled, the system SHOULD provide watermarked previews. Raw downloads (if allowed) MUST be auditable.
**Rationale**: Watermarks deter unauthorized redistribution; audit trail supports leak investigation.

#### BR-35: Access Attempt Logging
**Rule**: Every document access attempt (view or download) MUST be logged, including denied attempts.
**Rationale**: Complete audit trail for security investigations and compliance.

---

### 8.12 Messaging Safety & Abuse Handling Rules

#### BR-36: Mutual Block Rule
**Rule**: Blocking is mutual. When either party blocks, messaging and calling MUST be disabled in both directions.
**Rationale**: Prevents harassment via response attempts; clean break for both parties.

#### BR-37: Server-Side Rate Limit Enforcement
**Rule**: The platform MUST enforce rate limits server-side. Clients CANNOT bypass rate limits.
**Rationale**: Prevents spam even from modified or malicious clients.

#### BR-38: Moderation Action Reversibility (P1)
**Rule**: Moderation actions (mute, suspend, ban) SHOULD be reversible by Admin and MUST be fully audited.
**Rationale**: Allows appeals and error correction while maintaining accountability.

---

### 8.13 Notification Rules

#### BR-39: Preference and Quiet Hours
**Rule**: Notifications MUST respect user preferences and quiet hours, EXCEPT for mandatory security alerts (e.g., suspicious login, password change).
**Rationale**: Balances user control with critical security communication.

#### BR-40: Delivery Failure Handling (P1)
**Rule**: Notification delivery failures SHOULD be retried and surfaced to operations via dead-letter queue monitoring.
**Rationale**: Ensures reliability and allows operations to address systematic delivery issues.

---

### 8.14 Cancellations, Refunds, and Holds Rules

#### BR-41: State-Based Cancellation (P1)
**Rule**: Cancellation eligibility MUST depend on order state. Once PAID, cancellation MUST trigger refund workflow (where supported by gateway).
**Rationale**: Protects buyer rights to cancel while ensuring refund process initiated.

#### BR-42: Refund Finality (P1)
**Rule**: Refund outcomes are final only after gateway confirmation. Partial refunds (if supported) MUST reconcile amounts with order records.
**Rationale**: Prevents premature order closure before refund actually processed.

#### BR-43: Hold Order Restrictions (P1)
**Rule**: Orders in HOLD status MUST NOT progress to service delivery or transaction step completion requiring payment release until released by Admin/Support.
**Rationale**: Protects platform from delivering service/releasing funds for potentially fraudulent orders.

---

*[End of Batch 3 - FR-44 to FR-93 + BR-1 to BR-43 Complete]*
