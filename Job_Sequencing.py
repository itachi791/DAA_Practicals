def job_sequencing(jobs):
    # Sort jobs by descending profit
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize an array to keep track of free slots
    max_deadline = max(job[1] for job in jobs)
    schedule = [None] * max_deadline
    
    total_profit = 0
    scheduled_jobs = []

    # Try to schedule each job
    for job in jobs:
        for slot in range(job[1] - 1, -1, -1):  # Check slots from job's deadline
            if schedule[slot] is None:  # Slot is free
                schedule[slot] = job[0]  # Schedule the job
                total_profit += job[2]  # Add job profit
                scheduled_jobs.append(job[0])  # Record the job
                break

    return scheduled_jobs, total_profit

# Example usage
jobs = [
    ('J1', 4, 20),
    ('J2', 1, 10),
    ('J3', 1, 40),
    ('J4', 1, 30)
]

scheduled_jobs, total_profit = job_sequencing(jobs)
print(f"Scheduled Jobs: {scheduled_jobs}")
print(f"Total Profit: {total_profit}")
