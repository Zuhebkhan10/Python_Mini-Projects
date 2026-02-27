import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_details():
    number = entry.get()

    try:
        parsed_number = phonenumbers.parse(number)

        country = geocoder.description_for_number(parsed_number, "en")
        sim = carrier.name_for_number(parsed_number, "en")
        time = timezone.time_zones_for_number(parsed_number)

        result.set(
            f"Country: {country}\n"
            f"Carrier: {sim}\n"
            f"Timezone: {time}"
        )
    except:
        messagebox.showerror("Error", "Enter valid phone number with country code")

# Main window
root = tk.Tk()
root.title("Phone Number Location Finder")
root.geometry("400x320")
root.resizable(False, False)

# Title
tk.Label(root, text="Phone Number Location Finder",font=("Arial", 14, "bold")).pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=10)
entry.insert(0, "+91")

# Button
tk.Button(root, text="Find Details", command=get_details, bg="green", fg="white").pack(pady=10)

# Result label
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 11), justify="left").pack(pady=10)

root.mainloop()