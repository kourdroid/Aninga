## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.

## 2024-05-19 - Visual Feedback for Blocking Operations in CustomTkinter
**Learning:** In Tkinter/CustomTkinter, synchronous blocking operations within callbacks freeze the main UI thread. Because of this, assigning UI state changes (such as disabling a button and changing text to "Downloading...") won't visually render unless `window.update()` is called immediately after before the blocking task begins.
**Action:** Apply UI state changes and call `window.update()` prior to blocking operations, and ensure the state is reliably restored inside a `finally` block to prevent the app from getting permanently stuck in a loading state if an error occurs.

## 2024-05-20 - CustomTkinter Input Focus States
**Learning:** CustomTkinter `CTkEntry` widgets with `border_width=0` provide no visual feedback when a user tabs into them, breaking keyboard accessibility and failing WCAG focus visible requirements.
**Action:** Always provide a default `border_width` matching the background color, and bind `<FocusIn>`/`<FocusOut>` events to toggle the `border_color` to a primary highlight color to ensure keyboard users know which input is active.

## 2024-05-21 - CustomTkinter Keyboard Submission Support
**Learning:** In CustomTkinter, `CTkEntry` components don't natively trigger button clicks or form submissions on "Enter", leading to an unexpected dead end for users navigating via keyboard. Attempting to use the underlying tkinter `.invoke()` on a `CTkButton` may not work as expected due to CustomTkinter's custom event handlers.
**Action:** Enhance accessibility by explicitly binding `<Return>` to CustomTkinter entries so that pressing Enter directly triggers the associated form logic/handler.
