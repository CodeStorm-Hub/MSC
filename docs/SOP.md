# Standard Operating Procedure (SOP)
## MSC Home Rental & Real Estate Platform  
**(Web Application + Android & iOS Mobile Applications)**

---

## 1. Document Information

| Item | Details |
|----|--------|
| Document Title | Standard Operating Procedure (SOP) |
| Project Name | MSC Home Rental & Real Estate Platform |
| Prepared By | MSC Digital Solutions |
| Version | 1.0 |
| Date | 01 January 2026 |

---

## 2. Purpose of the SOP

The purpose of this SOP is to **define standard processes, responsibilities, and workflows** for the **development, deployment, operation, and maintenance** of the MSC Home Rental & Real Estate Platform.

This SOP ensures:
- Consistent development practices  
- Clear communication between stakeholders  
- Secure, scalable, and maintainable system delivery  
- Proper post-deployment support and maintenance  

---

## 3. Scope

This SOP applies to:
- Backend development team  
- API development team  
- Web and mobile frontend teams  
- Quality assurance team  
- Deployment and maintenance team  
- Project stakeholders and administrators  

---

## 4. System Overview

The system follows a **distributed architecture**:

**Backend → API → Frontend (Web + Android + iOS)**

### Core Components
- Centralized backend system  
- RESTful API layer  
- Web application  
- Android and iOS mobile applications  
- Admin and monitoring modules  

---

## 5. Roles & Responsibilities

| Role | Responsibilities |
|----|------------------|
| Project Manager | Planning, coordination, timeline tracking |
| Backend Developer | Business logic, database, security |
| API Developer | API design, documentation, integration |
| Frontend Developer | Web UI implementation |
| Mobile Developer | Android & iOS application development |
| UI/UX Designer | Design, usability, user experience |
| QA Engineer | Testing, bug reporting, validation |
| System Admin | Deployment, monitoring, backups |
| Support Engineer | Maintenance and AMC support |

---

## 6. Development SOP

### 6.1 Project Governance & RACI Matrix

**RACI Legend:**
- **R** = Responsible (does the work)
- **A** = Accountable (final approval)
- **C** = Consulted (provides input)
- **I** = Informed (kept in the loop)

| Activity | PM | Tech Lead | Backend | API | Frontend | Mobile | QA | DevOps | UI/UX | Support | Client |
|----------|----|-----------|---------|----|----------|--------|-----|--------|-------|---------|--------|
| **Planning & Governance** |
| Project planning | A/R | C | I | I | I | I | I | I | I | I | C |
| Sprint planning | A/R | C | C | C | C | C | C | C | C | I | I |
| Requirement refinement | C | C | R | R | R | R | C | I | R | I | A |
| Risk management | A/R | C | I | I | I | I | I | I | I | I | C |
| Change requests | A | C | I | I | I | I | I | I | I | I | R |
| **Design & Architecture** |
| Technical architecture | C | A/R | C | C | C | C | I | C | I | I | I |
| Database schema design | I | A | R | C | I | I | I | C | I | I | I |
| API design | I | A | C | R | C | C | I | I | I | I | I |
| UI/UX design | C | I | I | I | C | C | I | I | A/R | I | A |
| **Development** |
| Backend development | I | A | R | C | I | I | C | I | I | I | I |
| API development | I | A | C | R | C | C | C | I | I | I | I |
| Web development | I | A | C | C | R | I | C | I | C | I | I |
| Mobile development | I | A | I | C | I | R | C | I | C | I | I |
| Code reviews | I | A | R | R | R | R | I | I | I | I | I |
| **Testing & QA** |
| Test planning | C | C | I | I | I | I | A/R | I | I | I | I |
| Unit testing | I | C | R | R | R | R | A | I | I | I | I |
| Integration testing | I | C | R | R | R | R | A | C | I | I | I |
| UAT coordination | A/R | C | I | I | I | I | C | I | I | I | R |
| **Deployment & Operations** |
| Deployment planning | A | R | C | C | C | C | C | R | I | I | I |
| Production deployment | C | A | C | C | C | C | C | R | I | I | I |
| Monitoring setup | I | C | I | I | I | I | I | A/R | I | I | I |
| Incident response | C | A | R | R | C | C | C | R | I | R | I |
| **Support & Maintenance** |
| AMC support delivery | C | C | R | R | C | C | C | R | I | A/R | I |
| Bug triage | C | A | R | R | R | R | C | C | I | R | I |
| Security patches | I | A | R | R | C | C | C | R | I | I | I |

---

### 6.2 Development Workflow

#### Branching Model (Git Flow)

**Branch Structure:**
```
main (production)
├── develop (integration branch)
│   ├── feature/AUTH-123-user-login
│   ├── feature/LIST-456-property-search
│   └── feature/PAY-789-payment-gateway
├── release/v1.0.0 (release candidate)
├── hotfix/CRITICAL-fix-payment-bug
```

**Branch Naming Conventions:**
- **Feature branches:** `feature/[TICKET-ID]-brief-description`
  - Example: `feature/AUTH-101-oauth-login`
- **Bug fix branches:** `bugfix/[TICKET-ID]-brief-description`
  - Example: `bugfix/LIST-202-search-crash`
- **Release branches:** `release/v[MAJOR].[MINOR].[PATCH]`
  - Example: `release/v1.2.0`
- **Hotfix branches:** `hotfix/[TICKET-ID]-brief-description`
  - Example: `hotfix/CRITICAL-payment-failure`

**Branch Lifecycle:**

1. **Feature Development:**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/AUTH-123-user-login
   # Develop and commit
   git push origin feature/AUTH-123-user-login
   # Create Pull Request to develop
   ```

2. **Release Preparation:**
   ```bash
   git checkout develop
   git checkout -b release/v1.0.0
   # Final testing, version bumps, changelog
   git push origin release/v1.0.0
   # Merge to main and develop after QA approval
   ```

3. **Hotfix for Production:**
   ```bash
   git checkout main
   git checkout -b hotfix/CRITICAL-fix-payment-bug
   # Fix, test, commit
   git push origin hotfix/CRITICAL-fix-payment-bug
   # Merge to main and develop after approval
   ```

---

#### Code Review Policy

**Mandatory Code Reviews:**
- All code changes must be reviewed before merging to `develop` or `main`
- Minimum 1 approving review required for feature branches
- Minimum 2 approving reviews required for release and hotfix branches
- Tech Lead approval required for architecture changes

**Review Checklist:**
- [ ] Code follows project coding standards and style guide
- [ ] Functionality matches requirements and acceptance criteria
- [ ] Unit tests added and passing (minimum 80% coverage for new code)
- [ ] No commented-out code or debug statements
- [ ] Error handling implemented properly
- [ ] Security best practices followed (input validation, SQL injection prevention, XSS protection)
- [ ] Performance considerations addressed (N+1 queries, caching)
- [ ] API changes documented in Swagger/OpenAPI spec
- [ ] Database migrations included if schema changes
- [ ] No secrets or credentials committed

**Review Timeline:**
- Reviews should be completed within 24 hours of PR submission
- If not reviewed within 24 hours, escalate to Tech Lead
- Critical hotfixes: Reviews within 2 hours

---

#### Pull Request (PR) Checklist

**Before Creating PR:**
- [ ] Code compiles/runs without errors
- [ ] All new code has unit tests
- [ ] All tests pass locally
- [ ] Code formatted per style guide (use linter)
- [ ] No merge conflicts with target branch
- [ ] Commit messages follow convention: `[TICKET-ID] Brief description`

**PR Template:**
```markdown
## Description
Brief description of changes

## Ticket
Jira/Ticket ID: AUTH-123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing performed:
- Unit tests added/updated
- Manual testing steps
- Edge cases considered

## Screenshots (if UI changes)
[Attach screenshots]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed my code
- [ ] Added tests that prove fix is effective or feature works
- [ ] New and existing tests pass
- [ ] API documentation updated
- [ ] No secrets or sensitive data committed
```

---

#### Merge Rules

**Protected Branches:**
- `main` and `develop` are protected branches
- Direct commits not allowed
- Requires pull request with approvals
- Status checks must pass before merge

**Merge Requirements:**
- All CI checks pass (build, tests, linters)
- Code review approved by required reviewers
- No merge conflicts
- Up to date with target branch

**Merge Strategy:**
- Feature branches → `develop`: **Squash and merge** (clean history)
- Release branches → `main`: **Merge commit** (preserve release history)
- Hotfix branches → `main` and `develop`: **Merge commit**

---

### 6.3 CI/CD Pipeline

#### Pipeline Stages

**Stage 1: Build**
- Checkout code from repository
- Install dependencies (npm install, composer install, pip install)
- Compile/build application
- **Success Criteria:** Build completes without errors
- **Duration Target:** < 5 minutes

**Stage 2: Test**
- Run unit tests with coverage report
- Run integration tests
- Run linters and code quality checks (ESLint, PHPStan, Pylint)
- **Success Criteria:** All tests pass, coverage > 80%, no linting errors
- **Duration Target:** < 10 minutes

**Stage 3: Security Scan**
- Run dependency vulnerability scan (npm audit, Snyk)
- Run static application security testing (SAST)
- Check for secrets in code (git-secrets, truffleHog)
- **Success Criteria:** No critical vulnerabilities, no secrets found
- **Duration Target:** < 5 minutes

**Stage 4: Build Artifacts**
- Build Docker images (if applicable)
- Package application for deployment
- Tag artifacts with version and commit SHA
- **Success Criteria:** Artifacts created successfully
- **Duration Target:** < 5 minutes

**Stage 5: Deploy (Environment-Specific)**
- Deploy to target environment (dev/staging/prod)
- Run database migrations
- Clear caches
- Perform smoke tests
- **Success Criteria:** Deployment successful, smoke tests pass
- **Duration Target:** < 10 minutes

---

#### Environments

| Environment | Purpose | Trigger | URL Pattern | Deployment Frequency |
|-------------|---------|---------|-------------|----------------------|
| **Development** | Continuous integration, rapid testing | Auto-deploy on merge to `develop` | dev.mschome.app | Multiple times daily |
| **Staging** | Pre-production testing, UAT | Auto-deploy on merge to `release/*` | staging.mschome.app | Weekly or before releases |
| **Production** | Live environment for end users | Manual approval after `main` merge | www.mschome.app | Bi-weekly or as needed |

**Environment Configuration:**
- Each environment has separate configuration files (`.env.dev`, `.env.staging`, `.env.prod`)
- Secrets managed via environment variables (never in code)
- Database: Separate database per environment
- Third-party services: Use sandbox/test modes in dev/staging

---

#### Required CI Checks

All checks must pass before merge to `develop` or `main`:

| Check | Tool | Pass Criteria |
|-------|------|---------------|
| **Build** | npm/composer/pip | Build completes successfully |
| **Unit Tests** | Jest/PHPUnit/Pytest | All tests pass, coverage > 80% |
| **Linting** | ESLint/PHPStan/Pylint | No errors, warnings < 10 |
| **Code Quality** | SonarQube | Quality Gate passed, no critical issues |
| **Security Scan** | Snyk/npm audit | No critical vulnerabilities |
| **API Tests** | Postman/Newman | All API tests pass |
| **Accessibility** | axe-core | No critical accessibility violations |

---

#### Release Promotion Schedule

**Regular Releases:**
- **Feature Releases:** Every 2 weeks (bi-weekly sprints)
- **Patch Releases:** As needed for bug fixes
- **Hotfixes:** Immediate for critical production issues

**Release Process:**
1. **Code Freeze:** 2 days before release date
2. **Release Branch Creation:** From `develop` branch
3. **Staging Deployment:** Deploy release branch to staging
4. **UAT & Testing:** 1-2 days of testing in staging
5. **Production Deployment:** Scheduled maintenance window (preferably Sunday 2-4 AM Bangladesh time)
6. **Post-Deployment Monitoring:** 24-hour hypercare period

---

#### Rollback Plan

**Rollback Triggers:**
- Critical bug affecting core functionality
- Data loss or corruption risk
- Security vulnerability exposed
- System performance degradation >50%
- User-reported critical issues >10 within 1 hour

**Rollback Procedure:**

1. **Immediate Action (< 5 minutes):**
   ```bash
   # Rollback to previous version
   git checkout main
   git revert <commit-hash>
   git push origin main
   # Trigger deployment of previous version
   ```

2. **Database Rollback (if migrations applied):**
   ```bash
   # Run down migrations
   php artisan migrate:rollback --step=1
   ```

3. **Verification (< 10 minutes):**
   - Run smoke tests on rolled-back version
   - Verify critical user flows working
   - Check monitoring dashboards for error rates

4. **Communication (< 15 minutes):**
   - Notify stakeholders via Slack/email
   - Post status update on status page
   - Inform support team of known issues

5. **Root Cause Analysis:**
   - Tech Lead investigates issue
   - Document findings in incident report
   - Create hotfix plan if needed

**Rollback Testing:**
- Rollback procedure tested quarterly in staging environment
- Documented in runbook with step-by-step instructions

---

## 7. Testing & Quality Assurance SOP

| Test Type | Description |
|---------|-------------|
| Unit Testing | Test individual components |
| Integration Testing | Validate backend, API, and frontend |
| Functional Testing | Validate user workflows |
| Security Testing | Check authentication and data safety |
| User Acceptance Testing (UAT) | Client approval |

All identified issues must be **documented, prioritized, and resolved** before deployment.

---

### 7.1 Testing Strategy & Workflow

**Test Pyramid Approach:**
- **Unit Tests (70%):** Fast, isolated tests for individual functions/methods
- **Integration Tests (20%):** Tests for API endpoints, database interactions, service integrations
- **E2E Tests (10%):** Full user journey tests through UI

#### Unit Testing SOP

**Responsibilities:** Developers (Backend, API, Frontend, Mobile)

**Requirements:**
- Minimum 80% code coverage for new code
- All business logic functions must have unit tests
- Use mocking for external dependencies
- Tests must be fast (< 1 second per test)

**Tools:**
- Backend: Jest (Node.js), PHPUnit (PHP), Pytest (Python)
- Frontend: Jest + React Testing Library
- Mobile: JUnit (Android), XCTest (iOS)

**Execution:**
- Run locally before committing code
- Auto-run in CI pipeline on every commit

---

#### Integration Testing SOP

**Responsibilities:** QA Engineer + Backend/API Developers

**Requirements:**
- Test all API endpoints with various inputs (happy path, edge cases, error cases)
- Validate database transactions and rollbacks
- Test third-party service integrations (payment gateways, SMS, email)
- Test authentication and authorization flows

**Tools:**
- Postman/Newman for API testing
- Database fixtures for consistent test data
- Mock servers for third-party APIs (WireMock, Mockoon)

**Execution:**
- Run nightly in staging environment
- Run before each release

**Test Cases Include:**
- Valid requests with expected responses
- Invalid requests (missing fields, wrong formats)
- Authentication failures (invalid tokens, expired sessions)
- Authorization failures (insufficient permissions)
- Rate limiting behavior
- Idempotency verification (for payment endpoints)

---

#### End-to-End (E2E) Testing SOP

**Responsibilities:** QA Engineer

**Requirements:**
- Test complete user journeys from UI to database
- Cover critical business flows (registration, listing, payment, transaction)
- Test across browsers and devices

**Tools:**
- Web: Cypress, Playwright, Selenium
- Mobile: Appium, Detox

**Critical Test Scenarios:**
1. **User Registration & Verification:**
   - Register → Verify email/phone → Switch to professional mode → Upload verification docs → Get verified badge

2. **Listing Creation & Publication:**
   - Create listing → Upload images → Submit for review → Admin approves → Listing appears in search

3. **Property Search & Inquiry:**
   - Search by location/price → Filter results → View listing details → Save to favorites → Contact seller

4. **Offer & Payment Flow:**
   - Submit offer → Seller accepts → Payment initiated → Gateway redirect → Payment success → Order confirmed

5. **Transaction Tracking:**
   - View transaction → Upload Bayna proof → Admin verifies → Track Dalil → Complete Namjari

**Execution:**
- Run daily in staging environment
- Run smoke tests after production deployment

---

#### Security Testing SOP

**Responsibilities:** Tech Lead + Security Specialist (external if available)

**Requirements:**
- Perform security testing before each major release
- Re-test after any security-related changes

**Test Categories:**

1. **Authentication & Session Management:**
   - Test password strength enforcement
   - Test session timeout and invalidation
   - Test "remember me" functionality
   - Verify multi-device session handling

2. **Authorization & Access Control:**
   - Test RBAC implementation (role-based permissions)
   - Test ownership checks (users can only modify their own data)
   - Test admin privilege escalation prevention

3. **Input Validation & Injection:**
   - SQL injection testing (all form inputs, API parameters)
   - XSS (cross-site scripting) testing
   - File upload validation (type, size, malicious content)
   - Command injection testing

4. **Data Protection:**
   - Verify sensitive data encryption (passwords, payment info)
   - Test HTTPS enforcement (no HTTP endpoints)
   - Verify secure cookie flags (HttpOnly, Secure, SameSite)

5. **API Security:**
   - Test rate limiting effectiveness
   - Test API authentication bypass attempts
   - Test CORS configuration
   - Test API parameter tampering

**Tools:**
- OWASP ZAP (automated vulnerability scanning)
- Burp Suite (manual penetration testing)
- SQLMap (SQL injection testing)
- Nikto (web server scanning)

**Pass Criteria:**
- Zero critical vulnerabilities
- Zero high-severity vulnerabilities
- Medium/low vulnerabilities documented with mitigation plan

---

#### Performance Testing SOP

**Responsibilities:** DevOps + Backend Lead

**Requirements:**
- Perform load testing before major releases
- Validate performance targets from SRS

**Test Scenarios:**

1. **Load Testing:**
   - Simulate 1,000 concurrent users
   - Test sustained load for 30 minutes
   - Monitor response times, error rates, resource usage

2. **Stress Testing:**
   - Gradually increase load until system breaks
   - Identify breaking point and bottlenecks
   - Verify graceful degradation

3. **Spike Testing:**
   - Simulate sudden traffic spikes (5x normal load)
   - Verify system recovers after spike

**Tools:**
- JMeter, Gatling, Locust, k6

**Performance Targets:**
| Metric | Target |
|--------|--------|
| Search API response time | < 2s (P95) |
| Listing detail page load | < 1.5s (P90) |
| Payment processing | < 30s end-to-end |
| API response time | < 500ms read, < 1s write (P95) |
| Concurrent users | Support 5,000+ |

**Execution:**
- Run before each major release
- Run quarterly to validate infrastructure capacity

---

#### User Acceptance Testing (UAT) SOP

**Responsibilities:** Client Representative + Project Manager + QA Lead

**UAT Process:**

1. **UAT Planning (1 week before):**
   - Identify UAT participants from client team
   - Prepare UAT test cases based on user stories
   - Set up UAT environment (staging with production-like data)
   - Schedule UAT sessions

2. **UAT Execution (1-2 weeks):**
   - Client team executes test cases
   - QA team provides support and observes
   - Document issues in defect tracking system
   - Prioritize issues (Critical, High, Medium, Low)

3. **Defect Resolution:**
   - Development team fixes critical and high-priority issues
   - Re-test fixed issues in UAT environment
   - Update test case status

4. **UAT Sign-off:**
   - All critical test cases passed
   - <5% of test cases have medium/low issues
   - Client representative signs UAT acceptance form
   - Issues backlog documented for post-launch fixes

**UAT Acceptance Criteria:**
- 100% of critical user journeys working
- 95% of test cases passed
- No critical or high-priority defects remaining
- Performance acceptable per user expectations
- Client team trained and confident in using the system

**UAT Sign-off Form Template:**
```
Project: MSC Home Platform
UAT Period: [Start Date] to [End Date]
UAT Environment: staging.mschome.app

Test Results:
- Total Test Cases: ___
- Passed: ___
- Failed: ___
- Blocked: ___

Defect Summary:
- Critical: ___ (all must be resolved)
- High: ___ (target: 0)
- Medium: ___
- Low: ___

UAT Acceptance Decision:
☐ APPROVED - Ready for production deployment
☐ CONDITIONAL APPROVAL - Deploy with documented known issues
☐ REJECTED - Major issues require resolution and re-testing

Client Sign-off:
Name: _________________
Title: _________________
Signature: _________________
Date: _________________
```

---

## 7A. Deployment SOP

### Pre-Deployment Checklist

**Code & Configuration:**
- [ ] All code merged to release branch and approved
- [ ] Version number updated in application
- [ ] Changelog prepared
- [ ] Configuration files reviewed (database, API keys, feature flags)
- [ ] Environment variables verified in production config
- [ ] Database migration scripts reviewed and tested in staging

**Testing & Quality:**
- [ ] All tests passing in CI pipeline
- [ ] UAT completed and signed-off
- [ ] Security scan passed (no critical vulnerabilities)
- [ ] Performance testing completed
- [ ] Cross-browser/device testing completed

**Infrastructure:**
- [ ] Production servers ready and accessible
- [ ] Database backup completed and verified
- [ ] SSL certificates valid and not expiring soon
- [ ] DNS configuration verified
- [ ] Load balancer configured (if applicable)
- [ ] CDN cache purging plan ready

**Communication:**
- [ ] Deployment window scheduled and communicated
- [ ] Stakeholders notified (client, team, support)
- [ ] Status page prepared for maintenance mode (if needed)
- [ ] Rollback plan reviewed and ready

**Monitoring & Support:**
- [ ] Monitoring dashboards accessible
- [ ] Alert rules configured
- [ ] On-call engineer identified and available
- [ ] Support team briefed on new features/changes

---

### Deployment Procedure

**Step 1: Pre-Deployment (T-30 minutes)**
1. Enable maintenance mode (if applicable):
   ```bash
   php artisan down --message="System maintenance in progress. We'll be back shortly."
   ```
2. Notify users via status page
3. Take final database backup:
   ```bash
   mysqldump -u [user] -p [database] > backup_pre_deploy_$(date +%Y%m%d_%H%M%S).sql
   ```
4. Create snapshot of production server (if using cloud VMs)

**Step 2: Deployment (T-0)**
1. Pull latest code from release branch:
   ```bash
   git fetch origin
   git checkout release/v1.0.0
   git pull origin release/v1.0.0
   ```
2. Install/update dependencies:
   ```bash
   npm ci --production
   composer install --no-dev --optimize-autoloader
   ```
3. Run database migrations:
   ```bash
   php artisan migrate --force
   ```
4. Clear and rebuild caches:
   ```bash
   php artisan cache:clear
   php artisan config:cache
   php artisan route:cache
   php artisan view:cache
   ```
5. Restart application services:
   ```bash
   pm2 restart all
   systemctl restart php-fpm
   systemctl restart nginx
   ```

**Step 3: Post-Deployment Verification (T+5 minutes)**
1. Run smoke tests:
   - [ ] Home page loads
   - [ ] User can login
   - [ ] Search functionality works
   - [ ] Listing detail page loads
   - [ ] Payment gateway accessible
2. Check application logs for errors
3. Verify monitoring dashboards show normal metrics
4. Test critical API endpoints with Postman

**Step 4: Hypercare & Monitoring (T+1 hour)**
1. Disable maintenance mode:
   ```bash
   php artisan up
   ```
2. Monitor error rates, response times, traffic
3. Check for user-reported issues
4. On-call engineer remains available

**Step 5: Post-Deployment Report (T+24 hours)**
- Document deployment outcome (success/issues)
- Report any incidents or rollbacks
- Update runbook with lessons learned

---

### Smoke Tests (Post-Deployment)

**Critical User Flows to Verify:**

| Test | Expected Result | Status |
|------|-----------------|--------|
| Access home page | Page loads in < 3s, no errors | ☐ Pass / ☐ Fail |
| User login | Successful login, dashboard loads | ☐ Pass / ☐ Fail |
| Search listings | Search results appear, no errors | ☐ Pass / ☐ Fail |
| View listing detail | Listing details and images load | ☐ Pass / ☐ Fail |
| Create new listing (draft) | Listing saved as draft | ☐ Pass / ☐ Fail |
| Submit payment (sandbox) | Redirect to gateway successful | ☐ Pass / ☐ Fail |
| Upload document | Document uploaded and visible | ☐ Pass / ☐ Fail |
| Send message (chat) | Message delivered | ☐ Pass / ☐ Fail |
| View admin dashboard | Dashboard loads with statistics | ☐ Pass / ☐ Fail |

**API Health Check:**
```bash
curl -X GET https://api.mschome.app/health
# Expected: {"status": "ok", "version": "1.0.0", "timestamp": "2026-01-01T10:00:00Z"}
```

---

### Database Migration Policy

**Pre-Migration:**
- All migrations tested in development and staging
- Migrations are backward-compatible when possible
- Data migration scripts reviewed by Tech Lead
- Rollback migration tested

**Migration Types:**

1. **Non-Breaking Migrations (safe for zero-downtime):**
   - Adding new tables
   - Adding new columns (with default values)
   - Adding indexes (use `CREATE INDEX CONCURRENTLY` for PostgreSQL)
   - Creating new views

2. **Breaking Migrations (require maintenance window):**
   - Dropping columns
   - Renaming columns
   - Changing column types
   - Dropping tables

**Rollback Strategy:**
- Always include "down" migration for rollback
- Test rollback before production deployment
- For data migrations, keep backup of affected data

---

### Feature Flags Usage

**Purpose:** Deploy code to production without enabling features immediately, allowing gradual rollout and easy rollback.

**Use Cases:**
- New major features (enable for beta users first)
- Risky changes (enable for internal team first)
- A/B testing variations

**Implementation:**
```javascript
if (featureFlags.isEnabled('NEW_SEARCH_ALGORITHM')) {
    // New search logic
} else {
    // Old search logic
}
```

**Feature Flag Lifecycle:**
1. **Development:** Flag off by default
2. **Staging:** Flag on for testing
3. **Production (gradual rollout):**
   - Week 1: Enable for internal users (5%)
   - Week 2: Enable for 25% of users
   - Week 3: Enable for 50% of users
   - Week 4: Enable for 100% of users
4. **Cleanup:** Remove flag and old code after successful rollout

**Tools:** LaunchDarkly, Unleash, or custom feature flag service

---

## 7B. Backup & Disaster Recovery Plan

## 7B. Backup & Disaster Recovery Plan

### Backup Strategy

**Backup Frequency:**

| Data Type | Backup Frequency | Retention Period | Backup Method |
|-----------|------------------|------------------|---------------|
| **Database** | Daily (automated) | 30 days (daily), 12 months (monthly) | Full dump + incremental |
| **User Uploaded Files** | Daily (automated) | 90 days | Snapshot to cloud storage |
| **Application Code** | On every commit | Indefinite (in Git) | Git repository |
| **Server Configuration** | Weekly | 60 days | Configuration as code (Ansible/Terraform) |
| **Logs** | Continuous | 90 days | Log aggregation service |

**Backup Storage:**
- Primary backup location: Cloud storage (AWS S3, DigitalOcean Spaces)
- Secondary backup location: Off-site backup (different region)
- Encryption: All backups encrypted at rest (AES-256)
- Access control: Restricted to authorized DevOps personnel only

---

### Database Backup Procedure

**Daily Automated Backup:**
```bash
#!/bin/bash
# Runs daily at 2:00 AM via cron

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/database"
DB_NAME="msc_home"

# Full database dump
mysqldump -u backup_user -p${DB_PASSWORD} ${DB_NAME} | gzip > ${BACKUP_DIR}/msc_db_${TIMESTAMP}.sql.gz

# Upload to cloud storage
aws s3 cp ${BACKUP_DIR}/msc_db_${TIMESTAMP}.sql.gz s3://msc-backups/database/

# Verify backup integrity
if [ $? -eq 0 ]; then
    echo "Backup successful: msc_db_${TIMESTAMP}.sql.gz"
else
    echo "Backup failed!" | mail -s "ALERT: Database Backup Failed" devops@codestormhub.dev
fi

# Clean up local backups older than 7 days
find ${BACKUP_DIR} -name "*.sql.gz" -mtime +7 -delete
```

**Incremental Backup (Binary Logs):**
- MySQL binary logs enabled for point-in-time recovery
- Binary logs archived hourly
- Retention: 7 days

---

### Recovery Time Objective (RTO) & Recovery Point Objective (RPO)

**Recommended Targets:**

| Service Tier | RTO (Recovery Time) | RPO (Max Data Loss) |
|--------------|---------------------|---------------------|
| **Critical Services** (Auth, Payments, Listings) | < 4 hours | < 1 hour |
| **Important Services** (Chat, Notifications) | < 8 hours | < 24 hours |
| **Non-Critical Services** (Reports, Analytics) | < 24 hours | < 48 hours |

**Factors Affecting RTO:**
- Availability of backup team
- Complexity of restoration
- Size of data to restore
- Network bandwidth

---

### Disaster Recovery Procedures

#### Scenario 1: Database Corruption

**Detection:** Database errors in application logs, monitoring alerts

**Recovery Steps:**
1. **Assess Impact (5 minutes):**
   - Identify affected tables/data
   - Determine if corruption is partial or full

2. **Isolate Issue (5 minutes):**
   - Enable maintenance mode to prevent further writes
   - Create snapshot of corrupted database for investigation

3. **Restore from Backup (30-120 minutes):**
   ```bash
   # Stop application services
   systemctl stop php-fpm nginx
   
   # Download latest backup
   aws s3 cp s3://msc-backups/database/msc_db_latest.sql.gz /tmp/
   
   # Restore database
   gunzip /tmp/msc_db_latest.sql.gz
   mysql -u root -p ${DB_NAME} < /tmp/msc_db_latest.sql
   
   # Apply binary logs for point-in-time recovery (if needed)
   mysqlbinlog /var/log/mysql/mysql-bin.000123 | mysql -u root -p ${DB_NAME}
   ```

4. **Verify Restoration (15 minutes):**
   - Run database integrity checks
   - Execute smoke tests
   - Verify critical data exists

5. **Resume Operations:**
   - Restart application services
   - Disable maintenance mode
   - Monitor for errors

**Estimated RTO:** 2-3 hours

---

#### Scenario 2: Complete Server Failure

**Detection:** Server unresponsive, monitoring alerts

**Recovery Steps:**
1. **Provision New Server (30 minutes):**
   - Spin up new VM from snapshot or base image
   - Configure networking, security groups

2. **Deploy Application (45 minutes):**
   - Install dependencies and application code
   - Restore configuration from backup
   - Deploy latest release

3. **Restore Database (60 minutes):**
   - Restore database from latest backup
   - Verify data integrity

4. **Restore User Files (30 minutes):**
   - Sync user uploads from cloud storage backup

5. **Update DNS (10 minutes + propagation time):**
   - Point domain to new server IP
   - Wait for DNS propagation (15-60 minutes)

6. **Verify & Monitor (30 minutes):**
   - Run comprehensive smoke tests
   - Monitor application performance
   - Verify all integrations working

**Estimated RTO:** 4-6 hours (excluding DNS propagation)

---

#### Scenario 3: Data Loss (Accidental Deletion)

**Examples:** User accidentally deletes listings, admin deletes users by mistake

**Recovery Steps:**
1. **Stop Further Changes (immediate):**
   - Identify affected records
   - Temporarily disable delete functionality if mass deletion

2. **Locate Backup (15 minutes):**
   - Identify most recent backup before deletion
   - Download backup file

3. **Extract Deleted Data (30 minutes):**
   ```bash
   # Restore backup to temporary database
   mysql -u root -p temp_db < /tmp/backup.sql
   
   # Extract deleted records
   mysql -u root -p -e "SELECT * FROM temp_db.listings WHERE id IN (123, 456, 789);" > deleted_records.sql
   ```

4. **Restore Deleted Records (15 minutes):**
   ```bash
   # Import deleted records to production
   mysql -u root -p ${DB_NAME} < deleted_records.sql
   ```

5. **Verify Restoration:**
   - Confirm records visible in application
   - Notify affected users (if applicable)

**Estimated RTO:** 1-2 hours

---

### Backup Verification & Testing

**Monthly Backup Verification:**
- Automated script verifies backup integrity (checksums)
- Test restoration to staging environment
- Document any issues or corruption

**Quarterly Disaster Recovery Drill:**
- Full disaster recovery test in isolated environment
- Measure actual RTO against targets
- Update DR procedures based on findings
- Train team on recovery procedures

**Backup Monitoring:**
- Daily email report of backup status
- Alerts triggered if backup fails
- Dashboard showing backup history and sizes

---

## 7C. Monitoring & Alerting

### Metrics to Monitor

**Application Metrics:**
- Request rate (requests per second)
- Error rate (percentage of failed requests)
- Response time (P50, P90, P95, P99)
- Active users (concurrent sessions)
- API endpoint latency breakdown

**Infrastructure Metrics:**
- CPU usage (%)
- Memory usage (%)
- Disk usage (%) and I/O
- Network traffic (bandwidth)
- Database connections (active/idle)

**Business Metrics:**
- New user registrations (daily)
- Active listings count
- Transactions completed (daily/monthly)
- Payment success rate (%)
- Search queries (volume and performance)

**Security Metrics:**
- Failed login attempts
- Suspicious API requests (rate limit violations)
- Security scan alerts
- SSL certificate expiration

---

### Service Level Objectives (SLO) & Service Level Indicators (SLI)

**Core Service SLOs:**

| Service | SLI | SLO Target | Measurement Window |
|---------|-----|------------|-------------------|
| **API Availability** | % of successful API requests | 99.5% | 30 days rolling |
| **Search Performance** | % of searches completed < 2s | 95% | 24 hours |
| **Payment Processing** | % of payments processed < 30s | 99% | 24 hours |
| **Page Load Time** | % of pages loaded < 3s | 90% | 24 hours |
| **Error Rate** | % of requests without 5xx errors | 99.9% | 1 hour |

**Error Budget:**
- For 99.5% uptime SLO → 3.6 hours downtime allowed per month
- Error budget consumed by incidents and planned maintenance
- If error budget exhausted, freeze feature releases and focus on reliability

---

### Alert Thresholds

**Critical Alerts (Immediate Response):**
- API error rate > 5% (sustained for 5 minutes)
- Database connection failures
- Payment processing stopped
- Server CPU > 90% (sustained for 10 minutes)
- Disk space > 90%
- Application crashed/unresponsive

**High Priority Alerts (Response within 30 minutes):**
- API response time > 5s (P95, sustained for 10 minutes)
- Search latency > 5s (P95)
- Memory usage > 85%
- Failed backup
- SSL certificate expiring in < 7 days

**Medium Priority Alerts (Response within 2 hours):**
- API response time > 2s (P95)
- Elevated error rate (2-5%)
- High CPU usage (70-90%)
- Unusual traffic patterns

**Alert Channels:**
- Critical: PagerDuty/OpsGenie + SMS + Phone call
- High: Slack #alerts channel + Email
- Medium: Slack #alerts channel

---

### On-Call Rotation

**On-Call Schedule:**
- Primary on-call: Rotates weekly among DevOps and senior developers
- Secondary on-call (escalation): Tech Lead
- On-call hours: 24/7 coverage
- Handoff: Monday 9:00 AM Bangladesh time

**On-Call Responsibilities:**
- Respond to critical and high-priority alerts
- Perform incident triage and initial troubleshooting
- Escalate to appropriate team members if needed
- Document incidents and resolutions
- Update status page during incidents

**On-Call Compensation:**
- Regular on-call week: BDT 5,000 stipend
- Per incident response (off-hours): BDT 500
- Major incident (>2 hours response): BDT 2,000

---

### Monitoring Tools & Dashboards

**Recommended Tools:**
- **Application Performance Monitoring:** New Relic, DataDog, or Elastic APM
- **Infrastructure Monitoring:** Prometheus + Grafana, CloudWatch
- **Log Aggregation:** ELK Stack (Elasticsearch, Logstash, Kibana) or Loki
- **Uptime Monitoring:** UptimeRobot, Pingdom, or StatusCake
- **Error Tracking:** Sentry, Rollbar, or Bugsnag

**Required Dashboards:**

1. **System Health Overview:**
   - Service status (up/down indicators)
   - Request rate and error rate (last 24 hours)
   - Response time trends
   - Active users

2. **Payment Monitoring:**
   - Payment success rate by gateway
   - Failed payments (with reasons)
   - IPN processing lag time
   - Pending reconciliations

3. **Business KPIs:**
   - Daily registrations
   - Active listings
   - Transaction volume
   - Revenue (if applicable)

4. **Infrastructure:**
   - CPU/Memory/Disk usage per server
   - Database query performance
   - Cache hit rate
   - CDN bandwidth

---

### Runbook Links

**Common Issues & Resolutions:**
- [Runbook: High API Error Rate](https://wiki.mschome.internal/runbook/high-error-rate)
- [Runbook: Database Connection Issues](https://wiki.mschome.internal/runbook/db-connection)
- [Runbook: Payment Gateway Timeout](https://wiki.mschome.internal/runbook/payment-timeout)
- [Runbook: Disk Space Full](https://wiki.mschome.internal/runbook/disk-full)
- [Runbook: Application Restart Procedure](https://wiki.mschome.internal/runbook/app-restart)

**Each runbook includes:**
- Symptoms and detection method
- Impact assessment
- Step-by-step troubleshooting
- Resolution steps
- Escalation path
- Prevention measures

---

## 7D. Incident Management

### Incident Severity Definitions

| Severity | Definition | Examples | Response Time | Communication |
|----------|------------|----------|---------------|---------------|
| **P1 (Critical)** | Complete service outage or data loss | Database down, site unreachable, payment system failed | < 15 minutes | Hourly updates to stakeholders |
| **P2 (High)** | Major functionality degraded | Search broken, slow response times, partial feature unavailable | < 1 hour | Updates every 4 hours |
| **P3 (Medium)** | Minor functionality impacted | Non-critical feature bug, UI glitch | < 4 hours | Daily update |
| **P4 (Low)** | Minimal user impact | Typos, cosmetic issues, feature requests | < 24 hours | No proactive communication |

---

### Incident Response Process

#### Phase 1: Detection & Triage (0-15 minutes)

**Detection Sources:**
- Automated monitoring alerts
- User reports via support tickets
- Social media mentions
- Internal team observations

**Initial Triage:**
1. Acknowledge alert/report
2. Assess severity based on impact
3. Create incident ticket (Jira, PagerDuty)
4. Assign incident commander (on-call engineer)
5. Notify relevant team members

**Triage Checklist:**
- [ ] Severity determined (P1/P2/P3/P4)
- [ ] Incident commander assigned
- [ ] Initial impact assessment completed
- [ ] Incident communication channel created (Slack #incident-YYYY-MM-DD)

---

#### Phase 2: Investigation & Mitigation (15 minutes - 4 hours)

**Investigation Steps:**
1. Review monitoring dashboards
2. Check recent deployments/changes
3. Analyze application logs and error messages
4. Identify root cause or contributing factors

**Mitigation Options:**
- **Quick Fix:** Code hotfix if issue is localized
- **Rollback:** Revert to previous stable version
- **Disable Feature:** Use feature flag to turn off problematic feature
- **Workaround:** Provide temporary solution to unblock users
- **Scale Resources:** Add servers/increase capacity if performance issue

**Communication During Incident:**
- Update status page with current status and ETA
- Post updates in incident channel
- Notify stakeholders per severity schedule

---

#### Phase 3: Resolution & Verification (varies)

**Resolution:**
1. Apply permanent fix
2. Test thoroughly in staging
3. Deploy to production
4. Monitor for recurrence

**Verification Checklist:**
- [ ] Root cause eliminated
- [ ] Smoke tests passed
- [ ] Monitoring shows normal metrics
- [ ] No new errors related to fix
- [ ] User reports confirmed resolution

**Incident Closure:**
- Update incident ticket with resolution details
- Mark incident as resolved
- Post final update on status page
- Thank team members involved

---

#### Phase 4: Postmortem (within 48 hours)

**Required for P1 and P2 incidents**

**Postmortem Document Includes:**

1. **Incident Summary:**
   - Incident ID and severity
   - Start time, resolution time, total duration
   - Services affected
   - User impact (number of users, transactions lost)

2. **Timeline:**
   - Detailed timeline of events, actions taken, and communications

3. **Root Cause Analysis:**
   - Technical root cause
   - Contributing factors
   - Why detection/prevention failed

4. **Impact Assessment:**
   - Users affected
   - Revenue impact
   - SLO/SLA breach
   - Reputational damage

5. **What Went Well:**
   - Effective actions during incident
   - Team collaboration highlights

6. **What Could Be Improved:**
   - Gaps in monitoring/alerting
   - Slow response areas
   - Knowledge gaps

7. **Action Items:**
   - Preventive measures (with owners and deadlines)
   - Monitoring improvements
   - Documentation updates
   - Training needs

**Postmortem Meeting:**
- Blameless postmortem culture (focus on systems, not individuals)
- All involved team members attend
- Document shared with stakeholders
- Action items tracked to completion

---

### Incident Communication Templates

**Initial Incident Notice (Status Page):**
```
🔴 Incident Identified

We are currently investigating reports of [brief description of issue].
Our team is actively working on resolving this issue.

Started: [Timestamp]
Status: Investigating
Affected Services: [List]

We will provide an update in 30 minutes.
```

**Update During Incident:**
```
🟡 Incident Update

We have identified the root cause as [brief explanation].
Our team is implementing a fix and expects resolution within [ETA].

Started: [Timestamp]
Last Update: [Timestamp]
Next Update: [Timestamp]
```

**Resolution Notice:**
```
🟢 Incident Resolved

The issue affecting [service] has been resolved.
All services are operating normally.

Started: [Start Timestamp]
Resolved: [End Timestamp]
Duration: [Total Time]

Summary: [Brief explanation of issue and resolution]

We apologize for any inconvenience caused.
```

---

### Escalation Matrix

**Technical Escalation:**
1. **On-Call Engineer** (First responder)
   - Initial triage and basic troubleshooting
   - Escalate if unable to resolve in 30 minutes (P1) or 2 hours (P2)

2. **Senior Developer / Team Lead** (Subject matter expert)
   - Deep technical investigation
   - Implement complex fixes
   - Escalate if architectural decision needed

3. **Tech Lead / Architect**
   - Architectural changes
   - Critical system decisions
   - Cross-team coordination

**Business Escalation:**
1. **Support Engineer** → 2. **Project Manager** → 3. **Senior Management** → 4. **Client Executive**

---

## 7E. Security Checklist

## 7E. Security Checklist

### Secrets Management

**Requirements:**
- [ ] No secrets (API keys, passwords, tokens) committed to Git repository
- [ ] All secrets stored in environment variables or secure vault (HashiCorp Vault, AWS Secrets Manager)
- [ ] `.env` files added to `.gitignore`
- [ ] Separate secrets per environment (dev/staging/prod)
- [ ] Regular rotation of sensitive credentials (quarterly)
- [ ] Access to production secrets restricted to authorized personnel only

**Secrets Audit:**
- Run `git-secrets` or `truffleHog` in CI pipeline to detect accidentally committed secrets
- Immediate revocation and rotation if secret exposed

---

### TLS/SSL Configuration

**Requirements:**
- [ ] HTTPS enforced on all production endpoints (HTTP redirects to HTTPS)
- [ ] Valid SSL certificate from trusted CA (Let's Encrypt, DigiCert)
- [ ] TLS 1.2 or higher (TLS 1.0/1.1 disabled)
- [ ] Strong cipher suites configured
- [ ] HSTS (HTTP Strict Transport Security) header enabled
- [ ] SSL certificate auto-renewal configured

**Verification:**
- SSL Labs test score: A or A+ (https://www.ssllabs.com/ssltest/)
- Certificate expiration monitored (alert 30 days before expiry)

---

### OWASP Top 10 Controls

**1. Injection Prevention:**
- [ ] Parameterized queries (prepared statements) for all database operations
- [ ] Input validation on all user inputs (whitelist approach)
- [ ] ORM frameworks used properly (Laravel Eloquent, Sequelize, SQLAlchemy)
- [ ] No dynamic SQL query construction from user input

**2. Broken Authentication:**
- [ ] Strong password policy enforced (min 8 chars, complexity requirements)
- [ ] Password hashing with bcrypt, Argon2, or PBKDF2 (not MD5/SHA1)
- [ ] Account lockout after 5 failed login attempts (15-minute lockout)
- [ ] Session timeout after 30 minutes of inactivity
- [ ] Secure session management (HttpOnly, Secure, SameSite flags on cookies)
- [ ] Multi-factor authentication (MFA) available for admin accounts

**3. Sensitive Data Exposure:**
- [ ] Sensitive data encrypted at rest (database encryption, file encryption)
- [ ] Sensitive data encrypted in transit (TLS)
- [ ] PII (personally identifiable information) minimized and protected
- [ ] Payment card data not stored (PCI-DSS compliance)
- [ ] Logs do not contain sensitive data (passwords, tokens, credit cards)

**4. XML External Entities (XXE):**
- [ ] XML parsers configured to disable external entity processing
- [ ] Input validation on XML uploads
- [ ] Use JSON instead of XML where possible

**5. Broken Access Control:**
- [ ] RBAC (role-based access control) implemented
- [ ] Ownership checks on all resource modifications
- [ ] Direct object references not exposed (use UUIDs instead of sequential IDs)
- [ ] Admin endpoints protected with authentication and authorization
- [ ] Insecure direct object reference (IDOR) testing completed

**6. Security Misconfiguration:**
- [ ] Default credentials changed on all systems
- [ ] Unnecessary services disabled
- [ ] Error messages do not reveal sensitive information (stack traces in production)
- [ ] Security headers configured (CSP, X-Frame-Options, X-Content-Type-Options)
- [ ] Dependency versions up to date with security patches

**7. Cross-Site Scripting (XSS):**
- [ ] All user-generated content sanitized before display
- [ ] Output encoding applied (HTML entity encoding)
- [ ] Content Security Policy (CSP) header configured
- [ ] React/Vue.js frameworks used (auto-escaping)
- [ ] No `innerHTML` or `dangerouslySetInnerHTML` with user input

**8. Insecure Deserialization:**
- [ ] Deserialization of untrusted data avoided
- [ ] Input validation on serialized objects
- [ ] Digital signatures on serialized data

**9. Using Components with Known Vulnerabilities:**
- [ ] Dependency scanning in CI pipeline (npm audit, Snyk, OWASP Dependency-Check)
- [ ] Regular updates of dependencies
- [ ] Automated alerts for new vulnerabilities (GitHub Dependabot)

**10. Insufficient Logging & Monitoring:**
- [ ] Security events logged (login failures, access control failures, input validation failures)
- [ ] Logs centralized and monitored
- [ ] Alerting configured for suspicious patterns
- [ ] Log retention policy defined (90 days minimum)

---

### File Upload Security

**Requirements:**
- [ ] File type validation (whitelist allowed extensions: .jpg, .png, .pdf, .doc)
- [ ] File size limits enforced (max 10MB per file)
- [ ] Uploaded files scanned for malware (ClamAV integration)
- [ ] Files stored outside web root (not directly accessible)
- [ ] Uploaded files served with correct Content-Type headers
- [ ] Randomized filenames to prevent enumeration attacks
- [ ] Content-Disposition: attachment header for downloads (prevent XSS via file uploads)

---

### Data Encryption

**At Rest:**
- [ ] Database encryption enabled (transparent data encryption if available)
- [ ] Sensitive fields encrypted at application level (credit cards, government IDs)
- [ ] Backups encrypted (AES-256)
- [ ] Encryption keys stored securely (AWS KMS, Azure Key Vault)

**In Transit:**
- [ ] HTTPS for all external communications
- [ ] TLS for database connections
- [ ] Secure WebSocket (WSS) for real-time features

---

### Least Privilege Rules

**User Permissions:**
- [ ] Users granted minimum necessary permissions
- [ ] Role hierarchy implemented (User < Agent < Admin < Super Admin)
- [ ] Service accounts have restricted permissions

**Database Access:**
- [ ] Application uses database user with limited privileges (no DROP, CREATE USER)
- [ ] Separate read-only user for analytics/reporting
- [ ] Admin tools use separate privileged account

**Server Access:**
- [ ] SSH key-based authentication (password authentication disabled)
- [ ] `sudo` access limited to specific users
- [ ] Firewall configured to allow only necessary ports

---

### API Security

**Authentication:**
- [ ] JWT or OAuth 2.0 for API authentication
- [ ] API keys rotated regularly
- [ ] Token expiration configured (access tokens: 15 min, refresh tokens: 7 days)

**Rate Limiting:**
- [ ] Rate limits per endpoint (e.g., 100 requests/minute per user)
- [ ] IP-based rate limiting for unauthenticated endpoints
- [ ] Graduated response (warning → throttle → block)

**Input Validation:**
- [ ] Request size limits enforced
- [ ] JSON schema validation on API payloads
- [ ] SQL injection, XSS, command injection testing completed

---

### Security Testing Requirements

**Pre-Release Testing:**
- [ ] OWASP ZAP automated scan (no high/critical findings)
- [ ] Dependency vulnerability scan (npm audit, Snyk)
- [ ] Secrets scanning (git-secrets, truffleHog)
- [ ] SAST (Static Application Security Testing) completed

**Periodic Testing:**
- [ ] Penetration testing annually by external firm (recommended)
- [ ] Quarterly security reviews by internal security team
- [ ] Continuous monitoring with web application firewall (WAF)

---

## 8. Support & AMC Procedures

### Ticket Intake Process

**Support Channels:**
1. **Email:** support@mschome.app (monitored 9 AM - 6 PM BD time, Mon-Fri)
2. **Ticketing System:** https://support.mschome.app (24/7 submission)
3. **Phone (Critical Only):** +880-XXXX-XXXXXX (during business hours)

**Ticket Creation:**
- User submits ticket via email or support portal
- Auto-reply sent with ticket number and expected response time
- Ticket assigned to support queue based on priority

**Required Ticket Information:**
- Summary of issue
- Steps to reproduce (if applicable)
- Expected vs. actual behavior
- Screenshots or error messages
- User account details (if relevant)
- Urgency/business impact

---

### SLA Handling (Annual Maintenance Contract)

**Reference:** See Quotation Section 8 for full AMC SLA details

**Priority Definitions & Response/Resolution SLAs:**

| Priority | Response Time | Resolution Time | Monthly Hour Limit |
|----------|---------------|-----------------|-------------------|
| Critical | Within 4 hours | Within 24 hours | Unlimited during incident |
| High | Within 8 hours | Within 48 hours | Up to 6 hours |
| Medium | Within 24 hours | Within 5 business days | Up to 4 hours |
| Low | Within 48 hours | Within 10 business days | Up to 2 hours |

**Total Included Hours:** 12 hours/month (excluding Critical incidents)

**Ticket Priority Assignment:**
- Support engineer assigns priority based on impact and urgency
- Client can request priority review if they disagree
- Final priority decision: Project Manager or Tech Lead

**SLA Tracking:**
- Automated timer starts upon ticket creation
- Alerts sent to support team as SLA deadline approaches
- SLA breach automatically escalates ticket
- Monthly SLA compliance report generated (target: >95% SLA met)

---

### Escalation Matrix

**Support Escalation Path:**

| Level | Role | Escalation Trigger | Response Time |
|-------|------|-------------------|---------------|
| **L1** | Support Engineer | Initial ticket submission | Per SLA table |
| **L2** | Senior Developer | Not resolved within SLA or requires code change | Within 2 hours |
| **L3** | Tech Lead | Complex architectural issue or P1/P2 incident | Within 4 hours |
| **L4** | Project Manager | Client dissatisfaction or contract dispute | Within 8 hours |
| **L5** | Senior Management | Escalation requested by client executive | Within 24 hours |

**Escalation Process:**
1. Support engineer attempts resolution per SLA
2. If unable to resolve or SLA at risk, escalate to L2
3. Document escalation reason in ticket
4. Notify next level via Slack and email
5. Escalated party acknowledges within response time
6. Continue escalation if needed

---

### Monthly Reporting

**AMC Monthly Report Contents:**

1. **Executive Summary:**
   - Month: [Month Year]
   - Total tickets received: XX
   - Total tickets resolved: XX
   - Average resolution time: XX hours
   - SLA compliance: XX%

2. **Ticket Breakdown by Priority:**
   | Priority | Received | Resolved | Open | Avg Resolution Time |
   |----------|----------|----------|------|---------------------|
   | Critical | X | X | X | X hours |
   | High | X | X | X | X hours |
   | Medium | X | X | X | X hours |
   | Low | X | X | X | X hours |

3. **Support Hours Consumed:**
   - Hours used this month: XX / 12
   - Breakdown by priority: Critical: X, High: X, Medium: X, Low: X
   - Overage hours (if any): X hours (charged at BDT 1,500/hour)

4. **Top Issues & Resolutions:**
   - List of most common issues and resolutions
   - Proactive recommendations to prevent recurrence

5. **System Health:**
   - Uptime: XX%
   - Performance metrics (response times, error rates)
   - Security patches applied

6. **Maintenance Activities:**
   - Security updates applied
   - Bug fixes deployed
   - Configuration changes
   - Backup verification status

7. **Recommendations:**
   - Suggested improvements
   - Upcoming maintenance needs
   - Change requests to consider

**Delivery:** Sent to client by 5th of following month via email

---

### Change Request Handling

**Change Request Process:**

1. **Submission:**
   - Client submits change request via support portal or email
   - Change request form includes:
     - Description of desired change
     - Business justification
     - Urgency/timeline
     - Affected users/features

2. **Impact Assessment (3 business days):**
   - Tech Lead reviews request
   - Determines if change is within AMC scope or requires separate quotation
   - Estimates effort (hours) and impact (downtime, risks)

3. **Categorization:**
   - **Minor Change (< 4 hours):** Can be completed within AMC monthly hours
   - **Major Change (> 4 hours):** Requires separate quotation and approval

4. **Approval (Client):**
   - For minor changes: Client approves via email, deducted from monthly hours
   - For major changes: Formal quotation sent, requires 50% advance payment

5. **Scheduling:**
   - Change scheduled in coordination with client (to minimize disruption)
   - Deployment during maintenance window if downtime required

6. **Execution:**
   - Change implemented per agreed timeline
   - Testing performed in staging before production
   - Client notified upon completion

7. **Verification:**
   - Client validates change meets requirements
   - Sign-off obtained
   - Final invoice sent (if major change)

**Emergency Changes:**
- Critical security patches or urgent fixes
- Expedited approval process (verbal approval acceptable)
- Documented retroactively
- Charged as per AMC hours or emergency rates

---

## 9. Change Management SOP

### Change Request Submission

**Who Can Submit:**
- Client stakeholders
- Project Manager
- Tech Lead (for technical debt or infrastructure changes)

**Submission Method:**
- Via change request form in support portal
- Email to project-changes@codestormhub.dev

**Required Information:**
- Change description and objectives
- Business justification
- Affected systems/features
- Proposed timeline
- Expected benefits

---

### Change Approval Process

**Change Advisory Board (CAB):**
- Members: Project Manager, Tech Lead, Client Representative
- Meets weekly to review change requests
- Ad-hoc meetings for urgent changes

**Approval Criteria:**
- Impact on system stability
- Alignment with project goals
- Resource availability
- Budget approval (for out-of-scope changes)

**Approval Levels:**

| Change Type | Approval Required | Timeline |
|-------------|------------------|----------|
| **Minor Change** (< 4 hours, low impact) | Project Manager | 1 business day |
| **Standard Change** (4-20 hours) | CAB approval | 3 business days |
| **Major Change** (> 20 hours) | CAB + Senior Management | 5 business days |
| **Emergency Change** (critical fix) | Tech Lead + post-implementation CAB review | Immediate |

---

### Change Scheduling

**Maintenance Windows:**
- **Preferred:** Sunday 2:00 AM - 6:00 AM Bangladesh time (lowest traffic)
- **Alternate:** Weekday 11:00 PM - 2:00 AM Bangladesh time

**Communication:**
- 7 days advance notice for planned maintenance
- 24 hours advance notice for urgent changes
- Posted on status page and emailed to registered users

**Blackout Periods:**
- No changes during peak business periods (month-end, holidays)
- No changes without approval during high-traffic events

---

### Emergency Fixes Process

**Emergency Fix Criteria:**
- Production outage or critical functionality broken
- Security vulnerability requiring immediate patch
- Data loss or corruption risk

**Process:**
1. **Immediate Triage:**
   - On-call engineer assesses situation
   - Determines if emergency fix required

2. **Approval:**
   - Verbal approval from Tech Lead or PM
   - Document approval in ticket

3. **Implementation:**
   - Hotfix branch created from `main`
   - Minimal change to address issue
   - Expedited code review (within 30 minutes)

4. **Testing:**
   - Test in staging (if time permits)
   - Smoke test plan prepared

5. **Deployment:**
   - Deploy to production
   - Monitor closely for 1 hour

6. **Post-Implementation Review:**
   - Document change in CAB meeting
   - Root cause analysis
   - Plan permanent fix if hotfix was temporary

---

## 10. Data Security & Confidentiality SOP

### Confidentiality Obligations

- All client data treated as confidential
- Non-disclosure agreement (NDA) in effect
- Team members sign confidentiality agreements
- Access to production data restricted (need-to-know basis)
- No client data used for testing (use anonymized/synthetic data)

### Data Handling Procedures

**Development & Testing:**
- Use anonymized datasets in dev/staging environments
- Scrub sensitive data before copying to non-production environments
- Test data generation scripts for realistic data without PII

**Production Access:**
- Production database access logged and audited
- Read-only access by default for reporting/analytics
- Write access requires explicit approval and incident ticket
- All production access via VPN and MFA

**Data Disposal:**
- Secure deletion of data when no longer needed
- Database backups purged per retention policy
- Hard drives wiped before disposal (NIST 800-88 standards)

---

## 11. Maintenance & Support SOP (AMC)

### AMC Activities

- Bug fixing and error resolution  
- Security updates and patches  
- Backend and API monitoring  
- Mobile OS compatibility updates  
- Technical support via email/ticket  

### AMC Response Timeline

| Issue Priority | Response Time |
|---------------|---------------|
| Critical | Within 24 Hours |
| Medium | Within 48 Hours |
| Low | Within 72 Hours |

**Note:** See Section 8 for comprehensive AMC SLA details in Quotation document.

---

## 12. Documentation & Reporting SOP

- Maintain updated technical documentation  
- Provide deployment and handover documents  
- Maintain issue logs and support reports  
- Share periodic status updates with stakeholders  

### Documentation Requirements

**Technical Documentation:**
- Architecture diagrams (system, database, network)
- API documentation (Swagger/OpenAPI)
- Database schema documentation
- Deployment runbooks
- Configuration management documentation
- Disaster recovery procedures

**User Documentation:**
- User manuals (buyers, sellers, agents, admins)
- FAQ documents
- Video tutorials (optional)
- Quick start guides

**Operational Documentation:**
- Incident runbooks
- Monitoring dashboards and alert definitions
- Backup and restore procedures
- Security policies and procedures
- Change management logs

**Project Documentation:**
- Requirements specifications (SRS)
- Test plans and test cases
- Release notes
- Sprint retrospectives
- Postmortem reports

**Documentation Standards:**
- Markdown format for text documentation
- Diagrams using Mermaid, draw.io, or Lucidchart
- Code comments following language conventions
- Version controlled in Git repository
- Regular reviews and updates (quarterly)

---

### Status Reporting

**Daily Standup Reports (During Development):**
- Format: Slack/email brief
- Contents: Yesterday's work, today's plan, blockers
- Audience: Project team

**Weekly Status Reports:**
- Format: Email + dashboard link
- Contents: 
  - Sprint progress (completed stories, burndown chart)
  - Blockers and risks
  - Upcoming milestones
  - Key decisions needed
- Audience: Project stakeholders, client

**Monthly Reports (During AMC):**
- Format: PDF report
- Contents: See Section 8 (Monthly Reporting) for full details
- Audience: Client management

**Milestone Reports:**
- Format: Formal document
- Contents:
  - Milestone objectives vs. achievements
  - Deliverables completed
  - Issues and resolutions
  - Budget and timeline status
  - Next milestone preview
- Audience: Client executives, project sponsor

---

## 13. Risk Management SOP

| Risk | Mitigation |
|----|------------|
| Scope Creep | Formal change control |
| Security Threats | Regular audits & updates |
| Delay Risks | Milestone tracking |
| Data Loss | Regular backups |

### Risk Management Process

**Risk Identification:**
- Conducted during project planning
- Updated at each sprint retrospective
- Ad-hoc identification when new risks emerge

**Risk Assessment:**
- **Likelihood:** Low (10-30%), Medium (31-60%), High (61-90%)
- **Impact:** Low (minor delay), Medium (1-2 week delay), High (>2 week delay), Critical (project failure)
- **Risk Score:** Likelihood × Impact

**Risk Prioritization:**
- High/Critical risks addressed immediately
- Medium risks monitored and planned for
- Low risks accepted or monitored

**Risk Mitigation Strategies:**
- **Avoid:** Change plans to eliminate risk
- **Mitigate:** Reduce likelihood or impact
- **Transfer:** Outsource or insure
- **Accept:** Monitor and have contingency plan

**Risk Register:**
- Maintained in project management tool (Jira, Asana)
- Reviewed weekly in team meetings
- Updated after risk events
- See Quotation Section 8B for detailed risk register

---

## 14. Compliance & Acceptance SOP

- Ensure compliance with agreed requirements  
- Complete final testing and validation  
- Obtain written acceptance from client  
- Close project after successful handover  

### Compliance Verification

**Requirements Traceability:**
- Each requirement mapped to implementation
- Test cases linked to requirements
- Traceability matrix maintained (Requirement ID → User Story → Test Case → Result)

**Standards Compliance:**
- Coding standards adherence (linter checks in CI)
- Security standards (OWASP Top 10)
- Accessibility standards (WCAG 2.1 Level A minimum)
- Performance targets (per SRS and Review Analysis)

**Regulatory Compliance (if applicable):**
- Data protection regulations (local Bangladesh regulations)
- Payment card industry standards (PCI-DSS) for payment handling
- Industry-specific regulations (real estate licensing laws)

---

### Acceptance Testing Process

**Acceptance Criteria Definition:**
- Defined for each user story during sprint planning
- Reviewed and approved by product owner/client
- Must be measurable and testable

**Acceptance Testing Execution:**
1. **Developer Testing:** Developer verifies acceptance criteria before marking story complete
2. **QA Testing:** QA team validates against acceptance criteria
3. **Product Owner Review:** Product owner/client validates in sprint demo
4. **UAT:** Formal user acceptance testing per Section 7.1

**Acceptance Gates:**
- All acceptance criteria met
- No critical or high-priority defects
- Performance benchmarks achieved
- Security testing passed
- Documentation complete

---

### Project Closure Procedures

**Technical Closure:**
- [ ] All code merged to main branch
- [ ] Final production deployment completed
- [ ] All documentation delivered
- [ ] Source code repository access granted to client
- [ ] Handover training completed

**Administrative Closure:**
- [ ] Final acceptance certificate signed (see Quotation Section 12)
- [ ] Final payment received
- [ ] AMC contract activated
- [ ] Project closure report prepared
- [ ] Lessons learned documented
- [ ] Team members released to other projects

**Knowledge Transfer:**
- [ ] Technical handover sessions with client IT team
- [ ] Admin training completed
- [ ] Runbook and documentation reviewed
- [ ] Support handoff to AMC team

---

## 15. SOP Review & Updates

This SOP will be:
- Reviewed at major project milestones  
- Updated if scope or process changes occur  

### Review Schedule

**Regular Reviews:**
- **Sprint Retrospectives:** Process improvements identified and incorporated
- **Quarterly Reviews:** Major SOP sections reviewed for relevance and accuracy
- **Annual Reviews:** Complete SOP overhaul and update

**Trigger-Based Reviews:**
- Major incident postmortems may trigger SOP updates
- Regulatory or security requirement changes
- Technology stack changes
- Client feedback on processes

**Change Management for SOP:**
- Proposed changes discussed in team meeting
- Approved by Tech Lead and Project Manager
- Version number incremented
- Change log maintained in document header
- Team notified of updates

---

## 16. Approval & Sign-off

| Role | Name | Signature | Date |
|----|-----|----------|------|
| Client Representative |  |  |  |
| Project Manager |  |  |  |
| Vendor Representative |  |  |  |

---

**Document Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 01-Jan-2026 | MSC Digital Solutions | Initial SOP document |
| 2.0 | 01-Jan-2026 | CodeStorm Hub | Comprehensive expansion with operational details, CI/CD, security, incident management, testing, AMC, and DR procedures |

---

**Prepared By:**  
**CodeStorm Hub**  
Dhaka, Bangladesh  
**Contact:** contact@codestormhub.dev

---

## Appendix A: Acronyms & Definitions

| Term | Definition |
|------|------------|
| **AMC** | Annual Maintenance Contract |
| **API** | Application Programming Interface |
| **CAB** | Change Advisory Board |
| **CI/CD** | Continuous Integration / Continuous Deployment |
| **CSP** | Content Security Policy |
| **DR** | Disaster Recovery |
| **E2E** | End-to-End |
| **HSTS** | HTTP Strict Transport Security |
| **IDOR** | Insecure Direct Object Reference |
| **JWT** | JSON Web Token |
| **MFA** | Multi-Factor Authentication |
| **NFR** | Non-Functional Requirement |
| **OWASP** | Open Web Application Security Project |
| **PII** | Personally Identifiable Information |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RBAC** | Role-Based Access Control |
| **RPO** | Recovery Point Objective (max acceptable data loss) |
| **RTO** | Recovery Time Objective (max acceptable downtime) |
| **SAST** | Static Application Security Testing |
| **SLA** | Service Level Agreement |
| **SLI** | Service Level Indicator |
| **SLO** | Service Level Objective |
| **SOP** | Standard Operating Procedure |
| **SRS** | Software Requirements Specification |
| **TLS** | Transport Layer Security |
| **UAT** | User Acceptance Testing |
| **XSS** | Cross-Site Scripting |

---

## Appendix B: Contact Information

**Project Team:**
- **Project Manager:** pm@codestormhub.dev
- **Tech Lead:** tech@codestormhub.dev
- **Support Team:** support@codestormhub.dev
- **DevOps/On-Call:** devops@codestormhub.dev
- **Emergency (Critical Issues):** +880-1970279556

**Client Contacts:**
- **Primary Contact:** [To be filled during project kickoff]
- **Technical Contact:** [To be filled during project kickoff]
- **Escalation Contact:** [To be filled during project kickoff]

---

## Appendix C: Tool & Platform Links

**Development:**
- Git Repository: [URL to be provided]
- CI/CD Pipeline: [URL to be provided]
- API Documentation: [URL to be provided]

**Project Management:**
- Project Board: [URL to be provided]
- Documentation Wiki: [URL to be provided]

**Operations:**
- Monitoring Dashboard: [URL to be provided]
- Status Page: [URL to be provided]
- Support Portal: https://support.mschome.app

**Environments:**
- Development: dev.mschome.app
- Staging: staging.mschome.app
- Production: www.mschome.app

---

**End of Standard Operating Procedure**
