#!/usr/bin/env python
# coding: utf-8

# In[1]:


import queue
patients = [
    {"name": "P1", "arrival_time": 0, "treatment_time": 30, "urgency_level": 3},
    {"name": "P2", "arrival_time": 10, "treatment_time": 20, "urgency_level": 5},
    {"name": "P3", "arrival_time": 15, "treatment_time": 40, "urgency_level": 2},
    {"name": "P4", "arrival_time": 20, "treatment_time": 15, "urgency_level": 4},
]

def fcfs_schedule(patients):
    return sorted(patients, key=lambda x: x["arrival_time"])

def sjf_schedule(patients):
    return sorted(patients, key=lambda x: x["treatment_time"])

def ps_schedule(patients):
    return sorted(patients, key=lambda x: x["urgency_level"], reverse=True)

def rr_schedule(patients, time_quantum):
    result = []
    time = 0
    patient_queue = queue.Queue()

    for patient in patients:
        patient_queue.put(patient)

    while not patient_queue.empty():
        current_patient = patient_queue.get()
        
        if current_patient["treatment_time"] <= time_quantum:
            time += current_patient["treatment_time"]
            result.append(current_patient["name"])
            
        else:
            time += time_quantum
            current_patient["treatment_time"] -= time_quantum
            patient_queue.put(current_patient)

    return result

print("FCFS Schedule:")
for patient in fcfs_schedule(patients):
    print(patient["name"], end=" -> ")
print("\n")

print("SJF Schedule:")
for patient in sjf_schedule(patients):
    print(patient["name"], end=" -> ")
print("\n")

print("PS Schedule:")
for patient in ps_schedule(patients):
    print(patient["name"], end=" -> ")
print("\n")

print("RR Schedule:")
for patient in rr_schedule(patients, time_quantum=10):
    print(patient, end=" -> ")
print("\n")

print("Priority Scheduling (PS) might be the most suitable method because it prioritizes patients based on urgency levels.")


# In[ ]:




