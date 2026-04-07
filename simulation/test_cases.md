# Test Cases

## Test Case 1
**Input:** motion = True, daylight = 20, manual_override = None  
**Expected:** Lights ON (High Brightness)

## Test Case 2
**Input:** motion = True, daylight = 70, manual_override = None  
**Expected:** Lights ON (Dimmed)

## Test Case 3
**Input:** motion = False, daylight = 30, manual_override = None  
**Expected:** Lights OFF

## Test Case 4
**Input:** motion = True, daylight = 35, manual_override = ON  
**Expected:** Lights ON (Manual Override)

## Test Case 5
**Input:** motion = True, daylight = 60, manual_override = OFF  
**Expected:** Lights OFF (Manual Override)
