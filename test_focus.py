import customtkinter as ctk

app = ctk.CTk()

def on_focus_in(event, widget, prop, focus_val):
    if not hasattr(widget, f"_orig_{prop}"):
        setattr(widget, f"_orig_{prop}", widget.cget(prop))
    widget.configure(**{prop: focus_val})

def on_focus_out(event, widget, prop):
    orig = getattr(widget, f"_orig_{prop}", None)
    if orig is not None:
        widget.configure(**{prop: orig})

btn = ctk.CTkButton(app, text="Button")
btn.pack(pady=10)
btn.bind('<FocusIn>', lambda e, w=btn: on_focus_in(e, w, "fg_color", w.cget("hover_color")))
btn.bind('<FocusOut>', lambda e, w=btn: on_focus_out(e, w, "fg_color"))

rb = ctk.CTkRadioButton(app, text="Radio")
rb.pack(pady=10)
rb.bind('<FocusIn>', lambda e, w=rb: on_focus_in(e, w, "text_color", "#d10b0b"))
rb.bind('<FocusOut>', lambda e, w=rb: on_focus_out(e, w, "text_color"))

app.update()
print(rb.cget("text_color"))
