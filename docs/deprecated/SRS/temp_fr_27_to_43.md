### 7.7 Offers, Orders & Transactions

#### FR-27: Submit Offer (P0)
**Requirement**: The system SHALL allow buyers to submit secure, structured offers for properties.

**Offer Components**:
| Field | Required | Purpose |
|-------|----------|---------|
| **Proposed Price** | Yes | Buyer's offer amount |
| **Advance/Booking Money** | Yes | Bayana amount willing to pay |
| **Possession Timeline** | Yes | Desired handover/possession date |
| **Financing Method** | Yes | Cash/Loan/Mixed |
| **Contingencies** | Optional | Conditions (e.g., loan approval, inspection) |
| **Validity Period** | Yes | Offer expiry (default: 7 days) |
| **Additional Terms** | Optional | Free-text for special conditions |

**Details**:
- The system SHALL validate offer amount (minimum: 50% of asking price to prevent spam offers)
- The system SHALL notify seller/agent immediately via all enabled channels
- The system SHALL display offer status prominently on listing detail page for both parties
- The system SHALL allow only one active offer per buyer per listing

**Business Value**: Structured offers create formal records, reducing miscommunication and establishing clear negotiation starting points.

**Acceptance Criteria**:
- Buyer can submit offer with all required fields
- Offer validation enforces minimum price threshold
- Seller receives instant notification (in-app, email, SMS)
- Offer status tracked and visible to both parties
- Offer automatically expires after validity period

---

#### FR-28: Negotiate (P0)
**Requirement**: The system SHALL support multi-round offer negotiation with state management.

**Negotiation States**:
1. **SUBMITTED**: Initial offer sent by buyer
2. **COUNTERED**: Seller proposes modified terms
3. **ACCEPTED**: Both parties agree (creates transaction)
4. **REJECTED**: Seller declines offer with reason
5. **WITHDRAWN**: Buyer cancels offer before acceptance
6. **EXPIRED**: Offer validity period passed

**Negotiation Rules**:
- Maximum 5 counter-offer rounds to prevent infinite loops
- Each counter SHALL include modified price and/or terms
- Each counter resets validity period (default: 3 days)
- All negotiation history preserved with timestamps
- Either party can accept, counter, reject, or withdraw at any time

**Details**:
- The system SHALL track negotiation timeline with complete audit trail
- The system SHALL highlight changed fields between offers
- The system SHALL notify both parties of each negotiation action
- The system SHALL prevent acceptance of expired offers

**Business Value**: Transparent negotiation process builds trust and provides dispute resolution evidence. Clear state management prevents ambiguity.

**Acceptance Criteria**:
- Buyer/seller can counter with modified terms
- System limits to 5 counter rounds
- All negotiation history visible to both parties
- Acceptance immediately creates transaction record
- Rejection requires reason selection

---

#### FR-29: Transaction Step Tracking (P0)
**Requirement**: The system SHALL provide visual timeline tracking for all transaction steps with proof uploads.

**Bangladesh Property Transaction Steps** (12-step workflow):
1. **Offer Accepted**: Deal initiated
2. **Document Collection Started**: Gathering required documents
3. **Ownership & Information Verification**: Documents under review
4. **Bayna Agreement Signed**: Agreement to sell executed
5. **Legal Review Completed**: Lawyer verification done
6. **Sub-Registrar Appointment Booked**: Deed registration scheduled
7. **Payment Milestone 1**: Advance/booking money paid
8. **Dalil/Deed Registration**: Ownership transfer at Sub-Registrar office
9. **Payment Milestone 2**: Balance payment made
10. **Mutation Application Submitted**: e-Namjari/manual mutation applied
11. **Possession/Handover**: Keys and property transferred
12. **Transaction Completed**: All steps finalized

**Step Features**:
- Each step SHALL have:
  - Status (Pending, In Progress, Completed, Blocked)
  - Responsible party (Buyer/Seller/Agent/Lawyer/Both)
  - Expected completion date
  - Actual completion timestamp
  - Proof document uploads (see FR-32)
  - Notes/comments thread

**Details**:
- The system SHALL display timeline visually (progress bar + detailed list)
- The system SHALL allow both parties to update step status (with approval workflow for critical steps)
- The system SHALL send notifications when steps completed or blocked
- The system SHALL calculate estimated completion date based on step progress

**Business Value**: Visual step tracking reduces anxiety, sets expectations, and provides complete transaction history for dispute resolution.

**Acceptance Criteria**:
- Timeline visible to both buyer and seller
- Each step shows status, dates, and proofs
- Status updates notify all parties
- Completed steps locked and audited
- Estimated completion date updated in real-time

---

#### FR-30: Place Order (P0)
**Requirement**: The system SHALL allow users to place orders for properties and services with comprehensive order records.

**Order Types**:
1. **Property Purchase Order**: After accepted offer, formal order to proceed
2. **Service Order**: Legal/financial services, property management
3. **Subscription Order**: Agent/developer subscription plans (P1)

**Order Details**:
| Field | Required | Purpose |
|-------|----------|---------|
| **Order Type** | Yes | Property/Service/Subscription |
| **Item Reference** | Yes | Listing ID or Service ID |
| **Total Amount** | Yes | Full price including fees |
| **Payment Schedule** | Yes | One-time/Milestones/Installments |
| **Terms Accepted** | Yes | User agreement checkbox |
| **Delivery Timeline** | Yes | Expected completion date |

**Details**:
- The system SHALL generate unique order ID for tracking
- The system SHALL link order to transaction timeline (for property orders)
- The system SHALL calculate and display breakdown: price, platform fee, taxes, total
- The system SHALL validate order prerequisites (e.g., identity verified, offer accepted)

**Business Value**: Formal orders create legal records and enable structured payment processing. Clear order records support dispute resolution.

**Acceptance Criteria**:
- User can place order after offer acceptance or service selection
- Order ID generated and displayed immediately
- Order summary shows complete breakdown
- Order record preserved with full audit trail
- Order links to payment processing

---

#### FR-31: Confirm/Cancel Order (P0)
**Requirement**: The system SHALL support order confirmation and cancellation with appropriate state transitions and policies.

**Order States**:
1. **PENDING**: Order created, awaiting payment
2. **CONFIRMED**: Payment received, order active
3. **IN_PROGRESS**: Service delivery or transaction steps underway
4. **COMPLETED**: All obligations fulfilled
5. **CANCELLED**: Order cancelled (by user or admin)
6. **REFUNDED**: Payment returned after cancellation

**Confirmation Rules**:
- Order auto-confirmed upon successful payment
- Confirmation email sent within 5 minutes
- Confirmed orders trigger transaction step initialization (for property)

**Cancellation Policy**:
| Order State | Buyer Can Cancel? | Seller Can Cancel? | Refund Policy |
|-------------|-------------------|--------------------|-----------------|
| PENDING | Yes (full refund) | Yes (mutual consent) | 100% |
| CONFIRMED | Yes (with policy) | No (without mutual consent) | Per cancellation policy |
| IN_PROGRESS | Request only | Request only | Negotiated |
| COMPLETED | No | No | N/A |

**Cancellation Policy Details**:
- **Within 24 hours of payment**: 90% refund (10% processing fee)
- **After 24 hours, before step 4 (Bayna)**: 70% refund
- **After Bayna signed**: Mutual consent required, refund negotiated
- **Service orders**: Per service provider terms

**Details**:
- The system SHALL display cancellation policy clearly before payment
- The system SHALL enforce cancellation rules based on order state and timeline
- The system SHALL require cancellation reason (dropdown + free text)
- The system SHALL notify all parties of cancellations
- The system SHALL process refunds within 7-14 business days (gateway-dependent)

**Business Value**: Clear cancellation policies protect both buyers and sellers. Transparent rules reduce disputes.

**Acceptance Criteria**:
- User can view cancellation policy anytime
- Cancellation request processed based on order state
- Refund amount calculated automatically per policy
- All cancellations logged with reason and timestamps
- Refund status tracked and displayed

---

#### FR-32: Proof Uploads per Step (P0)
**Requirement**: The system SHALL enable upload of proof documents for each transaction step to maintain verifiable digital timeline.

**Required Proofs by Step**:
| Transaction Step | Required Proof Documents | Uploaded By |
|------------------|-------------------------|-------------|
| **Bayna Agreement Signed** | Signed Bayna copy (PDF/image), witness signatures | Buyer or Seller |
| **Legal Review Completed** | Lawyer certification letter or review report | Lawyer |
| **Payment Milestone** | Payment receipt, bank transfer confirmation | Buyer |
| **Dalil Registration** | Registered Dalil copy with Sub-Registrar seal | Buyer or Seller |
| **Mutation Applied** | Mutation application receipt, reference number | Seller |
| **Possession/Handover** | Handover certificate, keys photo, utility transfer docs | Both parties |

**Proof Upload Features**:
- Upload multiple files per step (max 5 files, 10MB each)
- Supported formats: PDF, JPG, PNG
- Preview capability for all parties
- Timestamp and uploader identity recorded
- Download option for transaction participants
- Proof validation status (uploaded, verified, rejected)

**Details**:
- The system SHALL validate file formats and sizes before upload
- The system SHALL store proofs in secure document vault
- The system SHALL notify all transaction parties when proof uploaded
- The system SHALL allow admin/verifier to mark proof as verified or request additional evidence
- Critical steps (Bayna, Dalil) SHALL not be marked complete without proof upload

**Business Value**: Proof uploads create complete digital audit trail, essential for dispute resolution and transaction confidence. Reduces reliance on physical document exchanges.

**Acceptance Criteria**:
- User can upload proofs from transaction timeline
- Proofs immediately visible to all transaction parties
- System validates and stores proofs securely
- Step completion dependent on proof upload for critical steps
- Proof verification tracked with timestamps

---

### 7.8 Payments

#### FR-33: Payment Methods (P0)
**Requirement**: The system SHALL support multiple payment methods through integrated payment gateway with security measures.

**Supported Payment Methods** (via SSLCOMMERZ or equivalent aggregator):
1. **Credit/Debit Cards**:
   - Visa, Mastercard, American Express
   - 3D Secure (3DS) authentication required
   
2. **Mobile Banking**:
   - bKash, Nagad, Rocket
   - OTP verification required
   
3. **Internet Banking**:
   - 20+ partner banks (City Bank, BRAC Bank, Dutch-Bangla Bank, etc.)
   - OTP/Token authentication

4. **Bank Transfer** (Manual verification):
   - Direct bank transfer with reference number
   - Admin verification required before order confirmation

**Security Requirements**:
- All card payments MUST use 3D Secure (3DS) or OTP verification
- Payment gateway MUST enforce TLS 1.2+ encryption
- System MUST NOT store card numbers (PCI DSS compliance)
- Payment credentials MUST be handled by gateway (hosted checkout)

**Details**:
- The system SHALL display all available payment methods during checkout
- The system SHALL highlight recommended methods (lowest fee, fastest)
- The system SHALL show estimated processing time for each method
- The system SHALL provide fallback options if primary gateway fails

**Business Value**: Multiple payment options increase checkout completion rates. Aggregator integration reduces individual bank integrations.

**Acceptance Criteria**:
- User can select from all available payment methods
- 3DS/OTP verification works for all methods
- Payment gateway charges clearly displayed
- Failed payments show clear error messages with retry option
- All payments logged with transaction ID and timestamp

---

#### FR-34: Secure Payment Records (P0)
**Requirement**: The system SHALL maintain comprehensive, tamper-proof payment records linked to orders with full audit trails.

**Payment Record Components**:
| Field | Purpose | Confidentiality |
|-------|---------|-----------------|
| **Payment ID** | Unique platform identifier | Internal + User |
| **Gateway Transaction ID** | Provider reference | Internal + User |
| **Order ID** | Linked order reference | Internal + User |
| **Amount & Currency** | Transaction value | Internal + User + Gateway |
| **Payment Method** | Card/MobileBanking/etc. | Internal + User |
| **Masked Card/Account** | Last 4 digits only | Internal + User |
| **Status** | PENDING/SUCCESS/FAILED/REFUNDED | Internal + User |
| **Timestamp** | Transaction date/time | Internal + User |
| **IP Address** | Security audit | Internal only |
| **Idempotency Key** | Duplicate prevention | Internal only |
| **Gateway Response** | Full response JSON | Internal only |

**Idempotency Implementation**:
- The system SHALL generate unique idempotency key for each payment attempt
- The system SHALL reject duplicate payment requests with same idempotency key
- The system SHALL maintain idempotency keys for 24 hours minimum

**Reconciliation**:
- The system SHALL provide daily reconciliation report (orders vs. payments)
- The system SHALL flag mismatches (payment without order, order without payment)
- The system SHALL maintain reconciliation status (RECONCILED/PENDING/MISMATCH)

**Details**:
- The system SHALL encrypt sensitive payment data at rest (AES-256)
- The system SHALL restrict payment record access to authorized roles only
- The system SHALL log all payment record access attempts
- The system SHALL maintain payment history indefinitely for audit/compliance

**Business Value**: Comprehensive payment records enable accurate financial reporting, dispute resolution, and regulatory compliance. Idempotency prevents double-charging.

**Acceptance Criteria**:
- Every payment has complete audit trail
- Idempotency prevents duplicate charges
- Reconciliation runs daily automatically
- Payment records accessible to authorized users only
- Audit logs track all access to payment data

---

#### FR-35: Buyer Protection / Dispute Hooks (P1)
**Requirement**: The system SHOULD support configurable buyer protection program with clear eligibility rules and dispute workflows.

**Protection Modes** (see Section 7.8.1 for detailed sub-requirements):
- **Mode A - Direct Pay (P0)**: Platform records only, no fund holding
- **Mode B - Platform Hold (P1)**: Funds held until milestone completion (gateway-dependent)

**Eligibility Criteria**:
- Buyer identity verified (minimum: phone OTP)
- Order linked to tracked transaction with recorded steps
- Evidence available (chat logs, proofs, appointment records)

**Claim Process**:
1. Buyer initiates dispute from order page (see FR-88 for full dispute lifecycle)
2. Buyer provides reason, evidence, and desired outcome
3. Platform reviews claim within 3 business days
4. Outcome: Refund/Partial Refund/Dismiss/Mediation

**Claim Windows**:
- **Property Orders**: Within 7 days of payment OR during active transaction
- **Service Orders**: Within 30 days of service completion
- No claims accepted after transaction marked complete by both parties

**Details**:
- The system SHALL display buyer protection policy summary at checkout
- The system SHALL clearly state what is and is not covered
- The system SHALL link disputes to payment records automatically
- The system SHALL freeze transaction step progress during active disputes

**Business Value**: Buyer protection builds marketplace trust and differentiates platform from informal transactions. Clear policies protect platform from abuse.

**Acceptance Criteria**:
- Buyer protection policy visible before payment
- Eligible users can file claims within time windows
- Claims reviewed within SLA (3 business days)
- Dispute outcomes clearly communicated to all parties
- Refunds processed within 7-14 days when approved

---

#### 7.8.1 Payment Protection Modes (Configurable)

##### Protection Mode A: Direct Pay (P0)
**Description**: Payment captured directly by gateway to seller/provider account. Platform records transaction but does not hold funds.

**Implementation**:
- Gateway API configured for direct capture to merchant/seller account
- Platform receives IPN/webhook notification of payment status
- Platform validates payment but does not process refunds directly
- Refunds handled via gateway refund API (where supported)

**Use Cases**:
- Rental payments
- Service provider payments
- Low-value transactions (< BDT 50,000)

**Pros**: Faster settlement for sellers, simpler compliance
**Cons**: Limited buyer protection, refunds dependent on gateway capabilities

---

##### Protection Mode B: Platform Hold / Milestone Hold (P1)
**Description**: Payment held by platform (via gateway escrow or platform account) until transaction milestone confirmed.

**Implementation** (requires gateway escrow support):
- Gateway API configured for platform as merchant of record
- Funds held in platform account/escrow
- Release triggered by milestone completion (e.g., Bayna signed, possession confirmed)
- Partial releases possible for multi-milestone transactions

**Use Cases**:
- High-value property transactions (> BDT 1 Crore)
- New buyer/seller with limited reputation
- Transactions flagged as risky

**Hold Release Triggers**:
- Automatic: Both parties mark milestone complete + proof uploaded
- Manual: Admin review approves release after evidence check
- Timeout: Auto-release after X days if no disputes (default: 30 days)

**Pros**: Strong buyer protection, reduces fraud
**Cons**: Slower seller settlement, requires legal/compliance review, gateway dependency

**Details**:
- The system SHALL clearly indicate hold mode before payment
- The system SHALL show estimated hold duration
- The system SHALL notify seller when funds released
- Platform SHALL comply with Bangladesh Bank regulations for fund holding

---

#### 7.8.2 Buyer Protection Policy (Platform Rules)

**Policy Summary**:
MSC Home provides limited buyer protection for eligible transactions to build marketplace trust. Protection is NOT insurance and does NOT cover all scenarios.

**What's Covered**:
- Fraudulent listings (property does not exist or ownership fake)
- Misrepresentation (property significantly different from listing)
- Service non-delivery (service provider fails to deliver as agreed)
- Document fraud (uploaded documents proven fake)

**What's NOT Covered**:
- Buyer's remorse (changed mind after legal agreement)
- Market value disputes (paid fair market price but unhappy)
- Cosmetic issues not disclosed in listing
- Delays caused by government processes (mutation, registration)
- Acts of nature or force majeure

**Evidence Requirements**:
For claim approval, buyer must provide:
- Complete chat/message history from platform
- All uploaded proof documents
- Payment receipts
- Appointment logs (if applicable)
- Transaction step timeline screenshots
- Third-party evidence (police report, lawyer statement, etc.)

**Outcomes**:
1. **Full Refund**: Fraud proven, no services delivered
2. **Partial Refund**: Partial services delivered, value adjustment warranted
3. **Rework/Redo**: Service provider corrects issues (service orders only)
4. **Dismissal**: Insufficient evidence or claim not covered

**Transparency Requirements**:
- The system SHALL display policy summary with expand/collapse sections
- The system SHALL use clear, non-legal language
- The system SHALL provide examples of covered vs. not covered scenarios
- The system SHALL show dispute statistics (% approved, average resolution time)

**Business Value**: Transparent protection policy builds trust while setting realistic expectations. Clear exclusions protect platform from frivolous claims.

---

### 7.9 Legal Support

#### FR-36: Legal Service Discovery (P0)
**Requirement**: The system SHALL enable users to discover and browse verified legal service providers specializing in real estate.

**Legal Service Categories**:
1. **Title Verification**: Deed/Dalil review, ownership chain verification
2. **Due Diligence**: Property background check, legal encumbrance search
3. **Document Drafting**: Bayna preparation, sale agreements, lease contracts
4. **Registration Support**: Sub-Registrar office representation, stamp duty calculation
5. **Dispute Resolution**: Land disputes, ownership conflicts, tenant issues
6. **General Consultation**: Legal advice, process explanation

**Provider Profiles Include**:
- BAR Council enrollment number
- Years of experience
- Practicing courts
- Specializations (land law, corporate real estate, etc.)
- Service areas (districts covered)
- Fee structure (consultation, per document, per case)
- Availability schedule
- Client reviews and ratings

**Search & Filter Options**:
- Location (district/area)
- Specialization
- Experience range
- Fee range
- Availability (urgent/scheduled)
- Verification status
- Rating threshold

**Details**:
- The system SHALL display lawyer verification status prominently
- The system SHALL show estimated response time
- The system SHALL provide comparison view for multiple lawyers
- The system SHALL highlight platform-recommended lawyers (P1 - algorithm-based)

**Business Value**: Centralized legal service discovery addresses major pain point from research (difficulty finding trustworthy lawyers). Verified providers reduce fraud risk.

**Acceptance Criteria**:
- User can search lawyers by location and specialization
- Lawyer profiles show all required information
- Verification badges clearly displayed
- User can initiate contact or booking directly from profile
- Search results sortable by rating, experience, fees

---

#### FR-37: Book Legal Agent (P0)
**Requirement**: The system SHALL allow users to book appointments with legal service providers through the platform.

**Booking Process**:
1. User selects lawyer from discovery or listing page
2. User selects service type (consultation, document review, etc.)
3. User views lawyer's available time slots
4. User selects date, time, and meeting mode (office visit, video call, phone)
5. User provides case details and uploads relevant documents
6. User pays consultation fee (if applicable) or books without payment
7. Lawyer receives notification and accepts/declines/reschedules
8. Confirmed booking added to both calendars with reminders

**Service Booking Types**:
- **Free Consultation** (15-30 min): Initial discussion, no payment
- **Paid Consultation** (per hour): Detailed advice, payment upfront
- **Document Review** (per document): Fixed fee per document type
- **Case Retainer**: Ongoing representation, payment schedule

**Details**:
- The system SHALL send booking confirmations to both parties
- The system SHALL send reminders 24 hours and 2 hours before appointment
- The system SHALL track no-show rates for both clients and lawyers
- The system SHALL allow rescheduling up to 24 hours before appointment

**Business Value**: Streamlined booking reduces friction and no-shows. Integrated payment increases lawyer trust in platform.

**Acceptance Criteria**:
- User can book lawyer in < 5 clicks
- Available time slots shown in real-time
- Payment processed before confirmation (for paid consultations)
- Both parties receive confirmation and reminders
- No-show tracking affects reputation scores

---

#### FR-38: Legal Case Tracking (P1)
**Requirement**: The system SHOULD provide basic case management features for ongoing legal engagements.

**Case Lifecycle**:
1. **Created**: User books lawyer for case representation
2. **Documents Uploaded**: Both parties upload relevant case documents
3. **In Progress**: Lawyer working on case
4. **Report Delivered**: Lawyer provides output (opinion letter, drafted agreement, etc.)
5. **Completed**: User confirms satisfactory completion
6. **Disputed**: Issue with service quality (links to dispute system)

**Case Dashboard Features**:
- Case status with progress indicators
- Document upload area (client and lawyer both can add)
- Milestone tracking (e.g., court filing done, hearing scheduled)
- Message thread specific to case
- Fee tracking (retainer, additional charges)
- Deliverable tracking (opinions, drafts, registrations)

**Details**:
- The system SHALL send notifications for case status updates
- The system SHALL allow lawyers to request additional information via case thread
- The system SHALL provide case completion certificate upon closure
- The system SHALL maintain case history for minimum 3 years

**Business Value**: Case tracking keeps clients informed and reduces "Where is my case?" inquiries. Organized documentation helps dispute resolution.

**Acceptance Criteria**:
- Both parties can view case status anytime
- Documents organized and searchable
- Milestone updates notify both parties
- Case completion requires client confirmation
- Case history preserved and downloadable

---

### 7.10 Financial Support

#### FR-39: Financial Service Discovery (P0)
**Requirement**: The system SHALL enable users to discover and browse verified financial service providers offering property-related services.

**Financial Service Categories**:
1. **Home Loans/Mortgages**: Banks and NBFIs offering property financing
2. **Loan Consulting**: Advisors helping with loan applications and approvals
3. **Property Valuation**: Professional valuers for loan/investment purposes
4. **Insurance**: Property insurance, title insurance
5. **Financial Planning**: Investment advice for real estate portfolio

**Provider Profiles Include**:
- Institution name and license
- Services offered
- Loan products (interest rates, tenure, eligibility)
- Processing time and fees
- Required documents
- Approval rates (if shared)
- Client reviews and ratings
- Contact information

**Search & Filter Options**:
- Institution type (Bank/NBFI/Consultant/Insurance)
- Loan amount range
- Property type supported
- Interest rate range
- Tenure options
- Service area (branches/coverage)

**Details**:
- The system SHALL display institutional verification status
- The system SHALL show current interest rates (updated monthly minimum)
- The system SHALL provide loan EMI calculator
- The system SHALL highlight promotional offers (reduced rates, fee waivers)

**Business Value**: Integrated financial services complete the property transaction journey. Verified providers reduce loan scam risks highlighted in research.

**Acceptance Criteria**:
- User can search financial providers by location and service type
- Provider profiles show current loan products
- Verification status clearly displayed
- User can compare multiple loan products
- EMI calculator accessible on all loan product pages

---

#### FR-40: Loan Assistance Workflow (P1)
**Requirement**: The system SHOULD support loan application tracking and communication workflow between users and financial providers.

**Loan Assistance Process**:
1. **Request**: User submits loan inquiry with basic details (property value, desired loan amount)
2. **Eligibility Check**: Provider reviews and provides preliminary eligibility feedback
3. **Document Submission**: User uploads required documents (NID, salary certificates, bank statements, property docs)
4. **Application Processing**: Provider processes formal application
5. **Status Updates**: Provider updates status (under review, more docs needed, approved, rejected)
6. **Approval**: Loan approved with terms (amount, rate, tenure)
7. **Disbursement Coordination**: Final docs signed, loan disbursement scheduled

**Loan Request Dashboard**:
- Request status with stage indicators
- Document checklist (submitted vs. pending)
- Provider messages and queries
- Eligibility estimation (if provided)
- Approval terms (when approved)
- Timeline estimates

**Details**:
- The system SHALL send notifications for each status change
- The system SHALL provide document upload reminders
- The system SHALL track average processing time per provider (for transparency)
- The system SHALL allow users to submit requests to multiple providers simultaneously

**Business Value**: Guided loan workflow reduces application complexity and increases approval rates. Transparent tracking reduces user anxiety.

**Acceptance Criteria**:
- User can submit loan request with basic info
- Document checklist shows what's needed
- Status updates notify user in real-time
- Multiple loan requests managed in one dashboard
- Processing time estimates shown per provider

---

### 7.11 Reviews & Reputation

#### FR-41: Mutual Rating (P0)
**Requirement**: The system SHALL enable mutual rating between buyers and sellers after transaction completion.

**Rating Components**:
| Component | Scale | Applies To |
|-----------|-------|------------|
| **Overall Rating** | 1-5 stars (required) | Both parties |
| **Communication** | 1-5 stars | Both parties |
| **Accuracy** | 1-5 stars | Seller (was listing accurate?) |
| **Professionalism** | 1-5 stars | Both parties |
| **Timeliness** | 1-5 stars | Both parties (meeting deadlines?) |
| **Would Recommend** | Yes/No | Both parties |

**Review Content**:
- Free-text review (100-1000 characters recommended)
- Pros and cons (structured, optional)
- Photo uploads (optional, max 5)
- Anonymous option (display as "Verified Buyer/Seller" without name)

**Rating Rules**:
- Rating window opens when transaction marked complete
- Rating window closes 30 days after completion
- Both parties rate independently (reviews revealed simultaneously to avoid bias)
- One rating per transaction per party
- Cannot edit rating after submission (prevent gaming)

**Details**:
- The system SHALL prompt both parties to rate when transaction complete
- The system SHALL display aggregated ratings on user profiles
- The system SHALL flag suspicious review patterns (all 5-star, repeated text, etc.)
- The system SHALL allow reporting of fake/abusive reviews

**Business Value**: Mutual ratings build accountability and reputation system. Post-transaction feedback improves platform quality.

**Acceptance Criteria**:
- Both parties can submit ratings independently
- Ratings revealed simultaneously
- Aggregated ratings displayed on profiles
- Review submission increases profile completion percentage
- Suspicious patterns flagged for admin review

---

#### FR-42: Listing/Agent Reviews (P0)
**Requirement**: The system SHALL allow users to review individual property listings and service provider agents.

**Listing Reviews** (Pre-Transaction):
- Overall rating (1-5 stars)
- Accuracy rating (listing vs. reality)
- Location rating (area, accessibility)
- Value for money rating
- Free-text review with photos
- Helpful/Not Helpful votes by other users

**Agent/Professional Reviews** (Post-Interaction):
- Overall rating (1-5 stars)
- Responsiveness rating
- Knowledge/Expertise rating
- Professionalism rating
- Free-text review
- Would recommend (Yes/No)

**Review Eligibility**:
- **Listing Reviews**: After viewing appointment or transaction initiation
- **Agent Reviews**: After appointment completion or transaction involvement

**Details**:
- The system SHALL prevent spam reviews (max 1 review per user per listing)
- The system SHALL display verified buyer/engaged user badges on reviews
- The system SHALL sort reviews by most helpful (upvotes) or most recent
- The system SHALL allow filtering reviews by star rating

**Business Value**: Pre-transaction reviews help buyers make informed decisions. Agent reviews drive service quality improvement.

**Acceptance Criteria**:
- User can review listing after viewing/interaction
- Review submission requires eligibility verification
- Reviews sortable and filterable
- Helpful/Not Helpful voting works
- Verified badges shown on eligible reviewers

---

#### FR-43: Feedback Tools (P1)
**Requirement**: The system SHOULD allow recipients to respond to reviews and provide issue resolution mechanisms.

**Response Features**:
- Seller/Agent can post public response to reviews
- Response limited to 500 characters
- One response per review
- Response timestamp shown
- Cannot delete review or response (edit window: 24 hours only)

**Issue Resolution Workflow**:
1. Reviewer submits review with negative rating/complaint
2. System notifies recipient and suggests private resolution
3. Recipient can offer private resolution (refund, service redo, compensation)
4. If resolution accepted, reviewer can update review or add positive note
5. If resolution rejected, review stands as-is

**Review Moderation**:
- Users can report reviews as fake, abusive, or violating guidelines
- Admin reviews reported reviews within 48 hours
- Proven fake reviews removed with explanation
- Abusive reviews edited to remove offensive content

**Details**:
- The system SHALL encourage private resolution before public response
- The system SHALL display resolution status badge on reviews ("Issue Resolved")
- The system SHALL track resolution success rate for sellers/agents
- The system SHALL prevent review spam through rate limiting

**Business Value**: Response and resolution tools allow feedback improvement and dispute de-escalation. Moderation maintains review credibility.

**Acceptance Criteria**:
- Recipients can respond to all reviews
- Private resolution workflow available
- Resolved issues show badge on reviews
- Reported reviews reviewed within 48 hours
- Review moderation actions logged and auditable

---

*[End of FR-27 to FR-43 - Batch 2 Complete]*
