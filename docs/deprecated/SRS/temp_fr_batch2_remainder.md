### 7.2 User Profile & Professional Data

#### FR-5: Profile Management (P0)
**Requirement**: The system SHALL allow all users to create and maintain personal profiles.

**Details**:
- **Required Fields**: Full name, primary phone number, primary email
- **Optional Fields**: Secondary phone, address, profile photo, bio/description
- The system SHALL validate Bangladesh phone numbers (+880 format)
- The system SHALL allow profile photo upload (max 5MB, formats: JPG, PNG)
- The system SHALL display profile completion percentage

**Business Value**: Complete profiles increase trust and facilitate communication between parties.

**Acceptance Criteria**:
- User can update all profile fields
- Phone number validated with OTP before saving
- Profile photo displayed across platform (listings, chats, reviews)
- Incomplete profiles show progress indicator

---

#### FR-6: Professional Profile (P0)
**Requirement**: The system SHALL capture comprehensive professional data for verified professionals.

**Professional Data Categories**:

| Category | Required Fields | Purpose |
|----------|----------------|---------|
| **Financial Details** | Bank name, account number, account holder name, routing number | Payout processing |
| **Tax Information** | BIN/TIN number, tax certificate upload | Compliance and verification |
| **Identity Documents** | NID/Passport number, NID/Passport scan | Identity verification |
| **Professional Credentials** | License numbers, certification documents | Professional verification |

**Role-Specific Requirements**:
- **URA-Certified Agent**: URA certificate, agent license, business address
- **Lawyer**: BAR Council certificate number, practicing court, years of experience
- **Financial Officer**: Institution name, employee ID, institution credential report
- **Real Estate Developer**: Company registration certificate, ongoing projects list

**Details**:
- The system SHALL store sensitive financial data with field-level encryption
- The system SHALL display professional profile completion checklist
- The system SHALL allow document uploads for each credential type (max 10MB per file)

**Business Value**: Comprehensive professional data enables thorough verification and builds user trust. Clear requirements reduce verification delays.

**Acceptance Criteria**:
- Professional user can complete all role-specific fields
- System validates BIN/TIN format
- Uploaded documents linked to verification requests
- Professional profile completion shown as percentage
- Missing required fields highlighted in checklist

---

#### FR-7: Reputation Summary (P1)
**Requirement**: The system SHALL display comprehensive reputation metrics on professional profiles.

**Reputation Metrics**:
1. **Average Rating**: Calculated from all reviews (1-5 stars)
2. **Total Reviews**: Count of completed reviews
3. **Response Time**: Median response time for chats and appointments (7-day and 30-day averages)
4. **Response Rate**: Percentage of inquiries responded to within 24 hours
5. **Verification Badges**: All earned verification types displayed prominently
6. **Active Listings**: Current number of active property listings
7. **Successful Transactions**: Count of completed transactions

**Details**:
- The system SHALL update reputation metrics in real-time or near-real-time (< 5 minutes delay)
- The system SHALL display response time metrics only after minimum 5 interactions
- The system SHALL allow users to filter professionals by reputation criteria

**Business Value**: Transparent reputation metrics help buyers/sellers choose reliable professionals, increasing transaction success rates and reducing platform disputes.

**Acceptance Criteria**:
- Professional profile displays all reputation metrics
- Metrics updated within 5 minutes of new reviews/responses
- "New Professional" label shown for profiles with < 5 interactions
- Reputation metrics visible in search results and professional directory

---

### 7.3 Verification & Trust (Tiered System)

> **Overview**: MSC Home implements a multi-tiered verification system with visible trust signals (badges) across listings and profiles. This addresses the critical Bangladesh market need for fraud prevention and trust-building.

#### FR-8: Submit Verification Request (P0)
**Requirement**: The system SHALL allow users to submit verification requests with supporting documents.

**Details**:
- Users SHALL be able to request one or more verification types simultaneously
- Each verification request SHALL include:
  - Verification type selection (Identity, Professional, Company, Property Ownership)
  - Required document uploads (type-specific)
  - Declaration/consent checkboxes
  - Submission timestamp
- The system SHALL validate document formats (PDF, JPG, PNG) and size limits (10MB per file)
- The system SHALL generate unique verification request ID for tracking

**Business Value**: Streamlined verification submission reduces friction while ensuring all necessary documents are collected upfront, reducing back-and-forth delays.

**Acceptance Criteria**:
- User can select multiple verification types in one request
- System validates all required documents uploaded before submission
- Verification request ID generated and displayed to user
- User receives confirmation notification with estimated review timeframe
- Incomplete requests saved as drafts

---

#### FR-9: Verification Review Workflow (P0)
**Requirement**: The system SHALL provide Admin/Verifier tools to review and approve/reject verification requests with full audit trails.

**Workflow States**:
1. **SUBMITTED**: Initial state after user submission
2. **UNDER_REVIEW**: Assigned to verifier for review
3. **CHANGES_REQUESTED**: Verifier needs additional information/documents
4. **APPROVED**: Verification successful, badge issued
5. **REJECTED**: Verification failed, reason provided

**Details**:
- Admin/Verifier SHALL have dedicated review queue sorted by submission date
- The system SHALL display all submitted documents with preview capability
- Verifier SHALL provide rejection reason from predefined categories + free-text notes
- The system SHALL log all review actions with verifier identity, timestamp, and decision
- The system SHALL notify user of review outcome within 1 hour of decision

**Business Value**: Structured review workflow ensures consistent verification quality and provides transparency to users. Audit trails support dispute resolution.

**Acceptance Criteria**:
- Verifier can approve/reject with required reason selection
- All review actions logged with full audit trail
- User notified of outcome with next steps (if changes requested)
- Average review completion time tracked and reported
- Rejected requests show clear reasons and resubmission options

---

#### FR-10: Verified Badge Display (P0)
**Requirement**: The system SHALL display verified badges prominently on user profiles and property listings.

**Badge Display Rules**:
- Verified badges SHALL appear on:
  - User profile header
  - Property listing cards (search results)
  - Property listing detail page
  - Chat interface (next to username)
  - Review/rating displays
- Badge SHALL show verification type on hover/tap
- Badge SHALL display verification date
- Multiple badges SHALL be displayed together (e.g., "Identity + Professional Verified")

**Details**:
- The system SHALL use consistent badge design across platform
- The system SHALL provide badge legend/explanation in help section
- The system SHALL allow users to click badges to view verification details (verification date, type)

**Business Value**: Prominent badge display increases user confidence and incentivizes verification. Clear badge types help users understand trust levels quickly.

**Acceptance Criteria**:
- Verified badge visible within 5 minutes of approval
- Badge shows verification type on hover
- Badge design consistent across all pages
- Unverified users show "Not Verified" status (not hidden)

---

#### 7.3.1 Verification Tiers (Badge Types)

##### FR-10-T1: Identity Verified Badge (P0)
**Requirement**: The system SHALL issue Identity Verified badge after successful identity verification.

**Verification Process**:
1. **Manual Verification** (MVP/P0):
   - User uploads NID/Passport front and back
   - User uploads selfie photo
   - Verifier performs manual comparison
   - Verifier checks document authenticity indicators
   
2. **e-KYC Verification** (P1 - Optional enhancement):
   - Integration with Porichoy or equivalent e-KYC provider
   - Automated NID verification via API
   - Fallback to manual if e-KYC fails/unavailable

**Business Value**: Identity verification is foundational for all other trust features. Reduces fraud and builds marketplace confidence.

**Acceptance Criteria**:
- User can submit NID/Passport + selfie
- Manual verification completed within 48 hours
- Badge issued immediately upon approval
- Verification valid for 2 years, requires renewal

---

##### FR-10-T2: Professional Verified Badge (P0/P1)
**Requirement**: The system SHALL issue Professional Verified badge for certified professionals with regulatory credentials.

**Supported Professional Types**:

1. **URA-Certified Agent (P0)** - Distinct credential:
   - URA certificate number and validity
   - Agent license document
   - Business address verification
   - Professional insurance proof (if applicable)

2. **BAR Council Lawyer (P0)**:
   - BAR Council enrollment certificate
   - Practicing license number
   - Court authorization documents

3. **Financial Institution Officer (P1)**:
   - Employment verification letter from recognized financial institution
   - Institution credential report
   - Professional designation proof

4. **Other Professional Bodies (P1)**:
   - Template-based verification for additional professions
   - Regulatory body certification
   - Credential documents

**Business Value**: Professional verification ensures service provider quality and regulatory compliance. URA certification specifically addresses agent credibility concerns from market research.

**Acceptance Criteria**:
- Each professional type has distinct verification checklist
- URA certificate validated against URA database (manual or API if available)
- Professional badge shows specific credential type
- Verification renewed annually or per regulatory requirement

---

##### FR-10-T3: Company Verified Badge (P0)
**Requirement**: The system SHALL issue Company Verified badge for registered businesses providing real estate services.

**Verification Requirements**:
- BIN/TIN certificate
- Trade license (valid and current)
- Company registration documents
- Bank account details matching company name
- Office address verification (document or field visit)

**Applicable Entity Types**:
- Real estate development companies
- Property management firms
- Legal firms offering real estate services
- Financial institutions offering property loans

**Business Value**: Company verification protects users from unregistered operators and builds trust in business listings/projects.

**Acceptance Criteria**:
- Company can submit all required business documents
- BIN/TIN validated against government database (manual)
- Trade license validity checked
- Company badge shows registration year
- Verification renewed annually

---

##### FR-10-T4: Property Ownership Verified Badge (P0)
**Requirement**: The system SHALL issue Property Ownership Verified badge for listings with verified ownership documentation.

**Verification Requirements**:
| Document Type | Purpose | Verification Method |
|---------------|---------|---------------------|
| **Deed/Dalil** | Legal ownership proof | Manual review by legal verifier |
| **Mutation/Namjari** | Government record update confirmation | Cross-reference with user-provided portal references |
| **Tax Receipts** | Current tax payment evidence | Receipt verification (manual) |
| **Allotment Letter** (for new developments) | Developer allocation proof | Developer credential check |

**Details**:
- The system SHALL link ownership verification to specific property listing
- The system SHALL store verified documents in secure document vault
- The system SHALL display verification date on listing
- The system SHALL require re-verification if ownership documents change

**Business Value**: Ownership verification is the most critical trust signal for property buyers, directly addressing fraud concerns. Reduces transaction abandonment rates.

**Acceptance Criteria**:
- Listing shows "Ownership Verified" badge after approval
- Badge links to verification date and document types verified
- Ownership changes trigger re-verification requirement
- Verified listings prioritized in search ranking

---

##### FR-10-T5: Listing Verified Badge (P0)
**Requirement**: The system SHALL issue Listing Verified badge for property listings meeting completeness and accuracy thresholds.

**Verification Checks**:
1. **Ownership Verification**: Property ownership documents verified (FR-10-T4)
2. **Address Verification**: Location pin placed accurately, address matches documents
3. **Completeness Score**: Listing accuracy score ≥ 80% (see FR-18-LS)
4. **Media Quality**: Minimum photo count met (10+ for apartments, 5+ for land)
5. **Contact Verification**: Listing owner/agent identity verified

**Details**:
- The system SHALL automatically evaluate listing against verification criteria
- The system SHALL display specific failed criteria to listing owner
- The system SHALL allow re-submission after corrections
- Listing verification SHALL be valid for 6 months, requires renewal for active listings

**Business Value**: Comprehensive listing verification ensures high-quality marketplace inventory. Reduces buyer time waste on incomplete or fraudulent listings.

**Acceptance Criteria**:
- Listing automatically evaluated upon submission
- Failed criteria clearly displayed with correction guidance
- Verified listing badge displayed prominently in search results
- Verification expires after 6 months for active listings

---

##### FR-10-T6: Reputation Verified Badge (P1)
**Requirement**: The system SHALL issue Reputation Verified badge (e.g., "Trusted Seller", "Top Agent") for users meeting reputation thresholds.

**Threshold Requirements**:
| Badge Type | Requirements |
|------------|--------------|
| **Trusted Seller** | ≥ 3 completed transactions, ≥ 4.5 star rating, 0 unresolved disputes |
| **Top Agent** | ≥ 10 completed transactions, ≥ 4.7 star rating, < 2-hour avg response time |
| **Verified Reviewer** | ≥ 5 completed transactions, consistent review activity |

**Details**:
- The system SHALL evaluate reputation thresholds daily
- The system SHALL automatically grant/revoke badges based on current metrics
- The system SHALL display badge earning criteria in help section
- Users MAY lose reputation badges if metrics fall below thresholds

**Business Value**: Reputation badges incentivize quality service and reward consistent performers. Creates aspirational goals for professionals.

**Acceptance Criteria**:
- System automatically evaluates reputation daily
- Badge granted within 24 hours of meeting criteria
- Badge revoked if user falls below threshold for 30 consecutive days
- Badge criteria clearly documented and visible to all users

---

#### 7.3.2 Credential Reports from Financial/Non-Financial Institutes

##### FR-10a: Credential Report Upload (P1)
**Requirement**: The system SHALL allow professionals and companies to upload credential reports issued by recognized institutions.

**Supported Credential Types**:

**Financial Institute Reports**:
- Bank statements (last 6 months)
- Solvency certificates
- Loan eligibility confirmations
- Credit facility letters

**Non-Financial Institute Reports**:
- Employer verification letters
- Membership/certification from professional bodies
- Training institute completion certificates
- Educational credentials

**Details**:
- The system SHALL validate report issuer against approved registry (FR-10b)
- The system SHALL extract key information: issuer name, issue date, validity period, credential type
- The system SHALL display credential status on professional profile ("Solvency Certified", "Employment Verified")
- Credential reports SHALL have expiry dates requiring renewal

**Business Value**: Institutional credentials add additional trust layers beyond basic verification. Particularly valuable for financial officers and corporate agents.

**Acceptance Criteria**:
- User can upload multiple credential reports
- System validates issuer against approved registry
- Credential status displayed on profile with verification date
- Expired credentials marked and require renewal

---

##### FR-10b: Credential Issuer Registry (P1)
**Requirement**: The system SHALL maintain an Admin-managed registry of approved credential issuers with verification rules.

**Registry Contents**:
| Issuer Type | Examples | Verification Method |
|-------------|----------|---------------------|
| **Banks** | Dutch-Bangla Bank, BRAC Bank, City Bank | Manual verification of bank seal/signature |
| **Professional Bodies** | URA, BAR Council, ICAB | Certificate number validation |
| **Training Institutes** | REHAB Training Center, BPATC | Institute seal verification |
| **Employers** | Listed companies, govt organizations | Employment verification call/email |

**Details**:
- Admin SHALL add/remove issuers with approval workflow
- Each issuer entry SHALL include: issuer name, type, verification method, required document elements
- The system SHALL support manual verification for all issuer types (API integration optional P2)

**Business Value**: Centralized issuer registry ensures consistent credential verification and prevents fraudulent claims.

**Acceptance Criteria**:
- Admin can add new issuers with verification rules
- System validates credential documents against issuer requirements
- Unrecognized issuers flagged for manual review
- Registry searchable by issuer name and type

---

#### 7.3.3 Optional e-KYC Provider Integration

##### FR-11: e-KYC Provider Check (P1)
**Requirement**: The system SHOULD integrate with Bangladesh e-KYC providers for automated identity verification, with manual fallback.

**Integration Requirements**:
- **Primary Provider**: Porichoy (National Identity Verification API)
- **Fallback**: Manual verification process
- **Scope**: NID verification only (no automated scraping of government portals)

**e-KYC Verification Flow**:
1. User consents to e-KYC check
2. System calls Porichoy API with NID number and DOB
3. Porichoy returns verification result:
   - **MATCH**: Identity verified, badge issued automatically
   - **NO_MATCH**: Falls back to manual verification
   - **ERROR/TIMEOUT**: Falls back to manual verification
4. System logs all API attempts for audit

**Details**:
- The system SHALL NOT bypass or scrape government identity portals
- The system SHALL store only verification result (PASS/FAIL), not personal data from provider
- Manual verification SHALL be available at all times as fallback
- e-KYC fee (if applicable) MAY be passed to user or absorbed by platform

**Business Value**: Automated e-KYC reduces verification time from 48 hours to < 5 minutes, improving user experience and reducing operational costs.

**Acceptance Criteria**:
- User can opt-in to e-KYC verification
- Successful e-KYC grants Identity Verified badge immediately
- Failed e-KYC falls back to manual without user re-submission
- All API calls logged with timestamp and result
- Manual verification always available regardless of e-KYC status

---

### 7.4 Listings & Media

#### FR-12: Create Listing (P0)
**Requirement**: The system SHALL allow verified users to create property listings with comprehensive details, media, and documents.

**Core Listing Fields**:
| Field Category | Required Fields | Optional Fields |
|----------------|----------------|-----------------|
| **Location** | Division, district, area/thana, address | GPS coordinates, landmark, mouza (for land) |
| **Property Details** | Property type, size, price | Bedrooms, bathrooms, floors, facing |
| **Terms** | Listing type (sale/rent), price | Negotiable flag, possession date, payment terms |
| **Media** | Minimum 3 photos | Virtual tour link, video, floor plan |
| **Documents** | Ownership proof | Tax receipts, NOC, utility bills |

**Property Types Supported** (see Section 7.4.1 for full matrix):
- Apartment/Flat (Buy/Sell)
- Apartment/Flat (Rent)
- Land (Buy/Sell)
- Commercial Property
- Project/Development

**Details**:
- The system SHALL validate required fields based on property type
- The system SHALL compute Listing Accuracy Score during creation (see FR-18-LS)
- The system SHALL save incomplete listings as drafts
- The system SHALL guide users with field-level help text and examples

**Business Value**: Comprehensive listing creation ensures high-quality inventory and reduces buyer inquiry friction. Draft functionality prevents user frustration from incomplete sessions.

**Acceptance Criteria**:
- User can create listing with all required fields
- System shows real-time accuracy score during creation
- Draft listings saved automatically every 2 minutes
- Property type-specific validation applied
- Listing preview available before publication

---

#### FR-13: Listing Verification (P0)
**Requirement**: The system SHALL verify listings for ownership and information accuracy before allowing publication.

**Verification Types**:

1. **Automated Checks** (Immediate):
   - Required field completeness
   - Media quality (resolution, count)
   - Price reasonableness (outlier detection)
   - Location pin validation

2. **Manual Verification** (24-48 hours):
   - Ownership document review
   - Address verification
   - Duplicate listing check
   - Fraud indicator assessment

**Verification Workflow**:
1. User submits listing
2. System runs automated checks immediately
3. If automated checks pass, listing enters manual review queue
4. Verifier reviews documents and approves/rejects/requests changes
5. User notified of outcome
6. Approved listings published immediately

**Details**:
- The system SHALL display verification status on listing dashboard
- The system SHALL provide clear guidance for rejected listings
- The system SHALL allow resubmission after corrections
- Verified listings SHALL display "Listing Verified" badge

**Business Value**: Two-tiered verification balances speed (automated) with thoroughness (manual), ensuring marketplace quality without frustrating users with delays.

**Acceptance Criteria**:
- Automated checks complete within 30 seconds
- Manual verification completed within 48 hours (business days)
- User receives real-time status updates
- Rejection reasons clearly stated with correction guidance
- Verification queue tracked with SLA reporting

---

#### FR-14: Virtual Tours (P1)
**Requirement**: The system SHOULD support virtual tour integration for immersive property viewing.

**Support Options**:
1. **External Link**: Link to Matterport, Google Street View, or YouTube 360° tours
2. **Embedded Player**: Iframe embedding of supported virtual tour platforms
3. **Native Upload** (P2): Direct 360° photo/video upload with viewer

**Details**:
- The system SHALL validate virtual tour URLs before saving
- The system SHALL display virtual tour prominently on listing detail page
- Virtual tours SHALL be optional but encouraged (increases accuracy score)
- The system SHOULD track virtual tour view counts

**Business Value**: Virtual tours reduce unnecessary physical visits by 30-40%, saving time for both buyers and sellers. Increases buyer confidence in listings.

**Acceptance Criteria**:
- User can add virtual tour link during listing creation/editing
- System validates URL accessibility
- Virtual tour displayed prominently on listing page
- Virtual tour views tracked and displayed to listing owner

---

#### FR-15: Favorites (P0)
**Requirement**: The system SHALL allow users to save listings to favorites for later viewing.

**Details**:
- Users SHALL save unlimited listings to favorites
- The system SHALL display favorite count on listing cards (optional - may influence seller)
- The system SHALL notify users if favorited listings have price changes or status updates
- Users SHALL organize favorites into custom collections/folders (P1 enhancement)
- Favorites SHALL be accessible from user dashboard

**Business Value**: Favorites enable buyer comparison and decision-making over time. Provides engagement metric for platform analytics.

**Acceptance Criteria**:
- User can add/remove listings from favorites with one click
- Favorites accessible from user profile menu
- User notified of price drops on favorited listings
- Favorite status persists across devices (cloud sync)

---

#### FR-16: Document Vault (P0)
**Requirement**: The system SHALL provide secure document storage for sensitive property and identity documents with strict access controls.

**Vault Document Categories**:
| Category | Document Types | Access Level |
|----------|----------------|--------------|
| **Property Ownership** | Deeds/Dalil, Mutation/Namjari, Tax receipts | Owner + Approved Requesters |
| **Allotment/Allocation** | Developer allotment letters, booking receipts | Owner + Approved Requesters |
| **Identity Documents** | NID/Passport scans, professional licenses | Owner + Verifiers only |
| **Financial Documents** | Bank statements, solvency certificates | Owner + Admin (with audit) |

**Access Control Rules** (See Section 7.22.2 for detailed FR-79 to FR-82):
- All documents private by default
- Access granted only via explicit request + approval workflow (FR-79, FR-80)
- Time-bound access grants with expiry
- Full audit logging of all access attempts

**Details**:
- The system SHALL encrypt documents at rest using AES-256
- The system SHALL encrypt documents in transit using TLS 1.3
- The system SHALL support document formats: PDF, JPG, PNG (max 10MB per file)
- The system SHALL generate secure time-limited URLs for document viewing
- The system SHALL implement watermarking for shared documents (P1)

**Business Value**: Secure document vault is critical differentiator for MSC Home, addressing primary user concern about document safety. Builds trust and encourages verification.

**Acceptance Criteria**:
- Documents encrypted at rest and in transit
- Access requests tracked with full audit trail
- Unauthorized access attempts blocked and logged
- Document URLs expire after configured time (default: 24 hours)
- Vault accessible only to authenticated users

---

#### FR-17: Unit Converter (P1)
**Requirement**: The system SHOULD provide real-time conversion between common Bangladeshi land measurement units.

**Supported Conversions**:
| From Unit | To Units |
|-----------|----------|
| Square Feet (Sqft) | Katha, Decimal, Shotok, Square Meter |
| Katha | Square Feet, Decimal, Shotok, Acre |
| Decimal | Square Feet, Katha, Shotok, Acre |
| Shotok | Square Feet, Katha, Decimal |

**Conversion Formulas** (Dhaka standard):
- 1 Katha = 720 Sqft (approx.)
- 1 Decimal = 435.6 Sqft
- 1 Shotok = 1 Decimal
- 1 Acre = 100 Decimal = 43,560 Sqft

**Details**:
- The system SHALL provide inline converter widget on listing creation/view pages
- The system SHALL display converted values in real-time as user types
- The system SHOULD note regional variations (Dhaka vs. other regions)
- Listing SHALL store size in multiple units for search compatibility

**Business Value**: Unit conversion removes confusion and enables users to compare properties easily across different measurement systems. Critical for land transactions.

**Acceptance Criteria**:
- Converter widget accessible on all listing pages
- Real-time conversion with < 100ms latency
- Conversion accuracy validated against official standards
- Regional variation notes displayed where applicable

---

#### FR-18: Market Value Guidance (P1)
**Requirement**: The system SHOULD provide market value guidance for properties with clear disclaimers and data source transparency.

**Value Guidance Sources**:
1. **Agent Manual Inputs**: URA-certified agents can provide area-wise price guidance
2. **Platform Analytics** (P2): Historical transaction data analysis
3. **Third-Party Data** (P2): Integration with market research firms

**Guidance Display Rules**:
- **Disclaimer Required**: "This is guidance only, not professional valuation"
- **Data Source Shown**: "Based on 15 recent transactions in this area"
- **Date Range**: "Data from last 6 months"
- **Confidence Level**: "Low/Medium/High confidence based on data volume"

**Details**:
- The system SHALL NOT present guidance as definitive valuation
- The system SHALL encourage users to consult professional valuers
- The system SHALL update guidance monthly or when sufficient new data available
- Guidance SHALL be optional to display on listings

**Business Value**: Market guidance helps set realistic buyer expectations and reduces price negotiation friction. Transparency about data sources builds trust.

**Acceptance Criteria**:
- Guidance displayed with prominent disclaimer
- Data source and date range clearly shown
- Confidence level indicated
- User can dismiss or hide guidance
- Guidance updated at least monthly

---

#### 7.4.1 Property Type Matrix

**Overview**: MSC Home supports multiple property types with specific required fields, documents, and step tracking templates. This addresses both apartment-focused positioning and land transaction workflows from the research phase.

| Property Type | Required Listing Fields (Minimum) | Required Documents (Minimum) | Step Tracking Template |
|---------------|----------------------------------|------------------------------|------------------------|
| **Apartment/Flat (Buy/Sell)** | Address/area, floor/unit, size (sqft), bedrooms/bathrooms, price, utilities, handover status, minimum 10 photos | Ownership proof OR allotment documents, HOA/utility bills (if available) | Offer → Booking/Bayna (optional) → Handover/Registration support |
| **Apartment/Flat (Rent)** | Rent amount, deposit, lease duration, move-in date, building rules, minimum 8 photos | Landlord proof (NID + ownership proof where possible) | Inquiry → Viewing → Agreement → Move-in |
| **Land (Buy/Sell)** | Mouza, Dag/Khatian numbers, size (katha/decimal), location pin/map, asking price, land type (residential/agricultural/commercial), access road status | Dalil/Deed, Mutation/Namjari, Tax receipts, Land development documents (if any) | Offer → Bayna → Deed Transfer → Mutation Follow-up |
| **Commercial/Project** | Project/company profile, unit inventory, pricing model, handover timeline, construction status | Project approvals/ownership documents, Company documents (BIN/TIN, Trade License) | Offer → Booking → Installment Tracking (optional P2) |

**Notes**:
- **Verified Land List**: Land ownership verification supported via Document Vault + Verification Checks + Government Portal Link-outs (see Section 7.20)
- **Property Type Validation**: System validates presence of required fields per property type
- **Listing Accuracy Score**: Computed based on property-type-specific completeness (see FR-18-LS below)

---

#### 7.4.2 Listing Accuracy Score (Completeness + Evidence)

##### FR-18-LS: Listing Accuracy Score Calculation (P0)
**Requirement**: The system SHALL compute and display a Listing Accuracy Score for all listings based on completeness and evidence strength.

**Score Components**:

| Component | Weight | Criteria |
|-----------|--------|----------|
| **Field Completeness** | 40% | Percentage of required + recommended fields filled |
| **Media Quality** | 25% | Photo count, resolution, virtual tour presence |
| **Document Evidence** | 25% | Ownership/identity documents uploaded and verified |
| **Verification Status** | 10% | Listing verification checks passed |

**Scoring Formula**:
$$\text{Accuracy Score} = (0.4 \times \text{Field%}) + (0.25 \times \text{Media%}) + (0.25 \times \text{Doc%}) + (0.1 \times \text{Verify%})$$

Where each percentage is calculated as:
- **Field%**: (Filled Fields / Total Expected Fields) × 100
- **Media%**: Based on photo count and quality thresholds
- **Doc%**: (Uploaded Required Docs / Total Required Docs) × 100
- **Verify%**: 100 if verified, 0 if not

**Score Thresholds**:
- **90-100%**: Excellent (green badge)
- **70-89%**: Good (blue badge)
- **50-69%**: Needs Improvement (yellow badge)
- **< 50%**: Incomplete (red badge)

**Details**:
- The system SHALL display accuracy score prominently on listing cards and detail pages
- The system SHALL provide actionable checklist showing missing items
- Score SHALL impact search ranking (higher scores ranked higher, all else equal)
- Score SHALL update in real-time as user adds information

**Business Value**: Accuracy score incentivizes complete listings, improving buyer experience and reducing low-quality inventory. Creates gamification effect encouraging sellers to improve listings.

**Acceptance Criteria**:
- Score calculated and displayed for all listings
- Score updates within 5 seconds of changes
- Checklist shows specific missing items with guidance
- Search ranking incorporates accuracy score
- Sellers can see score improvement suggestions

---

### 7.5 Search & Discovery

#### FR-19: Advanced Search (P0)
**Requirement**: The system SHALL provide advanced search functionality with comprehensive filters and verified-only options.

**Core Search Filters**:
| Filter Category | Available Options |
|----------------|-------------------|
| **Location** | Division, District, Area/Thana, Radius search (km) |
| **Price** | Min/Max range, price per sqft |
| **Property Type** | Apartment, Land, Commercial, Project |
| **Size** | Min/Max area (sqft, katha, decimal) |
| **Bedrooms/Bathrooms** | Count selectors |
| **Verification** | Verified only toggle, specific badge types |
| **Listing Quality** | Minimum accuracy score |
| **Additional** | Facing, floor range, amenities, handover status |

**Details**:
- The system SHALL support multiple filter combinations
- The system SHALL display result count as filters applied
- The system SHALL save recent searches for quick access
- The system SHALL provide "Clear All Filters" option
- Search results SHALL be sortable by: price, date posted, accuracy score, relevance

**Business Value**: Comprehensive filters enable precise property discovery, reducing search time and increasing user satisfaction.

**Acceptance Criteria**:
- User can apply multiple filters simultaneously
- Result count updates in real-time as filters change
- Filter selections persist during session
- Search returns results within 2 seconds for < 100 matches
- Mobile-optimized filter interface

---

#### FR-20: Map-Based Search (P1)
**Requirement**: The system SHOULD provide interactive map interface for geographic property discovery.

**Map Features**:
- Property markers clustered by location
- Marker color-coding by property type
- Marker size by price range (optional)
- Draw polygon/circle to define search area
- View listing card on marker click
- Map view synchronized with list view filters

**Details**:
- The system SHALL use Google Maps API (primary) or OpenStreetMap (fallback)
- The system SHALL display up to 500 properties on map simultaneously
- The system SHALL cluster markers when zoomed out
- The system SHALL update map as user pans/zooms (lazy loading)

**Business Value**: Visual geographic search is highly intuitive for property discovery, especially for location-sensitive buyers.

**Acceptance Criteria**:
- Map loads within 3 seconds
- Markers clickable to show listing preview
- Polygon search defines custom area
- Map viewport synced with search results
- Performance maintained with 500+ listings

---

#### FR-21: Saved Searches & Alerts (P1)
**Requirement**: The system SHOULD allow users to save search criteria and receive notifications for new matching listings.

**Saved Search Features**:
- Save unlimited search combinations with custom names
- Enable/disable email alerts per saved search
- Configure alert frequency (instant, daily digest, weekly)
- View recent matches for each saved search
- Delete or edit saved searches

**Notification Triggers**:
- New listing published matching criteria
- Price drop on existing match (≥ 5% reduction)
- Verification status upgraded on existing match
- Listing coming back to market (was archived)

**Details**:
- The system SHALL check for new matches every 15 minutes
- The system SHALL include up to 3 best matches per email notification
- The system SHALL track alert click-through rates for analytics

**Business Value**: Saved searches keep users engaged without active searching, increasing platform return rate and transaction likelihood.

**Acceptance Criteria**:
- User can save searches with one click
- Alert preferences configurable per search
- Email alerts sent within 30 minutes of new match
- Unsubscribe option in every alert email
- Saved searches accessible from user dashboard

---

#### FR-22: Compare Listings (P1)
**Requirement**: The system SHOULD allow users to compare multiple listings side-by-side.

**Comparison Features**:
- Compare up to 4 listings simultaneously
- Side-by-side table view with key attributes:
  - Price, price per sqft
  - Size, bedrooms, bathrooms
  - Location, distance from landmark
  - Verification status
  - Accuracy score
  - Agent/seller rating
- Photo galleries aligned for visual comparison
- Highlight differences in color
- Export comparison as PDF

**Details**:
- The system SHALL allow comparison only for same property type
- The system SHALL persist comparison selection across sessions
- The system SHALL provide "Why different price?" insights (if data available)

**Business Value**: Side-by-side comparison accelerates buyer decision-making and demonstrates platform value over traditional browsing.

**Acceptance Criteria**:
- User can select listings for comparison from search results
- Comparison view shows all key attributes
- Differences highlighted visually
- Comparison accessible on mobile with horizontal scroll
- PDF export includes all selected listings

---

### 7.6 Communication & Appointments

#### FR-23: Live Chat (P0)
**Requirement**: The system SHALL provide real-time chat functionality between buyers, sellers, agents, and service providers.

**Chat Features**:
- Real-time message delivery (WebSocket or similar)
- Message status indicators (sent, delivered, read)
- Text messages, emoji support
- Image and document sharing (max 10MB per file)
- Chat history preserved indefinitely
- Search within chat conversations
- Typing indicators
- Block and report options

**Chat Context**:
- Chat SHALL be initiated from:
  - Property listing page
  - User profile page
  - After appointment booking
  - Within transaction timeline
- Chat SHALL automatically include listing/transaction context

**Details**:
- The system SHALL enforce rate limits to prevent spam (max 10 messages per minute)
- The system SHALL detect and flag repeated content or suspicious link sharing
- The system SHALL provide offline messaging (delivered when recipient comes online)
- The system SHALL notify users of new messages via push/email (based on preferences)

**Business Value**: Direct communication increases engagement and transaction completion rates. Context-aware chat reduces miscommunication.

**Acceptance Criteria**:
- Messages delivered within 2 seconds
- Chat works seamlessly on web and mobile
- All messages stored with encryption
- User can access chat history anytime
- Block feature immediately prevents further contact

---

#### FR-24: Audio/Video Call (P1)
**Requirement**: The system SHOULD support integrated audio/video calling for property consultations.

**Call Features**:
- One-to-one video calls
- Audio-only option
- Screen sharing for document review (P2)
- Call recording with mutual consent (P2)
- Call history and duration tracking
- In-call chat
- Poor network quality indicator

**Call Initiation**:
- Call must be consent-based (recipient must accept)
- Call request shows caller profile and purpose
- Recipient can decline with reason
- Missed call notifications

**Integration**:
- **SDK Options**: Agora (primary), Twilio (secondary), Jitsi (open-source fallback)
- The system SHALL use SDK best suited to Bangladesh network conditions

**Details**:
- The system SHALL implement call quality monitoring
- The system SHALL provide abuse reporting during/after calls
- The system SHALL track call completion rates for professional reputation

**Business Value**: Video calls enable remote property viewing and consultations, expanding market reach beyond local buyers.

**Acceptance Criteria**:
- Call connects within 5 seconds of acceptance
- Video quality adapts to network conditions
- Call recording requires both parties' consent
- Call logs accessible from transaction timeline
- Abuse reports reviewed within 24 hours

---

#### FR-25: Appointment Booking (P0)
**Requirement**: The system SHALL provide appointment scheduling functionality for property visits and consultations.

**Appointment Features**:
- **Time Slot Selection**: Agent/professional defines available slots
- **Purpose Selection**: Property visit, document review, consultation, signing
- **Location**: Address pre-filled from listing, option to specify alternate location
- **Participant Count**: Specify number of people attending
- **Notes**: Free-text for special requests
- **Confirmation**: Accept/Decline/Reschedule by recipient

**Appointment Workflow**:
1. Requester selects date, time slot, purpose
2. Recipient receives notification
3. Recipient accepts/declines/proposes alternate time
4. Confirmed appointment added to both calendars
5. Reminders sent 24 hours and 2 hours before
6. Post-appointment: option to mark completed/no-show

**Details**:
- The system SHALL integrate with Google Calendar (optional sync)
- The system SHALL track no-show rates for reputation metrics
- The system SHALL allow recurring appointments (P2)
- The system SHALL provide emergency cancellation with notification

**Business Value**: Structured appointment booking reduces miscommunication and no-shows, saving time for professionals and buyers.

**Acceptance Criteria**:
- User can book appointments in 3 clicks
- Professionals receive instant notification
- Calendar view shows all upcoming appointments
- Reminders sent as configured in preferences
- No-show tracking affects professional reputation score

---

#### FR-26: Purpose Capture (P0)
**Requirement**: The system SHALL capture the purpose for all communication and appointment requests.

**Purpose Categories**:
| Category | Applicable To | Examples |
|----------|--------------|----------|
| **Property Inquiry** | Chat, Appointment | Price negotiation, property details, amenity questions |
| **Document Verification** | Chat, Appointment | Document review, ownership verification |
| **Legal Consultation** | Appointment | Deed review, title search, legal advice |
| **Financial Consultation** | Appointment | Loan eligibility, mortgage process |
| **Property Visit** | Appointment | Physical inspection, neighborhood tour |

**Details**:
- The system SHALL prompt users to select purpose before initiating contact
- The system SHALL use purpose for analytics and service quality tracking
- The system SHALL display purpose in professional dashboard for prioritization
- Purpose SHALL be editable if initially incorrect

**Business Value**: Purpose capture helps professionals prioritize responses and provides valuable data for service optimization.

**Acceptance Criteria**:
- Purpose selection required before message/appointment
- Purpose categories comprehensive and clear
- Purpose displayed in chat/appointment context
- Analytics dashboard shows purpose distribution

---

#### 7.6.1 Agent Responsiveness (Performance Tracking)

##### FR-26a: Response SLA Timers (P1)
**Requirement**: The system SHOULD track and display expected response times for professional service providers.

**SLA Metrics**:
- **Chat Messages**:
  - Expected response time: < 2 hours during business hours
  - Last active timestamp displayed
  - "Usually responds within X hours" badge
  
- **Appointment Requests**:
  - Expected decision time: < 2 hours
  - Auto-reminder if no response after 1 hour
  - Escalation if no response after 24 hours

**Details**:
- The system SHALL calculate response times based on professional's historical data (30-day rolling average)
- The system SHALL exclude nighttime hours (11 PM - 7 AM) from response time calculations
- The system SHALL display response time expectations to users before initiating contact

**Business Value**: Transparent response time expectations set realistic user expectations and incentivize professional responsiveness.

**Acceptance Criteria**:
- Response time badge shown on professional profile
- Real-time "last active" indicator in chat
- Auto-reminders sent to professionals for pending requests
- Response metrics updated daily

---

##### FR-26b: Reminders & Escalation (P1)
**Requirement**: The system SHOULD automatically remind professionals of pending responses and offer alternatives for unresponsive cases.

**Reminder System**:
1. **First Reminder**: 1 hour after initial request
2. **Second Reminder**: 6 hours after initial request
3. **Escalation**: 24 hours after initial request
   - Notify admin/support team
   - Offer user to contact alternative professionals in same area/category

**Alternative Suggestions**:
- The system SHALL suggest 3 alternative professionals with:
  - Similar expertise
  - Same geographic coverage
  - Better response rates
  - Available time slots

**Details**:
- The system SHALL send reminders via in-app notification, email, and SMS (based on preferences)
- The system SHALL track reminder effectiveness for reputation scoring
- The system SHALL allow professionals to set "away" status to pause reminders

**Business Value**: Reduces user abandonment due to unresponsive professionals. Protects platform reputation by ensuring service quality.

**Acceptance Criteria**:
- Reminders sent at configured intervals
- Professionals can mark themselves away with return date
- Alternative suggestions provided after 24-hour non-response
- Users can switch to alternative with one click

---

##### FR-26c: Response Metrics (P1)
**Requirement**: The system SHOULD maintain and display comprehensive response performance metrics for all professionals.

**Tracked Metrics**:
| Metric | Calculation | Display Location |
|--------|-------------|------------------|
| **Response Rate** | (Responded Requests / Total Requests) × 100 (7-day and 30-day) | Professional profile, search results |
| **Median Response Time** | Median time from request to first response | Professional profile badge |
| **Appointment Acceptance Rate** | (Accepted / Total Requests) × 100 | Professional analytics dashboard |
| **No-Show Rate** | (No-shows / Total Appointments) × 100 | Internal only (affects ranking) |

**Penalty System**:
- **Response Rate < 50%**: Warning message to professional
- **Response Rate < 30%**: Profile downranked in search
- **Chronic Non-Response** (3 consecutive weeks < 30%): Account flagged for review, possible suspension

**Details**:
- The system SHALL provide professionals with weekly performance reports
- The system SHALL highlight improving/declining trends
- Admin SHALL have override capability for penalized accounts with valid reasons

**Business Value**: Transparent performance metrics maintain marketplace quality and incentivize excellent service. Penalties protect user experience.

**Acceptance Criteria**:
- Metrics displayed accurately on all profiles
- Weekly reports emailed to professionals
- Penalty warnings sent before enforcement
- Appeal process available for disputed penalties

---

*[End of Batch 2 Functional Requirements Part]*