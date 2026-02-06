# Game Design Document: Schrödinger Industries

**Version:** 1.0  
**Date:** February 5, 2026  
**Designer:** [Your Name]  
**Document Purpose:** Portfolio project - self-contained quantum cat management game

---

## 1. Executive Summary

**High Concept:**  
A darkly comedic turn-based management game where players work as researchers at Schrödinger Industries, monitoring quantum cats in sealed boxes without directly observing them. Players must balance the reward of extended observation periods against degrading sensor reliability and the risk of catastrophic failure.

**Target Experience:**  
A 1-2 hour completable experience emphasizing strategic planning, risk assessment, and "press your luck" decision-making. Players can walk away satisfied after one playthrough.

**Core Loop:**  
Plan weekly care schedule → Monitor degrading sensors during weekday check-ins → Receive weekend technician reports → Decide whether to open the box or continue → Earn money for successful runs → Invest in better equipment

---

## 2. Game Overview

### 2.1 Premise
You're a researcher at Schrödinger Industries, a quantum research facility studying cats in isolated observation boxes. Your job is to keep the cats alive using indirect measurements—without opening the box. The longer you successfully maintain a cat without verification, the higher your bonus. But your measurement instruments degrade over time, and the company only tolerates 9 "incidents" before termination.

### 2.2 Victory Conditions
- **Primary Goal:** Survive 52 weeks (1 year) of employment
- **Optional:** Continue into Year 2+ for score-chasing
- **Failure State:** Lose all 9 lives before completing 52 weeks

### 2.3 Core Themes
- Uncertainty vs. verification
- Risk/reward decision-making
- Imperfect information management
- Dark corporate humor

---

## 3. Core Gameplay Loop

### 3.1 Weekly Cycle Structure

**MONDAY MORNING (Start of Week)**
1. **Box Resolution Decision**
   - Player chooses: "Open the box" or "Continue monitoring"
   - If opened: Reveals if cat is alive or dead, triggers payout/consequences
   - If continuing: Proceed to planning phase

2. **Planning Phase**
   - Set up full 7-day schedule (Mon-Sun)
   - Actions per day: Feeding frequency, waste removal frequency, other care tasks
   - Review current sensor reliability (from last weekend report)
   - Submit plan to begin week simulation

**WEEKDAY MORNINGS (Mon-Fri)**
- **Check-in Opportunities (Optional)**
  - View sensor readings (e.g., "Hunger: 65%", "Waste: 82%")
  - Sensor reliability is HIDDEN during the week
  - Can modify schedule for current day + remaining days only
  - Cannot change past days
  - Each check-in reduces money multiplier

**WEEKEND (Sat-Sun)**
- **Technician Report**
  - Box remains closed
  - Reveals current sensor reliability percentages
  - May include ominous notes about the box's status
  - Examples: "Unusual odor detected", "No movement in 72 hours", "Biological readings inconsistent"

- **Shop Phase**
  - Purchase new sensors
  - Repair existing sensors
  - Upgrade sensor quality

**REPEAT** for Week 2, 3, etc.

### 3.2 Cat Care Mechanics

**Required Care Actions:**
- **Feeding:** Must feed 3 times per day (over/under feeding can kill)
- **Waste Removal:** Must remove waste regularly (accumulation kills cat)
- **[Additional systems TBD]:** Temperature regulation, enrichment, health monitoring

**Failure Conditions:**
- Starvation (insufficient feeding)
- Overfeeding (too much food)
- Toxic environment (waste accumulation)
- [Other care failures TBD]

---

## 4. Sensor System

### 4.1 Sensor Types
Each sensor monitors one aspect of cat care:

- **Food Sensor:** Monitors hunger levels
- **Waste Sensor:** Monitors feces accumulation
- **Motion Sensor:** Detects cat movement/activity
- **[Additional sensors TBD]:** Temperature, health vitals, etc.

### 4.2 Sensor Reliability

**Degradation:**
- All sensors degrade over time
- Different sensor types have different degradation rates
- Example: Cheap motion sensor degrades 10%/week, premium bio-monitor degrades 2%/week

**Reliability Impact:**
- 100% reliable: Reading is accurate
- 50% reliable: Reading could be significantly off
- 10% reliable: Reading is nearly useless

**Player Knowledge:**
- During week: Players see sensor READINGS but not current reliability
- Weekend report: Players learn actual reliability percentages
- Creates uncertainty: "Is the cat really starving, or is my sensor broken?"

### 4.3 Sensor Economy

**Purchasing:**
- Basic sensors: Cheap, high degradation
- Premium sensors: Expensive, low degradation
- Repair kits: Restore percentage of reliability

**Example Pricing (TBD):**
- Cheap motion sensor: 100 coins, degrades 10%/week
- Premium bio-monitor: 2000 coins, degrades 2%/week
- Repair kit: 500 coins, restores 30% reliability

---

## 5. Economic System

### 5.1 Earning Money

**Primary Income: Survival Multiplier**
- Base reward per week survived
- Multiplier increases with consecutive weeks without opening box
- Example: Week 1 = 1x, Week 10 = 10x, Week 20 = 20x (exact scaling TBD)

**Check-in Penalty:**
- Each weekday check-in reduces multiplier (amount TBD)
- Encourages confident planning vs. constant monitoring

**Box Opening:**
- **If cat is alive:** Receive payout at 0.5x current multiplier (halved for verification)
- **If cat is dead:** 0x payout (lose everything)

### 5.2 Spending Money

**Shop Available on Weekends:**
- Purchase new sensors
- Repair existing sensors
- Upgrade sensor tiers
- [Possible future: Insurance, automation tools]

### 5.3 Progression Arc

**Early Weeks:**
- Limited budget, basic sensors
- Frequent checking required
- Small payouts, slow growth

**Mid-Game:**
- Can afford better sensors
- More confident planning
- Longer runs = bigger payouts

**Late Game:**
- Premium equipment enables multi-week runs
- Massive multipliers at stake
- High risk/high reward decisions

**[OPEN QUESTION]:** What happens to money/equipment between cats? Does it persist, partially reset, or fully reset?

---

## 6. Lives System

### 6.1 The 9 Lives Concept
- Corporate theme: Company tolerates 9 "incidents" before shutdown
- Each dead cat = 1 life lost
- Running out of lives = Game Over (before completing 52 weeks)

### 6.2 Escalating Consequences

**Deaths 1-3:** Warning phase
- Mild corporate warnings via email/memos
- "Please review feeding protocols"

**Deaths 4-6:** Scrutiny phase
- Mandatory retraining messages
- [Possible: Reduced starting budget for next cat]
- Increased management pressure

**Deaths 7-8:** Critical phase
- Executive oversight
- Severe pressure
- [Possible: Equipment restrictions]

**Death 9:** Termination
- Game Over
- Final performance review screen
- Displays stats and achievements

### 6.3 Transitioning Between Cats

**When a Cat Dies:**
- Incident report screen (darkly humorous)
- Corporate ID for cat (e.g., "Subject #4 expired due to excessive feeding")
- Lives remaining counter updates
- [TBD: What carries over to next cat?]

---

## 7. Narrative & Tone

### 7.1 Corporate Framing
Players are employees of **Schrödinger Industries**, a quantum research corporation with questionable ethics and bureaucratic absurdity.

### 7.2 Narrative Touchpoints

**Employee Communications:**
- Emails from management
- Incident reports
- Performance reviews
- "Employee of the Month" announcements

**Technician Notes:**
- Weekend sensor reports
- Increasingly ominous observations
- Dark humor about box conditions

**Year-End Review:**
- Annual performance summary
- Stats: Cats survived, money earned, longest streak
- Corporate rating (A-F based on performance)

### 7.3 Tone
- Dark comedy with corporate satire
- Absurdist bureaucracy meets quantum physics
- Morbid but not graphic
- Self-aware about the ethical implications

**Example Quotes:**
- "HR reminds staff: We're quantum physicists, not pet owners."
- "Subject #7 exceeded expected survival duration. Congratulations!"
- "Unusual odor detected. Maintenance has been notified."

---

## 8. User Interface & Experience

### 8.1 Core Screens

**1. Monday Morning Box Decision**
- Large sealed box visual
- "Open Box" vs "Continue Monitoring" choice
- Display: Current week, lives remaining, current multiplier

**2. Weekly Planning Screen**
- 7-day calendar grid
- Schedule feeding/cleaning for each day
- Sensor reliability display (from last weekend)
- Current equipment inventory

**3. Weekday Check-in Screen**
- Current day/time indicator
- Sensor readouts (reliability hidden)
- Editable schedule for current + future days
- Warning about multiplier penalty

**4. Weekend Report Screen**
- Technician notes
- Sensor reliability breakdown
- Shop interface
- Money earned this week (if cat still alive)

**5. Box Resolution Screen**
- Dramatic reveal: Cat alive or dead
- Money payout calculation
- Life lost notification (if dead)
- Stats summary

### 8.2 Key UI Elements

**Persistent HUD:**
- Current week (1-52)
- Lives remaining (X/9)
- Current multiplier
- Money/budget
- [Possible: Ominous notes indicator]

**Sensor Display:**
- Gauge or percentage readout
- Color coding (green/yellow/red zones)
- During week: No reliability shown
- Weekend: Reliability percentage visible

**Calendar/Schedule View:**
- Visual representation of planned care
- Ability to adjust future days
- Locked past days (grayed out)

---

## 9. Progression & Replayability

### 9.1 Single Playthrough Arc
- 52 weeks = natural completion
- Progressive difficulty through sensor degradation
- Economic scaling (better equipment unlocks over time)
- Narrative escalation (corporate pressure increases)

### 9.2 Optional Year 2+
- Continue beyond Week 52 for score-chasing
- Same cat (if alive) or new cat
- Increased difficulty: Faster sensor degradation, more complex needs
- Pure endless mode for mastery

### 9.3 Achievements/Challenges
- "Employee of the Month": Keep cat alive 4+ weeks consecutively
- "Leap of Faith": Survive 30+ weeks without opening box
- "Budget Conscious": Complete year without premium sensors
- "Perfect Record": Complete 52 weeks without losing a life
- [Additional achievements TBD]

### 9.4 Scoring/Leaderboard
- Total money earned
- Longest single cat survival
- Fewest lives lost
- Researcher grade (S/A/B/C/D/F)

---

## 10. Technical Scope

### 10.1 Platform
- Web-based (HTML/CSS/JavaScript)
- Portfolio website integration
- Mobile-friendly responsive design

### 10.2 Core Systems to Implement

**Essential (MVP):**
- Turn-based simulation engine
- Sensor degradation system
- Care scheduling system
- Economic system (earning/spending)
- Win/lose state detection
- Save/load (browser storage)

**Secondary:**
- Achievements system
- Leaderboard/scoring
- Narrative text/emails
- Visual polish (animations, effects)

**Nice-to-Have:**
- Multiple cat types with different needs
- Multi-cat management (Employee of Month reward)
- Advanced sensor types
- Meta-progression unlocks

### 10.3 Data Structure Considerations

**Game State:**
- Current week number
- Lives remaining
- Money/budget
- Active cat status (alive/dead/unknown)
- Sensor inventory and reliability
- Weekly schedule plan
- Multiplier value
- Historical stats

**Cat Simulation:**
- Internal state (hunger, waste, health)
- Care history
- Actual alive/dead status (hidden from player until opened)

---

## 11. Open Design Questions

### 11.1 Critical Decisions Needed

**1. Box Opening Mechanics**
- Does opening the box (when cat is alive) end that cat's run?
- Or can you continue with the same cat at reduced multiplier?
- **Impact:** Affects risk/reward balance and pacing

**2. Money/Equipment Persistence**
- What carries over between cats?
- Full persistence, partial, or reset?
- **Impact:** Affects difficulty curve and progression feel

**3. Check-in Penalty**
- How much does each check-in reduce multiplier?
- Fixed amount or percentage?
- **Impact:** Balance between safety and reward

**4. Exact Cat Care Rules**
- Precise feeding requirements (3x/day, but tolerance?)
- Waste accumulation rates
- Other care systems needed?
- **Impact:** Core simulation complexity

**5. Sensor Degradation Rates**
- Per-week degradation amounts
- Different rates per sensor type
- **Impact:** Economic balance and difficulty pacing

### 11.2 Feature Expansion Ideas (Post-MVP)

**Multi-Cat Management:**
- Unlock after Employee of Month achievement
- Manage 2-3 cats simultaneously
- Shared budget, separate schedules
- Significantly increased difficulty

**Cat Personality Types:**
- Different cats have different care requirements
- "Finicky eater" needs exact feeding times
- "Active" produces more waste
- Adds variety to runs

**Advanced Sensors:**
- Predictive AI sensors (forecast future needs)
- Multi-spectrum sensors (monitor multiple stats)
- Self-repairing sensors (slow reliability recovery)

**Automation Tools:**
- Auto-feeders (reduce feeding micromanagement)
- Waste recyclers (extend cleaning intervals)
- Expensive but reduce workload

---

## 12. Success Metrics (Portfolio Context)

### 12.1 Player Experience Goals
- **Completion Rate:** 70%+ of players finish one 52-week run
- **Session Length:** 60-120 minute average playthrough
- **Replayability:** 30%+ attempt second run
- **Engagement:** Players feel genuine tension during box decisions

### 12.2 Design Demonstration
This project showcases:
- **Systems Design:** Interconnected mechanics (sensors, economy, risk/reward)
- **Player Psychology:** Uncertainty, loss aversion, gambling impulses
- **Narrative Integration:** Corporate satire woven into mechanics
- **UI/UX:** Complex information presented clearly
- **Scope Management:** Complete, polished experience within constraints

---

## 13. Development Phases

### Phase 1: Core Loop Prototype
- Basic weekly cycle (plan → simulate → report)
- Simple cat simulation (hunger/waste only)
- Sensor system with degradation
- Box opening mechanics
- Win/lose detection

### Phase 2: Economic System
- Money earning (multiplier)
- Shop implementation
- Sensor purchasing/repair
- Balance tuning

### Phase 3: Polish & Narrative
- UI refinement
- Corporate emails/messages
- Technician notes
- Sound effects/music
- Visual effects

### Phase 4: Replayability
- Achievements
- Scoring system
- Year 2+ mode
- Save/load

---

## 14. Appendix

### 14.1 Reference Games
- **Into the Breach:** Turn-based planning with consequences
- **FTL:** Resource management under uncertainty
- **Reigns:** Simple choices with cascading effects
- **Papers Please:** Dark humor + bureaucracy
- **Universal Paperclips:** Incremental progression with narrative

### 14.2 Thematic Inspiration
- Schrödinger's Cat thought experiment
- Corporate satire (Office Space, The Office)
- Dark simulation games (This War of Mine)

---

**End of Document**

---

## Document Changelog
- v1.0 (Feb 5, 2026): Initial GDD created based on design discussion
