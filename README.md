# 🚇 Subway Payment System - CLI App

A Python-based terminal application for tracking subway user journeys through check-ins and check-outs using card IDs, and computing average travel times between station pairs.

---

## 📁 Project Folder Structure

```
subway-system/
├── subway_system.py         # Main application logic & CLI
├── __tests__/
│   └── test_cases.py        # Sample test input and execution
├── README.md                # Project documentation
├── flowchart.png            # Flowchart of user interaction (optional)
```

---

## 🧠 Features

* `check_in(card_id, station, time)` — logs when a user enters
* `check_out(card_id, station, time)` — logs when a user exits and computes trip time
* `get_average_distance(start, end)` — shows average time between 2 stations
* Handles missing data or inconsistent actions

---

## 🔄 System Flowchart

```
+-----------------------------+
|   Start Subway System CLI  |
+-------------+---------------+
              |
              v
   +------------------------+
   |   User selects option  |
   |  (checkin/checkout/avg)|
   +----------+-------------+
              |
     +--------+--------+
     |        |        |
     v        v        v
+--------+ +----------+ +-----------------+
| Checkin| | Checkout | | Get Average     |
+--------+ +----------+ +-----------------+
     |          |               |
     v          v               v
Save card   Get card ID     Retrieve all trips
& time      from checkins   from trips[start][end]
in checkins Calc duration   Calculate sum/len
     |      Save in trips    Return average
     |          |               |
     +----------+---------------+
                |
                v
         +-------------+
         |  Back to CLI|
         +-------------+
                |
                v
           Exit command?
              |
         Yes /   \ No
         v         v
   +---------+   Repeat
   |   End   |
   +---------+
```

---

## 🧮 Algorithm

### check\_in(card\_id, station, time):

1. If card is already in `check_ins`, show error
2. Else, store card\_id with (station, time)

### check\_out(card\_id, station, time):

1. Check if card\_id exists in `check_ins`
2. Retrieve start\_station, start\_time
3. Calculate duration = out\_time - in\_time
4. Add duration to `trips[(start_station, end_station)]`
5. Remove from `check_ins`

### get\_average\_distance(start, end):

1. Look up durations in `trips[(start, end)]`
2. Return average (sum / len) or "no trip data"

---

## 📜 Pseudocode

```plaintext
START SubwaySystem

IF command == checkin:
  INPUT card_id, station, time
  IF card_id in check_ins:
    PRINT error
  ELSE:
    check_ins[card_id] = (station, time)

IF command == checkout:
  INPUT card_id, station, time
  IF card_id not in check_ins:
    PRINT error
  ELSE:
    Get start_station, start_time
    duration = time - start_time
    Save duration in trips[(start, end)]
    Remove card_id from check_ins

IF command == avg:
  INPUT start, end
  IF (start, end) in trips:
    CALCULATE average
    PRINT average
  ELSE:
    PRINT no data
```

---

## ✅ Running the Program

Make sure you have Python 3 installed.

```bash
python subway_system.py
```

Then follow on-screen instructions:

* `checkin`, `checkout`, `avg`, `exit`

---

## 🧪 Test Cases (in **tests**/test\_cases.py)

```python
from subway_system import SubwaySystem

sys = SubwaySystem()
sys.check_in("001", "A", 5)
sys.check_out("001", "B", 10)
sys.check_in("002", "A", 3)
sys.check_out("002", "B", 9)
sys.get_average_distance("A", "B")
```

---

## 👨‍🏫 Author

**MhanStevo**
Built for DCIT 204 Python Assignment