from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import notification
import datetime
import random
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget

# Motivational quotes
quotes = [
    "Believe you can and you're halfway there.",
    "Success is no accident. It's hard work and persistence.",
    "Push yourself because no one else is going to do it for you.",
    "Dream big, work hard, stay focused, and surround yourself with good people.",
    "Your only limit is your mind.",
    "I know my kudu will give me the crown of pride.",
    "This is your last chance to prove yourself"
    "You are the only person who can make this work.",
    "Your success is the loudest slap in the face of your abusers "

]

# Custom widget for dynamic gradient background
class GradientBackground(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rect = None
        self.update_gradient()  # Initial gradient creation

    def update_gradient(self, *args):
        # Clear previous gradient if exists
        self.canvas.clear()

        with self.canvas:
            # Create gradient background (linear gradient)
            Color(0.5, 0.2, 0.7)  # Starting color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            # Update the gradient size and position to match the window's size
            self.bind(size=self.update_gradient, pos=self.update_gradient)

class NEETApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        
        # Add the Gradient Background Widget
        self.gradient_background = GradientBackground(size=self.size)
        self.add_widget(self.gradient_background)

        # Welcome Message
        self.add_widget(Label(
            text="Hi Nibedita,\nYou will definitely crack NEET AIIMS!",
            font_size='20sp',
            size_hint=(1, 0.2),
            halign='center'
        ))

        # Exam Date Picker
        self.add_widget(Label(
            text="Select your exam date:",
            font_size='16sp',
            size_hint=(1, 0.1)
        ))
        
        date_picker_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        
        # Year Spinner
        self.year_spinner = Spinner(
            text="2025",
            values=[str(year) for year in range(2024, 2026)],
            size_hint=(0.3, 1)
        )
        date_picker_layout.add_widget(self.year_spinner)
        
        # Month Spinner
        self.month_spinner = Spinner(
            text="1",
            values=[str(month) for month in range(1, 13)],
            size_hint=(0.3, 1)
        )
        date_picker_layout.add_widget(self.month_spinner)
        
        # Day Spinner
        self.day_spinner = Spinner(
            text="1",
            values=[str(day) for day in range(1, 32)],
            size_hint=(0.3, 1)
        )
        date_picker_layout.add_widget(self.day_spinner)
        
        self.add_widget(date_picker_layout)
        
        # Submit Date Button
        self.submit_date_button = Button(
            text="Set Exam Date",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5},
            on_release=self.set_date
        )
        self.add_widget(self.submit_date_button)
        
        # Countdown Timer
        self.countdown_label = Label(
            text="Countdown: Not Set",
            font_size='18sp',
            size_hint=(1, 0.2)
        )
        self.add_widget(self.countdown_label)
        
        # Daily Motivational Quote
        self.quote_label = Label(
            text=f"Motivational Quote: {random.choice(quotes)}",
            font_size='16sp',
            size_hint=(1, 0.2),
            halign='center'
        )
        self.add_widget(self.quote_label)

        # Reminder Button
        self.reminder_button = Button(
            text="Remind me every day",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5},
            on_release=self.set_reminder
        )
        self.add_widget(self.reminder_button)

        # Footer
        self.footer = Label(
            text="Designed & Developed By Ritwik (Brother)",
            font_size='14sp',
            size_hint=(1, 0.1),
            halign='right'
        )
        self.add_widget(self.footer)

    def set_date(self, instance):
        # Get selected year, month, day
        year = int(self.year_spinner.text)
        month = int(self.month_spinner.text)
        day = int(self.day_spinner.text)
        
        try:
            self.exam_date = datetime.date(year, month, day)
            self.update_countdown()
            Clock.schedule_interval(self.update_countdown, 0.01)  # Update every 0.01 seconds for sub-seconds
        except ValueError:
            self.countdown_label.text = "Invalid Date! Please select a valid date."

    def update_countdown(self, *args):
        if hasattr(self, 'exam_date'):
            now = datetime.datetime.now()
            exam_datetime = datetime.datetime.combine(self.exam_date, datetime.datetime.min.time())
            delta = exam_datetime - now

            if delta.total_seconds() > 0:
                days = delta.days
                hours, remainder = divmod(delta.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                microseconds = int(delta.microseconds / 1000)  # Convert to milliseconds
                self.countdown_label.text = (
                    f"Countdown: {days} days, {hours} hours, {minutes} minutes, "
                    f"{seconds}.{microseconds:03d} seconds"
                )
            else:
                self.countdown_label.text = "Exam Date Reached!"

    def set_reminder(self, instance):
        notification.notify(
            title="NEET Reminder",
            message="Stay focused! Keep working hard for your NEET exam.",
            timeout=10
        )

class NEETAppMain(App):
    def build(self):
        return NEETApp()

if __name__ == '__main__':
    NEETAppMain().run()
