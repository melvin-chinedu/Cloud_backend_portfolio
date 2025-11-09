"""
Day 2 — Git & Branching Tracker
A small simulation of managing Git branches using Python data structures.
"""

# Defining  the list of branches
branches = [
    {"name": "main", "description": "Stable branch with completed work", "status": "active"},
    {"name": "feature/Day1-linux-setup", "description": "Linux setup and AWS account", "status": "merged"},
    {"name": "feature/Day_2-git-branching", "description": "Practicing Git branches and PRs", "status": "active"},
]

def list_branches(branches):
    print("\n📂 Current Branches:")
    for b in branches:
        print(f"- {b['name']} ({b['status']}) → {b['description']}")

def add_branch(branches, name, description):
    branches.append({"name": name, "description": description, "status": "active"})
    print(f"\n✅ New branch '{name}' added successfully!")

def merge_branch(branches, name):
    for b in branches:
        if b["name"] == name:
            b["status"] = "merged"
            print(f"\n🔀 Branch '{name}' merged successfully!")
            return
    print(f"\n⚠️ Branch '{name}' not found!")

def delete_branch(branches, name):
    for b in branches:
        if b["name"] == name:
            branches.remove(b)
            print(f"\n🗑 Branch '{name}' deleted.")
            return
    print(f"\n⚠️ Branch '{name}' not found!")

# --- Simulation ---
list_branches(branches)
add_branch(branches, "feature/Day3-python-basics-recap", "Python functions and loops practice")
merge_branch(branches, "feature/day2-git-branching")
list_branches(branches)