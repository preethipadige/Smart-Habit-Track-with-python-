import tkinter as tk
from datetime import datetime, timedelta

#Base habit class
class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency  # daily or weekly
        self.streak = 0
        self.completed = None
    
    def complete(self):
        self.streak += 1
        self.last_completed = datetime.now()
        
    def get_streak(self):
        return self.streak
        
class daily_Habit(Habit):
    def __init__(self, name):
        super().__init__(name, "daily")
    
    def reward_points(self):
        return 10 * self.streak
    
class weekly_Habit(Habit):
    def __init__(self, name):
        super().__init__(name, "weekly")
         
    def reward_points(self):
        return 20 * self.streak
    
 
class User:
    def __init__(self, username):   
        self.username = username
        self.habits = []
        self.points = 0
        
    def add_habit(self, habit):
        self.habits.append(habit)
    
    def complete_habit(self, habit_index):
        habit = self.habits[habit_index]
        habit.complete()
        earned_points = habit.reward_points()
        self.points += earned_points
        return f"{habit.name} complete! streak: {habit.streak}, points earned: {earned_points} "
      
    
# GUI Application
    
class HabitTrackerApp:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Smart Habit Tracker")
        self.root.configure(bg="#f0f8ff")  # light blue background


            
        self.label = tk.Label(root, text=f"Welcome, {user.username}!", 
                              font=("Arial", 16, "bold"),
                              bg="#f0f8ff", fg="#2e8b57") # green text  
        self.label.pack(pady=10)       
        
        #habit buttons
            
        self.habit_buttons = []
        for i, habit in enumerate(user.habits):
            btn = tk.Button(root, 
                            text=f"{habit.name} ({habit.frequency})", 
                            command=lambda i=i: self.complete_habit(i),
                            font=("Arial", 12), bg="#ffcccb", fg="black", 
                            activebackground="#ff6347", activeforeground="white")
            btn.pack(pady=5, ipadx=10, ipady=5)
            self.habit_buttons.append(btn)
                
        self.output = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="#000080")  # navy text
        self.output.pack(pady=10)
                
        self.points_label = tk.Label(root, text=f"Total points: {user.points}", font=("Arial", 12, "bold"),
                                     bg="#f0f8ff", fg="#8b0000")
        self.points_label.pack(pady=10)
                
    def complete_habit(self, index):
        results = self.user.complete_habit(index)
        self.output.config(text=results)
        self.points_label.config(text=f"Total points: {self.user.points}")
                
# Main program with index input
            
if __name__ == "__main__":
    try:
        user = User("Preethi")
        user.add_habit(daily_Habit("Drink Water"))
        user.add_habit(daily_Habit("Read for 30 Minutes"))
        user.add_habit(daily_Habit("Meditate for 10 Minutes"))
        user.add_habit(daily_Habit("Exercise"))
        user.add_habit(daily_Habit("Sleep by 10 PM"))
        user.add_habit(weekly_Habit("Go Jogging"))
        
        root = tk.Tk()
        app = HabitTrackerApp(root, user)
        root.mainloop()
        
    except Exception as e:
        print(f" An error occoured: {e}")