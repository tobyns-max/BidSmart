# 📘 Project Scope: BidSmart

## 🧭 Project Name: BidSmart

### 🔑 Goal:
Help Australian property buyers determine property value and refine bidding strategy using modern, LLM-powered tools — starting with a robust, public-facing valuation module.

---

## ✅ Current Project Scope (Phase 1)

### 1. Coming Soon Page
- Clean landing page with email capture
- Hosted via Vercel
- Strong UX/UI inspired by high-end AI brands (e.g. Roam)
- Optional Sora/Runway video background

### 2. Valuation Engine
**Goal:** Estimate a property's fair value using:
- Comparable sales
- Historical listings
- Property features
- Area trends and improvements

**Core Logic:**
An LLM-enhanced comp-based valuation system with human-editable factors.

**Key Functional Modules:**
- Comparable Sales Ingestor: Scrapes or loads public property data (CSV or web).
- Property Feature Extractor: Parses text and photos to identify key attributes.
- Improvement Tracker: Detects changes between historical and current listings.
- Valuation Generator: Uses an LLM to compare subject property to comps.
- Confidence Engine: Adds intervals based on comp quality/spread.

**Frontend Output:**
- Subject property summary
- Side-by-side with 3–5 similar comps
- LLM-estimated price range with rationale
- Editable inputs (e.g. user says “they added a pool”)

---

## 🧠 How LLMs Will Be Used

### 1. Narrative Comparison + Price Justification
- Compare subject property to comps and explain pricing rationale
- Weigh trade-offs and generate a human-style valuation explanation

### 2. Natural Language Data Parsing
- Ingest and structure unstructured text from listings
- Score subjective descriptions and extract key features

### 3. Improvement Detection from Past Listings
- Compare historical listings using LLM to describe changes (e.g. renos, extensions)

### 4. Valuation Calibration via Prompt Engineering
- Adjust valuations using structured prompt logic (e.g. +/- adjustments by feature)

---

## 🗂️ Features Backlog (Future Phases)
- Bidding strategy tool (paused but scoped)
- User feedback loop ("Rank this price vs similar listings")
- Editable rationale (user can adjust AI valuation and explain why)
- Agent portal or pro tier
- Mobile UX optimization

---

## 🧪 Immediate Next Steps
- Finalize Coming Soon page
- Build MVP of:
  - Property comparison logic
  - LLM valuation prompt framework
  - Manual comp upload or scrape (NSW first)