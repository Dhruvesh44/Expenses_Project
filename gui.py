import tkinter as tk
from expense_manager import ExpenseManager

class ExpenseTrackerGUI:
    def __init__(self):
        # Color scheme
        self.BG_COLOR = "#2C3E50"      # Dark blue-gray
        self.FG_COLOR = "#ECF0F1"      # ← CHANGE: Light gray text (was #2C3E50)
        self.BUTTON_COLOR = "#3498DB"  # Blue
        self.BUTTON_HOVER = "#2980B9"  # Darker blue
        self.ACCENT_COLOR = "#1ABC9C"  # Teal
        self.ENTRY_BG = "#34495E"      # Darker blue-gray
        self.ENTRY_FG = "#ECF0F1"          # Light text
                
        self.window = tk.Tk()
        self.window.title("Expense Tracker")
        
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        self.window.geometry(f"{screen_width}x{screen_height}+0+0")
        
        self.window.configure(bg=self.BG_COLOR)
        
        # Make window resizable
        self.window.resizable(True, True)
        
        self.manager = ExpenseManager()
        self.setup_main_menu()
        
    def setup_main_menu(self):
        # Main frame for centering
        main_frame = tk.Frame(self.window, bg=self.BG_COLOR)
        main_frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="💰 Expense Tracker",
            font=("Helvetica", 28, "bold"),
            bg=self.BG_COLOR,
            fg=self.ACCENT_COLOR
        )
        title_label.pack(pady=(0, 30))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Track your expenses effortlessly",
            font=("Helvetica", 12, "bold"),
            bg=self.BG_COLOR,
            fg=self.FG_COLOR
        )
        subtitle_label.pack(pady=(0, 40))
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg=self.BG_COLOR)
        button_frame.pack()
        
        # Button styling function
        def create_styled_button(parent, text, command):
            btn = tk.Button(
                parent,
                text=text,
                command=command,
                font=("Helvetica", 12, "bold"),
                bg=self.BUTTON_COLOR,
                fg="#2C3E50" ,
                activebackground=self.BUTTON_HOVER,
                activeforeground="white",
                relief="flat",
                padx=30,
                pady=15,
                cursor="hand2",
                bd=0
            )
            # Hover effects
            def on_enter(e):
                btn['background'] = self.BUTTON_HOVER
            def on_leave(e):
                btn['background'] = self.BUTTON_COLOR
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            return btn
        
        # Create buttons
        add_btn = create_styled_button(button_frame, "➕ Add Expense", self.add_expense)
        add_btn.pack(pady=10, fill=tk.X)
        
        view_btn = create_styled_button(button_frame, "📋 View Expenses", self.view_expenses)
        view_btn.pack(pady=10, fill=tk.X)
        
        summary_btn = create_styled_button(button_frame, "📊 Show Summary", self.show_summary)
        summary_btn.pack(pady=10, fill=tk.X)
        
        # Exit button (different color)
        exit_btn = tk.Button(
            button_frame,
            text="🚪 Exit",
            command=self.window.quit,
            font=("Helvetica", 10,"bold"),
            bg="#E74C3C",
            fg="#2C3E50" ,
            activebackground="#C0392B",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            bd=0
        )
        exit_btn.pack(pady=(30, 0), fill=tk.X)
        
        # Footer
        footer_label = tk.Label(
            main_frame,
            text="Final Year Project • Computer Science",
            font=("Helvetica", 9),
            bg=self.BG_COLOR,
            fg="#2C3E50" 
        )
        footer_label.pack(side=tk.BOTTOM, pady=20)
    
    def create_styled_window(self, title, width=500, height=400):
        """Create a styled popup window"""
        window = tk.Toplevel(self.window)
        window.title(title)
        window.geometry(f"{width}x{height}")
        window.configure(bg=self.BG_COLOR)
        window.resizable(True, True)
        
        # Title label
        title_label = tk.Label(
            window,
            text=title,
            font=("Helvetica", 20, "bold"),
            bg=self.BG_COLOR,
            fg=self.ACCENT_COLOR
        )
        title_label.pack(pady=20)
        
        return window
    
    def create_styled_label(self, parent, text):
        """Create a styled label"""
        return tk.Label(
            parent,
            text=text,
            font=("Helvetica", 11),
            bg=self.BG_COLOR,
            fg=self.FG_COLOR
        )
    
    def create_styled_entry(self, parent):
        """Create a styled entry field"""
        entry = tk.Entry(
            parent,
            font=("Helvetica", 11),
            bg=self.ENTRY_BG,
            fg=self.ENTRY_FG,
            insertbackground=self.FG_COLOR,
            relief="flat",
            bd=2,
            highlightbackground=self.ACCENT_COLOR,
            highlightcolor=self.ACCENT_COLOR,
            highlightthickness=1
        )
        return entry
    
    def create_styled_button_small(self, parent, text, command):
        """Create a small styled button"""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 11, "bold"),
            bg=self.BUTTON_COLOR,
            fg="#2C3E50" ,
            activebackground=self.BUTTON_HOVER,
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            bd=0
        )
        # Hover effects
        def on_enter(e):
            btn['background'] = self.BUTTON_HOVER
        def on_leave(e):
            btn['background'] = self.BUTTON_COLOR
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn
    
    def add_expense(self):
        """Open add expense window"""
        add_window = self.create_styled_window("Add New Expense", 500, 450)
        
        # Input frame
        input_frame = tk.Frame(add_window, bg=self.BG_COLOR)
        input_frame.pack(pady=20)
        
        # Amount
        amount_label = self.create_styled_label(input_frame, "Amount ($):")
        amount_label.grid(row=0, column=0, padx=10, pady=15, sticky="e")
        
        self.amount_entry = self.create_styled_entry(input_frame)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=15, sticky="ew")
        
        # Category
        category_label = self.create_styled_label(input_frame, "Category:")
        category_label.grid(row=1, column=0, padx=10, pady=15, sticky="e")
        
        self.category_entry = self.create_styled_entry(input_frame)
        self.category_entry.grid(row=1, column=1, padx=10, pady=15, sticky="ew")
        
        # Description
        description_label = self.create_styled_label(input_frame, "Description:")
        description_label.grid(row=2, column=0, padx=10, pady=15, sticky="ne")
        
        self.description_entry = tk.Text(
            input_frame,
            height=4,
            width=30,
            font=("Helvetica", 11),
            bg=self.ENTRY_BG,
            fg=self.ENTRY_FG,
            insertbackground=self.FG_COLOR,
            relief="flat",
            bd=2,
            highlightbackground=self.ACCENT_COLOR,
            highlightcolor=self.ACCENT_COLOR,
            highlightthickness=1
        )
        self.description_entry.grid(row=2, column=1, padx=10, pady=15, sticky="ew")
        
        # Configure grid weights
        input_frame.columnconfigure(1, weight=1)
        
        # Button frame
        button_frame = tk.Frame(add_window, bg=self.BG_COLOR)
        button_frame.pack(pady=30)
        
        # Submit button
        submit_btn = self.create_styled_button_small(
            button_frame,
            "💾 Save Expense",
            lambda: self.save_expense(add_window)
        )
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        # Cancel button
        cancel_btn = tk.Button(
            button_frame,
            text="❌ Cancel",
            command=add_window.destroy,
            font=("Helvetica", 11, "bold"),
            bg="#7F8C8D",
            fg="#2C3E50",
            activebackground="#95A5A6",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=8,
            cursor="hand2",
            bd=0
        )
        cancel_btn.pack(side=tk.LEFT, padx=10)
    
    def save_expense(self, window):
        """Save expense from GUI"""
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get("1.0", tk.END).strip()
        
        success = self.manager.add_expense(amount, category, description)
        
        if success:
            # Show success message
            success_label = tk.Label(
                window,
                text="✅ Expense added successfully!",
                font=("Helvetica", 11, "bold"),
                bg=self.BG_COLOR,
                fg=self.ACCENT_COLOR
            )
            success_label.pack(pady=10)
            window.after(1500, window.destroy)  # Close after 1.5 seconds
        else:
            # Show error message
            error_label = tk.Label(
                window,
                text="❌ Error: Please enter a valid amount",
                font=("Helvetica", 11, "bold"),
                bg=self.BG_COLOR,
                fg="#E74C3C"
            )
            error_label.pack(pady=10)
    
    def view_expenses(self):
        """Open view expenses window"""
        view_window = self.create_styled_window("All Expenses", 700, 500)
        
        # Text display with scrollbar
        text_frame = tk.Frame(view_window, bg=self.BG_COLOR)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Text widget
        text_display = tk.Text(
            text_frame,
            font=("Courier New", 10),
            bg=self.ENTRY_BG,
            fg=self.FG_COLOR,
            insertbackground=self.FG_COLOR,
            relief="flat",
            bd=2,
            highlightbackground=self.ACCENT_COLOR,
            highlightthickness=1
        )
        text_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command=text_display.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_display.config(yscrollcommand=scrollbar.set)
        
        # Get and display data
        data = self.manager.view_expenses()
        text_display.insert("1.0", data if data else "No expenses recorded yet.")
        text_display.config(state="disabled")
        
        # Refresh button
        refresh_btn = self.create_styled_button_small(
            view_window,
            "🔄 Refresh",
            view_window.destroy
        )
        refresh_btn.pack(pady=10)
    
    def show_summary(self):
        """Open summary window"""
        summary_window = self.create_styled_window("Spending Summary", 500, 400)
        
        # Get summary data from manager
        summary_data = self.manager.show_summary()  # This now returns a string!
        
        # Display in text widget
        text_frame = tk.Frame(summary_window, bg=self.BG_COLOR)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        text_display = tk.Text(
            text_frame,
            font=("Courier New", 10),
            bg=self.ENTRY_BG,
            fg=self.FG_COLOR,
            relief="flat"
        )
        text_display.pack(fill=tk.BOTH, expand=True)
        
        # Insert the summary data
        text_display.insert("1.0", summary_data)
        text_display.config(state="disabled")
        
        ok_btn = self.create_styled_button_small(
            summary_window,
            "OK",
            summary_window.destroy
        )
        ok_btn.pack(pady=20)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ExpenseTrackerGUI()
    app.run()