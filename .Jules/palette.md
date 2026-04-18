## 2024-03-20 - CustomTkinter Radio Button Empty State
**Learning:** CustomTkinter `CTkRadioButton` components bound to a `StringVar` will render in an empty (unselected) visual state if the variable isn't explicitly initialized with a value that matches one of the radio buttons, potentially confusing users about what the default selection is.
**Action:** Always initialize CustomTkinter StringVars or IntVars with a `value='...'` argument that matches one of the radio button options to ensure a valid default state is visibly selected on mount.
