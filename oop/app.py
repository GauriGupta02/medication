from flask import Flask, render_template, request, redirect, url_for
from reminder import MedicineReminder
from scheduler import start_scheduler

app = Flask(__name__)
reminder_manager = MedicineReminder()

start_scheduler(reminder_manager)  # Pass reminder manager to scheduler


# This is the new default route, which will render medication.html
@app.route("/", methods=["GET", "POST"])
def medication():
    if request.method == "POST":
        med_name = request.form["med_name"]
        med_time = request.form["med_time"]
        email = request.form["email"]

        # Add reminder to the list
        reminder_manager.add_reminder(med_name, med_time, email)
        print(f"📝 Saved Reminder: {med_name} at {med_time} for {email}")

        # Send email or handle notification here (this can be part of the email sending logic)
        send_email(email, med_name, med_time)  # Add your send_email function

        return redirect(
            url_for("index")
        )  # Redirect to the reminder list page after form submission

    return render_template("Medication.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    reminders = reminder_manager.get_all_reminders()
    return render_template("index.html", reminders=reminders)


def send_email(email, med_name, med_time):
    # Your email-sending code here
    pass


if __name__ == "__main__":
    app.run(debug=True)
